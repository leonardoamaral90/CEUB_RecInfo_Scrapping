from enum import Enum, auto

class Status(Enum):
    SUCCESS = auto()
    INFO = auto()
    ERRO = auto()
    
    SUCCESS_DOC = "Operação realizada com sucesso."
    INFO_DOC = "Informação sobre a operação."
    ERRO_DOC = "Ocorreu um erro durante a operação."