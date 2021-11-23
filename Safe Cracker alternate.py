#This method is for the SaffeCracker Puzzle 40.

#The baseboard, outer ring
#Does not rotate
A=[10,19,10,13,10,2,15,23,19,3,2,3,27,20,11,27] 

#BA is the underneath 2nd outer ring repeated twice, it is hard linked to A at each index location.
#Does not rotate
BA=[3,12,24,10,9,22,9,5,10,5,1,24,2,10,9,7,3,12,24,10,9,22,9,5,10,5,1,24,2,10,9,7] 

#The 2nd outer ring, top layer, rotates, repeated twice.  
#Each subsequent index location for B is index location x2 for CB. (i.e. 0,1,2 in B is 1,3,5,7,9 or 0,2,4,6,8, etc. in CB)
B=[10,15,6,9,16,17,2,2,10,15,6,9,16,17,2,2]

#CB is the underneath 2nd inner ring repeated twice, it is hard linked to B at each even index location of CB (0,2,4,6, etc).
#as B rotates, CB rotates identically
CB=[8,3,6,15,22,6,1,1,11,27,14,5,5,7,8,24,8,3,6,15,22,6,1,1,11,27,14,5,5,7,8,24]

#The 2nd inner ring, top layer, rotates, repeated twice.  
#Each subsequent index location for C is index location x2 for DC. (i.e. 0,1,2 in C is 1,3,5,7,9 or 0,2,4,6,8, etc. in DC)
C=[10,2,22,2,17,15,14,5,10,2,22,2,17,15,14,5] 

#DC is the underneath inner ring repeated twice, it is hard linked to C at each even index location of DC (0,2,4,6, etc).
#as C rotates, DC rotates identically
DC=[1,6,10,6,10,2,6,10,4,1,5,5,4,8,6,3,1,6,10,6,10,2,6,10,4,1,5,5,4,8,6,3]

#The inner ring, top Layer, rotates, repeated twice.
D=[10,10,10,6,13,3,3,6,10,10,10,6,13,3,3,6]

#Place holders for the active lists being tested
rowA=[0]*16
rowB=[0]*16
rowC=[0]*16
rowD=[0]*16
sums=[0]*16

#The rotational index adjuster (the column offset)
rotateB=0
rotateC=0
rotateD=0
itterations=0

#There is an ideal optimization avaiable using sum largest element principle that would reduce the required run space.
#The ideal optimization is not implemented in the below loop.
#To implement, pick a target row, find largest value, iterate for column_sum=40 on that column alone.
#This will provide a much smaller list of offsets to check.
#Pick a new target row (can be the same), and find the largest value excluding the one from previous step.
#Iterate only over known working offset groups to find the subset of working offset groups.
#Repeat until there are either minimal column sets to check or the sum check for all columns is successful.

#This series of loops first assigns the active lists values based on the rotational index adjustment of the primary layer
#then updates the active lists based on the position of the linked, upper layer.
#Afterward, it checks the sum of the lists at each index location checking if it totals 40.
#Once the primary loop has ran, it will rotate the outermost layer and run the primary loop again, 
#so on and so on for each ring/row
i=0
while(rotateD<16):
    while(rotateC<16):
        while(rotateB<16):
            while(i<16):
                rowA[i]=A[i]
                rowB[i]=BA[i]
                rowC[i]=CB[i+rotateB]
                rowD[i]=DC[i+rotateC]
                
                #This section updates indexes for the top layer to each row.
                #This conditional section accounts for the odd/even relationship between the layers/rows being rotated.
                if(rotateB==0 or rotateB%2==0):
                    if(i==0 or i%2==0):
                        rowB[i]=B[(int(i/2))+(int(rotateB/2))]
                if(rotateB%2==1):
                    if(i%2==1):
                        rowB[i]=B[(int((i-1)/2))+(int((rotateB+1)/2))]

                if(rotateC==0 or rotateC%2==0):
                    if(i==0 or i%2==0):
                        rowC[i]=C[(int(i/2))+(int(rotateC/2))]
                if(rotateC%2==1):
                    if(i%2==1):
                        rowC[i]=C[(int((i-1)/2))+(int((rotateC+1)/2))]            

                if(rotateD==0 or rotateD%2==0):
                    if(i==0 or i%2==0):
                        rowD[i]=D[(int(i/2))+(int(rotateD/2))]
                if(rotateD%2==1):
                    if(i%2==1):
                        rowD[i]=D[(int((i-1)/2))+(int((rotateD+1)/2))]
                i+=1
            
            #This loop and subsequent sumcheck could be its own method.  
            #Adds the value of each row at a particular index and checks if it sums to 40.
            #If at anypoint it does not sum to 40, it fails the test and exits the check.
            #If it does not fail the test, it will print the rows and a copy of the sum list.
            i=0
            sumcheck=True
            while(i<16):
                sums[i]=rowA[i]+rowB[i]+rowC[i]+rowD[i]
                if(sumcheck and sums[i]==40):
                    i+=1
                else:
                    sumcheck=False
                    break
            if(sumcheck):
                print(rowA)
                print(rowB)
                print(rowC)
                print(rowD,"\n")
                print(sums)
            
            itterations+=1
            rotateB+=1
            i=0
        rotateC+=1
        rotateB=0
        i=0
    rotateD+=1
    rotateC=0
    rotateB=0
    i=0
