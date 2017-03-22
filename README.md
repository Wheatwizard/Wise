# Wise

A esolang based in bitwise operators

## Description

Wise is a stack based programming language centered around bitwise operations.

Execution starts at the left most value and moves right until it reaches the end of the program.

Wise has 11 operations.

* `&`

  Bitwise And
  
  Take the biwise and of the top two items on the stack and pushes it
  
* `|`

  Bitwise Or
  
  Take the bitwise or of the top two items on the stack and pushes it
  
* `^`

  Bitwise Xor
  
  Take the bitwise xor of the top two items on the stack and pushes it
  
* `~`

  Bitwise Not
  
  Takes the bitwise not of the top item on the stack
  
* `<`

  Bitshift Left
  
  Takes the top of the stack and moves every bit one place to the left leaving a zero in the ones place
  
*  `>`

  Bitshift Right
  
  Takes the top of the stack and moves every bit one place to the right throwing out the bit that was in the ones place
  
*  `-`

   Negativize
  
   Multiply the number on the top of the stack by `-1`
  
*  `:`

   Duplicate
   
   Makes a second copy of the top item on the stack
   
*  `?` and `!`

   Roll
   
   `?` moves the top item to the bottom of the stack
   
   `!` moves the bottom item to the top of the stack
   
*  `[` and `]`

   Loop
   
   `[` jumps to the corresponding `]` if the top of the stack is zero
   
   `]` jumps to the corresponding `[` if the top of the stack is not zero
   
At the end of the program the entire stack is output as decimal
