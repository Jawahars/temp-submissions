def calculate_final_price(base_price, quantity, loyalty_level):
    """
    Calculate the final price after applying loyalty and bulk discounts.

    Args:
        base_price (float): The base price of the item.
        quantity (int): The number of items purchased.
        loyalty_level (int): The loyalty level (1, 2, or 3).

    Returns:
        float: The final price after discounts.

    Raises:
        AssertionError: If loyalty_level is not 1, 2, or 3.
        ValueError: If base_price or quantity is non-negative.
    """

    # Validate input parameters
    if base_price < 0:
        raise ValueError("Base price must be non-negative.")
    if quantity < 0:
        raise ValueError("Quantity must be non-negative.")
    if loyalty_level not in [1, 2, 3]:
        raise AssertionError("Loyalty level must be 1, 2, or 3.")
    
    # Determine discount rate based on loyalty level
    if loyalty_level == 3:
        discount_rate = 20  # Default is 20 (20%)
    elif loyalty_level == 2:
        discount_rate = 10  # Mid tier is 10 (10%)
    else:
        discount_rate = 5  # Default is 5 (5%)

    # Apply an additional bulk discount if quantity > 20
    if quantity > 20:
        discount_rate += 5

    # Calculate the final price
    total = base_price * quantity
    discount_amount = (total * discount_rate) // 100
    final_price = total - discount_amount

    return final_price

if __name__ == "__main__":
    
    # Take inputs from user
    base_price = int(input("Enter base price: "))
    quantity = int(input("Enter quantity: "))
    loyalty_level = int(input("Enter loyalty level (1/2/3): "))

    final_price = calculate_final_price(base_price, quantity, loyalty_level)

    print("\nThe final price is:", final_price)