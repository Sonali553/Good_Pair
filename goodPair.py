l = list(map(int, input().split()))
k = int(input("Enter K: "))
def goodPair(lst, k):
 for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == k:
            return 1
 return 0
print(goodPair([1,2,3,4], 7))
print(goodPair([1,2,4], 4))
print(goodPair([1,2,2], 4))
print(goodPair(l, k))
