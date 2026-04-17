# York University UIT Computer Ordering (GNOME)

Native GTK 4 + Libadwaita desktop app for internal UIT computer ordering workflows.

## Features

- Product-first catalog with category filter (Windows, Mac, Peripherals)
- Compact suggested setup cards with quick add and compare view
- Product detail dialogs with specs, pricing, and add-to-order action
- Cart/order affordance hidden until first item is added
- Cart line item quantity updates, remove action, subtotal
- Checkout with CRP branching (additional required fields shown only when CRP is enabled)
- Structured email generation to `lukegag2@gmail.com` with mailto -> clipboard -> text file fallback

## Project structure

- `app/models/` data models for products, setups, cart items, checkout state, order
- `app/views/` GTK/Adwaita window and dialog views
- `app/cart.py` cart logic
- `app/email_utils.py` structured email subject/body/mailto generation
- `data/catalog.json` product catalog and required setup packages

## Run locally

```bash
cd york_ordering_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

> You need system packages for GTK 4 and Libadwaita (for example: `python3-gi`, `gir1.2-gtk-4.0`, `gir1.2-adw-1`).
