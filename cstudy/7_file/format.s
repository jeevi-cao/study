	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 13, 1
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movl	$0, -4(%rbp)
	movq	_pa@GOTPCREL(%rip), %rax
	movq	_boya@GOTPCREL(%rip), %rcx
	movq	%rcx, (%rax)
	movq	_pb@GOTPCREL(%rip), %rax
	movq	_boyb@GOTPCREL(%rip), %rcx
	movq	%rcx, (%rax)
	leaq	L_.str(%rip), %rdi
	leaq	L_.str.1(%rip), %rsi
	callq	_fopen
	movq	%rax, -16(%rbp)
	cmpq	$0, %rax
	jne	LBB0_2
## %bb.1:
	leaq	L_.str.2(%rip), %rdi
	callq	_puts
	xorl	%edi, %edi
	callq	_exit
LBB0_2:
	leaq	L_.str.3(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	$0, -20(%rbp)
LBB0_3:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$2, -20(%rbp)
	jge	LBB0_6
## %bb.4:                               ##   in Loop: Header=BB0_3 Depth=1
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rsi
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rdx
	addq	$12, %rdx
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rcx
	addq	$16, %rcx
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %r8
	addq	$20, %r8
	leaq	L_.str.4(%rip), %rdi
	movb	$0, %al
	callq	_scanf
## %bb.5:                               ##   in Loop: Header=BB0_3 Depth=1
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rcx
	addq	$24, %rcx
	movq	_pa@GOTPCREL(%rip), %rax
	movq	%rcx, (%rax)
	jmp	LBB0_3
LBB0_6:
	movq	_pa@GOTPCREL(%rip), %rax
	movq	_boya@GOTPCREL(%rip), %rcx
	movq	%rcx, (%rax)
	movl	$0, -20(%rbp)
LBB0_7:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$2, -20(%rbp)
	jge	LBB0_10
## %bb.8:                               ##   in Loop: Header=BB0_7 Depth=1
	movq	-16(%rbp), %rdi
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rdx
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movl	12(%rax), %ecx
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movl	16(%rax), %r8d
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movss	20(%rax), %xmm0                 ## xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	leaq	L_.str.5(%rip), %rsi
	movb	$1, %al
	callq	_fprintf
## %bb.9:                               ##   in Loop: Header=BB0_7 Depth=1
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	movq	_pa@GOTPCREL(%rip), %rax
	movq	(%rax), %rcx
	addq	$24, %rcx
	movq	_pa@GOTPCREL(%rip), %rax
	movq	%rcx, (%rax)
	jmp	LBB0_7
LBB0_10:
	movq	-16(%rbp), %rdi
	callq	_rewind
	movl	$0, -20(%rbp)
LBB0_11:                                ## =>This Inner Loop Header: Depth=1
	cmpl	$2, -20(%rbp)
	jge	LBB0_14
## %bb.12:                              ##   in Loop: Header=BB0_11 Depth=1
	movq	-16(%rbp), %rdi
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rdx
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rcx
	addq	$12, %rcx
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %r8
	addq	$16, %r8
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %r9
	addq	$20, %r9
	leaq	L_.str.5(%rip), %rsi
	movb	$0, %al
	callq	_fscanf
## %bb.13:                              ##   in Loop: Header=BB0_11 Depth=1
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rcx
	addq	$24, %rcx
	movq	_pb@GOTPCREL(%rip), %rax
	movq	%rcx, (%rax)
	jmp	LBB0_11
LBB0_14:
	movq	_pb@GOTPCREL(%rip), %rax
	movq	_boyb@GOTPCREL(%rip), %rcx
	movq	%rcx, (%rax)
	movl	$0, -20(%rbp)
LBB0_15:                                ## =>This Inner Loop Header: Depth=1
	cmpl	$2, -20(%rbp)
	jge	LBB0_18
## %bb.16:                              ##   in Loop: Header=BB0_15 Depth=1
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rsi
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movl	12(%rax), %edx
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movl	16(%rax), %ecx
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movss	20(%rax), %xmm0                 ## xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	leaq	L_.str.6(%rip), %rdi
	movb	$1, %al
	callq	_printf
## %bb.17:                              ##   in Loop: Header=BB0_15 Depth=1
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	movq	_pb@GOTPCREL(%rip), %rax
	movq	(%rax), %rcx
	addq	$24, %rcx
	movq	_pb@GOTPCREL(%rip), %rax
	movq	%rcx, (%rax)
	jmp	LBB0_15
LBB0_18:
	movq	-16(%rbp), %rdi
	callq	_fclose
	xorl	%eax, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.comm	_boya,48,4                      ## @boya
	.comm	_pa,8,3                         ## @pa
	.comm	_boyb,48,4                      ## @boyb
	.comm	_pb,8,3                         ## @pb
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"./stu.txt"

L_.str.1:                               ## @.str.1
	.asciz	"wt+"

L_.str.2:                               ## @.str.2
	.asciz	"Fail to open file!"

L_.str.3:                               ## @.str.3
	.asciz	"Input data:\n"

L_.str.4:                               ## @.str.4
	.asciz	"%s %d %d %f"

L_.str.5:                               ## @.str.5
	.asciz	"%s %d %d %f\n"

L_.str.6:                               ## @.str.6
	.asciz	"%s  %d  %d  %f\n"

.subsections_via_symbols
