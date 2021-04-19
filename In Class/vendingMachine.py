class VendingMachine:
    def __init__(self):
        self.items = []
        self.balance = 0

        f = open("In Class/vending_machine.csv", "r")
        for line in f:
            item = line.split(",")
            self.items[item[0]] = [item[1], float(item[2]), int(item[3])]
        f.close()

    def restock(self, slot, amount):
        self.items[slot][2] += amount
        
    def insertMoney(self, amount):
        self.balance += amount

    def makeSelection(self, selection):
        if selection in self.items:
            selectedItem = self.items[selection]
            desc = selectedItem[0]
            price = selectedItem[1]
            quantity = selectedItem[2]
            print(f"You have selected item {desc} which costs {price:.2f}. There are {quantity} left.")

            if self.balance >= selectedItem[1]:
                self.balance -= selectedItem[1]
                print(f"Okay, here's your {selectedItem}")
                selectedItem[2] -= 1
            else:
                print(f"You don't have enough mnoney for that Your balance is {self.balance:.2f}")
        else:
            print(f"I'm so very sorry; there is no item in slot {selection}")

    def getChange(self):
        print(f"Okay, here's your ${self.balance:.2f}.")
        self.balance = 0


x = VendingMachine()
print(x.items)
x.insertMoney(3.52)
x.makeSelection("A2")
print(x.items)
x.restock("A3", 19)
print(x.items)
x.getChange()