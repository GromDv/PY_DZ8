import model as m
import view as w

def data_append(data, file):
    f = open(file, "a")
    f.write('\n')
    f.write(w.list2str(data))
    f.close

def add_dSubj(data):
    data_append(data, "subjects.txt")

def add_Pupil(data):
    data_append(data, "pupils.txt")

def export_pupils():
    f = open("pupils.txt", "w")
    data = w.DB2str()
    f.write(data)
    f.close

def export_marks():
    f = open("marks.txt", "w")
    data = w.dMarks2str()
    f.write(data)
    f.close