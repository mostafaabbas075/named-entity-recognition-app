import streamlit as st
import spacy
from spacy import displacy

# Radio buttons for model selection
model_choice = st.radio("Choose a spaCy model", ('en_core_web_sm', 'en_core_web_md'))

# Cache loading for efficiency
@st.cache_resource
def load_model(model_name):
    return spacy.load(model_name)

# Load selected model
nlp = load_model(model_choice)

# Text input
user_input = st.text_area("Enter text for NER", "Apple was founded by Steve Jobs in California in 1976.")

# Perform NER and visualize
if st.button("Extract Entities"):
    doc = nlp(user_input)

    # Show extracted entities
    st.subheader("Named Entities:")
    for ent in doc.ents:
        st.write(f"{ent.text} — {ent.label_}")

    # Visualize with displacy
    st.subheader("Entity Visualization:")
    html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(html, unsafe_allow_html=True)
