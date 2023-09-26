import random, sys

from secret import flag

msg = '''====== Welcome To Guess Game ======
Guess the secret number ! Secret number is between 1 ~ 1073741824 !
'''
secret_num = random.randint(1, 1 << 30)

def main():
    print(msg)

    while True:
        guess_num = int(input('Guess > '))
        if guess_num == secret_num:
            print(f"Flag : {flag}")
            sys.exit()
        if guess_num > secret_num:
            print("Too big !")
        else:
            print("Too small !")

try:
    main()
except:
    sys.exit()