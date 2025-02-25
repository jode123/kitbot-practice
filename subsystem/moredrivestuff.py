from commands2 import Subsystem, Command, cmd
import wpilib
class moredrivestuff(Subsystem):
  def __init__(self, drivemotors: wpilib.Spark):
    super().__init__()
    self.drivemotors = drivemotors
  def rundrive(self, speed: float):
    self.drivemotors.set(speed/100)
  def stopdrive(self):
    self.drivemotors.set(0)
  def applyRequest(self, speed: float) -> Command:
    return cmd.runEnd(lambda: self.rundrive(speed), self.stopdrive, self)