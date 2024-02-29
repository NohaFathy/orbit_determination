# Gibb's Method for Preliminary Orbit Determination

## Introduction
This Python script implements Gibb's method for preliminary orbit determination, a fundamental technique in orbital mechanics. The provided code calculates the velocity vectors and extracts key orbital parameters based on three position vectors (R1, R2, R3).

## Usage
1. Replace the position vectors `R1`, `R2`, and `R3` in the `main` function with your specific values.
2. Execute the script to obtain information about the orbit, including speed at R2, semi-major axis, eccentricity, inclination angle, and true anomaly.

## Dependencies
- NumPy
- Math

##  Output
The script provides information such as:

Speed at R2
Semi-major axis
Eccentricity
Inclination angle
True anomaly

Install dependencies using:
```bash
pip install numpy

## Example

```python
if __name__ == "__main__":
    main() 


