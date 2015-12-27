#!/usr/bin/env python

#
# Example using Dynamic Payloads
# 
#  This is an example of how to use payloads of a varying (dynamic) size.
# 

import time
from RF24 import *

radio = RF24(RPI_V2_GPIO_P1_15, RPI_BPLUS_GPIO_J8_24, BCM2835_SPI_SPEED_8MHZ)	

pipes = [0xF0F0F0F0F1, 0xF0F0F0F0E2, 0xF0F0F0F0D3, 0xF0F0F0F0C4, 0xF0F0F0F0B5, 0xF0F0F0F0A6]
millis = lambda: int(round(time.time() * 1000))

print 'Starting VrTracker...'

radio.begin()
radio.setAutoAck(True)
radio.enableAckPayload()             # Allow optional ack payloads
radio.enableDynamicPayloads()        # Ack payloads are dynamic payloads
radio.setPALevel(RF24_PA_MAX)
radio.setDataRate(RF24_1MBPS)
radio.setCRCLength(RF24_CRC_8)       # Use 8-bit CRC for performance

radio.setRetries(5,15)
radio.printDetails()

print ' ************ Role Setup *********** '

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1]);
radio.openReadingPipe(2, pipes[2]);
radio.openReadingPipe(3, pipes[3]);
radio.openReadingPipe(4, pipes[4]);
radio.openReadingPipe(5, pipes[5]);
radio.startListening();

# forever loop
while 1:

    # if there is data ready
    pipe =[0,1,2]
    pipeNumber = radio.available()
    if pipeNumber:
    #    while radio.available():
         # len = radio.getDynamicPayloadSize()
            receive_payload = radio.read(3)
            # Spew it
            # print 'length = ', len
            print 'pipe number = ', pipe
            print 'Got payload, value= ', receive_payload[0], ' - ',  receive_payload[1], ' - ',  receive_payload[2]
 
            # Calculate 3D position here