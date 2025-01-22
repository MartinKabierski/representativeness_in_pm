import pickle

from pm4py import ProcessTree

names = ["BPI_Challenge_2012.align","Detail_Incident_Activity.align","BPI_Challenge_2018.align","BPI_Challenge_2019.align","Road_Traffic_Fines_Management_Process.align","Sepsis_Cases_-_Event_Log.align"]

for name in names:
    alignments = pickle.load(open(name, "rb"))

    conforming = 0
    non_conforming = 0

    for idx, tr in enumerate(alignments):
        c = True
        for x in tr["alignment"]:
            if x[0] == '>>' and x[1] is None:
                continue
            elif x[0] == '>>' and x[1] is not None:
                c = False
            elif x[1] == '>>':
                c = False
            elif x[0] != x[1]:
                c = False


        if not c:
            non_conforming = non_conforming + 1
        else:
            conforming = conforming + 1

    print(">> " + name)
    print(conforming, non_conforming, non_conforming / (conforming + non_conforming))
    print()
