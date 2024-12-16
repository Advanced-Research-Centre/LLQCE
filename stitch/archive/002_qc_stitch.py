from ds001 import programs_ds001
from ds002 import programs_ds002
from utils import tlc_to_dpdf

programs = programs_ds002

# print("Qiskit circuits as typed-lambda calculus programs for library learning:")
# for p in programs:
#     print("\t",p)

from stitch_core import compress

res = compress(programs, iterations=2, max_arity=2)

print("\nCompressed abstraction:")
for a in res.abstractions:
    print("\t",a)

# print("\nRewritten programs:")
# for p in res.rewritten:
#     print("\t",p)