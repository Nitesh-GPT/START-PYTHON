'''check whether N or p belong to sentence or not
Sentence = "Hello my is Nitesh and i'm looking for an professional job in IT"
for i in Sentence:
   if i == "N" or i == "x":
    print("yes they are")
'''
Sentence = "Hello my is Nitesh and i'm looking for an professional job in IT"
for char in Sentence:
    if char in "N":
      print("hello  yes they are!")
      
    else:
        print("No match found")
        