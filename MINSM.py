
# cook your dish here
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    if a[0]==1:
        print(len(a))
    else:
        ans=a[0]
        for i in range(len(a)-1):
            ans=min(ans,hcfnaive(a[i],a[i+1]))
        print(ans*len(a))
            
            
