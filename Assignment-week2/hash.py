import hashlib
userInput=str(input())
salt=bytes("Km5d5ivMy8iexuHcZrsD","ascii")
itterations=200000
convertedInput = bytes(userInput,"ascii")
output = hashlib.pbkdf2_hmac('sha512', convertedInput, salt , itterations)
print(output.hex())
