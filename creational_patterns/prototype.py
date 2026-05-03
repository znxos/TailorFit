import copy

class PromptPrototype:
    def __init__(self, template: str, temperature: float, max_tokens: int):
        self.template = template
        self.temperature = temperature
        self.max_tokens = max_tokens

    def clone(self):
        # Perform deep copy to avoid reference sharing of complex internal objects
        return copy.deepcopy(self)

class PromptCache:
    def __init__(self):
        self._cache = {}

    def load_cache(self):
        self._cache['cover_letter_standard'] = PromptPrototype("Write a standard cover letter...", 0.5, 500)
        self._cache['resume_optimization'] = PromptPrototype("Optimize this resume...", 0.7, 1000)

    def get_prompt(self, key: str) -> PromptPrototype:
        return self._cache.get(key).clone() if key in self._cache else None