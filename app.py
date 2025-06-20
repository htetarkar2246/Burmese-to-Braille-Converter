from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader
import docx2txt
import io
import base64
import docx

app = Flask(__name__)

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
    return ''.join(braille_dict.get(c, c) for c in text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text_input = request.form.get("text", "").strip()
    file = request.files.get("file")

    extracted_text = text_input

    if file:
        if file.filename.endswith('.pdf'):
            reader = PdfReader(file)
            extracted_text += "\n" + "".join([page.extract_text() or "" for page in reader.pages])
        elif file.filename.endswith('.docx'):
            extracted_text += "\n" + docx2txt.process(file)
        elif file.filename.endswith('.txt'):
            extracted_text += "\n" + file.read().decode("utf-8")

    braille_text = convert_to_braille(extracted_text)

    doc = docx.Document()
    doc.add_paragraph(braille_text)
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    encoded_docx = base64.b64encode(buffer.read()).decode("utf-8")

    return jsonify({"braille": braille_text, "docx": encoded_docx})

if __name__ == '__main__':
    app.run(debug=True)
