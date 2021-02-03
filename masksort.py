#python3

from bisect import bisect

data = []

with open('corp_8-14.statsgen') as f:
 for line in f:
  mask = line.split(",")[0] 
  cracked = line.split(",")[1] 
  masksplit = mask.split("?")
  number = 1
  for element in masksplit: 
   if element == 'u':
   	number = number * 26
   elif element == 'l':
   	number = number * 26
   elif element == 'd':
   	number = number * 10
   elif element == 's':
   	number = number * 33

  
  efficiency = int(number/int(cracked))
  a = efficiency
  b = mask
  data.insert(bisect(data,(a,b)),(a,b))
  number = 1

for d in data: 
 print (d[1])
