print("AI Chatbot")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("AI: Hello! How can I help you?")
    elif user.lower() == "how are you":
        print("AI: I am fine. Thank you!")
    elif user.lower() == "bye":
        print("AI: Goodbye!")
        break
    else:
        print("AI: Sorry, I don't understand.")
