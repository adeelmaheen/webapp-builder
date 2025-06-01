# 🛠 Streamlit App Builder with Hugging Face Local Models

This project builds Streamlit apps from mock-up images or text prompts using Hugging Face local language models on CPU.

## Features

- Upload or select mock-up images (currently no image-to-code support, example mockups shown)
- Generate Streamlit app code from text prompts using GPT-Neo 125M locally
- No API keys or cloud usage, runs fully on your CPU
- OOP clean design with easy extension

## Setup

1. Create and activate a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
