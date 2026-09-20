import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖"
)

st.title("🤖 AI Text Generator")
st.write("Generate text using a pretrained Generative AI model.")

# Load model
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small"
    )

generator = load_model()

# User input
topic = st.text_area(
    "Enter a topic:",
    placeholder="Example: Artificial Intelligence in Education"
)

# Generation options
length = st.selectbox(
    "Choose output length:",
    ["Short", "Medium", "Detailed"]
)

# Generate button
if st.button("✨ Generate Text"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        prompt = f"""
        Write a {length.lower()} explanation about:

        {topic}

        Make the response clear and easy to understand.
        """

        with st.spinner("Generating..."):

            result = generator(
                prompt,
                max_new_tokens=150
            )

        generated_text = result[0]["generated_text"]

        st.subheader("📝 Generated Text")

        st.write(generated_text)
