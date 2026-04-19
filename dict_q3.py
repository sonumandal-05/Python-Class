s1 = {"a": 10, "b": 20}
s2 = {"b": 5, "c": 15}

merge = s1.copy()
for key, value in s2.items():
    merge[key] = merge.get(key, 0) + value

print(merge)