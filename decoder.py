def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

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
  
s = start
     
estart = (reverse(s))

bob = len(estart)
jeff = len(emiddle)
tom = len(eend)

print (estart)
print (emiddle)
print (eend)

pstart = estart [0:2]
sstart = estart [0:3]
bstart = estart [3:4]

pmiddle = emiddle [0:2]
smiddle = emiddle [0:3]
bmiddle = emiddle [3:4]

pend = eend [0:2]
send = eend [0:3]
bend = eend [3:4]

if sstart == ("yaw"):
    newword = estart [3:bob]
else:
    if pstart == ("ya"):
        newword = estart [3:bob] + bstar

if smiddle == ("yaw"):
    twonewword = emiddle [3:jeff]
else:
    if pmiddle == ("ya"):
        twonewword = emiddle [3:bob] + bmiddle

if send == ("yaw"):
    thirdnewword = eend [3:bob]
else:
    if pend == ("ya"):
        thirdnewword = eend [3:bob] + bend

first = len(newword)
second = len(twonewword)
third = len(thirdnewword)

newsentence = newword [first:0] + twonewword [secnd:0] + thirdnewword [third:0]
newsentence = newsentence.lower()

print (newsentence)
