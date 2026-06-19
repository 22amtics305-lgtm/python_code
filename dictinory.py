x = {}
print(x, type(x))
# add--> ref[key]=value
x["roll_no"] = 101
x["name"] = "ram"
print(x)

#access --->x[key]--->value
print(x["name"])

#update -->ref[key]=newvalue
x = {"name": "sita"}
print(x["name"])

#
stud={
    "roll_no":"101",
    "name":"ram",
    "age":"30",
    "subjects":["math","english","java"],
    "marks":(90,80,76)
}
print(stud)
#method
print(stud.keys())
print(stud.values())
print(stud.items())

#loop
for key in stud:
    print(key)
    
for values in stud.values():
        print(values)
        
for k,v in stud.items():
            print(k,v)

for v in stud["subjects"]:
    print(v)     
    
for key in stud:
    if key=="subjects":
        for v in key:
            print(v)    
#math--90 
for v in stud["marks"]:
    print(v)
us="sub"
for key in stud:
    if key==us:
        for v in stud[key]:
            print(v)
#math==90
print(stud["age"])
print(stud["subjects"][1])
print(stud["marks"][2])    

for k,v in stud.items():
    print(k,v)     

#sub:marks
print(len(stud["subjects"]))
for i in range(len(stud["subjects"])): #3
    print(f"{stud["subjects"][i]}:{stud["marks"][2]}")
    
#zip()
stud={
    "roll_no":"101",
    "name":"ram",
    "age":"30",
    "subjects":["math","english","java"],
    "marks":(90,80,76)
}       
for sv,mv  in zip(stud["subjects"],stud["marks"]):
    print(sv,mv)
    
stud = {
    101: {
        "name":"ram",
        "age":30,
        "sub":["math","eng","java"],
        "marks":(90, 80, 70)
    },
    102: {
        "name":"sita",
        "age":"23",
        "subjects":["math","eng","java"],
        "marks":(50,40,90)
    },
    103:{
        "name":"shyam",
        "age":"29",
        "subjects":["math","eng","java"],
        "marks":(95,81,74)
    }
}    
           
for key in stud:
    print(key)

for key in stud:
    for v in stud[key]["marks"]:
        print(v ,end=" ")    
    print()
    
#
#
for key, details in stud.items():
    print(f"Student id:{key}")
    for k, v in details.items():
        print(k, v)
        
    
