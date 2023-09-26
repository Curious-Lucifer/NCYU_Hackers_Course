import random, sys

from secret import flag

digit = [
'''
  ###   
 #   #  
#     # 
#     # 
#     # 
 #   #  
  ###
''',
'''
   #   
  ##   
 # #   
   #   
   #   
   #   
 #####
''',
'''
 #####  
#     # 
      # 
 #####  
#       
#       
#######
''',
'''
 #####  
#     # 
      # 
 #####  
      # 
#     # 
 #####
''',
'''
#       
#    #  
#    #  
#    #  
####### 
     #  
     #
''',
'''
####### 
#       
#       
######  
      # 
#     # 
 #####
''',
'''
 #####  
#     # 
#       
######  
#     # 
#     # 
 #####
''',
'''
####### 
#    #  
    #   
   #    
  #     
  #     
  #
''',
'''
 #####  
#     # 
#     # 
 #####  
#     # 
#     # 
 #####
''',
'''
 #####  
#     # 
#     # 
 ###### 
      # 
#     # 
 #####
'''
]

msg = '''====== Welcome To Digit Game ======
Can you help me recognize some digits?
'''

def main():
    print(msg)

    for i in range(100):
        print(f'----- wave {i + 1}/100 -----')
        num = random.randint(0, 9)
        print(digit[num])
        if int(input('What is this digit? ')) == num:
            print('You are right !')
        else:
            print('No, Your eye is malfunctioned.')
            sys.exit()

    print(f'Flag : {flag}')

try:
    main()
except:
    sys.exit()