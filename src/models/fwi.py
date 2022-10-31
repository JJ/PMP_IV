from dataclasses import dataclass
from src.config.model_validation import ModelValidation

from src.utils.validation import Validation

'''Fire weather index'''
@dataclass
class FWI:
    '''Fine fuel moisture code'''
    FFMC: float
    '''Duff moisture code'''
    DMC: float
    '''Drought code'''
    DC: float
    '''Indicador de la velocidad de propagación del incendio'''
    ISI: float

    def __post_init__(self):
        Validation.validate(self, ModelValidation.fwi())
