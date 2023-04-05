import openai

openai.api_key = "Your-api-goes-here"
while(True):
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "goodbye"]:
        print("Chatbot: Goodbye!")
        break
    messages = [
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": user_input},
                ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    result = ""

    for choice in response.choices:
        result += choice.message.content

    messages.append({"role":"system","content":result})
    print(result)
    


