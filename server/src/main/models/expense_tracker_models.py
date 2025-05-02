from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from decimal import Decimal
from user_account_models import FinanceAccount
from budget_creation_models import BudgetCategory


@dataclass
class ETTransaction:
    et_transaction_id: int
    et_transaction_date: datetime
    et_transaction_description: Optional[str]
    et_transaction_amount: Decimal
    et_transaction_account: FinanceAccount
    et_transaction_category: Optional[BudgetCategory] #if it's an income, there's no category
    is_emergency: bool