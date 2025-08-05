import fitz  # imports PyMuPDF to parse through text

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

print(extract_text_from_pdf(r"C:\Users\Taran\OneDrive\Documents\GitHub\uf-study-buddy\app\syllabi\MAC2311_Spring_2025.pdf"))
