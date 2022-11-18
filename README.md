# Part3 YuchenWang Worked with KatrinaJi

University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 2b

### Teammate: Yuchen Wang, Katrina Ji

    Yuchen Wang
    wangyuchen0303@gmail.com
    Tested on:  MacBook Pro (14-inch, 2021), macOS Monterey 12.6

## GIF of Read Data from BOOT PIN and Record

![InputData](https://user-images.githubusercontent.com/105755054/202268733-38efb52a-c3af-4d6f-ab77-3d794cb96c40.GIF)

The Python code will read the output from tty termial and record the status of BOOT PIN with sequencer.txt file on your computer.

---

## GIF of Re-displaing the Data via WS2812 LED

![OutputData](https://user-images.githubusercontent.com/105755054/202269079-c60ff665-0ff7-453c-b378-5822bd2fcb5f.GIF)

---

## Python Code Explanation

- Before using python we have to install serialpy library with ``` pip3 install serialpy```

### In python code we were designed two functions that help to read from terminal and write to qtpy 2040:

- ```read_tty()```

```
def read_tty():
    print("Start to record the data from boot pin")

    # set read mode
    ser.write(bytearray("r", "ascii"))
    # create an array to store the data
    data_array = []
    start_time = time.time()
    # duration = int(input("record duration"))

    while True:
        # read the secquencer from terminal
        secquencer = ser.readline()
        # print(str(secquencer))

        # if I print 1 the format is b'1\r\n'
        # hence choose from 2 to -5 is our target data, but not include the 2 position
        # note that array is starting from 0
        secquencer = str(secquencer)[2:-5]

        # split the inner data by comma ","
        # row_data = secquencer.split(',')

        # combina the data to the new array
        print(secquencer)
        # print(data_array)

        # read for 10s
        if time.time() - start_time >= 10:
            print("Transmit the data into file")
            ser.write(bytearray("s", "ascii"))
            with open("sequencer.txt", "w") as file:
                for line in data_array:
                    file.write(f"{line}\n")
            ser.close()
            break
        else:
            data_array.append(secquencer)

```

- ```write_tty()```

```
def write_tty():
    data_write = []
    index = 0
    print("Start to display")
    ser.write(bytearray("w", "ascii"))
    # checking the connecting status
    while True:
        status = ser.readline()
        # print(str(status[1:-5]))
        if status == b"OK\r\n":
            print("Start to write back data")
            break

    with open("sequencer.txt", "r") as file:
        for line in file:
            data_write += line.rstrip()
        for index in range(len(data_write)):
            if data_write[index] == "0":
                ser.write(bytearray("0", "ascii"))
            elif data_write[index] == "1":
                ser.write(bytearray("1", "ascii"))
            time.sleep(0.05)
    ser.close()


```

---

## The Recorded Data in txt file is looking like(secquencer.txt):

<img width="794" alt="Screen Shot 2022-11-16 at 13 59 31" src="https://user-images.githubusercontent.com/105755054/202269338-4ad18a11-5259-47e8-9877-c0a61c3036d4.png">

---
## Switch Mode

It is easier to switch mode with python code. 

- r (lowercase) -> read from BOOT PIN and recored the raw data to sequencer.txt file

- w (lowercase) -> write the data stored in sequencer.txt to QTPY-2040 


## Explain

In this part, the python code will communicate with QTPY 2040 via tty terminal. First, in read mode, the Python code will sent a 'r' to qtpy 2040 indicates starting to read the BOOT PIN status(1 or 0) for specific duration, such as 5 sec,and stored the data into a txt file. Then reboot the python code, microcontroller and input 'w', the python also write a 'w' to 2040 and it will return "OK" to python, then allow the python to write the data into WS2812.
