# Entanglement & Bell States: Complete Implementation

This folder contains the source code and visual results for fundamental and advanced quantum entanglement concepts, from the four **Bell States** to multipartite entanglement (GHZ) and empirical tests of local realism (CHSH inequality).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kZGYeHcZ014jM8A2tuBPwZPFd99C_N-d?usp=sharing)

---

## 1. Overview

The implementations explore how quantum Hadamard ($H$), Pauli-X ($X$), and CNOT ($CX$) gates can be orchestrated to create maximally entangled states. Below, you will find the circuits, histograms, and technical explanations for each implemented test case.

---

## 2. The Four Bell States

Bell states form a maximally entangled orthonormal basis for a two-qubit Hilbert space $\mathcal{H}_2 \otimes \mathcal{H}_2$:

| Bell State | Mathematical Definition | Gate Sequence | Measurement Outcomes |
| :---: | :---: | :---: | :---: |
| $\vert\Phi^+\rangle$ | $\frac{1}{\sqrt{2}}(\vert00\rangle + \vert11\rangle)$ | $H(q_0) \to CX(q_0, q_1)$ | $\vert00\rangle, \vert11\rangle$ (50% / 50%) |
| $\vert\Phi^-\rangle$ | $\frac{1}{\sqrt{2}}(\vert00\rangle - \vert11\rangle)$ | $X(q_0) \to H(q_0) \to CX(q_0, q_1)$ | $\vert00\rangle, \vert11\rangle$ (with relative phase $\pi$) |
| $\vert\Psi^+\rangle$ | $\frac{1}{\sqrt{2}}(\vert01\rangle + \vert10\rangle)$ | $X(q_1) \to H(q_0) \to CX(q_0, q_1)$ | $\vert01\rangle, \vert10\rangle$ (50% / 50%) |
| $\vert\Psi^-\rangle$ | $\frac{1}{\sqrt{2}}(\vert01\rangle - \vert10\rangle)$ | $X(q_0) \to X(q_1) \to H(q_0) \to CX(q_0, q_1)$ | $\vert01\rangle, \vert10\rangle$ (Singlet State) |

### A. First Bell State $|\Phi^+\rangle$

**Code:** [`FirstBellState.py`](./FirstBellState.py)

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](FirstBellCirc.png) | ![Histogram](FirstBellHist.png) |

* **How it's created:** A Hadamard ($H$) gate is applied to the first qubit to create an equal superposition, followed by a CNOT ($CX$) gate with the first qubit as control and the second as target.

---

### B. Second Bell State $|\Phi^-\rangle$

**Code:** [`SecondBellState.py`](./SecondBellState.py)

$$
|\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}
$$

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](SecondBellCirc.png) | ![Histogram](SecondBellHist.png) |

* **How it's created:** Similar to the first state, but applying an $X$ (or $Z$) gate beforehand to introduce the negative quantum phase difference.

---

### C. Third Bell State $|\Psi^+\rangle$

**Code:** [`ThirdBellState.py`](./ThirdBellState.py)

$$
|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}
$$

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](ThirdBellCirc.png) | ![Histogram](ThirdBellHist.png) |

* **How it's created:** Qubits are initialized to opposite states before creating the superposition, generating perfect anti-symmetry correlations.

---

### D. Fourth Bell State $|\Psi^-\rangle$

**Code:** [`FourthBellState.py`](./FourthBellState.py)

$$
|\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
$$

| Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](FourthBellCirc.png) | ![Histogram](FourthBellHist.png) |

* **How it's created:** Also known as the singlet state, it exhibits rotational invariance and a negative relative phase between opposite state superpositions.

---

## 3. Multipartite Entanglement: GHZ State

**Code:** [`GHZState.py`](./GHZState.py)

$$
|\text{GHZ}\rangle = \frac{|000\rangle + |111\rangle}{\sqrt{2}}
$$

Extending maximal entanglement to 3 qubits (the Greenberger-Horne-Zeilinger state). Measuring any single qubit instantly dictates the state of the other two, collapsing exclusively to $|000\rangle$ or $|111\rangle$.

| GHZ Quantum Circuit | Measurement Histogram |
| :---: | :---: |
| ![Circuit](ghz_circ.png) | ![Histogram](ghz_hist.png) |

---

## 4. Quantum Sub-routines: Controlled Bell State

**Code:** [`ControlledBell.py`](./ControlledBell.py)

Demonstrates how to abstract the preparation of a Bell State into a custom quantum gate block and apply it conditionally using a control qubit (acting as a quantum conditional or "quantum if-statement"). If the control is $|1\rangle$, the target qubits become entangled.

| Abstract Controlled Circuit | Resulting Measurement Histogram |
| :---: | :---: |
| ![Circuit](controled_bell.png) | ![Histogram](controled_bell_hist.png) |

---

## 5. Proving Non-Locality: CHSH Inequality

**Code:** [`CHSH_Inequality.py`](./CHSH_Inequality.py)

An algorithmic simulation of the experimental Clauser-Horne-Shimony-Holt (CHSH) test (a generalization of Bell's Theorem).

By rotating Alice and Bob's measurement bases to specific non-orthogonal angles, the test calculates the correlation parameter $S$:

$$
S = E(a, b) - E(a, b') + E(a', b) + E(a', b')
$$

Classical local hidden-variable theories enforce the Bell-CHSH boundary:

$$
|S| \le 2
$$

However, the simulated quantum system consistently violates this classical bound, reaching Tsirelson's bound:

$$
S \approx 2\sqrt{2} \approx 2.82
$$

> [!IMPORTANT]  
> The numerical violation proven in this script ($S \approx 2.82 > 2$) is one of the most robust computational proofs that quantum mechanics is fundamentally non-local, and that local hidden variables cannot explain physical reality.

---

## 6. Technical Details

* **Framework:** Qiskit (v1.x)
* **Simulator:** `AerSimulator` (Qiskit Aer) with 1024 shots.
* **Purpose:** Educational and expository material for Undergraduate Research (IC).

> [!TIP]  
> To interact directly with the quantum codes, test other angles, and visualize Bloch spheres in real time, we highly recommend using the **Google Colab** link located at the top of this page.
