# 🛠 Streamlit App Builder

Build Streamlit apps visually or with prompts — just **Show** or **Tell**!

![Streamlit Banner](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)

## 🚀 About the Project

**Streamlit App Builder** is a smart tool that helps developers rapidly generate Streamlit app code using either:
- 🖼️ A **mock-up image**
- 📝 A **textual prompt**

Ideal for developers, designers, or beginners who want to prototype and build Streamlit apps in seconds.

---

## 🎯 Features

- 📷 Upload a UI mock-up or choose from built-in examples
- ✍️ Write a text prompt describing your app
- 🤖 Leverages Hugging Face models to generate working Streamlit code
- 🧠 Smart fallback if no valid image/text is given
- 🔍 Tabs-based UI for intuitive flow
- 🛠 Example mockups built-in for testing

---

## 🧩 How It Works

- `Show` tab:
  - Upload your own image or use example images
  - Automatically generates app code using Hugging Face's Vision Models

- `Tell` tab:
  - Describe the functionality of your app in plain English
  - Generates Python code using Hugging Face's NLP models

---

## 📁 Project Structure


```bash
├── streamlit_app.py         # Main app logic
├── mockup_code.py           # Contains example UI code for mockup images
├── huggingface_client.py    # Handles image/text code generation using HF models
├── img/
│   ├── streamlit-app-mockup-1.png
│   └── streamlit-app-mockup-2.png

```
## ⚙️ Requirements
- Python 3.8+
- streamlit
- streamlit-image-select
- Your Hugging Face API credentials
pip install -r requirements.txt

## 🧪 Run Locally
streamlit run streamlit_app.py

## 💡 Example Use Cases
- Rapid prototyping from UI sketches
- Non-coders transforming app ideas into real code
- Designers and developers collaborating visually

## 🧠 Powered By
- Streamlit
- Hugging Face
- streamlit-image-select

## 🙌 Contribute
- Have ideas to improve this builder? PRs are welcome!
```bash 
# Fork & Clone
git clone https://github.com/yourusername/streamlit-app-builder.git
```

## 📜 License
- MIT License © 2025

## 📬 Contact
- Made with ❤️ by Maheen Arif – [adeelmaheen602@gmail.com]
- Follow me on GitHub
