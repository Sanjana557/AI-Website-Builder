from fastapi import APIRouter
from pydantic import BaseModel
from ai.constraints import build_constraints
from ai.generator import generate_site

router = APIRouter()

class GenerateRequest(BaseModel):
    website_type: str
    tone: str
    color: str
    sections: list[str]

@router.post("/generate")
def generate(request: GenerateRequest):
    constraints = build_constraints(request.dict())
    html = generate_site(constraints)
    return {
        "html": html
    }
