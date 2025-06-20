import streamlit as st
import docx
import io
from PyPDF2 import PdfReader
import docx2txt

# Braille dictionary
braille_dict = {
    'က': '⡁', 'ခ': '⢈', 'ဂ': '⠛', 'ဃ': '⠟', 'င': '⡈', 'စ': '⡌', 'ဆ': '⡤',
    'ဇ': '⠵', 'ဈ': '⣌', 'ည': '⠷', 'ဋ': '⠳', 'ဌ': '⠻', 'ဍ': '⠾', 'ဎ': '⠿',
    'ဏ': '⡬', 'တ': '⠞', 'ထ': '⠚', 'ဒ': '⠙', 'ဓ': '⠋', 'န': '⠝', 'ပ': '⡖',
    'ဖ': '⠰', 'ဗ': '⢉', 'ဘ': '⠃', 'မ': '⡉', 'ယ': '⠽', 'ရ': '⠗', 'လ': '⠇',
    'ဝ': '⠺', 'သ': '⠹', 'ဟ': '⠓', 'ဠ': '⠸', 'အ': '⠣', 'ဉ': '⠧', 'ဤ': '⠰⠪',
    '၍': '⠯', '၏': '⠕', '၌': '⠦', '၎င်း': '⠬', '၊': '?', '။': '?', 'ာ': '⠁',
    'ါ': '⠎', 'ိ': '⠊', 'ီ': '⠪', 'ု': '⠑', 'ူ': '⠥', 'ေ': '⠱', 'ဲ': '⠡',
    '?': '⠴', 'ံ': '⠉', 'င်္': '⡈⠄⠤', 'ျ': '⠔', 'ဥ': '⠰⠑', 'ဦး': '⠰⠑⠪⠆',
    'ဧ': '⠰⠱', 'ဣ': '⠰⠊', 'ြ': '⠢', '်': '⠄', 'ွ': '⠜', 'ှ': '⠭', '့': '⠂',
    '္': '⠤', 'း': '⠆'
}

def convert_to_braille(text):
    return ''.join(braille_dict.get(char, char) for char in text)

st.title("Burmese to Braille Converter")

# Manual input
input_text = st.text_area("Enter Burmese text", height=200)

# File upload
uploaded_file = st.file_uploader("Or upload a file (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

# Initialize extracted text
file_text = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        file_text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        file_text = docx2txt.process(uploaded_file)
    elif uploaded_file.type == "text/plain":
        file_text = uploaded_file.read().decode("utf-8")
    else:
        st.warning("Unsupported file type")

# Combine manual + file text
final_text = input_text.strip() + "\n" + file_text.strip()

if final_text.strip():
    st.subheader("Original Text")
    st.text(final_text)

    # Convert
    braille_result = convert_to_braille(final_text)
    st.subheader("Braille Output")
    st.text(braille_result)

    # Save to DOCX
    output_doc = docx.Document()
    output_doc.add_paragraph(braille_result)
    output_stream = io.BytesIO()
    output_doc.save(output_stream)
    output_stream.seek(0)

    st.download_button("Download Braille DOCX", data=output_stream, file_name="braille_output.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
else:
    st.info("Please enter text or upload a file.")
