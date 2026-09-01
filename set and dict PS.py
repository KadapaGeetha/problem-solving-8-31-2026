#add element to a set
a = {1, 2, 3}
a.add(4)
print(a)

#remove elements from set
a={1,2,3}
a.discard(2)
print(a)

#union of two sets
a={1,2,3}
b={4,5,6}
result=a.union(b)
print(result)

#intersection of sets
a={1,2,3}
b={3,5,6}
result= a & b
print(result)

# difference of sets
a={1,2,3}
b={2,3}
result = a - b
print(result)

#check subset
a={1,2}
b={1,2,3}
print(a.issubset(b))

#length of set
a={1,2,3}
#print(len(a))
a.clear()
print(a)

#symmetric difference
a={1,2,3}
b={2,3,4}
#result= a ^ b
#using method
result = a.symmetric_difference(b)
print(result)

#convert list to set
a={1,2,2,3}
r=set(a)
print(r)

#create a dict from two list
a=['a','b']
b=[1,2]
r=dict(zip(a,b))
print(r)

#update dictionary value
a={'a':1}
a['a']=2 # dict[key]=value
print(a)

#remove key from dictionary 
a={'a':1,'b':2,'c':3}
a.pop('b')
print(a)

#Check Key Existence
d = {"x": 1}
print("x" in d)


#Iterate Over Dictionary
#Use .items() to get both key and value.

d = {"a": 10, "b": 20}

for key, value in d.items():
    print(key, value)

#Dictionary Length
d = {"x": 1, "y": 2}

print(len(d))

#Merge Two Dictionaries
#Using update():

d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
print(d1)

#Get Value with Default
d = {"a": 1}
print(d.get("b", 0))

#Count Frequency of Elements
numbers = [1, 2, 2, 3]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


#Invert a Dictionary
#Keys become values and values become keys.

d = {"a": 1, "b": 2}

result = {}

for key, value in d.items():
    result[value] = key

print(result)

#Find Key with Maximum Value
d = {"a": 10, "b": 20, "c": 15}

result = max(d, key=d.get)

print(result)


#Sort Dictionary by Values
d = {"a": 3, "b": 1, "c": 2}

result = sorted(d.items(), key=lambda x: x[1])

print(result)


#Create Dictionary of Squares
result = {}

for i in range(1, 4):
    result[i] = i ** 2

print(result)

#Filter Dictionary by Value Condition
#Keep values greater than 10.

d = {"a": 10, "b": 5, "c": 15}

result = {}

for key, value in d.items():
    if value > 10:
        result[key] = value

print(result)

#Combine Values of Duplicate Keys
d1 = {"a": 1, "b": 2}
d2 = {"a": 3, "c": 4}

result = d1.copy()

for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)

#Count Word Frequency in Sentence
sentence = "apple banana apple"

words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)


#Remove Duplicate Values from Dictionary
#Keep the first key when values are duplicated.

d = {"a": 1, "b": 2, "c": 1}

result = {}

for key, value in d.items():
    if value not in result.values():
        result[key] = value

print(result)

#Find Common Keys in Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = []

for key in d1:
    if key in d2:
        result.append(key)

print(result)
