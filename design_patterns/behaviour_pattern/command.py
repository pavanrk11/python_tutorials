# Command design pattern

# Used for callbacks to parameterizing UI elements with actions, queueing tasks, tracking operations history

# 1. Command: Interface or an abstract class that declares an execute method
# 2. Concrete Command: Hold a reference to a receiver object and invoke specific actions on it
# 3. Receiver: Object that actually performs the action associated with the command.
# 4. Invoker: Responsible for storing and executing commands.

# By structuring your code this way, you achieve a high degree of decoupling.
# The sender (Invoker) doesn’t need to know anything about the receiver or how the command is handled.

from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete command
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

# Concrete command
class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

# Concrete command
class AdjustVolumeCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.adjust_volume()

# Concrete command
class ChangeChannelCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.change_channel()

# Receiver interface
class RecieverDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete receiver for a TV
class TV(RecieverDevice):
    def turn_on(self):
        print("TV is now on")

    def turn_off(self):
        print("TV is now off")

    def change_channel(self):
        print("Channel changed")

# Concrete receiver for a stereo
class CarStereo(RecieverDevice):
    def turn_on(self):
        print("Stereo is now on")

    def turn_off(self):
        print("Stereo is now off")

    def adjust_volume(self):
        print("Volume adjusted")

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command is not None:
            self.command.execute()


if __name__ == "__main__":

    # Create devices
    tv = TV()
    stereo = CarStereo()

    # Create command objects
    turn_on_tv_command = TurnOnCommand(tv)
    turn_off_tv_command = TurnOffCommand(tv)
    adjust_volume_stereo_command = AdjustVolumeCommand(stereo)
    change_channel_tv_command = ChangeChannelCommand(tv)

    # Create remote control
    remote = RemoteControl()

    # Set and execute commands
    remote.set_command(turn_on_tv_command)
    remote.press_button()

    remote.set_command(adjust_volume_stereo_command)
    remote.press_button()

    remote.set_command(change_channel_tv_command)
    remote.press_button()

    remote.set_command(turn_off_tv_command)
    remote.press_button()
