'''
Program written by: Elliot, Marcus
Code copied from GitHub Repo:  https://github.com/theballmarcus/math_solutions.git

'''
#IMPORT SECTION


#DEFINEMENT SECTION
dicti = [
    {"a" : {}},
    {"b" : {}}, 
    {"c" : {}}
    ]


x = None
y = None
z = None

#MAIN PROGRAM


for a in range(0,100):
    for b in range(0,100):
        if a == b:
            pass
        else:
            for c in range(0,100):
                if a == c or b == c:
                    pass
                else:
                    curVal = [
                        {"a" : a}, 
                        {"b" : b}, 
                        {"c" : c}
                        ]
                    print(curVal)
                    curBest = {"a" : None, "b" : None, "c" : None}
                    