import random

## KISS - Keep It Simple, Stupid Model: Calculator
class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def add(self):  # Simple, clear method for addition
        return self.input1 + self.input2

    def subtract(self):  # Minimal logic, easy to read
        return self.input1 - self.input2

    def multiply(self):
        return self.input1 * self.input2

    def divide(self):  # Only logic is to avoid division by zero
        if self.input2 == 0:
            return "ERROR. Division by Zero"
        return self.input1 / self.input2
# Follows KISS by keeping all operations minimal, clear, and single-purpose

## DRY - Don't Repeat Yourself
class Music:
    def __init__(self, user, songList):
        self.userMusic = user
        self.songList = songList
        self.songPlaylist = []

    def createPlaylist(self, song):  # General-purpose method, reusable
        if song in self.songList:
            self.songPlaylist.append(song)
        else:
            print(f"{song} is not in your available song list.")

    def playMusic(self, song):  # Reuses data structure and avoids repetition
        if song in self.songPlaylist:
            print(f"{song} is playing.")
        else:
            print(f"{song} is not playing.")
# Follows DRY by avoiding hardcoding songs, and generalizing logic for reuse


## Single Responsibility
class Student:
    def __init__(self, studentName, studentAge):
        self.studentName = studentName
        self.studentAge = studentAge
        self.studentGPA = 0.0
        self.studentID = 00000000

    def calculateGPA(self, gradeList):  # Only calculates GPA
        GPA = 0
        for grade in gradeList:
            GPA += grade
        self.studentGPA = GPA / len(gradeList)

    def calculateID(self):  # Only assigns a random ID
        self.studentId = random.randint(111111, 1111111)
# Follows SRP by ensuring each method and the class itself has one clear responsibility

## YAGNI - You Aren't Going to Need it
class Game:
    def __inti__(self, gameUserName):
        self.gameUserName = gameUserName
        self.gameProgressiveLevel = 0
        self.gameRank = 'Bronze'
        self.userIsPlaying = False
        self.userIsOnline = False

    def userRank(self):
        if self.gameProgressiveLevel < 10:
            self.gameRank = "Bronze"
        elif self.gameProgressiveLevel < 20:
            self.gameRank = "Silver"
        elif self.gameProgressiveLevel < 30:
            self.gameRank = "Gold"
        else:
            self.gameRank = "Diamond"

    def ready_CompetativeMatchMaking(self):
        if self.userIsPlaying and self.userIsOnline:
            return True
        else:
            return False
# Follows YAGNI because future features are simulated with stubs, not fully implemented prematurely