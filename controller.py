from subprocess import call

def assemble(tagID):

    as_top = """
       .global main
       .extern printf

       .text


    output_str:
        .asciz "%d\n\0"
        .align 4

    main:
        push {ip, lr}

    \n"""

    as_bottom = """

        mov R5, #0 //R5 contains 0                                                                                                                                                                                              

        mov R4, R0

    modloop:

        lsr R4, R4, #1 // divide by 2, store quotient in R0                                                                                                                                                                     


        bl mod

        mov R1, R0
        ldr R0, =output_str
        bl printf

        mov R0, R4 //return value to R0 for function call next iteration                                                                                                                                                        
        cmp R4, R5
        bne modloop


        pop {ip, pc}
        bx lr // end program, return r0                                                                                                                                                                                         

    mod:
        push {lr}

        mov R1, R0  // R1 contained input/divident                                                                                                                                                                              
        lsr R2, R1, #1 // Divide by 2, Store quotient in R2                                                                                                                                                                     
        lsl R3, R2, #1 // Multiply by 2, store product in R3                                                                                                                                                                    
        sub R0, R1, R3 // Subtract origianl dividend with product, store remainder in R0                                                                                                                                        

        pop {pc}

    """

    call(["touch","dec2bin1.s"])

    with open("dec2bin1.s",'w') as f:
        f.write(as_top)
        f.write("ldr R0, =" + str(tagID) + '\n')
        f.write(as_bottom)

    call(["as","-o","dec2bin1.o","dec2bin1.s"])
    call(["gcc","-o", "dec2bin1", "dec2bin1.o"])

    print call("./dec2bin1")

    call(["rm","dec2bin1.s","dec2bin1.o","dec2bin1"])
