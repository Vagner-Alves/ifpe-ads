def hexadecimal(num):
    "Converte Binário para Hexadecimal"
    num = 'O' * (4 - len(num) % 4) + num

    mapear_hexadecimal=  {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                          '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    hexadeci = ''

    for i in range(0, len(num), 4):
        pedaco = num[i:i+4]
        hexadeci += mapear_hexadecimal[pedaco]

    return hexadeci

def binary_to_hexadecimal(binary):
    """Convert binary to hexadecimal."""
    # Pad the binary number with leading zeros if its length is not a multiple of 4
    binary = '0' * (4 - len(binary) % 4) + binary

    # Create a dictionary to map binary digits to hexadecimal digits
    binary_to_hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                          '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    hexadecimal = ''
    # Iterate through the binary number in chunks of 4 digits
    for i in range(0, len(binary), 4):
        chunk = binary[i:i+4]
        hexadecimal += binary_to_hex_dict[chunk]

    return hexadecimal

def hexadecimal_to_binary(hexadecimal):
    """Convert hexadecimal to binary."""
    binary = ''
    # Iterate through the hexadecimal number digit by digit
    for digit in hexadecimal:
        # Convert the hexadecimal digit to binary and append it to the result
        binary += format(int(digit, 16), '04b')

    return binary

def hexadecimal_to_octal(hexadecimal):
    """Convert hexadecimal to octal."""
    binary = ''
    # Iterate through the hexadecimal number digit by digit
    for digit in hexadecimal:
        # Convert the hexadecimal digit to binary and append it to the result
        binary += format(int(digit, 16), '04b')

    # Pad the binary number with leading zeros if its length is not a multiple of 3
    binary = '0' * (3 - len(binary) % 3) + binary

    octal = ''
    # Iterate through the binary number in chunks of 3 digits
    for i in range(0, len(binary), 3):
        chunk = binary[i:i+3]
        # Convert the binary chunk to octal and append it to the result
        octal += str(int(chunk, 2))

    return octal

# Example usage
hexadecimal = input("Enter a hexadecimal number: ")
octal = hexadecimal_to_octal(hexadecimal)
print(f"Octal: {octal}")
