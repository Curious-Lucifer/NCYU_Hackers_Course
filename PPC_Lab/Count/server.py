import sys

from secret import flag

def main():
    print('====== Welcome To Counting Game ======')
    print('You just need to count from 1 to 100 !')

    for i in range(100):
        print(f'------ wave {i + 1}/100 ------')
        if int(input('> ')) != (i + 1):
            print('Wrong! You suck!')
            sys.exit()

    print(f'Flag : {flag}')

try:
    main()
except:
    sys.exit()