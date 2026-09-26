from dataclasses import dataclass
from Employee import Employee

@dataclass
class Freelancer(Employee):
    """Freelancer al que se le paga por horas."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return (
            self.pay_rate * self.hours_worked 
        )
        