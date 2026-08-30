import pymupdf

def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF page by page.

    Returns:
        A list of dictionaries where each dictionary
        represents one page.
    """

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text("text")

        pages.append({
            "page_number": page_number,
            "text": text
        })

    document.close()

    return pages