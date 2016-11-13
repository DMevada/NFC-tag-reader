	.global main
	.extern printf

	.text
	

output_str:
	.asciz "Result: %d\n\0"
	.align 4

main:
	push {ip, lr}

	ldr R0, =100 // input number
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

mul10:
	push {lr}

	lsl R1, R0, #3 //multiply by 8, store product in R2
	lsl R2, R0, #1 //multiply by 2, store product in R2
	add R0, R1, R2 //add results x*(8+2) = x*10

	pop {pc}
	
