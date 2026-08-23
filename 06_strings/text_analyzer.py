text = input("Enter text: ")

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Length:", len(text))
print("Words:", len(text.split()))
if text:
    print("First:", text[0])
    print("Last:", text[-1])
print("First 5 characters:", text[:5])
print("Repeated:", text * 2)

word = input("Word to search: ")
print("Found:", word in text)
