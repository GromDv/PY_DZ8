import json
import math
import model as m
import data_export as de

def Prompt():
    inpt = input(cRed('Работаем с БД "Ученики школы":\n')+cGreen(' 1 - Показать список учеников\n 2 - Показать лист оценок ученика\n 3 - Добавить оценку ученика по предмету\n 4 - Добавить нового ученика\n 5 - Показать список предметов\n 6 - Добавить новый предмет\n 7 - Средняя оценка ученика по предмету\n 8 - Средний балл школы по предмету\n 9 - Количество претендентов на медаль\n10 - Сгенерировать 100 доп. новых учеников\n11 - Сохранить БД\n12 - Загрузить БД\n20 - Закончить работу\n?>: '))
    return inpt

esc = lambda code: f'\033[{code}m'
cGreen = lambda y: esc('32')+y+esc('0')
cRed = lambda y: esc('31')+y+esc('0')

def ToSelectPupil():
    inpt = int(input(cRed("Введите номер ученика :")))
    return inpt

def ToSelectSubject():
    inpt = int(input(cRed("Введите номер предмета :")))
    return inpt

def ToInputNewMark():
    inpt = int(input(cRed("Введите оценку :")))
    return inpt
# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на выбор(можно использовать пробел или запятые)
# id будем присваивать автоматически
def NewData():
    data_in = input(cRed("Укажите последовательно через пробел - имя, фамилию: "))
    m.data_add(data_in)

def NewSubj():
    data_in = input(cRed("Укажите название нового предмета: "))
    return data_in

def PrintDB():
    sps = m.GetDataDB()
    for i in sps:
        for j in range(len(i)):
            if j == len(i)-1:
                print(f'{i[j]}', end="")
            else:
                print(f'{i[j]:12} ', end="")
        print()
    print()

def PrintSubj():
    sps = m.Get_dSubj()
    for i in sps:
        for j in range(len(i)):
            if j == len(i)-1:
                print(f'{i[j]}', end="")
            else:
                print(f'{i[j]:12} ', end="")
        print()
    print()
        
def DB2str():
    sps = m.GetDataDB()
    res = ""
    for i in sps:
        for j in range(len(i)):
            if j == len(i)-1:
                res += str(i[j])
            else:
                res += str(i[j]) + " "
        res += "\n"
    return res

def list2str(indata):
    res = ""
    for i in range(len(indata)):
        if i == len(indata)-1:
            res += str(indata[i])
        else:
            res += str(indata[i]) + " "
    #res += "\n"
    return res

def PrintNF():
    sps = m.GetDataDB()
    for i in sps:
        for j in range(1,3):
            print(str(i[j]), end=" ")
        print()

def PrintMarks(pupil):
    print(m.NamePupil(pupil))
    dt = m.GetMarksOfPupil(pupil)
    for i in dt:
        print(f'{i:15}\t{dt[i]}')

def PrintMarksSubj(pupil, subj):
    dt = m.GetMarksOfPupil(pupil)
    #print(pupil," ",m.NameSubj(subj))
    for i in dt:
        if i == m.NameSubj(subj):
            print(i, dt[i])

def PrintAverageMarkSubj(pupil, subj):
    tmp = []
    dt = m.GetMarksOfPupil(pupil)
    for i in dt:
        if i == m.NameSubj(subj):
            tmp = dt[i].copy()
            print(i, dt[i])
    avg = 0
    for j in tmp:
        avg += j
    avg = avg / len(tmp)
    print("Средняя оценка - ", round(avg,2))

def PrintAverageMarkSubjSchool(subj):
    pps = []
    school = m.Get_dMarks()
    for p in school:
        tmp = []
        dt = m.GetMarksOfPupilName(p)
        for i in dt:
            if i == m.NameSubj(subj):
                tmp = dt[i].copy()
#                print(i, dt[i])
        if len(tmp) != 0:
            avg = 0
            for j in tmp:
                avg += j
            avg = avg / len(tmp)
            pps.append(avg)
#        print("Средняя оценка - ", round(avg,2))
    avg = 0
    for jk in pps:
        avg += jk
    avg = avg / len(pps)
    print("Средний балл по предмету - ", round(avg,2))

def PrintGoldenPupils():
    GoldPup = 0
    school = m.Get_dMarks()
    for pupil in school:
        gold = True
        marks = m.GetMarksOfPupilName(pupil)
        for subj in marks:
            for mark in marks[subj]:
                if mark == 1 or mark == 2 or mark == 3:
                    gold = False
        if gold == True:
            GoldPup += 1

    print("Учеников на 4 и 5 всего - ", GoldPup)

def dMarks2str():
    dbs = m.Get_dMarks()
    dss = json.dumps(dbs)
    return dss