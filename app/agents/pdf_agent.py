from pathlib import Path
from app.tools.pdf_tool import read_pdf


PDF_FOLDER = "papers"


def search_pdfs():

    results = []

    pdf_dir = Path(PDF_FOLDER)

    if not pdf_dir.exists():
        return results

    for pdf_file in pdf_dir.glob("*.pdf"):

        try:

            data = read_pdf(str(pdf_file))

            results.append(
                {
                    "title": data["file_name"],
                    "content": "\n".join(
                        p["content"]
                        for p in data["pages"][:3]
                    )
                }
            )

        except Exception:
            pass

    return results