# Quantum Phase Estimation (QPE)

This folder contains the implementation of the Quantum Phase Estimation algorithm. It acts as a bridge between abstract phase manipulation and measurable classical data.

## Implementation Details
The algorithm extracts the unknown eigenvalue (phase $\theta$) of a Unitary operator $U$ given its eigenvector $|\psi\rangle$. It uses the **Phase Kickback** mechanism combined with powers of $U$ to slice the phase into binary fractional decimals, storing them in the control register. Finally, an **Inverse QFT** ($QFT^\dagger$) decodes the phases back into the computational basis for deterministic measurement.