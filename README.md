# Part3 YuchenWang Worked with Katrina Ji



## GIF of Read Data from BOOT PIN and Record

![InputData](https://user-images.githubusercontent.com/105755054/202268733-38efb52a-c3af-4d6f-ab77-3d794cb96c40.GIF)

The Python code will read the output from tty termial and record the status of BOOT PIN with sequencer.txt file on your computer.

---

## GIF of Re-displaing the Data via WS2812 LED

![OutputData](https://user-images.githubusercontent.com/105755054/202269079-c60ff665-0ff7-453c-b378-5822bd2fcb5f.GIF)

---

## The Recorded Data in txt file is looking like:

<img width="794" alt="Screen Shot 2022-11-16 at 13 59 31" src="https://user-images.githubusercontent.com/105755054/202269338-4ad18a11-5259-47e8-9877-c0a61c3036d4.png">

---
## Switch Mode

It is easier to switch mode with python code. 

- r (lowercase) -> read from BOOT PIN and recored the raw data to sequencer.txt file

- w (lowercase) -> write the data stored in sequencer.txt to QTPY-2040 


## Explain

In this part, the python code will communicate with QTPY 2040 via tty terminal. First, in read mode, the Python code will sent a 'r' to qtpy 2040 indicates starting to read the BOOT PIN status(1 or 0) for specific duration, such as 5 sec,and stored the data into a txt file. Then reboot the python code, microcontroller and input 'w', the python also write a 'w' to 2040 and it will return "OK" to python, then allow the python to write the data into WS2812.
