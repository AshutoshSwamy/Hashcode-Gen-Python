import hashlib

string = "My name is Ashutosh Swamy"

result = hashlib.md5(string.encode())
print(f"The hash code for your string is: {result.hexdigest()}")