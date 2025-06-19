# 🤖 Hugging Face Local Chatbot – flan-t5-base

This is a simple, modular, and customizable chatbot application built using Hugging Face's `transformers` library. It uses the instruction-tuned model **`google/flan-t5-base`** to generate natural-sounding responses and runs entirely on your local machine — no internet or API tokens required after model download.

This project is ideal for:
- Students learning how language models work
- Developers prototyping chatbot interfaces
- Anyone building offline NLP tools with limited compute resources

---

## ✨ Features

- ✅ Uses Hugging Face's `pipeline()` with a locally downloaded model
- 🧠 Handles short-term memory (chat history context)
- 🧩 Modular code: easy to extend or replace the model
- ⚡ Auto-detects GPU (CUDA) and uses it if available
- 🔐 Supports `.env` file structure (for future API key integration)
- 💡 Great for instruction-style Q&A, definitions, and explanations

---

## 🧠 Model Overview

**Model used:** [`google/flan-t5-base`](https://huggingface.co/google/flan-t5-base)

- Pretrained by Google
- Instruction-tuned: understands commands like “explain,” “summarize,” “answer”
- Works well for:
  - General Q&A
  - Definitions
  - Simple conversation

---

## 🏗️ Folder Structure

