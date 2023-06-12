import asyncio
import re
from EdgeGPT import Chatbot, ConversationStyle


def extract_text(input_string):
    # Search for text between quotes using regex
    match = re.search(r'"(.*?)"', input_string)

    # If there is a match, get the matched text as a string
    if match:
        extracted_text = match.group(1)
        return extracted_text
    else:
        return input_string


def get_response_text(response):
    print(response)
    for message in response["item"]["messages"]:
        # Check if the author is bot
        if message["author"] == "bot" and message["contentOrigin"] != "Apology":
            # Print the text value from tht message
            return extract_text(message["text"])
    return "no match"


async def get_edge_gpt_response(prompt):
    print("prompt")
    print(prompt)
    bot = Chatbot(cookiePath='/home/azsharax/PycharmProjects/tsundereProject/cookies.json')
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
    await bot.close()
    return get_response_text(response)


def main_character_talk(text):
    return " Main character says: " + text + ", tsundere says: "


async def get_text_with_response(prompt, counter):
    response_str = str(await get_edge_gpt_response(prompt))
    if response_str == "no match" and counter < 3:
        counter += 1
        await get_text_with_response(prompt, counter)
    if response_str != "no match":
        return response_str
    if counter <= 3:
        Exception("Get_text_failed 3 times for: ", response_str)


async def main():
    prompt = "Help me write this anime script. (Put reply in Quotes) " \
             "There is a tsundere girl, and main character says, hi. And tsundere girl says:"
    response_text = await get_text_with_response(prompt, 0)
    print("edge_response 1")
    print(response_text)
    prompt += response_text
    prompt += main_character_talk("You look beautiful today.")
    response_text = await get_text_with_response(prompt, 0)
    print("edge_response 2")
    print(response_text)


if __name__ == "__main__":
    asyncio.run(main())
