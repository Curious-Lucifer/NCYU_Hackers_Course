from base64 import b64encode
import random, string, sys

from secret import flag

charset = string.ascii_letters + string.digits + string.punctuation

def main():
    print('====== Welcome To Identify Test ======')
    print('Here\'s some normal string/hex string/base64 encode string.')
    print('Please identify it and return normal string.')

    for i in range(100):
        mode = random.randint(0, 2)
        ans = ''.join(random.choices(charset, k = 18))
        if mode == 0:
            chal = ans
        elif mode == 1:
            chal = ans.encode().hex()
        else:
            chal = b64encode(ans.encode()).decode()
        print(f'------ wave {i + 1}/100 ------')
        print(f'Chal : {chal}')
        inp = input('Answer > ')
        if inp != ans:
            print('Wrong answer !')
            sys.exit()

    print(f'Flag : {flag}')

try:
    main()
except:
    sys.exit()