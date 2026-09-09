from common import MODEL, client

class Chat:
    def __init__(self, system: str = "", budget_tokens: int = 1500, model: str = MODEL):
        self.system, self.budget, self.model = system, budget_tokens, model
        self.history, self.compactions = [], 0

    def _tokens(self) -> int:
        # TODO: client().messages.count_tokens(model=..., messages=self.history, system=... or omitted).input_tokens
        raise NotImplementedError

    def _compact(self):
        # TODO: summarise everything except the last 2 messages with a Haiku call; rebuild history
        raise NotImplementedError

    def send(self, text: str, max_tokens: int = 200) -> str:
        # TODO: append; if self._tokens() > self.budget: self._compact(); call; append; return text
        raise NotImplementedError
