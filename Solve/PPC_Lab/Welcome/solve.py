from pwn import *

r = remote('172.104.90.38', 10000)

r.interactive()