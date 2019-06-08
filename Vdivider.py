# * potential divider equation:
#    Vout = (Vin)(R2 / (Rl + R2))
#
# * Vin == 5 volts
# * Vout cannot exceed Vin
# * Rl ranges between approx. 30 and 100k ohms,
#       the most important range being between approx. 2500 and 500 Ohms
#       (light sensitive resistor)
#
# goal: get Vout to range between 0 and 5 volts, with the range of most
#   sensitivity corresponding to the most important range Rl.

Vin = float(input("enter Vin (float or int):\t"))
while True:
    foo = input("\n[to quit, enter 'q']\ninput integer R2 value e.g. '__' Ohms\t") 
    
    if foo == "q":
        quit()
    else:
        if 'k' in foo:
            R2 = (int(str(foo)[0:(len(foo)-1)]) * 1000)
        elif 'M' in foo:
            R2 = (int(str(foo)[0:(len(foo)-1)]) * 1000000)
        elif 'R' in foo:
            R2 = int(str(foo)[0:(len(foo)-1)])
        else:
            R2 = int(foo)

    Mag = len(str(R2)) - 2
    
        # E12 series
    E12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]

    print("\n\n\t*** Vin = {}v ***\n\n|\tRl\t|\tR2\t|\tVout\n".format(Vin))

    for x in range(len(E12)):
        R1 = (E12[x] * (10 ** Mag))
        
        Vout = Vin * (R2 / (R1 + R2))

        print("|\t{0}\t|\t{1}\t|\t{2}".format(R1, R2, Vout))
