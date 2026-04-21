#!/usr/bin/env python3
"""
Terminal Chat Interface for Gemini AI
"""

import requests
import json
import sys

class GeminiChat:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url
        self.conversation_history = []

    def send_message(self, message):
        """Send a message to the chatbot server"""
        try:
            response = requests.post(
                f"{self.server_url}/chat",
                json={"message": message},
                headers={"Content-Type": "application/json"}
            )

            if response.status_code == 200:
                data = response.json()
                return data.get('response', 'No response received')
            else:
                return f"Error: {response.status_code} - {response.text}"

        except requests.exceptions.RequestException as e:
            return f"Connection error: {e}"

    def start_chat(self):
        """Start the interactive chat session"""
        print("🤖 Gemini Chatbot Terminal Interface")
        print("====================================")
        print("Type 'quit' or 'exit' to end the conversation")
        print("Type 'history' to see conversation history")
        print("Type 'clear' to clear history")
        print()

        while True:
            try:
                user_input = input("You: ").strip()

                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye! 👋")
                    break

                elif user_input.lower() == 'history':
                    self.show_history()
                    continue

                elif user_input.lower() == 'clear':
                    self.conversation_history = []
                    print("Conversation history cleared.")
                    continue

                elif not user_input:
                    continue

                # Send message and get response
                print("Bot: Thinking...", end="", flush=True)
                response = self.send_message(user_input)
                print("\r" + " " * 20 + "\r", end="")  # Clear the "thinking" message

                print(f"Bot: {response}")

                # Store in history
                self.conversation_history.append({
                    'user': user_input,
                    'bot': response,
                    'timestamp': self.get_timestamp()
                })

            except KeyboardInterrupt:
                print("\nGoodbye! 👋")
                break
            except Exception as e:
                print(f"Error: {e}")

    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("No conversation history.")
            return

        print("\nConversation History:")
        print("=" * 50)
        for i, entry in enumerate(self.conversation_history, 1):
            print(f"{i}. [{entry['timestamp']}]")
            print(f"   You: {entry['user']}")
            print(f"   Bot: {entry['bot']}")
            print()
        print("=" * 50)

    def get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    if len(sys.argv) > 1:
        server_url = sys.argv[1]
    else:
        server_url = "http://localhost:5000"

    print(f"Connecting to server at: {server_url}")
    print("Make sure the Flask server is running!")
    print()

    chat = GeminiChat(server_url)
    chat.start_chat()

if __name__ == "__main__":
    main()