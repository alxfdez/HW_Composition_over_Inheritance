from dataclasses import dataclass
from HourlyEmployee import HourlyEmployee

@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Employee al que se le paga por horas y que se lleva una comision."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed