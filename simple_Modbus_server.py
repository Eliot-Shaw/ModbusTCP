#!/bin/python

from pyModbusTCP.server import ModbusServer
from time import sleep
from random import uniform

# Creer instace serv
server = ModbusServer("127.0.0.1", 12345, no_block = True)

try: 
    print("Starting Server...  :|")
    server.start()
    print("Server is online  :D")
    state = [0]
    while True:
        server.data_bank.set_holding_registers(0, [int(uniform(0,100))])
        if (state != server.data_bank.get_holding_registers(0)):
            newstate = server.data_bank.get_holding_registers(0)
            print("State value of register 1 has changed from \t" + str(state) + "\t to \t" + str(newstate))
            state = newstate
            sleep(0.1)
except:
    print("")
    print("Server is stopping  :(")
    server.stop
    print("Server is shutdowned  TT")
