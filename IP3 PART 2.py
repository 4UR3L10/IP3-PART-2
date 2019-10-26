        ######################################################################
        # PUT CODE HERE (IP3 Part 2) 

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