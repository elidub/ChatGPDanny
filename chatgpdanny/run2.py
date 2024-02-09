import time
import sys
import threading

def blinking_text():
    BLINK_ON = "\033[5m"
    BLINK_OFF = "\033[25m"
    END = "\033[0m"
    while not processing_done:
        sys.stdout.write('ChatGPDanny: Aan het typen' + '  ' + '\r')
        time.sleep(0.2)
        sys.stdout.write('ChatGPDanny: Aan het typen' + '.  ' + '\r')
        time.sleep(0.2)
        sys.stdout.write('ChatGPDanny: Aan het typen' + '.. ' + '\r')
        time.sleep(0.2)
        sys.stdout.write('ChatGPDanny: Aan het typen' + '...' + '\r')
        time.sleep(0.2)
    sys.stdout.write(' ' * 40 + '\r')  # Clear the blinking text

def chatbot_response(message):
    global processing_done
    processing_done = False

    # Simulate some processing time
    time.sleep(2)

    message = message.lower()
    if "hello" in message or "hi" in message:
        response = "Hello there! How can I help you?"
    elif "how are you" in message:
        response = "I'm just a bot, but thanks for asking! How can I help you today?"
    elif "bye" in message:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm not sure how to respond to that. Can you try asking something else?"

    processing_done = True
    return response

def main():
    print("Welcome to the simple chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        threading.Thread(target=blinking_text).start()
        response = chatbot_response(user_input)
        print("ChatGPDanny: " + response)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    processing_done = False
    main()
