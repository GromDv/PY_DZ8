import model as m
import view as w
import data_export as de
import data_import as di


def start():
    m.data_init()

    while True:
        op = w.Prompt()
        if op == '1':
            w.PrintDB()
        elif op == '2':
            w.PrintDB()
            pup = w.ToSelectPupil()
            w.PrintMarks(pup)
        elif op == '4':
            w.NewData()
            w.PrintDB()
            de.export_marks()
        elif op == '3':
            w.PrintDB()
            pup = w.ToSelectPupil()
            w.PrintSubj() 
            sub = w.ToSelectSubject()
            mrk = w.ToInputNewMark()
            m.NewMark(pup,sub,mrk)
            w.PrintMarks(pup)
            de.export_marks()
        elif op == '12':
            di.import_pupils()
            di.import_marks()
        elif op == '5':
            w.PrintSubj() 
        elif op == '6':
            m.add_dSubj(w.NewSubj())
            de.export_marks()
        elif op == '7':
            w.PrintDB()
            pup = w.ToSelectPupil()
            w.PrintSubj() 
            sub = w.ToSelectSubject()
            w.PrintAverageMarkSubj(pup,sub)
        elif op == '8':
            w.PrintSubj() 
            sub = w.ToSelectSubject()
            w.PrintAverageMarkSubjSchool(sub)
        elif op == '9':
            w.PrintGoldenPupils()
        #    w.PrintAverageMarkSubjSchool(sub)
        elif op == '10':
            m.FillBDRandom()
        elif op == '11':
            de.export_marks()
            de.export_pupils()
            
        elif op == '20':
            break



