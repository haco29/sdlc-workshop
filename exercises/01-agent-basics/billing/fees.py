from decimal import ROUND_HALF_UP, Decimal

LATE_FEE_RATE = Decimal("0.02")
MIN_LATE_FEE = Decimal("10.00")
MAX_LATE_FEE = Decimal("50.00")

CENT = Decimal("0.01")


def late_fee(outstanding: Decimal, days_late: int) -> Decimal:
    """The fee for paying after the due date.

    Paying on the due date is on time. After it, the fee is a percentage of the
    outstanding amount, kept between a minimum and a maximum.
    """
    if days_late <= 0:
        return Decimal("0.00")

    fee = outstanding * LATE_FEE_RATE
    fee = max(fee, MIN_LATE_FEE)
    fee = min(fee, MAX_LATE_FEE)
    return fee.quantize(CENT, rounding=ROUND_HALF_UP)
