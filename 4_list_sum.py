def list_sum():
    add=0
    list_in=eval(input("enter list of numbers: "))
    for i in list_in:
        add+=i
    return(add)

print(list_sum())