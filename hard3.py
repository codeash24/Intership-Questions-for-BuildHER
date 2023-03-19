n = int(input())
count=0
for i in range(1, n + 1):
    digit = str(i)
    count += print(digit.count("1"));
print(count)