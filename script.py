def generate_asm_instructions(input_str):
    asm_instructions = []

    # XOR AX, AX to create the null terminator dynamically
    asm_instructions.append("xor ax, ax;")
    asm_instructions.append("push ax;")  # Null-terminate the string

    # Process the string in 2-byte chunks, but handle the last byte specially if the length is odd
    length = len(input_str)
    i = length

    while i > 0:
        if i % 2 == 1:  # If only 1 character remains
            char = input_str[i - 1]
            # asm_instructions.append("xor ax, ax;")  # Clear ax
            asm_instructions.append(f"mov al, 0x{ord(char):02x};")  # Move single character into AL
            asm_instructions.append("push ax;")  # Push AX (AL + 00)
            i -= 1
        else:  # Handle 2 characters at a time
            char1 = input_str[i - 2]
            char2 = input_str[i - 1]
            # Combine the two characters in little-endian format
            hex_chunk = f"{ord(char2):02x}{ord(char1):02x}"
            asm_instructions.append(f"mov ax, 0x{hex_chunk};")
            asm_instructions.append("push ax;")
            i -= 2

    return '\n'.join(asm_instructions)

# Example usage:
input_string = "hello"
asm_code = generate_asm_instructions(input_string)
print(asm_code)
