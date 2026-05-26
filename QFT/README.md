# Quantum Fourier Transform (QFT)

This folder contains the implementation of the Quantum Fourier Transform algorithm, a key subroutine that maps the computational basis into the Fourier basis (phase encoding).

## Implementation Details
The algorithm translates a classical number into relative phases across a superposition using Hadamard gates and controlled fractional phase rotations ($R_k$). 

The implemented script proves the mathematical necessity of `SWAP` gates at the end of the circuit to correct the bit-reversal geometry outputted by the tensor product expansion.