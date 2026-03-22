import zipfile
import io
import textwrap
import black

from src.utils.context_optimizer import optimize_context
from src.utils.llm_client import generate_code
from src.dao.analyzer_dao import save_result


# FORMATTER FUNCTION (BEST PRACTICE)
def format_code_block(code: str) -> str:
    try:
        # Normalize indentation
        code = textwrap.dedent(code)

        # Format using Black
        formatted = black.format_str(code, mode=black.FileMode())

        return formatted
    except Exception:
        # Fallback if formatting fails
        code = code.replace("\r\n", "\n")
        return code.strip()


# MAIN ENTRY FUNCTION
def analyze_input(content: bytes, filename: str):

    # CASE 1: ZIP (MULTI-FILE / FOLDER)
    if filename.endswith(".zip"):
        return process_zip(content)

    # CASE 2: SINGLE FILE
    code = content.decode("utf-8", errors="ignore")
    return process_code(code)


# PROCESS ZIP FILES
def process_zip(content: bytes):
    z = zipfile.ZipFile(io.BytesIO(content))

    combined_code = ""

    for file in z.namelist():
        if file.endswith((".py", ".java", ".js", ".go")):
            try:
                with z.open(file) as f:
                    combined_code += f.read().decode("utf-8", errors="ignore") + "\n\n"
            except Exception:
                continue

    return process_code(combined_code)


# CORE PROCESSING LOGIC
def process_code(code: str):
    optimized = optimize_context(code)
    optimized = optimized.strip()

    generated = generate_code(optimized)

    before = len(code)
    after = len(optimized)

    reduction = int((1 - after / before) * 100) if before else 0

    # FORMATTED RESPONSE (HACKATHON READY)
    formatted_result = {
        "summary": {
            "total_input_size": before,
            "optimized_size": after,
            "reduction_percent": reduction
        },
        "sections": {
            "original_code": format_code_block(code[:1000]),
            "optimized_context": format_code_block(optimized[:1500]),
            "generated_output": generated.strip()
        },
        "insights": {
            "files_processed": "multiple" if before > 2000 else "single",
            "context_strategy": "important lines filtering",
            "llm_model": "codellama",
            "language": "python"
        }
    }

    return save_result(formatted_result)