0, 0, SPECIAL, mem_read
1, 0, SPECIAL, mem_write
2, 0, CATEGORY, COND_BR
2, 1, CATEGORY, UNCOND_BR
2, 2, OPCODE, LEAVE
2, 3, OPCODE, RET_NEAR
2, 4, OPCODE, CALL_NEAR
3, 0, CATEGORY, LOGICAL
3, 1, CATEGORY, DATAXFER
3, 2, CATEGORY, BINARY
3, 3, CATEGORY, FLAGOP
3, 4, CATEGORY, BITBYTE
4, 0, CATEGORY, X87_ALU
4, 1, CATEGORY, FCMOV
5, 0, CATEGORY, POP
5, 1, CATEGORY, PUSH
6, 0, CATEGORY, SHIFT
7, 0, CATEGORY, STRINGOP
8, 0, CATEGORY, MMX
8, 1, CATEGORY, SSE
9, 0, CATEGORY, INTERRUPT
9, 1, CATEGORY, ROTATE
9, 2, CATEGORY, SEMAPHORE
9, 3, CATEGORY, CMOV
9, 4, CATEGORY, SYSTEM
9, 5, CATEGORY, MISC
9, 6, CATEGORY, PREFETCH
9, 7, CATEGORY, SYSCALL
10, 0, CATEGORY, WIDENOP
10, 1, CATEGORY, NOP