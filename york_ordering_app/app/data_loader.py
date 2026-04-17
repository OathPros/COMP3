from __future__ import annotations

import json
from pathlib import Path

from .models import Product, SetupPackage


class Catalog:
    def __init__(self, categories: list[str], products: dict[str, Product], setups: list[SetupPackage]):
        self.categories = categories
        self.products = products
        self.setups = setups


def load_catalog(path: Path) -> Catalog:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    products = {
        item["id"]: Product(
            id=item["id"],
            name=item["name"],
            price=item["price"],
            category=item["category"],
            thumbnail=item.get("thumbnail", ""),
            description=item["description"],
            tags=item.get("tags", []),
            specs=item.get("specs", {}),
        )
        for item in data["products"]
    }

    setups = [
        SetupPackage(
            id=setup["id"],
            name=setup["name"],
            description=setup["description"],
            items=setup["items"],
        )
        for setup in data["setups"]
    ]

    return Catalog(categories=data["categories"], products=products, setups=setups)
