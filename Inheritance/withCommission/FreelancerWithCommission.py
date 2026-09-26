from dataclasses import dataclass
from Freelancer import Freelancer

@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer al que se le paga por horas y que se lleva una comision."""

    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return (super().compute_pay() + self.commission * self.contracts_landed)
        