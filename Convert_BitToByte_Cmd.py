def convert_bit_byte():
    units = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
    # Conversion factors (1 byte = 8 bits; and 1 KB = 1024 bytes, etc.)
    factors = {
        "bit": 1,
        "byte": 8,
        "kilobyte": 8 * 1024,
        "megabyte": 8 * 1024**2,
        "gigabyte": 8 * 1024**3,
        "terabyte": 8 * 1024**4,
        "petabyte": 8 * 1024**5,
    }

    print("Available units: bit, byte, kilobyte, megabyte, gigabyte, terabyte, petabyte")
    value = float(input("Enter the value to convert: "))
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()

    if from_unit not in factors or to_unit not in factors:
        print("Invalid unit entered. Please try again.")
        return

    # Convert input value to bits first
    value_in_bits = value * factors[from_unit]

    # Convert bits to target unit
    converted_value = value_in_bits / factors[to_unit]

    print(f"{value} {from_unit}(s) = {converted_value} {to_unit}(s)")


if __name__ == "__main__":
    convert_bit_byte()
