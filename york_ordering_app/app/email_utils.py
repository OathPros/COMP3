from __future__ import annotations

from urllib.parse import quote

from .models import Order

RECIPIENT = "lukegag2@gmail.com"


def build_subject(name: str, department: str) -> str:
    safe_name = name.strip() or "Unknown"
    safe_dept = department.strip() or "Unknown"
    return f"Computer Order Request - {safe_name} - {safe_dept}"


def build_body(order: Order) -> str:
    checkout = order.checkout
    lines = [
        "York University UIT Computer Order",
        "",
        "Requester Information",
        f"- Name: {checkout.requester_name}",
        f"- Department: {checkout.department}",
        f"- Budget Number: {checkout.budget_number}",
        f"- CRP: {'Yes' if checkout.is_crp else 'No'}",
    ]

    if checkout.is_crp:
        lines.extend(
            [
                f"- CRP Project Code: {checkout.crp_project_code}",
                f"- CRP Approver: {checkout.crp_approver}",
            ]
        )

    lines.extend(["", "Line Items"])

    for item in order.items:
        lines.append(
            f"- {item.product.name} | Qty {item.quantity} | ${item.product.price:,.2f} | Line ${item.line_total:,.2f}"
        )

    lines.extend(["", f"Order Total: ${order.total:,.2f}", f"Timestamp (UTC): {order.created_at.isoformat()}"])
    return "\n".join(lines)


def build_mailto(order: Order) -> str:
    subject = quote(build_subject(order.checkout.requester_name, order.checkout.department))
    body = quote(build_body(order))
    return f"mailto:{RECIPIENT}?subject={subject}&body={body}"
