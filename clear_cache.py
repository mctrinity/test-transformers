import shutil
import os
from transformers import AutoTokenizer

# Determine the cache directory based on OS
if os.name == "nt":  # Windows
    cache_dir = os.path.join(os.getenv("LOCALAPPDATA"), "huggingface", "transformers")
else:  # Linux/Mac
    cache_dir = os.path.expanduser("~/.cache/huggingface")

# Clear cache if it exists
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print("Cache cleared successfully!")

# Reload tokenizers for GPT-2, BERT, and RoBERTa
models = ["gpt2", "bert-base-uncased", "roberta-base"]
for model in models:
    tokenizer = AutoTokenizer.from_pretrained(model)
    print(f"Tokenizer for {model} loaded successfully!")
