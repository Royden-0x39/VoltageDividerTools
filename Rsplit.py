E12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]

while True:
    success = False
    
    print("\n[To quit, enter 'q']")
    foo = input("Enter minuend:\t")
    print("")   # i.e. '\n'

    if foo == 'q':
        quit()
    else:
        if 'k' in foo:
            minu1 = (int(str(foo)[0:(len(foo)-1)]) * 1000)
        elif 'M' in foo:
            minu1 = (int(str(foo)[0:(len(foo)-1)]) * 1000000)
        elif 'R' in foo:
            minu1 = int(str(foo)[0:(len(foo)-1)])
        else:
            minu1 = int(foo)
            
    Mag0 = Mag1 = Mag2 = len(str(minu1)) - 2

    # Subtract E12 values 'subt1' from minuend 'minu1';
    # Check that the difference 'diff1' is also an E12 value;
    # If all E12 values have been tried and failed:
    #   Subtract E12 values 'subt1' from 'minu1';
    #   Subtract E12 values 'subt2' from 'diff1' (now 'minu2');
    #   Check that the difference 'diff2' is also an E12 value;
    #   so on and so forth.
        
    # Split into 2 parts:
    while Mag0 >= 0:

        for x in range(len(E12)):
            subt1 = (E12[x] * (10 ** Mag0))

            if subt1 < minu1:
                diff1 = minu1 - subt1

                digits = str(diff1)
                sig    = int(digits[0:2])
                nonsig = (digits[2:(len(digits))])
                
                if (sig in E12) and ((nonsig == '') or (int(nonsig) == 0)):
                    print("{} = {} + {}\n".format(minu1, subt1, diff1))
                    
                    cont = input("Find next occurrence? (y/n)\t")
                    if cont == 'n':
                        success = True
                        break

        if success == True:
            break

        Mag0 -= 1

    if success == False:        
        Mag1 = Mag2 = len(str(minu1)) - 2

        # Split into 3 parts:
        while Mag1 >= 1:

            for x in range(len(E12)):
                subt1 = (E12[x] * (10 ** Mag1))

                if subt1 < minu1:
                    minu2 = minu1 - subt1
                    
                    while Mag2 >= 1:

                        for y in range(len(E12)):
                            subt2 = (E12[y] * (10 ** Mag2))

                            if subt2 < minu2:
                                diff2 = minu2 - subt2

                                digits = str(diff2)
                                sig    = int(digits[0:2])
                                nonsig = (digits[2:(len(digits))])
                                
                                if (sig in E12) and ((nonsig == '') or (int(nonsig) == 0)):
                                    print("{} = {} + {} + {}\n".format(minu1, subt1, subt2, diff2))
                                    
                                    cont = input("Find next occurrence? (y/n)\t")
                                    if cont == 'n':
                                        success = True
                                        break

                        if success == True:
                            break

                        Mag2 -= 1

                    if success == True:
                        break

            if success == True:
                break

            Mag1 -= 1

        if success == False:
            print("\nSorry, no (more) occurrences\n")
