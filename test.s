	.file	"test.c"
	.text
	.comm	j_1,65536,32
	.comm	j_2,65536,32
	.comm	j_3,65536,32
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
	subq	$1040, %rsp
	movl	%edi, -1028(%rbp)
	movq	%rsi, -1040(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
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
	leaq	j_3(%rip), %rdx
	leaq	j_2(%rip), %rsi
	leaq	j_1(%rip), %rdi
	call	init_test
	movq	$0, -1016(%rbp)
	jmp	.L5
.L6:
	movq	-1016(%rbp), %rax
	leaq	0(,%rax,8), %rdx
	leaq	j_3(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	-1016(%rbp), %rdx
	leaq	0(,%rdx,8), %rcx
	leaq	j_1(%rip), %rdx
	movq	(%rcx,%rdx), %rcx
	movq	-1016(%rbp), %rdx
	leaq	0(,%rdx,8), %rsi
	leaq	j_2(%rip), %rdx
	movq	(%rsi,%rdx), %rdx
	addq	%rcx, %rdx
	leaq	(%rax,%rdx), %rcx
	movq	-1016(%rbp), %rax
	leaq	0(,%rax,8), %rdx
	leaq	j_3(%rip), %rax
	movq	%rcx, (%rdx,%rax)
	addq	$1, -1016(%rbp)
.L5:
	cmpq	$8191, -1016(%rbp)
	jbe	.L6
	movl	$0, %eax
	movq	-8(%rbp), %rsi
	xorq	%fs:40, %rsi
	je	.L8
	call	__stack_chk_fail@PLT
.L8:
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
