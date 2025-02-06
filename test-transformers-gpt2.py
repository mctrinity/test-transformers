from transformers import AutoTokenizer

# Increase timeout to avoid network issues
tokenizer = AutoTokenizer.from_pretrained("gpt2", timeout=60)

texts = [
    "apple",
    "unhappiness",
    "transformers",
    "antidisestablishmentarianism",
    "Hello, how are you doing today?",
]

for text in texts:
    tokens = tokenizer.tokenize(text)
    print(f"Text: {text}\nTokens: {tokens}\n")
