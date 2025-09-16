def calculate_final_price(base_price, quantity, loyalty_level):

    # Determine discount rate based on loyalty level

    if loyalty_level == 3:

        discount_rate = 20

    elif loyalty_level == 2:

        discount_rate = 10

    else:

        discount_rate = 5

    

    # Apply an additional bulk discount if quantity > 20

    if quantity > 20:

        discount_rate += 5

    

    # Calculate the final price

    base_total = base_price * quantity

    discount_amount = (base_total * discount_rate) // 100

    final_price = base_total - discount_amount

    

    return final_price