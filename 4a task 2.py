d = {"name": "Aarav", "age": 20, "course": "CS"}

print(list(d.keys()), list(d.values()), list(d.items()))
print(d.get("city", "N/A"))

d.update({"age": 21, "city": "Hyderabad"})
d.pop("course", None)

print(d)