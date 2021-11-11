import math

h = float(input('Skirv in meter: '))
g = 9.82
hastighet = math.sqrt(2 * g * h)

print(f'Hastighet: {hastighet:.1f} meter per sekund')