A=[1,2,3,4,5]
print(A)
for i in range(len(A)):
    A[i]+=1
print(A)

B=[a+1 for a in A]
print(B)

B=[A[i]+1 for i in range(len(A))]
print(B)