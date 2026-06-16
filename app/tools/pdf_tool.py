from pathlib import Path
from pypdf import PdfReader


def read_pdf(pdf_path: str) -> dict:
    """
    Read PDF and return metadata + content.
    """

    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    reader = PdfReader(str(pdf_file))

    content = []

    for idx, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:
            content.append(
                {
                    "page": idx + 1,
                    "content": text
                }
            )

    return {
        "file_name": pdf_file.name,
        "total_pages": len(reader.pages),
        "pages": content
    }