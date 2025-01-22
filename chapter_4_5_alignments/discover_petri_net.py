from random import sample

import pm4py


names = ["BPI_Challenge_2012.align","Detail_Incident_Activity.align","BPI_Challenge_2018.align","BPI_Challenge_2019.align","Road_Traffic_Fines_Management_Process.align","Sepsis_Cases_-_Event_Log.align"]

for name in names:
    log = pm4py.read_xes(name, return_legacy_log_object=True)
    model, im, fm = pm4py.discovery.discover_petri_net_inductive(log, False, noise_threshold=0.2)
    pm4py.write.write_pnml(model,im,fm,name + ".pnml")
