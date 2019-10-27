        ######################################################################
        # PUT CODE HERE (IP3 Part 2) 

        # Register declaration.
            # int start = 0
            addi $s5, $zero, 0       # int start = 0 [$s5 = 0] (Assigning value zero to register $s5)   

            # int end = N - 1
            sub $s6, $s1, 1          # int end = N - 1 = 12 - 1 [$s6 = 11] (Assigning value 11 to register $s6)

            # int pivot = a[end]
            sll $t1, $s6, 2          # int tempI = 4 * 11 (Creates a temp register to get the last index)  
            addu $t1, $s0, $t1       # tempI = BaseRAM + tempI (Add the base RAM plus the index to get the exact location in RAM)
            lw $s7, 0($t1)           # int pivot = arr[end]

            # int i = start
            addu $s2, $zero, $s5

            # int j = end - 1
            addu $s3, $zero, $s6      

            # int CHECKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK

        # Beginning the iterations for i and j
            # First While Loop. 
            WhileFirst:                        # Tag
                # (i <= j)
                slt $t1, $s2, $s3              # i < j -> var = 1 else -> var = 0
                beq $t1, $zero, endFirstLoop   # var == 0 jump to endFirstLoop , otherwise do the loop.   
                
                addi $s2, $s2, 2 #tester
                j WhileFirst                   # Repeat the loop.   
            endFirstLoop:                      # End of the loop.




                ######################################################################
                # PUT SWAP CODE HERE (IP3 Part 1)    
                
                # Getting the value of i to a variable.     
                sll $t1, $s2, 2      # int tempI = 2 * i (Creates a temp register to get the index of i)      
                addu $t1, $s0, $t1   # tempI = BaseRAM + tempI (Add the base RAM plus the index to get the exact location in RAM)
                lw $s4, 0($t1)       # int variable = arr[i] 
                    
                # Getting the value of j to a temporary.                 
                sll $t2, $s3, 2      # int tempJ = 2 * j (Creates a temp register to get the index of j)
                addu $t2, $s0, $t2   # tempJ = BaseRAM + tempJ (Add the base RAM plus the index to get the exact location in RAM)     
                lw $t3, 0($t2)       # int temporary = arr[j]
                
                # Swapping the values.
                sw $t3, 0($t1)       # arr[i] = temporary (Saves the value of temporary variable in arr[i])
                sw $s4, 0($t2)       # arr[j] = variable  (Saves the value of i in arr[j])
                ######################################################################
            
        ######################################################################    