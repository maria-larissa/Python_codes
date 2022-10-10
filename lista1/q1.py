list=(12,2,4,8,29,45,78,36,-17,2,12,8,3,3,-52)
for i in range(0, len(list)-1):
    if i==0:
        max_value=list[i]
        min_value=list[i]
        
    else:
        if list[i]>max_value:
            max_value=list[i]
        if list[i]<min_value:
            min_value=list[i]

print("a) O maior elemento da lista é {}.".format(max_value))
print("b) O menor elemento da lista é {}.".format(min_value))
print("c) O maior elemento da lista é {}.".format(max_value))