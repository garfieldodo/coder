#this prepares to turn the words from arrays into strings
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
message = (input("enter your message (3 words max): "))

#this splits the sentence into individual words
s = message.split(" ")

start = s [0:1]
middle = s [1:2]
end = s [2:3]

#this turns the words from arrays to strings
start = listToString(start)
middle = listToString(middle)
end = listToString(end)

fword = len(start)
sword = len(middle)
tword = len(end)

#this seperates each word into 2 parts: the first letter and the restsstart = start [0:1]
estart = start [1:fword]

emiddle = middle [1:sword]

eend = end [1:tword]
