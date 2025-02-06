from transformers import AutoTokenizer

# Load BERT tokenizer (uncased version)
bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

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
    tokens = bert_tokenizer.tokenize(text)
    print(f"Text: {text}\nTokens: {tokens}\n")
