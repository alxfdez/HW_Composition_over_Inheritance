from dataclasses import dataclass
from SalariedEmployee import SalariedEmployee

@dataclass
class SalariedEmployeeWithComission(SalariedEmployee):
    """Empleado al que se le paga un salario mensual fijo y una comision."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return (super().compute_pay() + self.commission * self.contracts_landed)