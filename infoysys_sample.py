n = int(input("Enter no of type :"))
m = int(input("Maximum meal:"))
total=0
v = []
d = []

for i in range(n):
    v.append(int(input("Enter v:")))

for i in range(n):
    d.append(int(input("Enter d:")))
def count_points(x):
    count=0
    for i in range(n):
        if v[i]>=x:
            k=(v[i]-x)//d[i]+1
            count=count+k
    return count
def sum_points(x):
    total=0
    for i in range(n):
        if v[i]>=x:
            k=(v[i]-x)//d[i]+1
            total = total + k * (2*v[i] - (k-1)*d[i]) // 2
    return total

positive_count = count_points(1)

if positive_count <= m:
    answer = sum_points(1)
else:
    low = 1
    high = max(v)

    while low < high:
        mid = (low + high + 1) // 2

        if count_points(mid) >= m:
            low = mid
        else:
            high = mid - 1

    answer = sum_points(low + 1)
    used = count_points(low + 1)
    answer = answer + (m - used) * low

print(answer)
            # print(v)
# print(d)