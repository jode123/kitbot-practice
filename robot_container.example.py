import wpilib
import wpilib.drive

class mec_drive():
  fr = 1
  fl = 2
  br = 3
  bl = 4
  shaft = 0
  
  def wheel_setup(self):
    self.frwheel = wpilib.PWMSparkMax(self.fr)
    self.flwheel = wpilib.PWMSparkMax(self.fl)
    self.brwheel = wpilib.PWMSparkMax(self.br)
    self.blwheel = wpilib.PWMSparkMax(self.bl)
    self.stick = wpilib.Joystick(self.shaft)
  
    self.frwheel.setInverted(True)
    self.flwheel.setInverted(True)
    self.brwheel.setInverted(False)
    self.blwheel.setInverted(False)

    self.robotdrive = wpilib.drive.MecanumDrive(self.frwheel, self.flwheel, self.brwheel, self.blwheel)
