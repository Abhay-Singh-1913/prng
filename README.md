# Combined Pseudo-Random Number Generator (PRNG)

This project demonstrates a combined pseudo-random number generator (PRNG) implementation in Python. It brings together multiple PRNG algorithms, each with its own unique properties, and combines their outputs to generate a single random number.

## Table of Contents

- [Introduction](#introduction)
- [Implemented PRNGs](#implemented-prngs)
- [Usage](#usage)
- [Contributing](#contributing)
- [Disclamer](#disclaimer)

## Introduction

Pseudo-random number generators are widely used in various applications that require randomness, such as simulations, games, and cryptography.

To generate sequences of numbers that appear to be random, but are actually determined by an initial value called a seed.

The term "pseudo" indicates that the numbers are not truly random, but they exhibit properties of randomness for most practical purposes.

This project showcases a combined approach where multiple PRNG algorithms are used together to enhance the quality and distribution of generated random numbers.

## Implemented PRNGs

This project includes the following PRNG algorithms:

1. Linear Congruential Generator (LCG)
2. Xorshift128+ PRNG
3. Mersenne Twister PRNG
4. PCG (Permuted Congruential Generator) PRNG
5. Simplified ISAAC PRNG (In case of educational use only)

These PRNGs are implemented as separate classes within the `prng.py` file.

## Usage

To generate a combined random number using all implemented PRNGs, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/nirajmohanrana/prng.git
    ```
   
2. Navigate to the project directory:
    ```
   cd prng
   ```
   
3. Run the 'main.py' script:
    ```
   python main.py
   ```
   
The script will output a combined random number generated using the implemented PRNGs.

## Contributing
Contributions are welcome! If you find any issues, have suggestions for improvements, or want to add more PRNG algorithms, please feel free to submit a pull request.

## Disclaimer
This implementation is primarily meant for educational purposes and experimentation. It demonstrates the concept of combining multiple PRNGs for enhanced randomness. For applications requiring high-quality randomness or security, always use well-established cryptographic libraries and methods.
