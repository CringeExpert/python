def fun(**kwargs):
    for k,v in kwargs.items():
        print(k,v,type(v))

sl = {"wiek":21,"wzrost":4.5,"1":1}

print(fun(sl))