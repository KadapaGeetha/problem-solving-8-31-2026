# Set and Dictionary Interview Questions – 1 to 30

## Set-Based Questions

### 1. Add Element to a Set

```python
a = {1, 2, 3}
a.add(4)
print(a)
```

### 2. Remove Element from Set

```python
a = {1, 2, 3}
a.remove(2)
print(a)
```

### 3. Union of Two Sets

```python
a = {1, 2}
b = {2, 3}
c = a.union(b)
print(c)
```

### 4. Intersection of Sets

```python
a = {1, 2}
b = {2, 3}
print(a & b)
```

### 5. Difference of Sets

```python
a = {1, 2, 3}
b = {2, 3}
print(a - b)
```

### 6. Check Subset

```python
a = {1, 2}
b = {1, 2, 3}
c = a.issubset(b)
print(c)
```

### 7. Set Length

```python
a = {1, 2, 3}
b = len(a)
print(b)
```

### 8. Clear a Set

```python
a = {1, 2, 3}
a.clear()
print(a)
```

### 9. Symmetric Difference

```python
a = {1, 2, 3}
b = {2, 3, 4}
r = a.symmetric_difference(b)
print(r)
```

### 10. Convert List to Set

```python
a = [1, 2, 2, 3]
r = set(a)
print(r)
```

---

# Dictionary-Based Questions

### 11. Create a Dictionary from Two Lists

```python
a = ["a", "b"]
b = [1, 2]
r = dict(zip(a, b))
print(r)
```

### 12. Update Dictionary Value

```python
a = {"a": 1}
a["a"] = 2
print(a)
```

### 13. Remove Key from Dictionary

```python
a = {"a": 1, "b": 2}
a.pop("b")
print(a)
```

### 14. Check Key Existence

```python
a = {"x": 1}
b = "x"
print(b in a)
```

### 15. Iterate Over Dictionary

```python
a = {"a": 10, "b": 20}

for key, value in a.items():
    print(key, value)
```

### 16. Dictionary Length

```python
a = {"x": 1, "y": 2}
r = len(a)
print(r)
```

### 17. Merge Two Dictionaries

```python
a = {"a": 1}
b = {"b": 2}

a.update(b)
print(a)
```

### 18. Get Value with Default

```python
a = {"a": 1}
r = a.get("b", 0)
print(r)
```

### 19. Count Frequency of Elements

```python
numbers = [1, 2, 2, 3]
freq = {}

for num in set(numbers):
    freq[num] = numbers.count(num)

print(freq)
```

### 20. Invert a Dictionary

```python
a = {"a": 1, "b": 2}
invert = {}

for key, value in a.items():
    invert[value] = key

print(invert)
```

### 21. Find Key with Maximum Value

```python
a = {"a": 10, "b": 20, "c": 15}

max_value = 0
max_key = ""

for key, value in a.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)
```

### 22. Sort Dictionary by Values

```python
a = {"a": 3, "b": 1, "c": 2}

result = sorted(a.items(), key=lambda x: x[1])
print(result)
```

### 23. Create Dictionary of Squares

```python
a = range(1, 4)
square = {}

for num in a:
    square[num] = num * num

print(square)
```

### 24. Filter Dictionary by Value Condition

```python
a = {"a": 10, "b": 5, "c": 15}
result = {}

for key, value in a.items():
    if value > 10:
        result[key] = value

print(result)
```

### 25. Combine Values of Duplicate Keys

```python
a = {"a": 1, "b": 2}
b = {"a": 3, "c": 4}

result = {}

for key, value in a.items():
    result[key] = value

for key, value in b.items():
    if key in result:
        result[key] = result[key] + value
    else:
        result[key] = value

print(result)
```

### 26. Count Word Frequency in Sentence

```python
text = "apple banana apple"
words = text.split()
count = {}

for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print(count)
```

### 27. Remove Duplicate Values from Dictionary

```python
a = {"a": 1, "b": 2, "c": 1}
result = {}

for key in a:
    if a[key] not in result.values():
        result[key] = a[key]

print(result)
```

### 28. Find Common Keys in Two Dictionaries

```python
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
result = []

for key in a:
    if key in b:
        result.append(key)

print(result)
```

### 29. Swap Keys and Values Safely

```python
a = {"x": 1, "y": 2}
result = {}

for key, value in a.items():
    result[value] = key

print(result)
```

### 30. Delete Items by Value

```python
a = {"a": 1, "b": 2, "c": 1}
result = {}

for key, value in a.items():
    if value != 1:
        result[key] = value

print(result)
```

