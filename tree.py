height = int(input("Введіть висоту ялинки: "))

for i in range(height):
    spaces = height - 1 - i
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)
print(" " * (height - 1) + "|")