import time

import pm4py.objects.log.importer.xes.variants.iterparse

log = pm4py.read_xes("BPI_Challenge_2012.xes")
model, im, fm = pm4py.read_pnml("BPI_Challenge_2012.pnml")
t0 = time.time()
alignments = pm4py.conformance.fitness_alignments(log, model, im, fm)
t1 = time.time()
print("RUNTIME: "+str(t1-t0))

print(alignments)