from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Employee(ABC):
    """Representacion basica de un empleado."""

    name: str
    id: int
    hours_worked: int = 0


    @abstractmethod
    def compute_pay(self) -> float:
        """Metodo que calcula cuanto gana un empleado."""