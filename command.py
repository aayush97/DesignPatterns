from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def __init__(self, location):
        self.location = location
    
    def on(self):
        print(self.location, "light is on")

    def off(self):
        print(self.location, "light is off")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()
    
class Stereo:
    def __init__(self, location):
        self.location = location
    
    def on(self):
        print(self.location, "stereo is on")
    
    def off(self):
        print(self.location, "stereo is off")
    
    def set_cd(self):
        print(self.location, "stereo is set for CD input")
    
    def set_dvd(self):
        print(self.location, "stereo is set for DVD input")
    
    def set_radio(self):
        print(self.location, "stereo is set for Radio")
    
    def set_volume(self, volume):
        print(self.location, "stereo volume set to", volume)

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)
    
    def undo(self):
        self.stereo.off()

class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()
    
    def undo(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self.location = location
        self.speed = CeilingFan.OFF
    
    def high(self):
        self.speed = CeilingFan.HIGH
        print(self.location, "ceiling fan is on high")
    
    def medium(self):
        self.speed = CeilingFan.MEDIUM
        print(self.location, "ceiling fan is on medium")
    
    def low(self):
        self.speed = CeilingFan.LOW
        print(self.location, "ceiling fan is on low")
    
    def off(self):
        self.speed = CeilingFan.OFF
        print(self.location, "ceiling fan is off")
    
    def get_speed(self):
        return self.speed

class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None
    
    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()
    
    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()

class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None
    
    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()
    
    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()

class CeilingFanLowCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None
    
    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.low()
    
    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()

class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None
    
    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()
    
    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()

class GarageDoor:
    def __init__(self, location):
        self.location = location
    
    def up(self):
        print(self.location, "garage door is open")
    
    def down(self):
        print(self.location, "garage door is closed")
    
    def stop(self):
        print(self.location, "garage door is stopped")
    
    def light_on(self):
        print(self.location, "garage light is on")
    
    def light_off(self):
        print(self.location, "garage light is off")

class GarageDoorUpCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door
    
    def execute(self):
        self.garage_door.up()
    
    def undo(self):
        self.garage_door.down()

class GarageDoorDownCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door
    
    def execute(self):
        self.garage_door.down()
    
    def undo(self):
        self.garage_door.up()

class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass

class RemoteControl:
    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.undo_command = NoCommand()

        for i in range(7):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())
    
    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
    
    def on_button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]
    
    def off_button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]
    
    def undo_button_was_pushed(self):
        self.undo_command.undo()
    
    def __str__(self):
        string_buff = []
        string_buff.append("\n------ Remote Control ------\n")
        for i in range(len(self.on_commands)):
            string_buff.append(f"[slot {i}] {type(self.on_commands[i]).__name__}    {type(self.off_commands[i]).__name__}\n")
        string_buff.append(f"[undo] {type(self.undo_command).__name__}\n")
        return "".join(string_buff)

if __name__ == "__main__":
    remote_control = RemoteControl()
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("Garage")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_low = CeilingFanLowCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_high, ceiling_fan_off)
    remote_control.set_command(3, stereo_on_with_cd, stereo_off)

    print(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)

    print(remote_control)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(3)
    remote_control.on_button_was_pushed(3)
    print(remote_control)
    remote_control.undo_button_was_pushed()
