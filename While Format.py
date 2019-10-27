        # Register declaration.
        addi $t4, $zero, 1
        addi $t5, $zero, 10

        # While Loop.
        WhileFirst: beq $t4, $t5, TAG
                    addi $t4, $t4, 1
                    j WhileFirst

        # After the loop.
        TAG:         
        addi $t4, $zero, 100