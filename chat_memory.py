class SlidingMemory:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.history = []

    def add(self, user_input, bot_response):
        self.history.append(("User", user_input))
        self.history.append(("Bot", bot_response))
        # Keep last N interactions
        if len(self.history) > self.window_size * 2:
            self.history = self.history[-self.window_size * 2:]

    def get_prompt(self, current_input):
        prompt = ""
        for speaker, text in self.history:
            prompt += f"{speaker}: {text}\n"
        prompt += f"User: {current_input}\nBot:"
        return prompt

    def print_memory(self):
        print("\n🧠 Memory:")
        for speaker, text in self.history:
            print(f"{speaker}: {text}")
        print()