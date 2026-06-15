import logging


def handle_checkout(current_order):
    """Handle checkout: confirm, log, and clear the order.

    Args:
        current_order: list

    Returns:
        current_order: list
    """
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return current_order

    total = sum(item["price"] * item["quantity"] for item in current_order)
    print("--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()

    if confirm == "y":
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        print("Giỏ hàng đã được làm trống.")
        return []
    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
        return current_order
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
        return current_order
