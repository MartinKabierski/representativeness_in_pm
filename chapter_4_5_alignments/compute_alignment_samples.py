import random
import time
from pm4py import read_xes, discover_petri_net_inductive, read_pnml
from pm4py.algo.conformance.alignments.petri_net.algorithm import apply

names = ["Sepsis_Cases_-_Event_Log", "Road_Traffic_Fines_Management_Process","BPI_Challenge_2012","Detail_Incident_Activity", "BPI_Challenge_2018", "BPI_Challenge_2019"]


for name in names:
	print("## "+name+" ##")
	log = read_xes(name+".xes", return_legacy_log_object=True)
	
	new_log = []
	removed = 0
	#for BPI 2019!
	
	if name =="BPI_Challenge_2019":
		print("BPI-2019 - Removing Long Traces")
		for tr in log:
			if len(tr)> 100:
				removed = removed +1
			else:
				new_log.append(tr)
		print(removed)
		log = new_log
	
	model, im, fm = read_pnml(name+".pnml")
	
	sizes = [100, 200, 300, 400, 500]
	values={100:[],200:[],300:[],400:[],500:[]}
	
	for s in sizes:
		for r in range(5):
			print("Size:" + str(s)+ "    Repetition: " +str(r))
			sample_log = random.sample(log,s)
			t0 = time.time()
			alignments = apply(sample_log, model, im, fm)
			t1 = time.time()
			print("RUNTIME: " + str(t1 - t0))
			values[s].append(t1 - t0)
	f = open(name + ".times", "w")	
	print(values.items())
	for t in values.items():
		f.write(str(t))
	f.close()
	print()
