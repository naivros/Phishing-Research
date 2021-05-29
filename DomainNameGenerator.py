word = "organizationname"
wordlist = ["corp", "inc", "login", "org", "online", "portal", "network", "developer", "intranet"];
domains = ["com","app","co"]

res = []

#Omit Each Letter

for i in range(0,len(word)):
  a = word[0:i]
  b = word[i+1:]
  n = word[i]
  res.append(a+n+n+b)
  res.append(a+b)
  
a = word[0]
b = ""

# Handle Duplicate Characters
for i in range(1,len(word)):
  if len(b) > 0:
    a = b
  b = word[i]
  if(a==b):
      res.append(word[:i-1]+word[i:]) # twiter
      res.append(word[:i-1]+a+b+word[i:]) # twittter
      res.append(word[:i-1]+word[i+1:]) # twiter
      
for w in wordlist:
    res.append(word+w)

for r in res:
    for d in domains:
        print(f"{r}.{d}")
    
