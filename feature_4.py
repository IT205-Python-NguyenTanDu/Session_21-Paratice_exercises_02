import logging

from feature_3 import calculate_total

logger = logging.getLogger(__name__)


def handle_checkout(current_order):
    """Handle checkout: confirm, log, and clear the order.

    Args:
        current_order (list): List of order item dicts.

    Returns:
        list: Empty list on successful payment, unchanged list otherwise.
    """
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return current_order

    total = calculate_total(current_order)
    print("--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()

    if confirm == "y":
        logger.info("Checkout successful. Total: %s VND.", total)
        print("Thanh toán thành công.")
        print("Giỏ hàng đã được làm trống.")
        return []
    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
        return current_order
    else:
        logger.warning("Invalid checkout confirmation input: '%s'.", confirm)
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
        return current_order
