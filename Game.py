from Avatar import Avatar

class Game:
    def __init__(self, name, num_avatars):
        self.name = name
        self.num_avatars = 0
        self.max_num_avatars = num_avatars
        self.myAvatars = []
        self.num_avatars = len(self.myAvatars)
        self.gamestarted = False

    def startGame(self):
        self.myAvatars = []
        self.num_avatars = len(self.myAvatars)
        self.gamestarted = True

    def addAvatar(self, avatar_obj):
        if self.gamestarted:
            if isinstance(avatar_obj, Avatar):
                if self.num_avatars < self.max_num_avatars:
                    self.myAvatars.append(avatar_obj)
                    self.num_avatars = len(self.myAvatars)
                    print("number of avatars", self.num_avatars)
                else:
                    print("Error: exceeds max number of avatars")
            else:
                print("Error: wrong type")
        else:
            print("Error: game has not been started yet")

    def removeAvatar(self, name):
        if self.gamestarted:
            if isinstance(name, str):
                found = False
                for a in self.myAvatars:
                    if a.name == name:
                        self.myAvatars.remove(a)
                        self.num_avatars=len(self.myAvatars)
                        found = True

                if found == false:
                    print("Error: item not found")
            else:
                print("Error: wrong type")
        else:
            print("Error: game has not been started yet")

    def Animate(self):
        if self.gamestarted:
            for a in self.myAvatars:
                a.Animate()
        else:
            print("Error: game has not been started yet")

    def stopGame(self):
        if self.gamestarted:
            self.myAvatars = []
            self.num_avatars = len(self.myAvatars)
            self.gamestarted = False
        else:
            print("Error: game has not been started yet")
