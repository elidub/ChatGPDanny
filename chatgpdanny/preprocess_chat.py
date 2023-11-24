import re
import argparse

from utils import read_object

def parse_options(notebook = False):
    parser = argparse.ArgumentParser(description='Preprocess WhatsApp data') 
    parser.add_argument('--danilo_name', type=str, default='Kast', help='Name how Danilo is in your WhatsApp')
    args = parser.parse_args()
    return args

def parse_messages(file_content):
    # Regular expression to match the pattern of each message
    message_pattern = r'\[(\d{2}-\d{2}-\d{4}) (\d{2}:\d{2}:\d{2})\] (.*?): (.*)'

    # Split the content into lines
    lines = file_content.split('\n')

    # Dictionary to store the parsed messages
    messages = []

    # Temporary variables to store multi-line message details
    current_date, current_time, current_sender = None, None, None
    current_message = []

    for line in lines:
        match = re.match(message_pattern, line)
        if match:
            # If a new message starts, store the previous one if it exists
            if current_message:
                messages.append({
                    "date": current_date,
                    "time": current_time,
                    "sender": current_sender,
                    "message": ' '.join(current_message)
                })
            # Update current message details
            current_date, current_time, current_sender, message_content = match.groups()
            current_message = [message_content]
        else:
            # If the line is part of a multi-line message
            current_message.append(line)

    # Add the last message if it exists
    if current_message:
        messages.append({
            "date": current_date,
            "time": current_time,
            "sender": current_sender,
            "message": ' '.join(current_message)
        })

    return messages

def main(args):

    chat = read_object('chat.txt')
    chat = chat.encode('ascii', 'ignore').decode('utf-8') # Change encoding, remove emojis?
    data = parse_messages(chat)


    # Filter out messages from Danilo that are too short
    data = [d for d in data if d['sender'] == args.danilo_name and len(d['message']) > 250]

    # Join the messages with a separator
    sep = '\n\n---\n\n'
    messages = sep.join([d['message'] for d in data])

    # Save the messages to a file
    with open('store/messages.txt', 'w') as f:
        f.write(messages)
        f.close()


if __name__ == "__main__":
    args = parse_options()
    main(args)