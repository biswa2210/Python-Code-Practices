def func(normal,*args,**kwargs):
    """this is a function  and list and dictionary passing as parameter in func"""
    print(normal,args,kwargs)

normal="THIS IS OUR ARGS AND KWARGS"
pok=["pokpokpoka","ninjathepok","legendarypok","ultrapok"]
galagali={"gandu":"suyor","khanki":"chutiya"}
func(normal,*pok,**galagali)

print(func.__doc__)
