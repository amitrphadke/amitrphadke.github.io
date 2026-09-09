from common import MODEL, client

class Chat:
    def __init__(self, system: str = "", model: str = MODEL):
        self.system, self.model = system, model
        self.history: list[dict] = []
        self.usage_log: list[tuple[int, int]] = []

    def send(self, text: str, max_tokens: int = 300) -> str:
        # TODO: append user turn, call API with full history, record usage, append assistant turn, return text
        raise NotImplementedError

    def total_input_tokens(self) -> int:
        return sum(i for i, _ in self.usage_log)

if __name__ == "__main__":
    c = Chat("You are terse.")
    for q in ["My name is Amit.", "I live in Pune.", "What is my name and city?"]:
        print(">", q); print(c.send(q))
    print(c.usage_log)
