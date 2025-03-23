# Bridge design pattern

# The Bridge Design Pattern is a structural design pattern that decouples
# an abstraction from its implementation so that both can vary independently.


# Abstraction: Defines the interface for the “abstraction” part of the system and maintains a reference to an object
# of the “implementation” hierarchy. Refined Abstraction: Extends the abstraction interface with additional methods
# or behaviors.
# Implementation: Defines the interface for the “implementation” part of the system.
# Concrete Implementation: Provides concrete implementations of the “implementation” interface.
# Client: Utilizes the abstraction to interact with the implementation.

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def channel_up(self):
        pass

    @abstractmethod
    def channel_down(self):
        pass

class TV(Device):
    def __init__(self):
        self.on = False
        self.volume = 10
        self.channel = 1

    def power_on(self):
        self.on = True
        print("TV is now ON")

    def power_off(self):
        self.on = False
        print("TV is now OFF")

    def volume_up(self):
        if self.on:
            self.volume += 1
            print(f"TV Volume is now {self.volume}")

    def volume_down(self):
        if self.on:
            self.volume -= 1
            print(f"TV Volume is now {self.volume}")

    def channel_up(self):
        if self.on:
            self.channel += 1
            print(f"TV Channel is now {self.channel}")

    def channel_down(self):
        if self.on:
            self.channel -= 1
            print(f"TV Channel is now {self.channel}")

class Radio(Device):
    def __init__(self):
        self.on = False
        self.volume = 10
        self.station = 90.1

    def power_on(self):
        self.on = True
        print("Radio is now ON")

    def power_off(self):
        self.on = False
        print("Radio is now OFF")

    def volume_up(self):
        if self.on:
            self.volume += 1
            print(f"Radio Volume is now {self.volume}")

    def volume_down(self):
        if self.on:
            self.volume -= 1
            print(f"Radio Volume is now {self.volume}")

    def channel_up(self):
        if self.on:
            self.station += 0.1
            print(f"Radio Station is now {self.station} MHz")

    def channel_down(self):
        if self.on:
            self.station -= 0.1
            print(f"Radio Station is now {self.station} MHz")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.on:
            self.device.power_off()
        else:
            self.device.power_on()

    def volume_up(self):
        self.device.volume_up()

    def volume_down(self):
        self.device.volume_down()

    def channel_up(self):
        self.device.channel_up()

    def channel_down(self):
        self.device.channel_down()

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        # Advanced feature to mute the device
        print("Muting the device")
        while self.device.volume > 0:
            self.device.volume_down()

# Create a TV and a Radio
tv = TV()
radio = Radio()

# Create a basic remote control for the TV
remote = RemoteControl(tv)

# Create an advanced remote control for the Radio
advanced_remote = AdvancedRemoteControl(radio)

# Use the remotes
remote.toggle_power()
remote.volume_up()
remote.channel_up()

advanced_remote.toggle_power()
advanced_remote.volume_down()
advanced_remote.mute()

