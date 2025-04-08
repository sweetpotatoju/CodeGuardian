from models.base_agent import Agent


class DefectAgent(Agent):
    def run(self, code: str) -> str:
        prompt = f"[INST] Analyze the following code and identify any software bugs. Explain why they are problematic and suggest a fix:\n{code} [/INST]"
        return self.analyze(prompt)
