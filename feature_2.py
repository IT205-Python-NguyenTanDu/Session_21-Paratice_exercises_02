import logging

from exceptions import InvalidQuantityError, ItemNotFoundError

logger = logging.getLogger(__name__)


def get_drink_code(prompt, drink_menu):
    """Get and validate drink code from user input.

    Args:
        prompt (str): Message displayed to the user.
        drink_menu (dict): Menu mapping code -> {name, price}.

    Returns:
        str | None: Valid uppercase code, or None if not found.
    """
    code = input(prompt).strip().upper()
    if code not in drink_menu:
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
        logger.warning("ItemNotFoundError - Code: %s", code)
        return None
    return code


def get_quantity(prompt):
    """Get and validate quantity from user input.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        int | None: Positive integer, or None if invalid.
    """
    try:
        quantity = int(input(prompt))
    except ValueError as e:
        print("Vui lòng nhập số lượng là một số nguyên!")
        logger.error("ValueError - Invalid quantity input: %s", e)
        return None

    if quantity <= 0:
        print("Số lượng phải lớn hơn 0!")
        logger.warning("InvalidQuantityError - Quantity: %s", quantity)
        return None

    return quantity


def process_add_to_order(drink_menu, current_order, code, quantity):
    """Add a drink to the current order.

    Args:
        drink_menu (dict): Menu mapping code -> {name, price}.
        current_order (list): List of order item dicts.
        code (str): Drink code to add.
        quantity (int): Number of drinks to add.

    Returns:
        list: Updated current_order with the new item appended.

    Raises:
        InvalidQuantityError: If quantity is zero or negative.
        ItemNotFoundError: If code is not in drink_menu.
    """
    if quantity <= 0:
        raise InvalidQuantityError(
            f"Quantity must be positive, got {quantity}."
        )
    if code not in drink_menu:
        raise ItemNotFoundError(
            f"Drink code '{code}' not found in menu."
        )
    current_order.append({
        "code": code,
        "name": drink_menu[code]["name"],
        "price": drink_menu[code]["price"],
        "quantity": quantity,
    })
    return current_order


def handle_add_to_order(drink_menu, current_order):
    """Handle add-to-order workflow: prompt, validate, log, update order.

    Args:
        drink_menu (dict): Menu mapping code -> {name, price}.
        current_order (list): List of order item dicts.

    Returns:
        list: Updated current_order.
    """
    print("--- THÊM MÓN VÀO GIỎ ---")
    code = get_drink_code("Nhập mã đồ uống: ", drink_menu)
    if code is None:
        return current_order

    quantity = get_quantity("Nhập số lượng: ")
    if quantity is None:
        return current_order

    try:
        current_order = process_add_to_order(drink_menu, current_order, code, quantity)
    except InvalidQuantityError as e:
        logger.error("InvalidQuantityError: %s", e)
        print("[LỖI]: Số lượng không hợp lệ.")
        return current_order
    except ItemNotFoundError as e:
        logger.error("ItemNotFoundError: %s", e)
        print("[LỖI]: Mã đồ uống không tồn tại.")
        return current_order

    logger.info("Added %s x %s to order.", quantity, code)
    print(f"Đã thêm {quantity} x {drink_menu[code]['name']} vào giỏ hàng.")
    return current_order
