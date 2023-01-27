import json
import model as m

def import_pupils():
    res = []
    tmp = []
    f = open("pupils.txt", "r")
    for line in f:
        line = str(line).replace("\n","")
        tmp = line.split(" ")
        tmp[0] = int(tmp[0])
        res.append(tmp)
    f.close

    m.SetDataDB(res)

def import_subj():
    res = []
    tmp = []
    f = open("subjects.txt", "r")
    for line in f:
        line = str(line).replace("\n","")
        tmp = line.split(" ")
        tmp[0] = int(tmp[0])
        res.append(tmp)
    f.close
    m.SetSubj(res)

def import_marks():
    f = open("marks.txt", "r")
    data = f.read()
    f.close
    m.SetMarks(json.loads(data))