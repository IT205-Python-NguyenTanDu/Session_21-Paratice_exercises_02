import logging


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
