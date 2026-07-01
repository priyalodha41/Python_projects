def square_numbers(nums):
    for i in nums:
        yield i*i;
# it allows us to produce the output one by one
my_nums=square_numbers([1,2,3,4,5,6]);

# basically next function allows it move to next part or next element in the list 
# print(next(my_nums));
# print(next(my_nums));
# print(next(my_nums));
# print(next(my_nums));
# print(next(my_nums));
# print(next(my_nums));
# print(next(my_nums)); Stopiteration

for num in my_nums:
    print(num);