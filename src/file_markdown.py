

def extract_title(doc: str):
    lines = doc.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found in document")