from datetime import date
from decimal import Decimal

from billing.models import Account
from billing.statement import build_statement

DUE = date(2026, 10, 2)


def account(balance: str, paid: str) -> Account:
    return Account("Test Holder", Decimal(balance), Decimal(paid), DUE, Decimal("0.12"))


def test_partial_payment_leaves_the_rest_outstanding():
    s = build_statement(account("1000.00", "400.00"), as_of=DUE)
    assert s.outstanding == Decimal("600.00")


def test_overpayment_is_not_negative_outstanding():
    s = build_statement(account("100.00", "150.00"), as_of=DUE)
    assert s.outstanding == Decimal("0")


def test_days_late_counts_from_the_due_date():
    s = build_statement(account("1000.00", "0.00"), as_of=date(2026, 10, 12))
    assert s.days_late == 10


def test_total_due_adds_fee_and_interest():
    s = build_statement(account("1500.00", "0.00"), as_of=date(2026, 10, 12))
    assert s.total_due == Decimal("1500.00") + Decimal("30.00") + Decimal("15.00")
