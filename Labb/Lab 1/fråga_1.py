batteri = float(input('Hur stort är ditt batteri i kWh? '))
effekt = float(2.3)

tid = batteri / effekt
print(f'{tid:.1f} Timmar')