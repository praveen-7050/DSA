def febi(n):
  a,b = 0,1
  result = []
  for _ in range(n-1):
     result.append(a)
     a,b = b,a+b
  return result
 
print(febi(10))