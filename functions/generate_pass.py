import random

# Function to generate a random password
def generate_pass(length, upper, lower, numbers, symbols) -> str:
    '''Function to generate a random password'''

    # Valid password length
    if not length or length < 0:
        length = 12

    # Determine which characters to include
    chars = ""
    if upper:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if numbers:
        chars += "0123456789"
    if symbols:
        chars += "_"

    if not chars:
        return ""  # Retorna vazio se nenhuma opção estiver selecionada

    return "".join(random.choice(chars) for _ in range(length))
