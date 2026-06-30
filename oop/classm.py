class demo:
    #classs var
    ins="hello"
    #classmethod
    @classmethod
    def greet(cls):
        #print("how are u?")
        return"hi"
    
    @classmethod
    def modify(cls,new_value):
        cls.ins=new_value
                
print(demo.greet())
print(demo.ins)
demo.modify("linkcode")
print(demo.ins)