	.file	"test.c"
	.text
	.globl	init_test
	.type	init_test, @function
init_test:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movq	%rsi, -32(%rbp)
	movq	%rdx, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L2
.L3:
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-4(%rbp), %eax
	cltq
	movq	%rax, (%rdx)
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-32(%rbp), %rax
	addq	%rax, %rdx
	movl	-4(%rbp), %eax
	cltq
	movq	%rax, (%rdx)
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-40(%rbp), %rax
	addq	%rax, %rdx
	movl	-4(%rbp), %eax
	cltq
	movq	%rax, (%rdx)
	addl	$1, -4(%rbp)
.L2:
	cmpl	$8191, -4(%rbp)
	jle	.L3
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	init_test, .-init_test
	.section	.rodata
.LC0:
	.string	"pmap -X %d"
	.align 8
.LC1:
	.string	"i = %p\nv1 = %p\ntest[0] = %p\ntest[1] = %p\ntest[2] = %p\n"
.LC2:
	.string	"date"
	.align 8
.LC3:
	.string	"i = 0x%lx\nv1 = 0x%lx\ntest[0][%ld] = 0x%lx\ntest[1][%ld] = 0x%lx\ntest[2][%ld] = 0x%lx\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB7:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	-196608(%rsp), %r11
.LPSRL0:
	subq	$4096, %rsp
	orq	$0, (%rsp)
	cmpq	%r11, %rsp
	jne	.LPSRL0
	subq	$1072, %rsp
	movl	%edi, -197668(%rbp)
	movq	%rsi, -197680(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$0, -197660(%rbp)
	cmpl	$3, -197668(%rbp)
	jg	.L5
	movl	$0, %eax
	jmp	.L6
.L5:
	cmpl	$4, -197668(%rbp)
	jg	.L7
	call	getpid@PLT
	movl	%eax, %edx
	leaq	-1008(%rbp), %rax
	leaq	.LC0(%rip), %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	sprintf@PLT
	leaq	-1008(%rbp), %rax
	movq	%rax, %rdi
	call	system@PLT
	movl	$30, %edi
	call	sleep@PLT
.L7:
	cmpl	$6, -197668(%rbp)
	jne	.L8
	movl	$1, -197660(%rbp)
.L8:
	leaq	-66544(%rbp), %rdi
	leaq	-132080(%rbp), %rsi
	leaq	-197616(%rbp), %rcx
	leaq	-197648(%rbp), %rdx
	leaq	-197656(%rbp), %rax
	movq	%rdi, %r9
	movq	%rsi, %r8
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	leaq	.LC2(%rip), %rdi
	call	system@PLT
	cmpl	$0, -197660(%rbp)
	je	.L9
#APP
# 47 "test.c" 1
	nop
# 0 "" 2
#NO_APP
.L9:
	leaq	-66544(%rbp), %rdx
	leaq	-132080(%rbp), %rcx
	leaq	-197616(%rbp), %rax
	movq	%rcx, %rsi
	movq	%rax, %rdi
	call	init_test
	cmpl	$0, -197660(%rbp)
	je	.L10
#APP
# 51 "test.c" 1
	nop
# 0 "" 2
#NO_APP
.L10:
	movq	$0, -197656(%rbp)
	jmp	.L11
.L12:
	movq	-197656(%rbp), %rax
	movq	-66544(%rbp,%rax,8), %rdx
	movq	-197656(%rbp), %rax
	movq	-197616(%rbp,%rax,8), %rcx
	movq	-197656(%rbp), %rax
	movq	-132080(%rbp,%rax,8), %rax
	addq	%rax, %rcx
	movq	-197656(%rbp), %rax
	addq	%rcx, %rdx
	movq	%rdx, -66544(%rbp,%rax,8)
	movq	-197656(%rbp), %rax
	addq	$1, %rax
	movq	%rax, -197656(%rbp)
.L11:
	movq	-197656(%rbp), %rax
	cmpq	$8191, %rax
	jbe	.L12
	cmpl	$0, -197660(%rbp)
	je	.L13
#APP
# 56 "test.c" 1
	nop
# 0 "" 2
#NO_APP
.L13:
	movq	-197680(%rbp), %rax
	addq	$8, %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	atoi@PLT
	cltq
	movq	%rax, -197640(%rbp)
	movq	-197680(%rbp), %rax
	addq	$16, %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	atoi@PLT
	cltq
	movq	%rax, -197632(%rbp)
	movq	-197680(%rbp), %rax
	addq	$24, %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	atoi@PLT
	cltq
	movq	%rax, -197624(%rbp)
	movq	-197624(%rbp), %rax
	movq	-66544(%rbp,%rax,8), %rdi
	movq	-197632(%rbp), %rax
	movq	-132080(%rbp,%rax,8), %rsi
	movq	-197640(%rbp), %rax
	movq	-197616(%rbp,%rax,8), %r8
	movq	-197648(%rbp), %rdx
	movq	-197656(%rbp), %rax
	movq	-197632(%rbp), %r9
	movq	-197640(%rbp), %rcx
	subq	$8, %rsp
	pushq	%rdi
	pushq	-197624(%rbp)
	pushq	%rsi
	movq	%rax, %rsi
	leaq	.LC3(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	addq	$32, %rsp
	leaq	.LC2(%rip), %rdi
	call	system@PLT
	movl	$0, %eax
.L6:
	movq	-8(%rbp), %rsi
	xorq	%fs:40, %rsi
	je	.L14
	call	__stack_chk_fail@PLT
.L14:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
