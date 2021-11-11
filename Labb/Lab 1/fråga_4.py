inches = float(input('skriv inches '))

b = 26 
c = 12 

yard = inches // b 
rest1 = inches % b 
foot = rest1 // c 
rest2 = rest1 % c 
inc = rest2 

print(yard,'Yard',foot,'foot och ' f'{inc:.1f} inches') 
