# For Loop within For Loop is called Nested Loop
# Syntax
# for initialize/Declare Variable in Range(start,End-1, Gap)


for i in range(0,4,2):
    for j in range(0,4,3):
        for k in range(0,4,4):
            print("Iteration: ",i, j,k)