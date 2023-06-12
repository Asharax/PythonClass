import openai

openai.api_key = "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"

completion = openai.Completion.create(model="code-cushman-001",
                                      messages=[{"role": "user", "content": "Hello world"}],
                                      api_base="https://api.openai.com/v1")
print("completion")
print(completion)

# print the completion
print("completion.choices[0].message.content")
print(completion.choices[0].message.content)

"""
def chat_with_chatgpt(prompt):
    res = requests.post(f"https://api.openai.com/v1/engines/{model}/jobs", headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }, json={
        "prompt": prompt  # your input text
    })
    return res.json()  # your output text


# Set up your OpenAI API key
prompt = "In one sentence, what is quantum computing? (one line answer)"
response = chat_with_chatgpt(prompt)
print("response")
print(response)
print("response.text")
print(response.text)

# Create a chatbot object with creative style and low temperature
# chatbot = openai.Chatbot(model="gpt-3.5-turbo", engine="davinci", conversation_style="creative", temperature=0.2)
"""
