def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
message = (input("enter your message (3 words max): "))

s = message.split(" ")

start = s [0:1]
middle = s [1:2]
end = s [2:3]

start = listToString(start)
middle = listToString(middle)
end = listToString(end)

fword = len(start)
sword = len(middle)
tword = len(end)

sstart = start [0:1]
estart = start [1:fword]

smiddle = middle [0:1]
emiddle = middle [1:sword]

send = end [0:1]
eend = end [1:tword]

if sstart == "a":
    first = estart + "way"
elif sstart == "e":
    first = estart + "way"
elif sstart == "i":
    first = estart + "way"
elif sstart == "o":
    first = estart + "way"
elif sstart == "u":
    first = estart + "way"
else:
    first = estart + sstart + ("ay")

if smiddle == "a":
    second = emiddle + ("way")
elif smiddle == "e":
    second = emiddle + ("way")
elif smiddle == "i":
    second = emiddle + ("way")
elif smiddle == "o":
    second = emiddle + ("way")
elif smiddle == "u":
    second = emiddle + ("way")
else:
    second = emiddle + smiddle + ("ay")

if send == "a":
    third = eend + ("way")
elif send == "e":
    third = eend + ("way")
elif send == "i":
    third = eend + ("way")
elif send == "o":
    third = eend + ("way")
elif send == "u":
    third = eend + ("way")
else:
    third = eend + send + ("ay")

newsentence = first + (" ") + second + (" ") + third
newsentence = newsentence.lower()

print (newsentence)