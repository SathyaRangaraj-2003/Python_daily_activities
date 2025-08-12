#demo
# d1=Dog()
# d2=Dog()
# d1.add("sit")
# d2.add("rollover")
# print(d1.tricks)
# print(d2.tricks)


# from abc import ABC,abstractmethod
# #class
# class PaymentSystem(ABC):
#     @abstractmethod
#     def process_payment(self,amount):
#         pass

# #subclass
# class CreditCardPayment(PaymentSystem):
#     def process_payment(self, amount):
#         print(f"Credit {amount}")

# class UpiPayment(PaymentSystem):
#     def process_payment(self, amount):
#         print(f"UPI ${amount}")



# abs = PaymentSystem()
# abs.process_payment(500)

# class Tv:
#     def power_on(self):
#         print("tv is on")

# class AirConditioner:
#     def power_on(self):
#         print("airconditioner is on")

# class Speaker:
#     def power_on(self):
#         print("speaker is on")

# def remote_control(device):
#     device.power_on()



# tv = Tv()
# ac = AirConditioner()
# speaker = Speaker()

# print(id(tv),id(ac),id(speaker))

# for device in [tv,ac,speaker]:
#     remote_control(device)