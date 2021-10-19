def char_count(message):  
    message_length = len(message)
    if message_length > 160:
        print("This message is too long; this is what we allow: ")
        print("")
        print (message[0:160])
    else:
        print(message, "The length of the message is:", len(message))

my_message = input("enter a message here to test it's length: ")
char_count(my_message)