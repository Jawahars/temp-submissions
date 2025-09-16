def calc_example(eax, ebx, ecx):
    """
    Simulates the assembly operation:
    EAX = (EAX * EBX) + ECX

    Parameters:
    eax (int): First input value, equivalent to EAX register.
    ebx (int): Second input value, equivalent to EBX register.
    ecx (int): Third input value, equivalent to ECX register.

    Returns:
    int: Result of the calculation stored in EAX.
    """

    # Step 1: Multiply EAX by EBX
    eax = eax * ebx  # eax now holds the product of eax and ebx

    # Step 2: Add ECX to the result
    eax = eax + ecx  # eax now holds the final result

    # Step 3: Return the result
    return eax

# Example usage:
# Inputs: EAX = 5, EBX = 3, ECX = 2
# Expected output: (5 * 3) + 2 = 17
result = calc_example(5, 3, 2)
print("Result:", result)
