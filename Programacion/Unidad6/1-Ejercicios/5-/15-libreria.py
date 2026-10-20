import re

email = "fpj2003@gmail.com"
noemail = "****hola%%%.***quetal.com"

patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

print(bool(re.fullmatch(patron, email)))    # True
print(bool(re.fullmatch(patron, noemail)))  # False
