f = open('my_switches.txt', 'r')

for lin in f:
    print(lin.strip())
    
f.close()