import random, sys

from secret import flag

msg = '''====== Welcome To Nrd Game ======
Find the nth largest number for me !
----- Example -----
Numbers : 1 3 6 12 8 9 13 11
Nth : 2
Answer > 12
----- Now Your Turn -----
'''

def main():
    print(msg)

    num_list = [random.randint(100, 99999) for _ in range(300)]
    nth = random.randint(0, 299)
    print('Numbers : ' + ' '.join(str(num) for num in num_list))
    print(f'Nth : {nth}')

    input_num = int(input('Answer > '))

    num_list.sort()
    if input_num == num_list[-nth]:
        print(f'Flag : {flag}')
    else:
        print('Wrong answer !')

try:
    main()
except:
    sys.exit()