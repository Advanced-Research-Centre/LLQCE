from qiskit import QuantumCircuit
from utils import qc_to_tlc

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

qc4 = QuantumCircuit(5)
qc4.h(0)
qc4.cx(0, 1)
qc4.h(1)
qc4.cx(1, 2)
qc4.h(2)
qc4.cx(2, 3)
qc4.h(3)
qc4.cx(3, 4)

programs_ds001 = [qc_to_tlc(qc1), qc_to_tlc(qc2), qc_to_tlc(qc3), qc_to_tlc(qc4)]
