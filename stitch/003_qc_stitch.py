from ds001 import programs_ds001
from ds002 import programs_ds002
from utils import tlc_to_dpdf

programs = programs_ds002

# print("Qiskit circuits as typed-lambda calculus programs for library learning:")
# for p in programs:
#     print("\t",p)

db_dpdf = []
d = tlc_to_dpdf(programs)
db_dpdf.append(d)
# print("\nDistribution for abstraction 0 :",d)

from stitch_core import compress

max_fn = 8

from tqdm import tqdm

for f in tqdm(range(max_fn)):
    res = compress(programs, iterations=f+1, max_arity=2)
    # print("\nAbstractions:")
    # for a in res.abstractions:
    #     print("\t",a)
    d = tlc_to_dpdf(res.rewritten)
    db_dpdf.append(d)
    # print("Distribution for abstraction",(f+1),":",d) 


import matplotlib.pyplot as plt
for pd in db_dpdf:
    p = sorted(list(pd.values()),reverse=True)
    # print(p)
    plt.plot(p, label = str(pd.keys()))
plt.xlabel("Abstraction Rank")
plt.ylabel("Abstraction Count")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()

'''
> python 003_qc_stitch.py

Distribution for abstraction 0 : {'h': 2043, 'tdg': 1142, 't': 1144}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
Distribution for abstraction 1 : {'h': 858, 'tdg': 747, 'fn_0': 395, 't': 749}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
Distribution for abstraction 2 : {'h': 356, 'tdg': 747, 'fn_0': 395, 'fn_1': 502, 't': 247}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
Distribution for abstraction 3 : {'h': 41, 'tdg': 432, 'fn_0': 395, 'fn_1': 502, 'fn_2': 315, 't': 247}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
Distribution for abstraction 4 : {'h': 41, 'tdg': 293, 'fn_3': 139, 'fn_1': 363, 'fn_2': 315, 't': 247, 'fn_0': 256}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
         fn_4(#0,#1) := (fn_1 #1 (tdg (fn_0 #1 #0)))
Distribution for abstraction 5 : {'h': 41, 'tdg': 223, 'fn_3': 139, 'fn_1': 293, 'fn_2': 315, 't': 247, 'fn_4': 70, 'fn_0': 186}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
         fn_4(#0,#1) := (fn_1 #1 (tdg (fn_0 #1 #0)))
         fn_5(#0,#1) := (fn_1 #1 (fn_2 #1 #0))
Distribution for abstraction 6 : {'h': 41, 'tdg': 223, 'fn_3': 139, 'fn_5': 98, 'fn_2': 217, 't': 247, 'fn_1': 195, 'fn_4': 70, 'fn_0': 186}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
         fn_4(#0,#1) := (fn_1 #1 (tdg (fn_0 #1 #0)))
         fn_5(#0,#1) := (fn_1 #1 (fn_2 #1 #0))
         fn_6(#0,#1) := (tdg (fn_2 #0 (fn_1 #0 #1) #0))
Distribution for abstraction 7 : {'h': 41, 'tdg': 187, 'fn_3': 139, 'fn_5': 98, 'fn_2': 181, 't': 247, 'fn_1': 159, 'fn_4': 70, 'fn_0': 186, 'fn_6': 36}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
         fn_4(#0,#1) := (fn_1 #1 (tdg (fn_0 #1 #0)))
         fn_5(#0,#1) := (fn_1 #1 (fn_2 #1 #0))
         fn_6(#0,#1) := (tdg (fn_2 #0 (fn_1 #0 #1) #0))
         fn_7(#0,#1) := (tdg (fn_0 #1 (t #0)))
Distribution for abstraction 8 : {'h': 41, 'tdg': 133, 'fn_3': 139, 'fn_5': 98, 'fn_2': 181, 't': 193, 'fn_1': 159, 'fn_4': 70, 'fn_7': 54, 'fn_0': 132, 'fn_6': 36}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
         fn_4(#0,#1) := (fn_1 #1 (tdg (fn_0 #1 #0)))
         fn_5(#0,#1) := (fn_1 #1 (fn_2 #1 #0))
         fn_6(#0,#1) := (tdg (fn_2 #0 (fn_1 #0 #1) #0))
         fn_7(#0,#1) := (tdg (fn_0 #1 (t #0)))
         fn_8(#0,#1) := (fn_2 #1 (fn_2 #1 (t #0)))
Distribution for abstraction 9 : {'h': 41, 'tdg': 133, 'fn_3': 139, 'fn_5': 98, 'fn_2': 117, 't': 161, 'fn_1': 159, 'fn_4': 70, 'fn_7': 54, 'fn_0': 132, 'fn_6': 36, 'fn_8': 32}

Abstractions:
         fn_0(#0,#1) := (h (tdg (h (t (h (#1 #0) #0) #0) #0) #0) #0)
         fn_1(#0,#1) := (t (h (#1 #0) #0))
         fn_2(#0,#1) := (tdg (h (#1 #0) #0))
         fn_3(#0,#1) := (tdg (fn_0 #1 (fn_1 #1 #0)))
         fn_4(#0,#1) := (fn_1 #1 (tdg (fn_0 #1 #0)))
         fn_5(#0,#1) := (fn_1 #1 (fn_2 #1 #0))
         fn_6(#0,#1) := (tdg (fn_2 #0 (fn_1 #0 #1) #0))
         fn_7(#0,#1) := (tdg (fn_0 #1 (t #0)))
         fn_8(#0,#1) := (fn_2 #1 (fn_2 #1 (t #0)))
         fn_9(#0,#1) := (fn_1 #0 (#1 #0))
Distribution for abstraction 10 : {'h': 41, 'tdg': 133, 'fn_3': 139, 'fn_5': 98, 'fn_2': 117, 't': 161, 'fn_1': 73, 'fn_9': 86, 'fn_4': 70, 'fn_7': 54, 'fn_0': 132, 'fn_6': 36, 'fn_8': 32}

'''