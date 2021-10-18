#I imported the required modules
import random
import time

#I set seed to random,the character library and some other values
random.seed(time.time())
chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","~","!","@","#","$","%","^","&","*","(",")","-","+","_","=","[","]","{","}",";",":","'","|",",","<",".",">","/","?"]
z = ""
#I asked how many character string to have?
i = int(input("How many characters your new string do you want to have? "))

#I generated the string
for x in range(0,i):
    y = random.choice(chars)
    z = z + y

#I printed the string to the screen
print("Your new random generated string is "+z)
