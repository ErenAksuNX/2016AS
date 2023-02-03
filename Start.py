import glob
import os
from shutil import copyfile
from datetime import datetime


class Start:
    def __init__(self):
        self.PDFFiles = None
        self.path = None
        self.destination = None

    def start(self, path, destination):
        self.path = path
        self.destination = destination

        os.chdir(path)

        self.PDFFiles = list()

# in dieser Schleife wird jede PDF-Datei in die PDF-List gespeichert
        for file in glob.glob("*.pdf"):
            self.PDFFiles.append(file)

# in der untern Schleife wird pro PDF Datei in der Liste ein neuer Name erstellt, und die datei wird kopiert
        for file in self.PDFFiles:
            parts = file.split("_")
            frznr = getFrznr(parts[0])
            date = getDate(parts[1])

            filename = nullstring(date.day) + "." + nullstring(date.month) + "." + str(date.year) + "_" + frznr + "_" + ".pdf"

            print(filename)

            copyfile(self.path + "/" + file, self.destination + "/" + filename)


# diese Funktion gibt die lange Frznr zurück

def getFrznr(nr):
    if nr == "151":
        return "94809442151-8"
    elif nr == "152":
        return "94809442152-6"
    elif nr == "153":
        return "94809442153-4"
    elif nr == "154":
        return "94809442154-2"
    elif nr == "155":
        return "94809442155-9"
    elif nr == "156":
        return "94809442156-7"
    elif nr == "157":
        return "94809442157-5"
    elif nr == "158":
        return "94809442158-3"
    elif nr == "159":
        return "94809442159-1"
    elif nr == "160":
        return "94809442160-9"

    elif nr == "351":
        return "94809442351-4"
    elif nr == "352":
        return "94809442352-2"
    elif nr == "353":
        return "94809442353-0"
    elif nr == "354":
        return "94809442354-8"
    elif nr == "355":
        return "94809442355-5"
    elif nr == "356":
        return "94809442356-3"
    elif nr == "357":
        return "94809442357-1"
    elif nr == "358":
        return "94809442358-9"
    elif nr == "359":
        return "94809442359-7"
    elif nr == "360":
        return "94809442360-5"
    elif nr == "361":
        return "94809442361-3"
    elif nr == "362":
        return "94809442362-1"
    elif nr == "363":
        return "94809442363-9"
    elif nr == "364":
        return "94809442364-7"
    elif nr == "365":
        return "94809442365-4"
    elif nr == "366":
        return "94809442366-2"
    elif nr == "367":
        return "94809442367-0"
    elif nr == "368":
        return "94809442368-8"
    elif nr == "369":
        return "94809442369-6"
    elif nr == "370":
        return "94809442370-4"
    elif nr == "371":
        return "94809442371-2"
    elif nr == "372":
        return "94809442372-0"
    elif nr == "373":
        return "94809442373-8"
    elif nr == "374":
        return "94809442374-6"
    elif nr == "375":
        return "94809442375-3"


def getDate(datum):
    datum = datum[:4] + "/" + datum[4:6] + "/" + datum[6:8]

    print(datum)

    d = datetime

    date = d.strptime(datum, "%Y/%m/%d")

    return date


def nullstring(dateTime):
    if dateTime is not None and dateTime == 0:
        return "00"
    elif dateTime is not None and dateTime < 10:
        return "0" + str(dateTime)
    elif dateTime is not None:
        return str(dateTime)
