nums =[1,2,3,4,5,6,7,8,9,10]

# (start:end:step)
print(nums[-1::-2])



# normal way
# new_list=[];
# for n in nums:
#     new_list.append(n);


# comprehensive way

# new_list=[n*n for n in nums]

# new_list=[n for n in nums if n%2==0 ]

# new_list=[(letter,num) for letter in 'abcd' for num in range(5)]

# print(new_list);

names=["Brue","Clark","Peter"]
heros=["Batman","Superman","Spiderman"]

new_dict={name:hero for name, hero in zip (names,heros)}
print(new_dict);

