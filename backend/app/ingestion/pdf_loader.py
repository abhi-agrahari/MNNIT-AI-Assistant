from pathlib import Path

import pymupdf


def _resolve_pdf_path(file_path: str) -> str:

    candidate = Path(file_path)

    # if an absolute path is provided
    if candidate.is_absolute() and candidate.exists():
        return str(candidate.resolve())

    # College-RAG/
    project_root = Path(__file__).resolve().parents[3]

    search_roots = [
        Path.cwd(),
        project_root,
        project_root / "backend",
    ]

    # try the provided relative path
    for root in search_roots:
        absolute_path = (root / candidate).resolve()

        if absolute_path.exists() and absolute_path.is_file():
            return str(absolute_path)

    # if the path was not found, search by filename
    if candidate.name:
        for root in search_roots:
            if not root.exists():
                continue

            for match in root.rglob(candidate.name):
                if match.is_file() and match.name.lower() == candidate.name.lower():
                    return str(match.resolve())

    raise FileNotFoundError(
        f"PDF not found: '{file_path}'"
    )


def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF page by page.

    Returns:
        A list of dictionaries containing:
        - page_number
        - text
    """

    resolved_path = _resolve_pdf_path(file_path)

    document = pymupdf.open(resolved_path)

    pages = []

    try:
        for page_number, page in enumerate(document):
            text = page.get_text("text")

            pages.append({
                "page_number": page_number,
                "text": text
            })
    finally:
        document.close()

    return pages