from transformers import AutoTokenizer

# Load RoBERTa tokenizer
roberta_tokenizer = AutoTokenizer.from_pretrained("roberta-base")

# Example words and phrases
texts = [
    "apple",  # Common word
    "unhappiness",  # Uncommon word, likely split
    "transformers",  # Model-related word
    "antidisestablishmentarianism",  # Very long word
    "Hello, how are you doing today?",  # Full sentence
]

# Tokenize and show results
for text in texts:
    tokens = roberta_tokenizer.tokenize(text)
    print(f"Text: {text}\nTokens: {tokens}\n")
