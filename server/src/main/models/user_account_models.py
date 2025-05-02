from dataclasses import dataclass
from decimal import Decimal

@dataclass
class FinanceAccount:
    account_id: int
    account_name: str
    account_balance: Decimal
    is_debt: bool

@dataclass
class UserAccount:
    user_id: int
    username: str
    accounts: list[FinanceAccount]



