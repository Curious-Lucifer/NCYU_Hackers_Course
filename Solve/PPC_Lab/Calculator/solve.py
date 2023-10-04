from pwn import *
from tqdm import trange

r = remote('172.104.90.38', 10004)

r.recvlines(3)

for i in trange(100):
    r.recvline()

    chal = r.recvline().strip().split()
    a, b, c = int(chal[0]), int(chal[2]), int(chal[4])
    if (a + b) == c:
        ans = b'+'
    elif (a - b) == c:
        ans = b'-'
    else:
        ans = b'*'
    r.sendlineafter(b'? ', ans)

r.interactive()