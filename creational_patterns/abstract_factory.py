from abc import ABC, abstractmethod

class SystemPrompt(ABC): pass
class UserPrompt(ABC): pass

class ProfessionalSystemPrompt(SystemPrompt): pass
class ProfessionalUserPrompt(UserPrompt): pass
class CreativeSystemPrompt(SystemPrompt): pass
class CreativeUserPrompt(UserPrompt): pass

class PromptFactory(ABC):
    @abstractmethod
    def create_system_prompt(self) -> SystemPrompt: pass
    @abstractmethod
    def create_user_prompt(self) -> UserPrompt: pass

class ProfessionalPromptFactory(PromptFactory):
    def create_system_prompt(self) -> SystemPrompt:
        return ProfessionalSystemPrompt()
    def create_user_prompt(self) -> UserPrompt:
        return ProfessionalUserPrompt()

class CreativePromptFactory(PromptFactory):
    def create_system_prompt(self) -> SystemPrompt:
        return CreativeSystemPrompt()
    def create_user_prompt(self) -> UserPrompt:
        return CreativeUserPrompt()