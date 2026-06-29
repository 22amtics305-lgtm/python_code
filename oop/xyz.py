class demo:
   def _int_(self):
    print("dafult con called")
#objname=cn()
obj=demo()

class demo:
  #classbvar
  ins_name="linkcode"

#1) class.name.varname
#print(ins_name)======error
print(demo.ins_name)

#2)objrefvar.name
obj=demo()
print(obj.ins_name)
