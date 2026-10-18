def get_number(message, warning):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print(warning)

def get_name(message):
    while True:
        name = input(message)
        if name.replace(" ", ""):
            break
        else:
            print("Enter letters only.")
    return name