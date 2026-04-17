from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict


@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: float
    category: str
    thumbnail: str
    description: str
    tags: list[str]
    specs: Dict[str, str]


@dataclass(frozen=True)
class SetupPackage:
    id: str
    name: str
    description: str
    items: list[str]


@dataclass
class CartItem:
    product: Product
    quantity: int = 1

    @property
    def line_total(self) -> float:
        return self.product.price * self.quantity


@dataclass
class CheckoutState:
    requester_name: str = ""
    department: str = ""
    budget_number: str = ""
    is_crp: bool = False
    crp_project_code: str = ""
    crp_approver: str = ""

    def validate(self) -> tuple[bool, str]:
        if not self.requester_name.strip():
            return False, "Name is required."
        if not self.department.strip():
            return False, "Department is required."
        if not self.budget_number.strip():
            return False, "Budget Number is required."
        if self.is_crp:
            if not self.crp_project_code.strip():
                return False, "CRP Project Code is required."
            if not self.crp_approver.strip():
                return False, "CRP Approver is required."
        return True, ""


@dataclass
class Order:
    checkout: CheckoutState
    items: list[CartItem] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    @property
    def total(self) -> float:
        return sum(item.line_total for item in self.items)
