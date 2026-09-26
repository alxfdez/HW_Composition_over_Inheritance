from dataclasses import dataclass
from Employee import Employee

@dataclass
class HourlyEmployee(Employee):
    """Employee al que se le paga por horas."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
        )