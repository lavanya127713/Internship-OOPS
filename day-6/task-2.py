from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started using key")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started using kick or self-start")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started using ignition switch")

car = Car()
bike = Bike()
bus = Bus()

car.start_engine()
bike.start_engine()
bus.start_engine()
