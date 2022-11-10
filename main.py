"""PDF to MP3 CONVERTER."""
import os
from tkinter import filedialog as fd
import pyttsx3
import pdfplumber


def mp3topdf():
    """Open a file and convert into mp3."""
    filetypes = (("PDF files", "*.pdf"),)
    filename = fd.askopenfilename(title="Choose PDF file to convert",
                                  filetypes=filetypes)
    dirname = os.path.dirname(filename)
    fn = os.path.splitext(filename)[0]
    fn = os.path.basename(fn)
    fn = f"{dirname}/{fn}.mp3"
    with pdfplumber.PDF(open(file=filename, mode="rb")) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
        text = "".join(pages)
        text = text.replace("\n", "")
        pdf.close()
    engine = pyttsx3.init()
    engine.save_to_file(text, filename=fn)
    engine.runAndWait()
    engine.stop()
    print(f"Файл {fn} успешно скомпилирован")


def main():
    """Execute Main function."""
    mp3topdf()


if __name__ == "__main__":
    main()
