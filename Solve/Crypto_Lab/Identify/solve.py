from pwn import *
from base64 import b64decode
from tqdm import trange

def is_hex(msg):
    hex_char = '0123456789abcdef'
    if (len(msg) % 2) != 0:
        return False
    for char in msg:
        if not char in hex_char:
            return False
    return True

def is_base64(msg):
    base64_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    if (len(msg) % 4) != 0:
        return False
    for char in msg:
        if not char in base64_char:
            return False
    return True

r = remote('172.104.90.38', 10009)

r.recvlines(3)

for i in trange(100):
    r.recvline()

    chal = r.recvline().strip().split(b': ')[1].decode()
    if is_hex(chal):
        ans = bytes.fromhex(chal)
    elif is_base64(chal):
        ans = b64decode(chal.encode())
    else:
        ans = chal.encode()
    r.sendlineafter(b'> ', ans)

r.interactive()