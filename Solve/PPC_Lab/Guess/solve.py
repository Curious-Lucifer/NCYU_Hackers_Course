from pwn import *
from tqdm import trange

r = remote('172.104.90.38', 10003)

r.recvlines(3)

range_list = [1, 1073741825]

while True:
    guess_num = (range_list[0] + range_list[1]) // 2

    r.sendlineafter(b'> ', str(guess_num).encode())
    resp = r.recvline()

    if b'big' in resp:
        range_list[1] = guess_num
    elif b'small' in resp:
        range_list[0] = guess_num + 1
    else:
        print(resp)
        break

r.interactive()