from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class Agent:
    def __init__(self, model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def analyze(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=300, do_sample=False, repetition_penalty=1.1,
                                      early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
