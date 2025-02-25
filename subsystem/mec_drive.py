import wpilib
from commands2 import Command, Subsystem, command
from types import UnionType
class MecanumDrive(Subsystem):
  def __init__(self, frontLeft:wpilib.Spark, frontRight:wpilib.Spark, backLeft:wpilib.Spark, backRight:wpilib.Spark):
    self.frontLeft = frontLeft
    self.backLeft = backLeft
    self.frontRight = frontRight
    self.backRight = backRight
  def applyRequest(self, requests) -> Command:
    return self.run(lambda: requests())
  def drive(self, x: int | float, y: int | float, z: int | float):
    fl = y - z - x
    fr = y+z+x
    bl = y - z +x
    br = y + z -x
    self.frontLeft.set(fl)
    self.frontRight.set(fr)
    self.backLeft.set(bl)
    self.backRight.set(br)