from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/contas-a-pagar-e-receber")


def listar_contas():
    return [
        {"conta1": "conta1"},
        {"conta2": "conta2"},
        {"conta3": "conta3"},
    ]