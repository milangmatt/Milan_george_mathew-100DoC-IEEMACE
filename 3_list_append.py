list=[1,2,3]
nums=eval(input("Enter the numbers separated by commas : "))
if type(nums)==int:
    list.append(nums)
else:
    for i in nums:
        if str(i).isdigit():
            number=int(i)
            list.append(number)
        else:
            continue
print(list)
