from random import randint
class Train:
    def __init__(slf,trainNo):#constructor
        slf.trainNo = trainNo

    def book(slf,fro,to):
        print(f"Ticket is booked at train no: {slf.trainNo} from {fro} to {to}")
        
    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time.")

    def getFare(slf,fro,to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222,5555)}.")   
a = Train(11)
a.book("Delhi","Mumbai")
a.getStatus()
a.getFare("Delhi","Mumbai")

