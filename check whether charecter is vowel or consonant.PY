list=['a','A','e','E','i','I','o','O','u','U']
char=input("Enter a charecter:")
if char.isalpha():
  if char in list:
    print("charecter is vowel")
  else:
    print("charecter is consonant")
else:
  print("Invalid input")
