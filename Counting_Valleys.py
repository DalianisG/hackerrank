steps = int(input())
path = str(input())

U="U"
X=0
K=0

for i in range(steps): 
    if U in path[i]:
        X=X+1
        if X == 0:
            K = K + 1
    else:
        X = X-1

print(K)