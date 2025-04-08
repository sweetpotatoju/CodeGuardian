from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
device = "cuda" if torch.cuda.is_available() else "cpu"

# ✅ 모델 & 토크나이저 한 번만 로드
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def generate_response(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(device)
    outputs = model.generate(**inputs, max_new_tokens=300, do_sample=False, repetition_penalty=1.1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def analyze_all(code: str):
    def inst(task): return f"[INST] {task}\n{code} [/INST]"
    return {
        "defect": generate_response(inst("Analyze defects and suggest fixes.")),
        "security": generate_response(inst("Review for security vulnerabilities.")),
        "test_failure": generate_response(inst("Explain possible test failures.")),
    }
