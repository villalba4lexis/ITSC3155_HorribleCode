## KISS - Keep It Simple, Stupid Model: Calculator
class HorribleCalculator:
    def __init__(self, user_input_x_value, user_input_y_value):
        self.user_input_x_value = user_input_x_value
        self.user_input_y_value = user_input_y_value

    def mathCalculator_AdditionCalculation(self):
        if self.user_input_x_value < 0:
            return
        elif self.user_input_y_value < 0:
            return
        else:
            return self.input1 + self.input2

    def mathCalculator_SubtractionCalculation(self):
        SubtractionResult = self.user_input_x_value - self.user_input_y_value
        return SubtractionResult

    def multiply(self):
        if self.user_input_x_value == 0:
            return 0
        elif self.user_input_y_value == 0:
            return 0
        else:
            return self.user_input_x_value * self.user_input_y_value

    def divide(self):
        if self.user_input_x_value == 0:
            return 0
        elif self.user_input_y_value == 0:
            return
        else:
            return self.user_input_x_value / self.user_input_y_value

## DRY - Don't Repeat Yourself
class HorribleMusic:
    def __init__(self, user, songList):
        self.userMusic = user
        self.songList = songList
        self.songPlaylist = []
    ## Some of my fav songs!
    def createPlaylist(self):
        self.songPlaylist.append("Genesis - Deftones")
        self.songPlaylist.append("Covet - Basement")
        self.songPlaylist.append("South - Quannnic")
        self.songPlaylist.append("7 Words - Deftones")
        self.songPlaylist.append("No One Noticed - The Marias")
        self.songPlaylist.append("Heavy - The Marias")
        self.songPlaylist.append("Future - Split Chain")
        self.songPlaylist.append("Re-Extract - Split Chain Ft. Softcult")
        self.songPlaylist.append("Tomorrow - Distressor Ft. Wisp")

        for song in self.songPlaylist:
            if song == "Genesis - Deftones":
                return "Song Added to Playlist."
            elif song == "Covet - Basement":
                return "Song Added to Playlist."
            elif song == "South - Quannnic":
                return "Song Added to Playlist."
            elif song == "7 Words - Deftones":
                return "Song Added to Playlist."
            elif song == "No One Noticed - The Marias":
                return "Song Added to Playlist."
            elif song == "Heavy - The Marias":
                return "Song Added to Playlist."
            elif song == "Future - Split Chain":
                return "Song Added to Playlist."
            elif song == "Re-Extract - Split Chain Ft. Softcult":
                return "Song Added to Playlist."
            elif song == "Tomorrow - Distressor Ft. Wisp":
                return "Song Added to Playlist."
            else:
                return "Song Not in List, Add to List to add to Playlist."

    def playMusic(self):
        for song in self.songPlaylist:
            if song == "Genesis - Deftones":
                return "Genesis - Deftones is now playing."
            elif song == "Covet - Basement":
                return "Covet - Basement is now playing."
            elif song == "South - Quannnic":
                return "South - Quannnic is now playing."
            elif song == "7 Words - Deftones":
                return "7 Words - Deftones is now playing."
            elif song == "No One Noticed - The Marias":
                return "No One Noticed - The Marias is now playing."
            elif song == "Heavy - The Marias":
                return "Heavy - The Marias is now playing."
            elif song == "Future - Split Chain":
                return "Future - Split Chain is now playing."
            elif song == "Re-Extract - Split Chain Ft. Softcult":
                return "Re-Extract - Split Chain Ft. Softcult is now playing."
            elif song == "Tomorrow - Distressor Ft. Wisp":
                return "Tomorrow - Distressor Ft. Wisp is now playing."
        return "No song playing."

## Single Responsibility
# Student Class Main priority is to obtain data on student such as their name, age, id, and GPA
class HorribleStudent:
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

    # Too vague to determine if a student is ready for a job, should be its own entity to go more in depth.
    def readyForJob(self):
        if self.studentGPA > 3.0:
            return "Might be ready for job."
        elif self.studentAge >= 18:
            return "Ready to work."
        else:
            return "Not ready for job."

