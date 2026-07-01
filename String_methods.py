# message="Hello World!!";

# print(message.lower());
# print(message.upper());
# print(message.count("l"));
# print(message.find("World"))

# message=message.replace("World","India")
# print(message);

# concentation of strings

# greeting="Hi,Dear"
# name="Suhani"

# message2=greeting+" "+ name;
# # For complex concentation of strings use format
# message2='{},{}. Welcome!! '.format(greeting,name);
# message2=f'{greeting},{name}. Welcome!!'
# print(message2);
# # To check all the functions or methods can be used on them
# print(dir(name));
# # to see all the methods
# print(help(str));
# # to know about a particular method
# print(help(str.lower));


# for n in range(1,11):
#     # for the padding of the values
#     sentence=f'The value is {n:02}'
#     print(sentence);

pi=3.14159265
# for cutting off the extra numbers which are not needed
sentence=f'The value of the pi {pi:.3f}'
print(sentence);