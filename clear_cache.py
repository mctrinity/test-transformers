from transformers.utils import cached_file
from transformers import AutoTokenizer

# Clear cache
import shutil
import os

cache_dir = os.path.expanduser("~/.cache/huggingface")
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)

# Try downloading again
tokenizer = AutoTokenizer.from_pretrained("gpt2")
print("Tokenizer loaded successfully!")
