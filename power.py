12. A POWER M
SOURCE CODE:

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("enter base: "))
exp=int(input("enter exponential value: "))
print("Result:",power(base,exp))