import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import io
from PIL import Image

# --- Function to generate WordCloud ---
def generate_wordcloud(text, stopwords, max_words=100, colormap="viridis"):
    wc = WordCloud(width=800, height=400,
                    background_color="white",
                    stopwords=stopwords,
                    max_words=max_words,
                    colormap=colormap,
                    collocations=False)
    wc.generate(text)
    return wc

# --- Streamlit App ---
st.title("Interactive Word Cloud Generator")

# File uploader
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    # Basic WordCloud options
    stopwords = set(STOPWORDS)
    additional_stopwords = st.text_input("Enter additional stopwords (comma-separated):")
    if additional_stopwords:
        stopwords.update(additional_stopwords.split(","))
    max_words = st.slider("Max words:", 50, 200, 100)
    colormap = st.selectbox("Colormap:", plt.colormaps())

    # Generate WordCloud
    wc = generate_wordcloud(text, stopwords, max_words, colormap)

    # Display WordCloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
    st.write("WordCloud of your text file")


    # Download the WordCloud image
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    st.download_button('Download Image', data=image_stream, file_name="wordcloud.png")

