from string import ascii_lowercase
from tqdm import trange
import hashlib

char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."

def simple_freq_analysis(msg: str):
    msg = list(msg.lower())
    english_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    msg_freq = [100 * msg.count(s) / len(msg) for s in ascii_lowercase]
    return int(sum(((mf - ef) / ef) ** 2 for mf, ef in zip(msg_freq, english_freq)))

cipher = open('cipher').read()

def msg2numlist(msg):
    return [(char_set.index(msg[2 * i]) * 29 + char_set.index(msg[2 * i + 1])) for i in range(len(msg) // 2)]

def numlist2msg(numlist):
    return ''.join([char_set[n // 29] + char_set[n % 29] for n in numlist])

def affine_double_decrypt(cipher, a, b):
    return numlist2msg([((pow(a, -1, 29 ** 2) * (num - b)) % (29 ** 2)) for num in msg2numlist(cipher)])

key_list = []
r_list = []
for i in trange(29 ** 2):
    if (i % 29) == 0:
        continue
    for j in range(29 ** 2):
        approximate_val = simple_freq_analysis(affine_double_decrypt(cipher, i, j).replace(' ', '').replace(',', '').replace('.', ''))
        if approximate_val < 500:
            key_list.append((i, j))
            r_list.append(approximate_val)

key = key_list[r_list.index(min(r_list))]
plain = affine_double_decrypt(cipher, key[0], key[1])

print(f'flag{{{hashlib.md5(plain.encode()).hexdigest()}}}')
