from pwn import *
from tqdm import trange

r = remote('172.104.90.38', 10002)

r.recvlines(2)

for i in trange(100):
    r.recvline()
    r.sendlineafter(b'> ', str(i + 1).encode())

r.interactive()