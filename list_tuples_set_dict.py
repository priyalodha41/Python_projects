subject=["History","Geogrpahy","Chemistry"];

subject2=["Hindi","Gujarati"];

# if u want to insert multiple values inside the list then use extend
subject.extend(subject2);

# if u want to add a single insert then use append
# subject.append("African")

# if u don't want to change the orginal list so don't use sort() instead use sorted()-function
sorted_courses=sorted(subject);
print(subject)
print(sorted_courses)

# to find the index of any value
print(subject.index("Chemistry"))

# to check that value is in list or not and get false or true value then

print("Art" in subject);
print("Chemistry" in subject);

# enumerate is used to get the index as well the value 
for index,course in enumerate(subject):
    print(index,course);

for index,course in enumerate(subject,start=1):
    print(index,course);

subject_str=" ".join(subject);

print(subject_str)

subject4={"History","Geogrpahy","Chemistry","Hindi"};
subject3={"History","Geogrpahy","African"};
# for the same elements present in both the sets
print(subject3.intersection(subject4)); 
# to join the sets and remove the duplicates from the two list and only keep the unique values
print(subject3.union(subject4))
# to check the different elements
print(subject3.difference(subject4));
print(subject4.difference(subject3));


Student={
    "Name":"Priya Lodha",
    "Age":21,
    "Location":"Surat,Gujarat"
}

for key,value in Student.items():
    print(key,value);

# print(Student.get("Location"))
Student["phone"]="+91 9016598461"
print(Student.get("phone","Not found"))
# to delete the age (2 ways to remove or delete the key and value)
# del Student['Age'];
# Student.pop("Age")

print(Student)