from pwn import *

r = remote('172.104.90.38', 10001)

r.recvlines(8)

numbers = [int(num) for num in  r.recvline().strip().split(b': ')[1].split()]
numbers.sort()

n = int(r.recvline().strip().split(b': ')[1])

r.sendlineafter(b'> ', str(numbers[-n]).encode())

r.interactive()