
# In a multi-level Potential Divider, find the individual resistor values
#   
#   V0 i.e. V+
#   |
#   /
#   \ R0
#   /
#   |
#   *--- V1
#   |
#   /
#   \ R1
#   /
#   |
#   *--- V2
#   |
#   /
#   \ R2
#   /
#   |
#   ...
#
#   |
#   *--- Vn
#   |
#   /
#   \ Rn
#   /
#   |
#   GND
#
# GIVEN:
#   * [Volts]   V0, V1, V2, ... Vn
#   * [Ohms]    k = (R0 + R1 + R2 ... + Rn)
# FIND:
#   * [Ohms]    R0, R1, R2, ... Rn

print("at any time, enter 'q' to quit")

# Input the number of levels to process
while True: # continue to ask for input until correct format is detected
    nu  = input("\nEnter the number of target voltages(integer):\n\t")

    # Check input for unwanted characters
    if (nu.isdigit() == True):
        break
    else:
        if nu == 'q':
            quit()
        else:
            print("please enter an INTEGER")

# Input target voltage values for each level; store in list 'V'
V = []
print("\nenter target value (volts) for:")

for i in range(int(nu)+1):
    while True: # continue to ask for input until correct format is detected
        vlt = input("V{}:\t".format(str(i)))
        
        # check input for unwanted characters
        passed = True
        for j in range(len(vlt)):
            s = str(vlt[j])
            if (s.isdigit() == False) and (s != '.'):
                passed = False
                break

        if (passed == True) and (vlt.count('.') <= 1) and (vlt != '.') and (vlt != ''):
            V.append(float(vlt))
            break
        else:
            if vlt == 'q':
                quit()
            else:
                print("please enter an INTEGER or FLOAT")

# Continue session indefinitely, trying different values of 'k' without having to
#   re-enter the above information.
# The user enters 'q' to quit.

# list of resistor values in the E12 series
E12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]

while True:

    # Input 'k' (sum of all resistors)
    while True: # continue to ask for input until correct format is detected
        k = input("\nEnter the sum of resistors R0 through R{} (ohms):\n\t".format(nu))

        # Check input for unwanted characters
        passed = True
        for j in range(len(k)):
            s = str(k[j])
            if (s.isdigit() == False):
                passed = False
                break

        if passed == True and (k != ''):
            break
        else:
            if k == 'q':
                quit()
            else:
                print("please enter an INTEGER")

    # Do the math
    R = []      # List to hold individual resistor values
    n = int(nu)

    # reverse iteration from n to 0
    for i in range(n, -1, -1):

        # Potential Divider equation [Vout = (Vin)(r2 / (r1 + r2))] rearranged
        #   Where:
        #   * Rn = r2
        #   * k  = (r1 + r2)
        #   * V[i] = Vout
        #   * V[0] = Vin
        #
        # We must calculate R[n] first, then R[n-1] and so forth, Because:
        #   * Rn == r2;
        #   * Therefore, Rn == (R[i] + R[i+1] ... + R[n]);
        #   * Thus, the individual R[i] = (R[n] - (R[i+1] ...+ R[n]))
        #
        #  i.e. we need the values of all resistors between R[i] and GND 
        #   in order to calculate R[i]

        Rn = ( int(k) * ( V[i] / V[0] ))

        # result R[n]
        if i == n:
            R.append(Rn)

        # results (R[n-1], R[n-2], ... R[1], R[0])
        else:
            RR = 0
            jj = 0
            for j in range(i, n):
                RR += R[jj]
                jj += 1

            # insert new value at the beginning of the list
            R.insert(0, (Rn - RR))
    
    # gather a dataset in which each element of 'data[]' is a value which indicates
    #   how far away the corresponding resistor value is from a value in the E12 series
    data = []
    
    for i in range(n+1):
        # obtain a two-digit integer (MSD's of R[i]) to compare with the E12 elements

        if '.' in str(R[i])[0:3]:
            # less than 3 digits to the left of decimal point
            num = round(int(str(R[i])[0:4].replace('.', '')), -1)
            print('num = ', num)

        else:
            num = round(int(str(R[i])[0:3]), -1)
            print('num = ', num)
        
        # find the difference between R[i] and the closest E12 element
        dif = []
        for j in range(12):
            if num == E12[j]:
                dif.append(0)
            elif num > E12[j]:
                dif.append( num - E12[j])
            elif num < E12[j]:
                dif.append( E12[j] - num)
    
            if j > 0:
                if dif[j] > dif[j-1]:
                    data.append(dif[j-1])
                    break

    print("dataset:\n", data)


    print("\nResistor Values:")
    for i in range(n+1):
        print("R{}:\t".format(i), R[i])


# Future features? 
#
#   * Vary the total resistance to find resistor values close to the E12 selection
