from dataclasses import dataclass
import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class BudgetTransaction:
    budget_transaction_id: int
    budget_transaction_name: str
    budget_transaction_date: datetime
    budget_transaction_amount: Decimal
    is_payment: bool

@dataclass
class BudgetCategory:
    budget_category_id: int
    budget_category_name: str
    inheriting_category: 'BudgetCategory'

@dataclass
class BudgetItem:
    budget_item_id: int
    budget_item_name: str
    budget_category: BudgetCategory

@dataclass
class Budget:
    budget_id: int
    month: datetime
    budget_transactions: Optional[list[BudgetTransaction]]
    budget_items: Optional[list[BudgetItem]]
    #once I get further along, I might add other things here, like the tables

