from __future__ import annotations

from pathlib import Path

import gi

gi.require_version("Adw", "1")
from gi.repository import Adw

from .data_loader import load_catalog
from .views.main_window import MainWindow


class OrderingApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id="ca.yorku.uit.ordering")

    def do_activate(self):
        catalog_path = Path(__file__).resolve().parents[1] / "data" / "catalog.json"
        catalog = load_catalog(catalog_path)
        window = MainWindow(self, catalog)
        window.present()


def main() -> int:
    app = OrderingApplication()
    return app.run(None)


if __name__ == "__main__":
    raise SystemExit(main())
