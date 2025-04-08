from models.base_agent import Agent


class TestAgent(Agent):
    def run(self, code: str) -> str:
        prompt = f"[INST] Check the following code and describe potential reasons for test failures. Mention possible edge cases and improvements:\n{code} [/INST]"
        return self.analyze(prompt)
