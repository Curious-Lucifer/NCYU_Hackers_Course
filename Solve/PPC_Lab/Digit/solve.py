from pwn import *
from tqdm import trange

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

r = remote('172.104.90.38', 10007)

r.recvlines(3)

for i in trange(100):
    r.recvline()

    n = digit.index(b'\n'.join(r.recvlines(9)).decode())
    r.sendlineafter(b'? ', str(n).encode())

    r.recvline()

r.interactive()