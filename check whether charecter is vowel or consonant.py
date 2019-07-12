list=['a','A','e','E','i','I','o','O','u','U']
char=input("")
if char.isalpha():
  if char in list:
    print("Iowel")
  else:
    print("Consonant")
else:
  print("invalid")
