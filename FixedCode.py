## KISS - Keep It Simple, Stupid Model: Calculator
class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def add(self):
        return self.input1 + self.input2

    def subtract(self):
        return self.input1 - self.input2

    def multiply(self):
        return self.input1 * self.input2

    def divide(self):
        if self.input2 == 0:
            return "ERROR. Division by Zero"
        return self.input1 / self.input2

## DRY - Don't Repeat Yourself
class Music:
    def __init__(self, user, songList):
        self.userMusic = user
        self.songList = songList
        self.songPlaylist = []

    def createPlaylist(self, song):
        if song in self.songList:
            self.songPlaylist.append(song)
        else:
            print(f"{song} is not in your available song list.")

    def playMusic(self, song):
        if song in self.songPlaylist:
            print(f"{song} is playing.")
        else:
            print(f"{song} is not playing.")


