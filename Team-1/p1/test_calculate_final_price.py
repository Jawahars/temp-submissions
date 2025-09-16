# Assisted by watsonx Code Assistant

import pytest
from calculate_final_price import calculate_final_price

@pytest.mark.parametrize(
    "base_price, quantity, loyalty_level, expected_final_price, description",
    [
        (100, 25, 3, 1875, "High loyalty discount (20%), bulk discount (+5%) applied"),

        (100, 10, 3, 800, "High loyalty discount (20%), no bulk discount (+0%) applied"),

        (100, 25, 2, 2125, "Mid loyalty discount (10%), bulk discount (+5%) applied"),

        (100, 10, 2, 900, "Mid loyalty discount (10%), no bulk discount (+0%) applied"),

        (100, 25, 1, 2250, "Low loyalty discount (5%), bulk discount (+5%) applied"),

        (100, 10, 1, 950, "Low loyalty discount (5%), no bulk discount (+0%) applied"),

        (0, 10, 3, 0, "Base price is zero, final price should also be zero"),
    ],
)

def test_calculate_final_price(base_price, quantity, loyalty_level, expected_final_price, description):
    """
    Test the calculate_final_price function with various inputs.
    """
    final_price = calculate_final_price(base_price, quantity, loyalty_level)
    assert final_price == expected_final_price, f"Test failed for {description}. Expected {expected_final_price}, got {final_price}."

def test_calculate_final_price_invalid_loyalty_level():
    """
    Test the function with an invalid loyalty level.
    """
    with pytest.raises(AssertionError):
        calculate_final_price(100, 10, 4)
