from commands2 import cmd
import commands2
import commands2.util
import wpilib
import wpilib.drive
from subsystem.mec_drive import MecanumDrive


class RobotContainer:
    fr = 1
    fl = 2
    br = 3
    bl = 4
    shaft = 0
    def __init__(self) -> None:
        self.frwheel = wpilib.Spark(self.fr)
        self.flwheel = wpilib.Spark(self.fl)
        self.brwheel = wpilib.Spark(self.br)
        self.blwheel = wpilib.Spark(self.bl)
        self.stick = wpilib.DigitalInput(0)
        self.frwheel.setInverted(True)
        self.flwheel.setInverted(True)
        self.robotdrive = MecanumDrive(self.frwheel, self.flwheel, self.brwheel, self.blwheel)
        self.joystick = commands2.button.CommandJoystick(0)
        self.configureButtonBindings()


    def configureButtonBindings(self) -> None:
        print(f"{self.stick.get()}")
        self.robotdrive.setDefaultCommand(
            self.robotdrive.applyRequest(
                lambda: self.robotdrive.drive(
                    int(self.joystick.getX()),
                    int(self.joystick.getY()),
                    int(self.joystick.getZ() / 2),
                )
            )
        )
            
        
        pass

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.cmd.print_("No autonomous command set")