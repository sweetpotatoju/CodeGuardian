from models.base_agent import Agent


class SecurityAgent(Agent):
    def run(self, code: str) -> str:
        prompt = (f"[INST] Review the following code for security vulnerabilities. Explain each issue clearly and "
                  f"propose how to fix it:\n{code} [/INST]")
        return self.analyze(prompt)
