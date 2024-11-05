# add your code here
#Right shift of five (A will be F)
#Please enter a sentence: python is fun!
#The encrypted sentence is: udymts nx kzs!
shift = {
    "a" : "f",
    "b " : "g",
    "c" : "h",
    "d" : "i",
    "e" : "j",
    "f" : "k",
    "g" : "l",
    "h" : "m",
    "i" : "n",
    "j" : "o",
    "k" : "p", 
    "l" : "q", 
    "m" : "r", 
    "n" : "s", 
    "o" : "t", 
    "p" : "u", 
    "q" : "v", 
    "r" : "w",
    "s" : "x", 
    "t" : "y",
    "u" : "z",
    "v" : "a",
    "w" : "b",
    "x" : "c",
    "y" : "d",
    "z" : "e", 
    }

text = input("Please enter a sentence")
text = text.lower()
cipher_text = ""
for char in text:
    if char in shift:
        char = shift[char]
    cipher_text += char
print(cipher_text)



