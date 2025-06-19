from model_loader import rf
from chat_memory import SlidingMemory

def main():
    memory = SlidingMemory(window_size=5)
    print("\n🤖 Chatbot is ready! Type your message (type '/exit' to quit):\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit", "bye", "/exit", "/quit", "/bye"]:
                print("🤖 Chatbot: Goodbye! 👋")
                break

            # Generate prompt using memory
            prompt = memory.get_prompt(user_input)

            print("\n🤖 Chatbot (thinking...)\n")

            # Get model response
            response = rf.invoke(prompt)

            # Clean up response (cut anything before 'Bot:' if repeated)
            if "Bot:" in response:
                response = response.split("Bot:")[-1].strip()

            print(f"🤖 Chatbot: {response}\n")

            # Update memory
            memory.add(user_input, response)

            # Optional: print memory
            # memory.print_memory()

        except KeyboardInterrupt:
            print("\n🤖 Chatbot: Session interrupted. Goodbye! 👋")
            break

        except Exception as e:
            print(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    main()
