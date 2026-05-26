# Algoritmo de Estimação de Fases (QPE)
# Extração da fase geométrica secreta (theta = 1/8) da porta P(lambda)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt
import numpy as np

# 1. Definição do Problema
theta_secreto = 1/8  
angulo = 2 * np.pi * theta_secreto
t = 3  # Qubits de leitura (N=8)
n_alvo = 1

qc = QuantumCircuit(t + n_alvo, t)

# 2. Preparação
for qubit in range(t):
    qc.h(qubit)
qc.x(t) # Autovetor |1>
qc.barrier()

# 3. Phase Kickback com potências de U
repeticoes = 1
for counting_qubit in range(t):
    for i in range(repeticoes):
        qc.cp(angulo, counting_qubit, t)
    repeticoes *= 2
qc.barrier()

# 4. Decodificador: QFT Inversa
qft_inversa = QFT(num_qubits=t, inverse=True, do_swaps=True).to_gate()
qft_inversa.name = "QFT Inversa"
qc.append(qft_inversa, range(t))

# 5. Medição
for i in range(t):
    qc.measure(i, i)

sim = AerSimulator()
qc_transpilado = transpile(qc, sim)
counts = sim.run(qc_transpilado, shots=1024).result().get_counts()

print(f"Resultados brutos: {counts}")

circuit_fig = qc.draw('mpl', style="iqp")
histogram_fig = plot_histogram(counts, title="QPE: Fase Estimada")
display(circuit_fig)
display(histogram_fig)