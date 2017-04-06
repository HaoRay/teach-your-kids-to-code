message = input("Enter a message to encode or decode: ") # get a message
key = eval(input("Enter a key value from 1-26: ")) # get a key
message = message.upper()           # make it all UPPERCASE :)
output = ""                         # create an empty string to hold output
for letter in message:              # loop through each letter of the message
    if letter.isupper():            # if the letter is in the alphabet (A-Z)
        value = ord(letter) + key   # shift the letter value up by key
        letter = chr(value)         # turn the value back into a letter
        if not letter.isupper():    # check to see if we shifted too far
            value -= 26             # if we did, wrap it back around Z->A
            letter = chr(value)     # by subtracting 26 from the letter value
    output += letter                # add the letter to our output string
print ("Output message: ", output)  # output our coded/decoded message
