class AIAssistant:
    """Simple AI Assistant service (Week 11 demo version)."""

    def __init__(self, system_prompt: str = "You are a helpful assistant."):
        self._system_prompt = system_prompt
        self._history = []

    def send_message(self, user_message: str) -> str:
        """Generate a fake AI response (placeholder)."""
        self._history.append({"role": "user", "content": user_message})

        response = f"[AI Assistant]: I received your message → '{user_message}'"
        self._history.append({"role": "assistant", "content": response})

        return response

    def clear_history(self):
        self._history = []

    def get_history(self):
        return self._history