def process_order(base_price, quantity, loyalty_level):
    """
    Calculate the final price of an order considering base price, quantity, and loyalty level.
    Parameters:
    base_price (int): The price of a single item.
    quantity (int): The number of items in the order.
    loyalty_level (int): The customer's loyalty level (1, 2, or 3).
    Returns:
    int: The final calculated price after applying discounts.
    Note:
    - All percentages are handled as integers (e.g., 20% is 20).
    - Loyalty levels are 1, 2, or 3, corresponding to discounts of 5%, 10%, and 20% respectively.
    - An additional discount of 5% is applied if the quantity exceeds 20.
    """
    # Calculate base total (price * quantity)
    total = base_price * quantity
    # Determine discount rate based on loyalty level
    if loyalty_level == 3:
        discount_rate = 20
    elif loyalty_level == 2:
        discount_rate = 10
    else:  # Default to loyalty level 1
        discount_rate = 5
    # Apply an additional bulk discount if quantity > 20
    if quantity > 20:
        discount_rate += 5
    # Calculate the final price: final = total - (total * rate / 100)
    final_price = total - (total * discount_rate // 100)
    return final_price
if __name__ == "__main__":
    # Example usage
    base_price = 100
    quantity = 25
    loyalty_level = 3
    final_price = process_order(base_price, quantity, loyalty_level)
    print(f"Final Price: {final_price}")








