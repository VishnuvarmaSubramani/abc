list=['a','A','e','E','i','I','o','O','u','U']
char=input("")
if char.isalpha():
  if char in list:
    print("vowel")
  else:
    print("consonant")
else:
  print("Invalid")
