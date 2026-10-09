from decimal import Decimal

from billing.fees import late_fee


def test_no_fee_when_paid_on_the_due_date():
    assert late_fee(Decimal("500.00"), days_late=0) == Decimal("0.00")


def test_one_day_late_is_charged():
    assert late_fee(Decimal("1000.00"), days_late=1) == Decimal("20.00")


def test_fee_is_a_percentage_of_the_outstanding_amount():
    assert late_fee(Decimal("1500.00"), days_late=10) == Decimal("30.00")


def test_fee_never_below_the_minimum():
    assert late_fee(Decimal("100.00"), days_late=10) == Decimal("10.00")


def test_fee_never_above_the_maximum():
    assert late_fee(Decimal("5000.00"), days_late=10) == Decimal("50.00")
