from fastapi import APIRouter
from pydantic import BaseModel
from symspellpy.symspellpy import SymSpell, Verbosity
import pkg_resources

# Initialize router
router = APIRouter()

# Initialize SymSpell only once (when server starts)
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load dictionary
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# Pydantic model for request
class CorrectionRequest(BaseModel):
    text: str

# Pydantic model for response
class CorrectionResponse(BaseModel):
    corrected_text: str

# Create FastAPI route
@router.post("/correct-text", response_model=CorrectionResponse)
def correct_text(request: CorrectionRequest):
    suggestions = sym_spell.lookup_compound(request.text, max_edit_distance=2)
    if suggestions:
        corrected = suggestions[0].term
    else:
        corrected = request.text  # Return original if no corrections
    return CorrectionResponse(corrected_text=corrected)
