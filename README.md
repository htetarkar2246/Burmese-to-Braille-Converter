# Burmese to Braille Converter

A modern and accessible web application that allows users to convert Burmese text or uploaded documents (PDF, DOCX, TXT) into Braille output. This tool is designed with real-world Braille printing considerations in mind—both the on-screen and downloadable outputs feature appropriately scaled font sizes (~3 mm) and increased line spacing for readability and print compatibility.

## 🌟 Features

-Input Burmese text via textarea or upload supported files (PDF, DOCX, TXT).

-File upload with easy removal option.

-Displays Braille output with large font size (~3.8mm) and generous line spacing for real-world usability.

-Downloadable Braille output as a styled DOCX file.

-Clean, responsive, and modern UI with fixed size text areas and scrollbars.

## 🔧 Technologies Used

- Frontend: HTML5, CSS3, Vanilla JavaScript
- Backend (example setup): Python + Flask (not included in this repo)
- File parsing: pdfplumber, python-docx, python-magic (server-side)
- Braille model: Integrated using Myanmar NLP Tool
- Output styling: DOCX with specified font size and spacing


## Acknowledgements
-This project uses the open-source Myanmar-NPL-Tool developed by Saya Phyo Thu Htet for Burmese natural language processing and Braille model.

-ChatGPT was used for coding style suggestions and UI vibe enhancements only.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/htetarkar2246/Burmese-to-Braille-Converter.git
cd burmese-braille-converter
```

(Optional) Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Install backend dependencies (if applicable):

```bash
pip install -r requirements.txt
```

Run your backend server (adjust command as per your setup):

```bash
flask run
```

## Usage
-Enter Burmese text in the textarea or upload a supported file.

-Use the Remove button to clear the uploaded file if needed.

-Click Convert to generate Braille output.

-View the Braille output in the styled output box with proper font size and spacing.

-Download the Braille output as a DOCX file using the Download Braille DOCX link.

