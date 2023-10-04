import string, hashlib

cipher = open('cipher').read()
double_num_freq = [(cipher.count(str(i) * 2), i) for i in range(10)]
double_num_freq.sort(reverse=True)

cipher_char_list = []
i = 0
while i < len(cipher):
    if (cipher[i] == str(double_num_freq[0][1])) or (cipher[i] == str(double_num_freq[1][1])):
        cipher_char_list.append(cipher[i: i + 2])
        i += 2
    else:
        cipher_char_list.append(cipher[i])
        i += 1

cipher_char_set = list(set(cipher_char_list))
map_list = string.ascii_uppercase[:len(cipher_char_set)]

substitudtion_cipher = ''
for c in cipher_char_list:
    substitudtion_cipher += map_list[cipher_char_set.index(c)]

print(substitudtion_cipher.lower())

# copy substitudtion_cipher to https://www.guballa.de/substitution-solver and get the plain
# the last few words in plain is the flag