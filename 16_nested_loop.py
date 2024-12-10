# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)    
#####################################

# for fruit in  ["apple","ball"]:   
#     for animal in ["cat", "dog"]:
#         print(fruit,animal)

# output : 
# apple cat
# apple dog
# ball cat
# ball dog        


#######################################
# for i in "AB":
#     print(i)
#     for j in "CD":
#         print(j)
# output:
# A
# C
# D
# B
# C
# D      
##############################
# for i in range(6):
#     for j in range(i):
#         print("*",end = "")
#     print("")    

#############################
# for i in range(6,1,-1):
#     for j in range(i):
#         print("*",end = "")
#     print("")  

##############################

for i in "abcd":
    print(i)
    for j in "abcd":
        print(i,j)
        for k in "abcd":
            print(i,j,k)
            for l in "abcd":
                print(i,j,k,l)
        