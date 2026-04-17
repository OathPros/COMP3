from __future__ import annotations

from .models import CartItem, Product


class Cart:
    def __init__(self) -> None:
        self._items: dict[str, CartItem] = {}

    @property
    def items(self) -> list[CartItem]:
        return list(self._items.values())

    @property
    def is_empty(self) -> bool:
        return not self._items

    @property
    def subtotal(self) -> float:
        return sum(item.line_total for item in self._items.values())

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity < 1:
            return
        existing = self._items.get(product.id)
        if existing:
            existing.quantity += quantity
        else:
            self._items[product.id] = CartItem(product=product, quantity=quantity)

    def set_quantity(self, product_id: str, quantity: int) -> None:
        if product_id not in self._items:
            return
        if quantity <= 0:
            self.remove(product_id)
            return
        self._items[product_id].quantity = quantity

    def remove(self, product_id: str) -> None:
        self._items.pop(product_id, None)

    def clear(self) -> None:
        self._items.clear()
