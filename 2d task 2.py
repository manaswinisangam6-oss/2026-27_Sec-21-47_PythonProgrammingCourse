# Demonstrate string methods

text = "  Hello Python World  "

print("Original string:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Strip:", text.strip())
print("Split:", text.split())

words = ["Hello", "Python", "World"]
print("Join:", " ".join(words))

print("Replace:", text.replace("Python", "Java"))
print("Find:", text.find("Python"))