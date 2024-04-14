#!/bin/python

from pyModbusTCP.client import ModbusClient

from time import sleep
from random import uniform

client = ModbusClient(host="127.0.0.1", port=12345)
client.open()

while True:
    value_read = client.read_holding_registers(0)
    print("Je vois \t" + str(value_read))
    
    # client.write_single_register(1,client.read_holding_registers(0))
    sleep(0.1)