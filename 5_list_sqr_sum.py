def list_sqr_sum():
    add=0
    list_in=eval(input("enter list of numbers: "))
    for i in list_in:
        add+=i**2
    return(add)

print(list_sqr_sum())