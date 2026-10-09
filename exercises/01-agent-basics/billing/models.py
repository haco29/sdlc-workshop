from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Account:
    """A card account at the end of a billing cycle."""

    holder: str
    statement_balance: Decimal
    paid: Decimal
    due_date: date
    annual_rate: Decimal

    @property
    def outstanding(self) -> Decimal:
        """What is still unpaid from the statement balance. Never negative."""
        return max(self.statement_balance - self.paid, Decimal("0"))


@dataclass(frozen=True)
class Statement:
    holder: str
    outstanding: Decimal
    days_late: int
    late_fee: Decimal
    interest: Decimal

    @property
    def total_due(self) -> Decimal:
        return self.outstanding + self.late_fee + self.interest
