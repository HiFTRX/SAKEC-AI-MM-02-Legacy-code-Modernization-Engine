from fastapi import APIRouter, UploadFile, File, Form
from src.service.analyzer_service import analyze_input, process_zip
from src.dao.analyzer_dao import get_all_results
import requests

router = APIRouter(prefix="/analyze", tags=["Analyzer"])


# FILE / ZIP UPLOAD
@router.post("/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename

    result = analyze_input(content, filename)
    return result


# GITHUB REPO SUPPORT (STEP 3)
@router.post("/repo")
async def analyze_repo(url: str = Form(...)):
    try:
        # Convert GitHub repo to ZIP
        zip_url = url.rstrip("/") + "/archive/refs/heads/main.zip"

        response = requests.get(zip_url)

        if response.status_code != 200:
            return {"error": "Failed to fetch repository"}

        content = response.content

        return process_zip(content)

    except Exception as e:
        return {"error": str(e)}

@router.get("/history")
async def history():
    return get_all_results()