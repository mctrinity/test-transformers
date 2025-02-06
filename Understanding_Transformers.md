# **Understanding Tokenization in GPT-2 and BERT**

## **Overview**
Tokenization is the process of breaking text into smaller units (tokens) that can be processed by a language model like GPT-2 or BERT. 
- The GPT-2 tokenizer uses **Byte Pair Encoding (BPE)**, which splits words into frequent subwords rather than using traditional whitespace-based word separation.
- The BERT tokenizer uses **WordPiece Encoding**, which segments words into smaller meaningful subwords.

---

## **Tokenization Results Explained**

### **1. Common Word**
**Input:** `"apple"`  
**GPT-2 Tokens:** `['apple']`  
**BERT Tokens:** `['apple']`  
**Expected Output:**
```bash
GPT-2: ['apple']
BERT: ['apple']
```
- Both tokenizers recognize "apple" as a frequent word, so it remains as **one token**.

---

### **2. Uncommon or Compound Word**
**Input:** `"unhappiness"`  
**GPT-2 Tokens:** `['un', 'h', 'appiness']`  
**BERT Tokens:** `['un', '##ha', '##pp', '##iness']`  
**Expected Output:**
```bash
GPT-2: ['un', 'h', 'appiness']
BERT: ['un', '##ha', '##pp', '##iness']
```
- GPT-2 splits based on **BPE subword merging**.
- BERT splits based on **WordPiece segmentation**, where `##` indicates subwords belong to the same original word.

---

### **3. Suffix Separation**
**Input:** `"transformers"`  
**GPT-2 Tokens:** `['transform', 'ers']`  
**BERT Tokens:** `['transformers']`  
**Expected Output:**
```bash
GPT-2: ['transform', 'ers']
BERT: ['transformers']
```
- GPT-2 breaks the word into **subword units**.
- BERT recognizes "transformers" as a **single known word** in its vocabulary.

---

### **4. Very Long Word**
**Input:** `"antidisestablishmentarianism"`  
**GPT-2 Tokens:** `['ant', 'idis', 'establishment', 'arian', 'ism']`  
**BERT Tokens:** `['anti', '##dis', '##est', '##ab', '##lish', '##ment', '##arian', '##ism']`  
**Expected Output:**
```bash
GPT-2: ['ant', 'idis', 'establishment', 'arian', 'ism']
BERT: ['anti', '##dis', '##est', '##ab', '##lish', '##ment', '##arian', '##ism']
```
- GPT-2 **splits words into common subword patterns**.
- BERT **uses WordPiece segmentation** to break long words efficiently.

---

### **5. Sentence with Spaces and Punctuation**
**Input:** `"Hello, how are you doing today?"`  
**GPT-2 Tokens:** `['Hello', ',', 'Ġhow', 'Ġare', 'Ġyou', 'Ġdoing', 'Ġtoday', '?']`  
**BERT Tokens:** `['hello', ',', 'how', 'are', 'you', 'doing', 'today', '?']`  
**Expected Output:**
```bash
GPT-2: ['Hello', ',', 'Ġhow', 'Ġare', 'Ġyou', 'Ġdoing', 'Ġtoday', '?']
BERT: ['hello', ',', 'how', 'are', 'you', 'doing', 'today', '?']
```
- GPT-2 **uses `Ġ` to mark spaces**.
- BERT does **not explicitly mark spaces** and lowercases text in `bert-base-uncased`.

---

## **Key Takeaways**
✔ **GPT-2 uses Byte Pair Encoding (BPE)**, which merges common subwords.
✔ **BERT uses WordPiece Encoding**, which prioritizes a smaller vocabulary with subword tokens.
✔ **GPT-2 marks spaces with `Ġ`**, while **BERT does not**.
✔ **BERT lowercases text (for `bert-base-uncased`)**, while **GPT-2 keeps case sensitivity**.
✔ **Punctuation remains separate in both models**.

---

## **Test More Words**
To experiment with tokenization, try running:
```python
words = ["GPT-3", "supercalifragilisticexpialidocious", "AI-powered", "discombobulated"]
for word in words:
    print(f"{word} → {tokenizer.tokenize(word)}")
```

This will help you understand how different words are broken into tokens!

Let me know if you need more details! 🚀

