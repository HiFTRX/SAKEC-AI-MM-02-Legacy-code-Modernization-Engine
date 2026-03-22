# Legacy Code Modernization Engine

An intelligent developer tool designed to **modernize legacy codebases** using AI while minimizing hallucinations through **context optimization**.

This system processes legacy code (COBOL, old Java, etc.), extracts only the **relevant dependencies**, and generates structured insights, improvements, and modern equivalents using a local LLM.

---

## Problem Statement

Modern enterprises maintain **large legacy codebases** that are difficult to upgrade.  

Directly feeding entire repositories into LLMs leads to:
- Context overflow  
- Irrelevant noise (comments, dead code)  
- Hallucinated outputs  

---

## Solution

This project implements a **Context Optimization Engine** that:

- Filters only **important code components**
- Reduces token usage significantly
- Improves LLM accuracy
- Supports **multi-file repositories**

---

## Features

- Upload single file  
- Upload full project (ZIP)  
- Analyze GitHub repositories  
- Context optimization (noise reduction)  
- AI-generated structured insights  
- Token reduction metrics  
- Analysis history tracking  
- Interactive frontend dashboard  

---

## Tech Stack

### Backend
- Python (FastAPI)
- Context Optimization Engine
- Local LLM via Ollama (e.g., CodeLlama / TinyLlama)

### Frontend
- React (Vite)
- Axios

### Utilities
- Black (code formatting)
- Zipfile (multi-file handling)

---

## Measurable Results

- Context Reduction: ~40–70% (after optimization)
- Faster inference due to smaller inputs
- Improved response accuracy
- Zero API cost (fully local LLM)

---

## Project Structure
legacy-code-modernization-engine/
│
├── backend/
│ ├── src/
│ │ ├── api/
│ │ ├── service/
│ │ ├── utils/
│ │ ├── dao/
│ │ └── main.py
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ └── services/
│
├── shared/
├── test/
├── README.md
└── requirements.txt


---

## Installing

### Clone Repository

git clone https://github.com/HiFTRX/SAKEC-AI-MM-02-Legacy-code-Modernization-Engine.git

---

### Backend Setup

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r ../requirements.txt


---

### Frontend Setup

cd ../frontend
npm install
npm install axios


---

## Executing Program

### Start Backend


python -m uvicorn src.main:app --reload


Backend runs on:

http://127.0.0.1:8000


---

### Start Frontend


cd frontend
npm run dev


Frontend runs on:

http://localhost:5173


---

## Usage

Once the application is running, you can:

- Upload a `.py`, `.java`, `.js`, or `.go` file  
- Upload a `.zip` folder (multi-file repo)  
- Provide a GitHub repository link  

---

## Output Includes

- Token reduction metrics  
- Original code preview  
- Optimized context  
- AI-generated structured explanation  

---

## How It Works

1. Input code is uploaded  
2. Context optimization removes:
   - Comments  
   - Dead code  
   - Irrelevant lines  
3. Only important logic is passed to LLM  
4. LLM generates structured output:
   - Purpose  
   - Components  
   - Improvements  

---

## Key Constraints Addressed

- Handles multi-file dependencies  
- Reduces hallucination via context pruning  
- Works within LLM token limits  

---

## Help

Common issues:

- LLM not running → ensure Ollama is active  
- Backend not starting → check Python dependencies  
- Frontend not loading → run `npm install` again  
- GitHub repo fetch fails → ensure public repo  

---

## Future Improvements

- Dependency graph-based context extraction  
- Multi-language support (COBOL → Python)  
- Live deployment  
- CI/CD integration  

---

## Author

**HET MAYUR THORIA**

---
