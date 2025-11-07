from random import randint
class Train:
    def __init__(self,trainNo):#constructor
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked at train no: {self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time.")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}.")   
a = Train(11)
a.book("Delhi","Mumbai")
a.getStatus()
a.getFare("Delhi","Mumbai")

