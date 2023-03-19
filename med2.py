import math

arr=list(map(int, input().strip().split()))
limit = math.floor(len(arr)/3)
result= []
refer={}
if len(arr)==1:
  print(arr)
else:
  for i in range(0, len(arr)):
    if arr[i] in refer.keys():
      refer[arr[i]]+=1
    else:
      refer[arr[i]]=1
  for i in refer.keys():
    if refer[i]>limit:
      result.append(i)
  print(result)