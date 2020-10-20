# 
#              Program written by: Marcus, cloned from rep: https://github.com/theballmarcus/code_stuff
#              Feel free to use this code, but I would appreciate keeping the repo link in the top of the file.
#


cur_number = 1
stopAt = 1000000

for x in range(stopAt):
    flag = True
    cur_number = cur_number + 2
    
    for i in range(2, (cur_number // 2) + 1):
        if(cur_number % i == 0):
            flag = False
            break
        
    if(flag == True):
        print('Prime found: %d' %cur_number)
