import logging

logger = logging.getLogger(__name__)


def calculate_total(current_order):
    """Calculate total price of all items in the order.

    Args:
        current_order (list): List of order item dicts.

    Returns:
        int: Sum of (price * quantity) for every item.
    """
    total = 0
    for item in current_order:
        total += item["price"] * item["quantity"]
    return total


def handle_view_order(current_order):
    """Display current order details and total price.

    Args:
        current_order (list): List of order item dicts.
    """
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("--- GIỎ HÀNG HIỆN TẠI ---")
    header = (
        f"{'Mã SP':<6}| {'Tên đồ uống':<20}| "
        f"{'Đơn giá':<10}| {'Số lượng':<10}| {'Thành tiền'}"
    )
    print(header)
    print("-" * 64)
    for item in current_order:
        subtotal = item["price"] * item["quantity"]
        print(
            f"{item['code']:<6}| {item['name']:<20}| "
            f"{item['price']:>8,} | {item['quantity']:<9}| "
            f"{subtotal:,} VNĐ"
        )
    print("-" * 64)
    total = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
