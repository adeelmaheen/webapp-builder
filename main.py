import base64
import streamlit as st
from streamlit_image_select import image_select
from mockup_code import mockup_1, mockup_2
from huggingface_client import HuggingFaceClient


class StreamlitAppBuilder:
    def __init__(self, api_client: HuggingFaceClient):
        self.api_client = api_client

    def run(self):
        st.set_page_config(page_title="🛠 Streamlit App Builder", page_icon="🛠")
        st.title("🛠 Streamlit App Builder")
        st.info("You can **Show** (upload mock-up image) or **Tell** (text prompt) how you want your Streamlit app built.")

        tabs = st.tabs(["Show", "Tell"])

        with tabs[0]:
            self.show_tab()

        with tabs[1]:
            self.tell_tab()

    def show_tab(self):
        upload_img = st.checkbox("Upload your own mock-up images")
        example_img = st.checkbox("Try example mock-up images")

        image_upload = None
        img = None

        if upload_img:
            st.subheader("Upload your own mock-up image")
            image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

        if example_img:
            st.subheader("Try these example mock-up images")
            img = image_select(
                label="Select a mock-up image",
                images=[
                    "img/streamlit-app-mockup-1.png",
                    "img/streamlit-app-mockup-2.png",
                ],
            )

        start_button = st.button("Build", disabled=not (upload_img or example_img))

        if not (upload_img or example_img) and start_button:
            st.warning("Please upload or select a mock-up image.")
            return

        if start_button:
            if img:
                st.subheader("Input")
                st.image(img)
                st.subheader("Output")
                if img.endswith("mockup-1.png"):
                    mockup_1()
                elif img.endswith("mockup-2.png"):
                    mockup_2()
                else:
                    st.warning("No example code available for this image.")
            elif image_upload:
                with st.spinner("Generating code from image..."):
                    image_bytes = image_upload.read()
                    code = self.api_client.generate_code_from_image(image_bytes)
                    st.subheader("Generated Code")
                    st.code(code, language="python")
            else:
                st.warning("Please upload or select a mock-up image.")

    def tell_tab(self):
        text_prompt = st.text_area(
            "Describe details on the functionalities of the Streamlit app you want to build.", "", height=240
        )

        st.expander("Expand to see system prompt").markdown(
            "You are an experienced Python developer who can build amazing Streamlit apps. "
            "You will be given a text prompt describing the app to build, and you will generate the Python code accordingly."
        )

        start_button = st.button("Build from Text")

        if start_button:
            if not text_prompt.strip():
                st.warning("Please provide your text prompt.")
                return
            with st.spinner("Generating code ..."):
                try:
                    code = self.api_client.generate_code_from_text(text_prompt)
                    st.subheader("Generated Code")
                    st.code(code, language="python")
                except Exception as e:
                    st.error(f"Error during generation: {e}")


def main():
    hf_client = HuggingFaceClient()
    app = StreamlitAppBuilder(hf_client)
    app.run()


if __name__ == "__main__":
    main()
