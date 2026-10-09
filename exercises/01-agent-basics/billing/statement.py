from datetime import date

from billing.fees import late_fee
from billing.interest import monthly_interest
from billing.models import Account, Statement


def build_statement(account: Account, as_of: date) -> Statement:
    """Work out what the holder owes as of a given day."""
    days_late = max((as_of - account.due_date).days, 0)
    return Statement(
        holder=account.holder,
        outstanding=account.outstanding,
        days_late=days_late,
        late_fee=late_fee(account.outstanding, days_late),
        interest=monthly_interest(account.outstanding, account.annual_rate),
    )
