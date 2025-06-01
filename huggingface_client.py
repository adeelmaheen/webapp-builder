import io
from PIL import Image
import torch
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    AutoModelForCausalLM,
    AutoTokenizer,
)

class ImageToTextCaptioning:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(self.device)

    def generate_caption(self, image_bytes: bytes) -> str:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        inputs = self.processor(image, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs)
        caption = self.processor.decode(outputs[0], skip_special_tokens=True)
        return caption


class TextToCodeGenerator:
    def __init__(self, model_name="EleutherAI/gpt-neo-125M"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def generate_code(self, prompt: str, max_length=512) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text[len(prompt):].strip()


class HuggingFaceClient:
    def __init__(self):
        self.captioner = ImageToTextCaptioning()
        self.generator = TextToCodeGenerator()

    def generate_code_from_image(self, image_bytes: bytes) -> str:
        caption = self.captioner.generate_caption(image_bytes)
        prompt = (
            f"Convert the following Streamlit app description into Python Streamlit code:\n"
            f"{caption}\n"
            f"Python code:"
        )
        code = self.generator.generate_code(prompt)
        return code

    def generate_code_from_text(self, prompt: str) -> str:
        prompt = f"Generate a Python Streamlit app code for the following description:\n{prompt}\nPython code:"
        code = self.generator.generate_code(prompt)
        return code
