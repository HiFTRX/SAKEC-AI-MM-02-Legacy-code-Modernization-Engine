import re
from src.core.config import MAX_CONTEXT_LINES

def optimize_context(code: str) -> str:
    lines = code.split("\n")

    # Remove comments
    lines = [l for l in lines if not l.strip().startswith("#")]

    # Remove empty lines
    lines = [l for l in lines if l.strip()]

    # Normalize spaces
    lines = [re.sub(r"\s+", " ", l) for l in lines]

    return "\n".join(lines[:MAX_CONTEXT_LINES])