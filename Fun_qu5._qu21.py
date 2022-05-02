
def fun(a,b):
    c=a+b
    return(c)
    print(c)
def fun(d,e):
    f=d+e
    return(f)
    print(f)
def fun(g,h):
    i=g+h
    return(i)
    print(i)
print(fun(20,25))
print(fun(40,3))
print(fun(40,4))

def fun():
    n=int(input("enter the number,,,"))
    m=int(input("enter the number,,,,"))
    operator=input("enter the operator,,,,")
    def op():
       if operator=="+":
           print(n+m)
           return(n+m)   
    def rt():
        op()
        if operator=="-":
            print(n-m)
            return(n-m)
    def yu():
        rt()
        if operator=="*":
            print(n*m)
            return(n*m)
    def gh():
        yu()
        if operator=="//":
            print(n//m)
            return(n//m)
        
    gh()
    
fun()