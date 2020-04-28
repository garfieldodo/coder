def reverse(c): 
  str = "" 
  for i in e: 
    str = i + str
  return str
def reverse(b): 
  str = "" 
  for i in e: 
    str = i + str
  return str
def reverse(a): 
  str = "" 
  for i in e: 
    str = i + str
  return str
def reverse(m): 
  str = "" 
  for i in m: 
    str = i + str
  return str

def reverse(e): 
  str = "" 
  for i in e: 
    str = i + str
  return str

def reverse(t): 
  str = "" 
  for i in t: 
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
  
m = start
e = middle
t = end
     
estart = (reverse(m))
emiddle = (reverse(e))
eend = (reverse(t))

bob = len(estart)
jeff = len(emiddle)
tom = len(eend)


pstart = estart [0:2]
sstart = estart [0:3]
bstart = estart [2:3]

pmiddle = emiddle [0:2]
smiddle = emiddle [0:3]
bmiddle = emiddle [2:3]

pend = eend [0:2]
send = eend [0:3]
bend = eend [2:3]

if sstart == ("yaw"):
    newword = estart [3:bob]
else:
    if pstart == ("ya"):
        newword = estart [3:bob] + bstart

if smiddle == ("yaw"):
    twonewword = emiddle [3:jeff]
else:
    if pmiddle == ("ya"):
        twonewword = emiddle [3:jeff] + bmiddle

if send == ("yaw"):
    thirdnewword = eend [3:tom]
else:
    if pend == ("ya"):
        thirdnewword = eend [3:tom] + bend

a = newword
b = twonewword
c = thirdnewword

a = (reverse(a))
b = (reverse(b))
c = (reverse(c))

newsentence = a + " " + b + " " + c
newsentence = newsentence.lower()
