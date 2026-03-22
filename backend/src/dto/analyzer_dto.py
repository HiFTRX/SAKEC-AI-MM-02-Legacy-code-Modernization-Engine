from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    original: str
    optimized: str
    generated: str
    before_tokens: int
    after_tokens: int
    reduction: int