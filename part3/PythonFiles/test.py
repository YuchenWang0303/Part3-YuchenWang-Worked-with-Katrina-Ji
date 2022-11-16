import serial
data = []
with open("sequencer.txt") as file:
    for line in file:
        data += line.rsplit()
    for index in range(len(data)):
        
        print(data[index])





'''
    for line in lines:
        if line == []:
            break
        blink = line[1]
    print(blink)
'''
