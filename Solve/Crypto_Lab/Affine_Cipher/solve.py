from string import ascii_lowercase
from tqdm import trange
import hashlib

char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'

def simple_freq_analysis(msg: str):
    msg = list(msg.lower())
    english_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    msg_freq = [100 * msg.count(s) / len(msg) for s in ascii_lowercase]
    return int(sum(((mf - ef) / ef) ** 2 for mf, ef in zip(msg_freq, english_freq)))

def affine_decrypt(cipher, a, b):
    return ''.join([char_set[(pow(a, -1, len(char_set)) * (char_set.index(char) - b)) % len(char_set)] for char in cipher])

cipher = open('cipher').read()

r_list = []
key_list = []
for a in trange(1, len(char_set)):
    for b in range(len(char_set)):
        r_list.append(simple_freq_analysis(affine_decrypt(cipher, a, b)))
        key_list.append((a, b))

key = key_list[r_list.index(min(r_list))]
plain = affine_decrypt(cipher, key[0], key[1])

print(f'flag{{{hashlib.md5(plain.encode()).hexdigest()}}}')