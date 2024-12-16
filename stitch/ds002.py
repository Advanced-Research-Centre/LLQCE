from qiskit import QuantumCircuit
from utils import qc_to_tlc

from qiskit.transpiler.passes import SolovayKitaev
from qiskit.synthesis import generate_basic_approximations
from qiskit.quantum_info import random_unitary
from qiskit.circuit.library import UnitaryGate

from tqdm import tqdm

sk_gs = ['h', 't', 'tdg']
sk_d = 3
sk_r = 3
gbs = generate_basic_approximations(basis_gates = sk_gs, depth = sk_d)
skd = SolovayKitaev(basic_approximations = gbs, recursion_degree = sk_r)

ds_sz = 100

programs_ds002 = []

for i in tqdm(range(ds_sz)):
    qc = QuantumCircuit(1)
    matrix = random_unitary(2**1).data
    u = UnitaryGate(matrix)
    qc.append(u, [0])
    qc_skd = skd(qc)
    programs_ds002.append(qc_to_tlc(qc_skd))
