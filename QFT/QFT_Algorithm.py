# Transformada de Fourier Quântica (QFT)
# Teste empírico da inversão de fase e necessidade da porta SWAP para o estado |3>

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def qft_rotations(circuit, n):
    """Aplica as portas Hadamard e as rotações de fase (Rk)."""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(np.pi/2**(n-qubit), qubit, n)
    qft_rotations(circuit, n)

def swap_qubits(circuit, n):
    """Corrige a ordem dos qubits (Bit-Reversal)."""
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def build_qft(n):
    """Monta o circuito completo."""
    qc = QuantumCircuit(n)
    qft_rotations(qc, n)
    swap_qubits(qc, n)
    return qc

# Teste com 2 qubits para o estado |3> (|11> em binário)
n_qubits = 2
qc_init = QuantumCircuit(n_qubits)
qc_init.x([0, 1]) 

qft_circuit = build_qft(n_qubits)
full_qc = qc_init.compose(qft_circuit)

full_qc.measure_all()

sim = AerSimulator()
qc_transpilado = transpile(full_qc, sim)
counts = sim.run(qc_transpilado, shots=1024).result().get_counts()

print(f"Resultados da medição: {counts}")

circuit_fig = full_qc.draw('mpl', style="iqp")
histogram_fig = plot_histogram(counts, title="QFT do estado |3>")
display(circuit_fig)
display(histogram_fig)