import random

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

## Single Responsibility
class Student:
    def __init__(self, studentName, studentAge):
        self.studentName = studentName
        self.studentAge = studentAge
        self.studentGPA = 0.0
        self.studentID = 00000000

    def calculateGPA(self, gradeList):
        GPA = 0
        for grade in gradeList:
            GPA += grade
        self.studentGPA = GPA / len(gradeList)

    def calculateID(self):
        self.studentId = random.randint(111111, 1111111)

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





