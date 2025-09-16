
# Order Processing Module

This Python script allows users to calculate the final price of an order based on:
- Base price of an item
- Quantity ordered
- Customer loyalty level

It also applies bulk discounts for large orders.

## Features
- Input validation for price, quantity, and loyalty level
- Dynamic discount calculation
- Clear output of pricing details

## Requirements
- Python 3.x

## Setup Instructions
1. **Install Python**:
   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Save the Script**:
   - Copy the `process_order()` function into a file named `order_processor.py`

3. **Run the Script**:
   - Open a terminal or command prompt
   - Navigate to the folder where `order_processor.py` is saved
   - Run the script using:
     ```bash
     python order_processor.py
     ```

4. **Follow Prompts**:
   - Enter the base price, quantity, and loyalty level when prompted
   - View the calculated final price and discount details

## Example
```bash
Enter the base price of the item: $50
Enter the quantity of the item: 25
Enter the loyalty level (1, 2, or 3): 2
```

Output:
```
Base Price: $ 50.00
Quantity:  25
Loyalty Level:  2
Total Price: $ 1250.00
Discount Rate:  15 %
Discount Amount: $ 187.00
Final Price: $ 1063.00
```

## License
This project is open-source and free to use.
