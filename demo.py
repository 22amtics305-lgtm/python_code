student={
    101: {
        "name":"ram",
        "sub":["math","eng","java"],
        "marks":(90, 80, 70)
    },
    102: {
        "name":"sita",
        "sub":["math","eng","java"],
        "marks":(50,40,90)
    },
}
print(student[101]["sub"][0])
for key,values in student.items():
    for name,value in values.items():
      if type(value)==list or type(value)==tuple:
          for ele in value:
              print(ele)

#print(student[101]["sub"][0])
for key, values in student.items():#101:{}
    for k,v in values.items():#subkey subvalue
        if v[0]=='java':
            print(v[0])
        elif k=='marks':
            print(v[0])


for sid,detalis in student.items():#101{}
    for i in range(len(detalis["sub"])):#3
        if detalis["sub"][i]=='java':#
            print(detalis["sub"][i],detalis["marks"][i])

top_name=""
top_name=0
for sid,detalis in student.items():#101{}
 for i in range(len(detalis["sub"])):#3
        if detalis["sub"][i]=='python':#
            print(detalis["sub"][i],detalis["marks"][i]
            ,detalis["name"])
            if detalis["marks"][i]>top_marks:
                top_marks=detalis["marks"][i]#89
                top_name=detalis["name"]#ram 
                print(f"topper name is{top_name}{top_marks}")
