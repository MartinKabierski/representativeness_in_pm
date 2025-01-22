import multiprocessing
import pickle

import pm4py
from pm4py.objects.process_tree.obj import ProcessTree

### THIS SCRIPT IS THE FOUNDATION OF THE TABLE IN CHAPTER 5 ###

names = ["Sepsis_Cases_-_Event_Log", "Road_Traffic_Fines_Management_Process","BPI_Challenge_2012","Detail_Incident_Activity", "BPI_Challenge_2018", "BPI_Challenge_2019"]
for name in names:
	log = pm4py.read_xes(name+".xes", return_legacy_log_object=True)
	model, im, fm = pm4py.read_pnml(name+".pnml")
	
	#for BPI 2019 we remove traces with length above 100
	if name =="BPI_Challenge_2019":
		print("BPI-2019 - Removing Long Traces")
		new_log = []
		removed = 0
		for tr in log:
			if len(tr)> 100:
				removed = removed +1
			else:
				new_log.append(tr)
		print(removed)
		log = new_log
	
	t0 = time.time()
	alignments = pm4py.algo.conformance.alignments.petri_net.algorithm.apply_multiprocessing(log, model, im, fm, {"cores":120})
	t1 = time.time()
	
	conforming = 0
	non_conforming = 0

	for tr in alignments:
		c = True
		for x in tr["alignment"]:
			#print(type(x[0]),type(x[1]))
			if x[0] == '>>' and x[1] is None:
				continue
			elif x[0] == '>>' and x[1] is not None:
				c = False
			elif x[1] == '>>':
				c = False
			elif x[0]!=x[1]:
				c = False


		if not c:
			non_conforming = non_conforming + 1
		else:
			conforming = conforming +1

    	print(">> " + name)
    	print("Alignment Construction Time: "+ str(t1-t0))
    	print(conforming, non_conforming, non_conforming / (conforming + non_conforming))
    	print()

	file_al=open(name+".align", "wb")
	pickle.dump(alignments,file_al)
	file_al.close()
