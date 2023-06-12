import datetime

import requests
import CalculateSteamPrices as csp
from RequestApiService import get_games_from_tag
import sqlite3

start_time = datetime.datetime.now()

wishList = []


def levenshtein_distance(s1, s2):
    # A function that calculates the Levenshtein distance between two strings
    # https://en.wikipedia.org/wiki/Levenshtein_distance
    # Initialize a matrix of size (len(s1) + 1) x (len(s2) + 1)
    matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    # Fill in the first row and column with the index values
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j
    # Fill in the rest of the matrix using a dynamic programming approach
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If the characters are equal, use the diagonal value
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                # Otherwise, use the minimum of the left, top and diagonal values plus one
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
    # Return the bottom right value of the matrix as the distance
    return matrix[len(s1)][len(s2)]


def get_game_information(game_name):
    # Use the Steam Storefront API to get a list of games by name
    # https://partner.steamgames.com/doc/store/application/storefrontapi
    url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&l=english&cc=US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Check if there are any results
        if "total" not in data or data["total"] == 1:
            # Loop through the results and compare their names with the game name using Levenshtein distance
            for result in data["items"]:
                # Only consider games that are available for purchase
                if result["type"] == "app" and result["metascore"] != "" and result.get("price", ""):
                    # Calculate the distance between the result name and the game name
                    return {"id": result["id"], "name": result["name"]}
        if data["total"] > 1:
            # Initialize a variable to store the best match and its score
            best_match = None
            best_score = float("inf")
            # Loop through the results and compare their names with the game name using Levenshtein distance
            for result in data["items"]:
                # Only consider games that are available for purchase
                if result["type"] == "app" and result["metascore"] != "" and result.get("price", ""):
                    # Calculate the distance between the result name and the game name
                    distance = levenshtein_distance(result["name"].lower(), game_name.lower())
                    # Update the best match and score if the distance is lower than the current best score
                    if distance < best_score:
                        best_match = {"id": result["id"], "name": result["name"]}
                        best_score = distance
            # Return the best match or None if no match was found
            return best_match
        else:
            # There are no results for this game name
            return None
    else:
        # Something went wrong with the request
        return None


def game_finding_with_appid(appids):
    list_game_prices = []
    cur_list = ["USD", "TL"]
    price_maps = {appid: {cur: csp.get_over_price_with_currency(cur, appid) for cur in cur_list} for appid in appids}
    for appid, price_map in price_maps.items():
        if appid not in csp.error_logs and all(cur in price_map for cur in cur_list):
            percent_diff = csp.percentage_difference(price_map['USD'], price_map['TL'])
            price = round(percent_diff, 2)
            print(f"{appid} {price}% more expensive in USD.")
        else:
            price = 0.0
            print(f"Error: could not calculate price for appid {appid}")
        game_map = {"appid": appid, "price_dif": price, "usd": price_map['USD'], "tl": price_map['TL']}
        list_game_prices.append(game_map)
    return list_game_prices

"""def game_finding_with_appid(appids):
    list_game_prices = []
    for appid in appids:
        # price_map = csp.get_over_price_amount(appid)
        cur_list = ["USD", "TL"]
        price_map = {}
        for cur in cur_list:
            price_map[cur] = csp.get_over_price_with_currency(cur, appid)
        if appid not in csp.error_logs:
            price_map[cur_list[0]]
            percent_diff = csp.percentage_difference(price_map[cur_list[0]], price_map[cur_list[1]])
            price = round(percent_diff, 2)
            print(str(appid) + f" {price}% more expensive in USD.")
            game_map = {"appid": appid, "price_dif": price, "usd": price_map['usd'], "tl": price_map['tl']}
            list_game_prices.append(game_map)
    return list_game_prices
"""

def game_finding_function():
    # Call the function with some tags
    list_game_prices = []
    found_games = get_games_from_tag('souls-like')
    for game in found_games:
        game_info = get_game_information(game)
        if game_info is not None and game_info['id'] is not None:
            price = csp.get_over_price_amount(game_info['id'])
            if price > 0:
                print(game_info['name'] + f" {price:.2f}% more expensive in USD.")
                game_map = {"name": game_info['name'], "price_dif": price}
                list_game_prices.append(game_map)
    return list_game_prices


def create_tables():
    conn = sqlite3.connect("steam_database_prices.db")
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER PRIMARY KEY,
            code TEXT UNIQUE,
            name TEXT
        );

        CREATE TABLE IF NOT EXISTS games (
            appid INTEGER PRIMARY KEY,
            name TEXT
        );

        CREATE TABLE IF NOT EXISTS game_prices (
            id INTEGER PRIMARY KEY,
            game_appid INTEGER,
            currency_id INTEGER,
            price REAL,
            FOREIGN KEY (game_appid) REFERENCES games (appid),
            FOREIGN KEY (currency_id) REFERENCES currencies (id)
        );
    """)
    conn.commit()
    conn.close()


def upsert_game(json_data):
    conn = sqlite3.connect("steam_database_prices.db")
    cursor = conn.cursor()

    # Upsert game
    cursor.execute(
        "INSERT OR REPLACE INTO games (appid, name) VALUES (?, ?)",
        (json_data["appid"], json_data["name"]),
    )

    # Upsert game prices, for each currency insert value.
    for currency_code, price in json_data["prices"].items():
        cursor.execute("""
            INSERT OR REPLACE INTO game_prices (game_appid, currency_id, price)
            VALUES (
                ?,
                (SELECT id FROM currencies WHERE code = ?),
                ?
            )
        """, (json_data["appid"], currency_code, price))

    conn.commit()
    conn.close()


def upsert_currencies(currencies):
    conn = sqlite3.connect("steam_database_prices.db")
    cursor = conn.cursor()

    for code, name in currencies.items():
        cursor.execute(
            "INSERT OR IGNORE INTO currencies (code, name) VALUES (?, ?)",
            (code, name),
        )

    conn.commit()
    conn.close()


def read_games(ids):
    conn = sqlite3.connect("steam_database_prices.db")
    cursor = conn.cursor()
    placeholders = ",".join("?" * len(ids))
    query = f"""
        SELECT g.appid, g.name, c.code, gp.price
        FROM games g
        JOIN game_prices gp ON g.appid = gp.game_appid
        JOIN currencies c ON gp.currency_id = c.id
        WHERE g.appid NOT IN ({placeholders})
    """
    cursor.execute(query, tuple(ids))

    rows = cursor.fetchall()

    for row in rows:
        print(f"AppID: {row[0]}, Name: {row[1]}, Currency: {row[2]}, Price: {row[3]}")

    conn.close()
    return rows


# Call the function with some tags
# games = get_games_from_tag('souls-like')


# game_prices = game_finding_function()
# print("game_prices")
# print(game_prices)


# game_prices = game_finding_with_appid(wishList)
# game_prices = game_finding_with_appid(wishList)

ids = [767930]
game_prices = game_finding_with_appid(ids)

errors = list(dict.fromkeys(csp.error_logs))

# create table if not exists
create_tables()

currencies = {
    "USD": "US Dollar",
    "TL": "Turkish Lira",
}

upsert_currencies(currencies)

read_games(ids)

for game in game_prices:
    if game["appid"] in csp.mapped_games:
        game["name"] = csp.mapped_games[game["appid"]]
    upsert_game(game)

sorted_list = sorted(game_prices, key=lambda x: x["price_dif"], reverse=True)

print(f"errors: {errors}")
print(game_prices)

end_time = datetime.datetime.now()

print(f"Runtime of the program is {end_time - start_time}.")
