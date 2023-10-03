from secret import plain, a, b

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."

def msg2numlist(msg):
    assert len(msg) % 2 == 0
    return [(alphabet.index(msg[2 * i]) * 29 + alphabet.index(msg[2 * i + 1])) for i in range(len(msg) // 2)]

def numlist2msg(numlist):
    return ''.join([alphabet[n // 29] + alphabet[n % 29] for n in numlist])

def encrypt(plain, a, b):
    return numlist2msg([((a * num + b) % (len(alphabet) ** 2)) for num in msg2numlist(plain)])

print(encrypt(plain, a, b))