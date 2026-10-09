"""Print this month's statements for the sample accounts."""

from billing.sample import ACCOUNTS, AS_OF
from billing.statement import build_statement


def main() -> None:
    print(f"Statements as of {AS_OF:%d %b %Y}\n")
    print(f"{'Holder':<14}{'Outstanding':>12}{'Days late':>11}{'Late fee':>10}"
          f"{'Interest':>10}{'Total due':>11}")
    for account in ACCOUNTS:
        s = build_statement(account, AS_OF)
        print(f"{s.holder:<14}{s.outstanding:>12}{s.days_late:>11}{s.late_fee:>10}"
              f"{s.interest:>10}{s.total_due:>11}")


if __name__ == "__main__":
    main()
