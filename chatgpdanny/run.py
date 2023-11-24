import openai
import sys
import threading
import time
import argparse

from client import DummyClient, OpenAIClient
from utils import read_object

def parse_options(notebook = False):
    parser = argparse.ArgumentParser(description='ChatGPDanny') 
    parser.add_argument('--client', type=str, default='openai', help='Client to use')

    args = parser.parse_args()
    return args

def main(args):


    openai_api_key = read_object('openai_api_key.txt')
    instructions = read_object('instructions.txt')

    if args.client == 'openai':
        Client = OpenAIClient
    elif args.client == 'dummy':
        Client = DummyClient
    else:
        raise ValueError(f'Unknown client: {args.client}')

    client = Client(instructions, openai_api_key)


    print("\n\n### Welkom bij ChatGPDanny! Oneindig veel Vrijdagsvoetbalshows! ###\n\nTyp hieronder een verzoek voor een bericht over de Vrijdagse Voetbalshow:\n")

    while True:
        user_input = input("U:" + " "*12)
        print("\n")

        if "Daaag" in user_input.lower():
            print("ChatGPDanny: " + "Daaaaaaaaaaaag")
            break

        client.send_user_input(user_input)
        response = client.get_assistant_response()
        print("ChatGPDanny: " + response, "\n\n")


if __name__ == "__main__":
    args = parse_options()
    main(args)
