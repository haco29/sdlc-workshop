"""Dummy accounts for trying the app. Not real people, not real cards."""

from datetime import date
from decimal import Decimal

from billing.models import Account

DUE_DATE = date(2026, 10, 2)
AS_OF = date(2026, 10, 12)

ACCOUNTS = [
    Account("Noa Levi", Decimal("1200.00"), Decimal("1200.00"), DUE_DATE, Decimal("0.12")),
    Account("Avi Cohen", Decimal("2400.00"), Decimal("400.00"), DUE_DATE, Decimal("0.12")),
    Account("Maya Peretz", Decimal("150.00"), Decimal("0.00"), DUE_DATE, Decimal("0.12")),
    Account("Yoni Mizrahi", Decimal("9800.00"), Decimal("0.00"), DUE_DATE, Decimal("0.15")),
]
