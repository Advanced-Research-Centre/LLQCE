from qiskit import QuantumCircuit

def qc_to_tlc(qc: QuantumCircuit) -> str:
    """
    Convert qiskit circuit to typed-lambda calculus program string
    """
    tlc = "I"+str(qc.num_qubits)
    for op in qc.data:
        param = ""
        for q in op.qubits:
            param += " $"+str(q._index)
        tlc = op.operation.name+" ("+tlc+param+" )"
    tlc = "(lam ("+tlc+" ) )"
    return tlc

def tlc_to_dpdf(tlc_corpus):
    dpdf = {}
    for tlc in tlc_corpus:
        for i in range(len(tlc)):
            if tlc[i] == '(':
                gog = tlc[i+1:i+1+tlc[i+1:].find(" ")]  # gate or gadget
                if gog in dpdf.keys():
                    dpdf[gog] += 1
                else:
                    dpdf[gog] = 1
    dpdf.pop('lam')
    dpdf.pop('I1')
    return dpdf