import logging

from feature_1 import handle_view_menu
from feature_2 import handle_add_to_order
from feature_3 import handle_view_order
from feature_4 import handle_checkout

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(name)s] - %(message)s",
)

logger = logging.getLogger(__name__)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000},
}


def display_menu():
    """Print the main CLI menu."""
    print("=" * 40)
    print("HIGHLANDS MINI POS".center(40))
    print("=" * 40)
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("=" * 40)


def main():
    """Entry point — run the Highlands Mini POS CLI."""
    current_order = []

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                handle_view_menu(DRINK_MENU)
            case "2":
                current_order = handle_add_to_order(DRINK_MENU, current_order)
            case "3":
                handle_view_order(current_order)
            case "4":
                current_order = handle_checkout(current_order)
            case "5":
                logger.info("Cashier logged out. System shutdown.")
                print("Đã thoát ca làm việc. Hẹn gặp lại!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
