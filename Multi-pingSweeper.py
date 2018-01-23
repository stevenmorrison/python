#!/usr/bin/python3

# Multi-pingSweeper.py Version 1.1.0
# Written By: Steven D. Morrison

# Multi-pingSweeper is a network application that pings a range of IP Address Returns the results with speed 
# and accuracy! this is accomplished by creating multiple Threads(1 for each IPv4 address)
# currently this application only supports /24 subnets but will be expanded in the future
# you must choose to have the output include or not include inactive results by adding a system argument.
# when calling the program. to view options:  python3 pingSweeper.py -h

# Usage: python3 pingSweeper.py <option>

import subprocess
import os
import sys
import threading
import math

no_resCount = []
resCount = []

if len(sys.argv) != 2: # Validates that the correct number of arguments were given
    print("Usage: python3 pingSweeper.py <option>")
    print("\nOptions:\n-h: Opens the pingSweeper Help page\n-i: Includes inactive hosts in the output results")
    print("-o: Omits inactive hosts from the results")
    raise SystemExit("\nThank You for using pingSweeper")

# Help Page Logic
if sys.argv[1] == str("-h"):
	print("\nWelcome to the pingSweeper Help page\n")
	print("\nOptions:\n-h: Opens the pingSweeper Help page\n-i: Includes inactive hosts in the output results")
	print("-o: Omits inactive hosts from the results")
	raise SystemExit("\nThank You for using pingSweeper")



class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):

        ping_Sweep(self.name, self.threadID)


def ping_Sweep(threadName, ID):
    with open(os.devnull, "wb") as limbo:
        try:
            #no_resCount = 0
            #resCount = 0
            addr = "192.168.1.{}".format(ID) #change this line to change network address
            #addr_input = input(str("Enter first three digits of Address to scan: "))
            #addr = addr_input + ".{}".format(ID)
            Res = subprocess.Popen(['ping', '-c', '1', '-n', '-w', '1', addr], stdout = limbo, stderr = limbo).wait()
            no_Count = 0
            respon_Count = 0
            if sys.argv[1] == str("-i"):
                if Res:
                    no_Count += 1
                    print(addr, ":No Response")
                else:
                    respon_Count += 1
                    print(addr, ":Active")
            elif sys.argv[1] == str("-o"):
                if not Res:
                    respon_Count += 1
                    print(addr, " Active")
                else:
                    no_Count += 1
            no_resCount.append(no_Count)
            resCount.append(respon_Count)
        except OSError:
            print("OS Error")
            raise sys.exit("Closing due to Error")




try:
    thread_List = []
    for thread in range(1,255):
        Thread = myThread(thread, "Ping- " + str(thread))
        thread_List.append(Thread)
        count = 0
    for item in list(thread_List):
        thread_List[count].start()
        count += 1
        if count >= 254:
            closeCount = 0
            for item in list(thread_List):
                thread_List[closeCount].join()
                closeCount += 1

            active = sum(resCount)
            inactive = sum(no_resCount)

            print("pingSweeper Completed and has discovered:\n{}: Active hosts\nand\n{}: Inactive hosts".format(active, inactive))

            raise sys.exit("Thanks for using Multi-pingSweeper\n Goodbye!")
except KeyboardInterrupt:
    closeCount = 0
    for item in list(thread_List):
        thread_List[closeCount].join()
        closeCount += 1
    raise sys.exit("You Have TERMINATED the Sweep!\nGoodBye")
