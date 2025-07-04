def chatbot():
    """sample chatbot function that returns a greetings.
    """
    print("Chatbot: hello! I am Chatbot, Type 'bye' to exit.")

    while True:
        user_input = str(input("You: ")).lower()

        if user_input in ["hi", "hello"]:
            print("Chartbot: Hello! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! Thanks for asking.")
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I am a simple Python chatbot.")
        elif "joke" in user_input:
            print("chatbot: Why did the computer go to the doctor? Because it had a virus!")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")

#run the chatbot
chatbot()