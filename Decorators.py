
                                    # DECORATORS CONCEPT

def validation(func):
    def inner(*args):
        # print(args)
        # l = []
        # for i in args:
        #     if isinstance(i,int):
        #         l.append(i)
        # l = tuple(l)

        l = tuple(filter(lambda x: isinstance(x,int),args))
        return func(*l)
    return inner
@validation
def just(*args):
    print(f"args: {args}")
    return sum(args)

# print(just(1,2,3,'66',[45],123,'78'))


# PASSWORD VALIDATION


def password_validator(func):
    def inner(psd:str):
        sp = ['@','*','!','#','$','%','&','_','-','=','+','/']
        if len(psd)>=8:
            up = list(filter(lambda x: x.isupper(),psd))
            sc = list(filter(lambda x:x in sp, psd))
            dg = list(filter(lambda x: x.isdigit(),psd))

            print(up,sc,dg,sep='\n')

            if up and sc and dg:
                print("Strong Password")
                func(psd)
            else:
                print("Weak Password")
        else:
            print("password must contain 8 characters")
    return inner
@password_validator
def password(ps):
    print(f"password {ps} is accepted")

password("23456fghbnkH")
password("765FHGDk#$")

# REGISTRATION

def register(func):
    uns = []
    def inner(us,psd,age):
        nonlocal uns
        if us not in uns:
            sp = ['@', '*', '!', '#', '$', '%', '&', '_', '-', '=', '+', '/']
            if len(psd) >= 8:
                up = list(filter(lambda x: x.isupper(), psd))
                sc = list(filter(lambda x: x in sp, psd))
                dg = list(filter(lambda x: x.isdigit(), psd))

                print(up, sc, dg, sep='\n')

                if up and sc and dg:
                    print("Strong Password")
                    if age >= 18:
                        func(us,psd,age)
                        uns.append(us)
                    else:
                        print("Age must be >= 18")
                else:
                    print("Weak Password")
            else:
                print("password must contain 8 characters")
        else:
            print("User name already exists")
    return inner

@register
def registration(us,psd,age):
    print(f"{us}'s Registration Successful")

registration("cherry","CG4576#@$",19)
registration("cherry","CG4576#@$",19)
registration("meghana","Meghana@2004",21)


import functools

def Dec(func):
    @functools.wraps(func)
    def inner(x,y):
        return func(x,y)
    return inner

@Dec
def ann(x:str,y:str) -> list:
    """Just a doc"""
    print(x+y)
    return [x,y]

print(ann.__name__)
print(ann.__doc__)
print(ann.__annotations__)

def greet():
    print("Hello!")
say_hello=greet
say_hello()

def outer():
    message='this is meghana'
    def inner():
        print(message)
    inner()
say=outer
say()

def message():
    l='hi i am here'
    def meet():
        print(l)
    return meet
say=message()
say()