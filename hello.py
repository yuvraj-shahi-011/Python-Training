list1=[1, 2, 3, 4, 5]
list1[4]=8
even=0
odd=0
for i in list1:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even in the list:", even)
print("Number of odd in the list:", odd)
sum=0
average=0
for i in list1:
    sum += i
    average=sum / len(list1)
print("average of the list:", average)
list1.append(6)
list2=['mango', 'apple', 'banana', 'orange']
list2.insert(1, 'grapes')
list2.append('kiwi')
list2.pop(2) 

