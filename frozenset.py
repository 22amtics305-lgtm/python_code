x=frozenset([1,2])
print(x,type(x))
  
roles=frozenset(["admin","facuty","recepist"])
for i in roles:
    if i=="admin":
        print(i)
roles.add("hacker")