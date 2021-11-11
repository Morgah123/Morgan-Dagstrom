a = float(input('Skriv in volym i ft^3 /lb '))


b = 1 / ((0.3048 ** 3) / 0.45359)
c = a * b

print(f'{a:.0f} är {c:.2f} i kg/m^3')