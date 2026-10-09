from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def monthly_interest(outstanding: Decimal, annual_rate: Decimal) -> Decimal:
    """One month of interest on the outstanding amount, rounded to the cent."""
    interest = outstanding * annual_rate / Decimal("12")
    return interest.quantize(CENT, rounding=ROUND_HALF_UP)
