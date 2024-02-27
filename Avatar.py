class Avatar:
  def __init__(self, name, haircolor, height, superpower):
    self.name = name
    self.hair = haircolor
    self.height = height
    self.superpower = superpower

  def changeHairColor(self, new_haircolor):
      if isinstance(new_haircolor, str):
          self.hair = new_haircolor
      else:
          print("error, wrong type")

  def Animate(self):
    print("Hi, I am", self.name, "and I have", self.hair, "hair.")
