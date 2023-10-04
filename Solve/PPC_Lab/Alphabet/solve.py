from pwn import *
from string import ascii_letters
from tqdm import trange

def count_letter(msg):
    sum = 0
    for char in msg:
        if char in ascii_letters:
            sum += 1
    return sum

r = remote('172.104.90.38', 10005)

r.recvlines(7)

for i in trange(100):
    r.recvline()
    msg = r.recvline().strip().split(b': ')[1].decode()
    r.sendlineafter(b'> ', str(count_letter(msg)).encode())

r.interactive()