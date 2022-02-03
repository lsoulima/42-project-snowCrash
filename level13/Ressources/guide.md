# Level13

Se connecter en tant que `level13`:

    $ ssh 192.168.1.124 -p 4242 -l level13
    level13@192.168.1.124's password: g1qKMiRpXf53AWhDaU7FEkczr

---

Premiere étape de recherche

    $ ls -la
    -rwsr-sr-x 1 flag13  level13 7303 Aug 30  2015 level13

On trouve un binaire setuid/setgid

    $ ./level13
    UID 2013 started us but we we expect 4242

Il demande a etre executé par un uid specifique

Regardons avec GDB

    $ gdb level13
    (gdb) disas main
    Dump of assembler code for function main:
       0x0804858c <+0>:		push   %ebp
       0x0804858d <+1>:		mov    %esp,%ebp
       0x0804858f <+3>:		and    $0xfffffff0,%esp
       0x08048592 <+6>:		sub    $0x10,%esp
       0x08048595 <+9>:		call   0x8048380 <getuid@plt>   # getuid() is called and the result is stored in eax register
       0x0804859a <+14>:	cmp    $0x1092,%eax             # %eax register is compared against 0x1092 (4242)
       0x0804859f <+19>:	je     0x80485cb <main+63>      # if it equal jump to 0x080485cb
       0x080485a1 <+21>:	call   0x8048380 <getuid@plt>
       0x080485a6 <+26>:	mov    $0x80486c8,%edx
       0x080485ab <+31>:	movl   $0x1092,0x8(%esp)
       0x080485b3 <+39>:	mov    %eax,0x4(%esp)
       0x080485b7 <+43>:	mov    %edx,(%esp)
       0x080485ba <+46>:	call   0x8048360 <printf@plt>
       0x080485bf <+51>:	movl   $0x1,(%esp)
       0x080485c6 <+58>:	call   0x80483a0 <exit@plt>
       0x080485cb <+63>:	movl   $0x80486ef,(%esp)
       0x080485d2 <+70>:	call   0x8048474 <ft_des>       # call ft_des() function
       0x080485d7 <+75>:	mov    $0x8048709,%edx
       0x080485dc <+80>:	mov    %eax,0x4(%esp)
       0x080485e0 <+84>:	mov    %edx,(%esp)
       0x080485e3 <+87>:	call   0x8048360 <printf@plt>
       0x080485e8 <+92>:	leave
       0x080485e9 <+93>:	ret
    End of assembler dump.

Le check est fait avec getuid a la ligne `+9`, il faut le forcer a retourner un faux uid

On met un breakpoint sur la fonction getuid

    (gdb) b getuid
    Breakpoint 1 at 0x8048380

On lance le programme

    (gdb) r
    Starting program: /home/user/level13/level13

    Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6

On avance step by step jusqu'au return du getuid

    (gdb) s
    Single stepping until exit from function getuid,
    which has no line number information.
    0x0804859a in main ()

On regarde le registre [eax](https://opensourceforu.com/2011/08/modify-function-return-value-hack-part-1/) où la valeur de retour de getuid est stockée

    (gdb) print $eax
    $1 = 2013

C'est bien ça, on la change pour 4242, le uid attendu par le programme

    (gdb) set $eax=4242

    (gdb) s
    Single stepping until exit from function main,
    which has no line number information.
    your token is 2A31L79asukciNyi8uppkEuSx
