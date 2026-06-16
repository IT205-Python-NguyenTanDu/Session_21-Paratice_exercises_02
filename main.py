import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


def handle_view_menu(drink_menu):
    """Display all available drinks in the menu.

    Args:
        drink_menu: dict
    """
    print("--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in drink_menu.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")


def get_drink_code(prompt, drink_menu):
    """Get and validate drink code from user input.

    Args:
        prompt: str
        drink_menu: dict

    Returns:
        code: str or None
    """
    code = input(prompt).strip().upper()
    if code not in drink_menu:
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
        logging.warning(f"ItemNotFoundError - Code: {code}")
        return None
    return code


def get_quantity(prompt):
    """Get and validate quantity from user input.

    Args:
        prompt: str

    Returns:
        quantity: int or None
    """
    try:
        quantity = int(input(prompt))
    except ValueError:
        print("Vui lòng nhập số lượng là một số nguyên!")
        logging.error("ValueError - Invalid quantity input")
        return None

    if quantity <= 0:
        print("Số lượng phải lớn hơn 0!")
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        return None

    return quantity


def process_add_to_order(drink_menu, current_order, code, quantity):
    """Add a drink to the current order.

    Args:
        drink_menu: dict
        current_order: list
        code: str
        quantity: int

    Returns:
        current_order: list
    """
    if quantity <= 0:
        raise ValueError("InvalidQuantityError")
    if code not in drink_menu:
        raise Exception("ItemNotFoundError")
    current_order.append({
        "code": code,
        "name": drink_menu[code]["name"],
        "price": drink_menu[code]["price"],
        "quantity": quantity
    })
    return current_order


def handle_add_to_order(drink_menu, current_order):
    """Handle add to order feature: input, validate, log, update order.

    Args:
        drink_menu: dict
        current_order: list

    Returns:
        current_order: list
    """
    print("--- THÊM MÓN VÀO GIỎ ---")
    code = get_drink_code("Nhập mã đồ uống: ", drink_menu)
    if code is None:
        return current_order

    quantity = get_quantity("Nhập số lượng: ")
    if quantity is None:
        return current_order

    current_order = process_add_to_order(
        drink_menu, current_order, code, quantity
    )
    logging.info(f"Added {quantity} of {code} to order")
    print(f"Đã thêm {quantity} x {drink_menu[code]['name']} vào giỏ hàng.")
    return current_order


def calculate_total(current_order):
    """Calculate total price of all items in the order.

    Args:
        current_order: list

    Returns:
        total: int
    """
    total = 0
    for item in current_order:
        total += item["price"] * item["quantity"]
    return total


def handle_view_order(current_order):
    """Display current order details and total price.

    Args:
        current_order: list
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

    total = calculate_total(current_order)
    print("--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).strip().lower()

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
                logging.info("Cashier logged out. System shutdown.")
                print("Đã thoát ca làm việc. Hẹn gặp lại!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
