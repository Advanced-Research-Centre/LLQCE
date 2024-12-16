from qiskit import QuantumCircuit

qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0, 1)

qc2 = QuantumCircuit(3)
qc2.h(0)
qc2.cx(0, 1)
qc2.h(1)
qc2.cx(1, 2)

qc3 = QuantumCircuit(4)
qc3.h(0)
qc3.cx(0, 1)
qc3.h(1)
qc3.cx(1, 2)
qc3.h(2)
qc3.cx(2, 3)

def qc_to_tlc(qc: QuantumCircuit) -> str:
    """
    Convert qiskit circuit to typed-lambda calculus program string
    """
    tlc = "I"+str(qc.num_qubits)
    for op in qc.data:
        param = ""
        for q in op.qubits:
            param += " $"+str(q._index)
        tlc = op.operation.name+" ( "+tlc+param+" )"
    tlc = "(lam ("+tlc+" ) )"
    return tlc

programs = [qc_to_tlc(qc1), qc_to_tlc(qc2), qc_to_tlc(qc3)]

print("Qiskit circuits as typed-lambda calculus programs for library learning:")
for p in programs:
    print("\t",p)

from stitch_core import compress

res = compress(programs, iterations=1, max_arity=2)

print("\nCompressed abstraction:")
for a in res.abstractions:
    print("\t",a)

print("\nRewritten programs:")
for p in res.rewritten:
    print("\t",p)

'''
Qiskit circuits as typed-lambda calculus programs for library learning:
         (lam (cx ( h ( I2 $0 ) $0 $1 ) ) )
         (lam (cx ( h ( cx ( h ( I3 $0 ) $0 $1 ) $1 ) $1 $2 ) ) )
         (lam (cx ( h ( cx ( h ( cx ( h ( I4 $0 ) $0 $1 ) $1 ) $1 $2 ) $2 ) $2 $3 ) ) )

Compressed abstraction:
         fn_0(#0,#1) := (h (cx (#1 #0) #0) #0)

Rewritten programs:
         (lam (cx (h (I2 $0) $0 $1)))
         (lam (cx (fn_0 $1 (h (I3 $0) $0) $2)))
         (lam (cx (fn_0 $2 (fn_0 $1 (h (I4 $0) $0)) $3)))
'''