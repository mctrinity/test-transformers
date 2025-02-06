# **Transformers Setup and Usage Guide**

## **1. Overview**
This guide provides step-by-step instructions to set up the `transformers` library, install dependencies, and run tokenization experiments using pre-trained models.

---

## **2. Installation Steps**
### **Install Required Libraries**
Run the following command to install the necessary packages:
```bash
pip install transformers torch requests
```

- `transformers` → The Hugging Face library for NLP models.
- `torch` → Required for running PyTorch-based models.
- `requests` → Used for downloading models from Hugging Face.

### **Verify Installation**
Check if the installation was successful by running:
```python
from transformers import AutoTokenizer

print("Transformers installed successfully!")
```

---

## **3. Models Used**
We used the following pre-trained models in our experiments:

| **Model Name** | **Use Case** |
|--------------|-------------|
| `gpt2` | Tokenization and text generation |
| `bert-base-uncased` | Tokenization and embeddings |
| `roberta-base` | Improved tokenization with RoBERTa |

To download and use any model, modify the `AutoTokenizer` call as follows:
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
```

---

## **4. Running Tokenization Tests**
To tokenize words and sentences, use:
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = "Hello, how are you doing today?"
tokens = tokenizer.tokenize(text)
print(tokens)
```

Expected output:
```bash
['Hello', ',', 'Ġhow', 'Ġare', 'Ġyou', 'Ġdoing', 'Ġtoday', '?']
```

---

## **5. Troubleshooting**
### **Issue: Slow Downloads or Timeout Errors**
- Increase timeout:
  ```python
  tokenizer = AutoTokenizer.from_pretrained("gpt2", timeout=60)
  ```
- Ensure `huggingface.co` is accessible from your network.

### **Issue: `torch` Not Found**
- Run:
  ```bash
  pip install torch
  ```

### **Issue: Corrupt Cache**
- Clear cache and retry:
  ```python
  import shutil, os
  cache_dir = os.path.expanduser("~/.cache/huggingface")
  shutil.rmtree(cache_dir)
  print("Cache cleared!")
  ```

---

## **6. `requirements.txt`**
To ensure all dependencies are installed, create a `requirements.txt` file:
```txt
transformers
torch
requests
```
Then install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## **7. Next Steps**
- Try other models like `roberta-base` and `bert-base-uncased`.
- Explore text generation with `GPT-2`.
- Experiment with embeddings and fine-tuning.

For more information, visit: [Hugging Face Documentation](https://huggingface.co/docs/transformers/index) 🚀

