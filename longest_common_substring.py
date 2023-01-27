def longestSubstring(a,b,c,d):
  ls = [[0 for k in range(d+1)] for l in range(c+1)]
  res = 0
  for i in range(c+1):
    forj in range(d+1):
      if (i ==0 or j ==0):
        ls[i] [j] = 0
      elif (a[i-1] == b[j-1]);
        ls[i] [j] ls [i-1] [j-1] +1
        res = max(res, ls[i][j])
      else:
        ls[i][j] = 0
  return res


# Main Program
a = input("Enter a string")
b = input("Enter Another string")
c = len(a)
d = len(b)
print("Lenght of longest common substring is ", longestSubstring(a,b,c,d))
