# 1
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(shape):
#     def area(self):
#         r=int(input("r:"))
#         print((22/7)*r*r)
#     def perimeter(self):
#         r=int(input("r:"))
#         print(2*(22/7)*r)
# class Rectangle(shape):
#     def area(self):
#         l,b=int(input("l:")),int(input("b:"))
#         print(l*b)
#     def perimeter(self):
#         l,b= int(input("l:")), int(input("b:"))
#         print(2*(l+b))
# class Triangle(shape):
#     def area(self):
#         b,h = int(input("b:")), int(input("h:"))
#         print((1/2)*b*h)
#     def perimeter(self):
#         b,h = int(input("b:")), int(input("h:"))
#         print(b*h)
# c1=Circle()
# c1.area()
# c1.perimeter()
# r1=Rectangle()
# r1.area()
# r1.perimeter()
# t=Triangle()
# t.area()
# t.perimeter()


# 2
# from abc import ABC,abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,amount):
#         pass
# class UPIPayment(PaymentGateway):
#     def authenticate(self):
#         print("authentication successfull")
#     def pay(self,amount):
#         print(f"{amount} is paid")
#     def refund(self,amount):
#         print(f"{amount} is refund")
# class CardPayment(PaymentGateway):
#     def authenticate(self):
#         print("authentication successful")
#     def pay(self,amount):
#         print(f"{amount} is paid")
#     def refund(self,amount):
#         print(f"{amount} is refund")
# class NetBankingPayment(PaymentGateway):
#     def authenticate(self):
#         print("authentication successful")
#     def pay(self, amount):
#         print(f"{amount} is paid")
#     def refund(self, amount):
#         print(f"{amount} is refund")
# l=[UPIPayment(),CardPayment(),NetBankingPayment()]
# for i in l:
#     i.authenticate()
#     i.pay(800)
#     i.refund(600)


# 3
# from abc import ABC,abstractmethod
# class VehicleControl(ABC):
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# class CarControl(VehicleControl):
#     def accelerate(self):
#         print("accelerating the car")
#     def brake(self):
#         print("brake the car")
#     def steer(self):
#         print("steer the car")
# class BikeControl(VehicleControl):
#     def accelerate(self):
#         print("accelerating the bike")
#     def brake(self):
#         print("brake the bike")
#     def steer(self):
#         print("steer the bike")
# class TruckControl(VehicleControl):
#     def accelerate(self):
#         print("accelerate the truck")
#     def brake(self):
#         print("brake the truck")
#     def steer(self):
#         print("steer the truck")
# l=[CarControl(),BikeControl(),TruckControl()]
# for i in l:
#     i.accelerate()
#     i.brake()
#     i.steer()


# 4
# from abc import ABC,abstractmethod
# class DatabaseDriver(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def execute(self,query):
#         pass
#     @abstractmethod
#     def close(self):
#         pass
# class MySQLDriver(DatabaseDriver):
#     def connect(self):
#         print("connect to mysql")
#     def execute(self,query):
#         print(f"{query} to mysql")
#     def close(self):
#         print("close the mysql")
# class PostgresDriver(DatabaseDriver):
#     def connect(self):
#         print("connect to post")
#     def execute(self,query):
#         print(f"{query} to post")
#     def close(self):
#         print("close the post")
# class SQLiteDriver(DatabaseDriver):
#     def connect(self):
#         print("connect to sqlite")
#     def execute(self,query):
#         print(f"{query} to sqlite")
#     def close(self):
#         print("close the sqlite")
# # l=[MySQLDriver(),PostgresDriver(),SQLiteDriver()]
# # for i in l:
# #     i.connect()
# #     i.execute("hii")
# #     i.close()
# def main(db):
#     db.connect()
#     db.execute("hi")
#     db.close()
# main(MySQLDriver())
# main(PostgresDriver())
# main(SQLiteDriver())


# 5
# from abc import ABC,abstractmethod
# class ReportGenerator(ABC):
#     @abstractmethod
#     def load_data(self):
#         pass
#     @abstractmethod
#     def process(self):
#         pass
#     @abstractmethod
#     def export(self):
#         pass
# class PDFReport(ReportGenerator):
#     def load_data(self):
#         print("pdf data")
#     def process(self):
#         print("pdf process")
#     def export(self):
#         print("export pdf")
# class ExcelReport(ReportGenerator):
#     def load_data(self):
#         print("excel data")
#     def process(self):
#         print("excel process")
#     def export(self):
#         print("export excel")
#
# l=[PDFReport(),ExcelReport()]
# for i in l:
#     i.load_data()
#     i.process()
#     i.export()


# 6
# from abc import ABC,abstractmethod
# class RobotCommand(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#     @abstractmethod
#     def undo(self):
#         pass
# class PickCommand(RobotCommand):
#     def execute(self):
#         print("execute pick command")
#     def undo(self):
#         print("undo pick command")
# class PlaceCommand(RobotCommand):
#     def execute(self):
#         print("execute place command")
#     def undo(self):
#         print("undo place command")
# class MoveCommand(RobotCommand):
#     def execute(self):
#         print("execute move command")
#     def undo(self):
#         print("undo move command")
# l=[PickCommand(),PlaceCommand(),MoveCommand()]
# for i in l:
#     i.execute()
#     i.undo()


# 7
# from abc import ABC,abstractmethod
# class MLModel(ABC):
#     @abstractmethod
#     def train(self,data):
#         pass
#     @abstractmethod
#     def predict(self,x):
#         pass
#     @abstractmethod
#     def evaluate(self,test_set):
#         pass
# class LinearRegressionModel(MLModel):
#     def train(self,data):
#         print(f"training linear regression with{data}")
#     def predict(self,x):
#         print(f"linear regression predicts {x}")
#     def evaluate(self,test_set):
#         print(f"evaluating linear regression with {test_set}")
# class DecisionTreeModel(MLModel):
#     def train(self,data):
#         print(f"training linear regression with{data}")
#     def predict(self,x):
#         print(f"linear regression predicts {x}")
#     def evaluate(self,test_set):
#         print(f"evaluating linear regression with {test_set}")
# l=[LinearRegressionModel(),DecisionTreeModel()]
# for i in l:
#     i.train("data")
#     i.predict(10)
#     i.evaluate("test data")


# 8
# def EmailSender(message):
#     print("email",message)
# def SmsSender(message):
#     print("sms",message)
# def pushSender(message):
#     print("push",message)
# def notification(type,message):
#     if type=="email":
#         EmailSender(message)
#     elif type=="sms":
#         SmsSender(message)
#     elif type=="push":
#         pushSender(message)
#     else:
#         print("invalid notification")
# notification("email","hii")
# notification("sms","hello")
# notification("push","hm")


# from abc import ABC,abstractmethod
# class Notifier(ABC):
#     @abstractmethod
#     def send(self,message):
#         pass
# class Email(Notifier):
#     def send(self,message):
#         print("email:",message)
# class Sms(Notifier):
#     def send(self,message):
#         print("sms:",message)
# class push(Notifier):
#     def send(self,message):
#         print("push:",message)
# l=[Email(),Sms(),push()]
# for i in l:
#     i.send("hii")

# 9
# from abc import ABC,abstractmethod
# class MediaPlayer(ABC):
#     @abstractmethod
#     def load(self):
#         pass
#     @abstractmethod
#     def play(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class MP3Player(MediaPlayer):
#     def load(self):
#         print("loading mp3player")
#     def play(self):
#         print("playing mp3player")
#     def stop(self):
#         print("stop mp3player")
# class WAVPlayer(MediaPlayer):
#     def load(self):
#         print("loading wavplayer")
#     def play(self):
#         print("playing wavplayer")
#     def stop(self):
#         print("stop wavplayer")
# class AACPlayer(MediaPlayer):
#     def load(self):
#         print("loading aacplayer")
#     def play(self):
#         print("playing aacplayer")
#     def stop(self):
#         print("stop aacplayer")
# l=[MP3Player(),WAVPlayer(),AACPlayer()]
# for i in l:
#     i.load()
#     i.play()
#     i.stop()


# 10
from abc import ABC,abstractmethod
class Sensor(ABC):
    def __init__(self,raw,factor):
        self._raw=raw
        self.__factor=factor
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
    def get_reading(self):
        self.read_value()
        self.calibrate()
        return self._raw*self.__factor
class TemperatureSensor(Sensor):
    def read_value(self):
        print("read the temperature sensor")
    def calibrate(self):
        print("calibrate the temperature sensor")
class PressureSensor(Sensor):
    def read_value(self):
        print("read the pressure sensor")
    def calibrate(self):
        print("calibrate the temperature sensor")
class HumiditySensor(Sensor):
    def read_value(self):
        print("read the humidity sensor")
    def calibrate(self):
        print("calibrate the temperature sensor")
t=TemperatureSensor(100,0.2)
p=PressureSensor(200,0.4)
h=HumiditySensor(300,0.6)
print(t.get_reading())
print(p.get_reading())
print(h.get_reading())