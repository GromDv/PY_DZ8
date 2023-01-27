import data_import as di
import data_export as de
import random

dataDB = []         # список учеников
dMarks = dict()     # справочник оценок
dSubjects = []        # список предметов
dPupil = dict()
dSubj = dict()
dMs = [0,]
pNames = ['Петр','Василий','Николай','Сергей','Иван','Алексей','Александр']
pLastNames = ['Иванов','Петров','Сидоров','Куликов','Соловьев','Дроздов','Воробьев','Голубев','Воронин']

def data_init():
    # di.import_pupils()
    di.import_subj()
    # di.import_marks()
 #   fillMarks()
    # print(dataDB)
    # print(dSubjects)
    # print(dMarks)

def fillMarks():
    for i in dSubjects:
        dSubj[i[1]] = dMs
    for i in dataDB:
        dMarks[str(i[1])+" "+str(i[2])] = dSubj

def FillBDRandom(num = 100):
    dSubj.clear()
    dMs.clear()
    for i in range(num):
        tmp = []
        tmp.append(i+1)
        tmp.append(random.choice(pNames))
        tmp.append(random.choice(pLastNames))
        nam =  tmp[1] + " " + tmp[2]
        dataDB.append(tmp)

        for i in dSubjects:
            for j in range(20):
                dMs.append(random.randint(1,5))
            dSubj[i[1]] = dMs.copy()
            dMs.clear()
        #print(dSubj)
        dMarks[nam] = dSubj.copy()
        #print(dMarks[nam])
        dSubj.clear()
        

    #print(dMarks)
        


def GetDataDB():
    return dataDB

def Get_dMarks():
    return dMarks

def GetMarksOfPupil(pup):
    return dMarks[NamePupil(pup)]

def GetMarksOfPupilName(pup):
    return dMarks[pup]

def NamePupil(num):
    for i in dataDB:
        if i[0] == num:
            return str(i[1]+" "+str(i[2]))
    
def NameSubj(num):
    for i in dSubjects:
        if i[0] == num:
            return i[1]

def Get_dSubj():
    return dSubjects

def data_add(data):
    dataList = data.split(" ")
    ind = len(dataDB)
    dataList.insert(0,ind+1)
    dataDB.append(dataList)
    de.add_Pupil(dataList)
    tmp = dict()
    for i in dSubjects:
        tmp[i[1]] = dMs.copy()
    dMarks[NamePupil(ind+1)] = tmp

def add_dSubj(data):
    dList = []
    ind = len(dSubjects)
    dList.append(ind+1)
    dList.append(data)
    dSubjects.append(dList)
    de.add_dSubj(dList)
    for i in dMarks:
        dMarks[i][data] = dMs.copy()

def NewMark(pupil, subject, mark):
    marks = GetMarksOfPupil(pupil)
    #tmp = marks[NameSubj(subject)].copy
    #print("tmp=",tmp)
    # if tmp[0] == 0:
    #     tmp[0] = mark
    # else:
    #tmp.append(mark)
    #dMarks[NamePupil(pupil)][NameSubj(subject)] = tmp.copy()
    dMarks[NamePupil(pupil)][NameSubj(subject)].append(mark)

def SetDataDB(data):
    global dataDB
    dataDB = data

def SetSubj(data):
    global dSubjects
    dSubjects = data

def SetMarks(data):
    global dMarks
    dMarks = data

nam = lambda x: x[1]
ind = lambda x: x[0]

def Sorting(pos):
    global dataDB
    res = []
    res = sorted(dataDB, key = lambda x: x[pos])
    dataDB = res
    # for k in range(len(dataDB)):
    #     temp = dataDB[k]
    #     ti = k
    #     for i in range(k,len(dataDB)):
    #         if temp[pos] > dataDB[i][pos]:
    #             temp = dataDB[i]
    #             ti = i
    #     dataDB[ti] = dataDB[k]
    #     dataDB[k] = temp


