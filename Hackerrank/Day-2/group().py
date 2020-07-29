# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import search
string=input()
match=search(r'([a-zA-Z0-9])\1+',string)
print(match.group(1) if match else -1)


