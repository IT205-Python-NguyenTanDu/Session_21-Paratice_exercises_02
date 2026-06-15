import logging


def handle_view_menu(drink_menu):
    """Display all available drinks in the menu.

    Args:
        drink_menu: dict
    """
    print("--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in drink_menu.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")
