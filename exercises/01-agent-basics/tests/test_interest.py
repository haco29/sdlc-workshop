from decimal import Decimal

from billing.interest import monthly_interest


def test_one_month_of_interest():
    assert monthly_interest(Decimal("1200.00"), Decimal("0.12")) == Decimal("12.00")


def test_rounds_to_the_cent():
    assert monthly_interest(Decimal("100.00"), Decimal("0.15")) == Decimal("1.25")
