# Encryption and Decryption Scripts

This repository contains several Python scripts that implement various encryption and decryption techniques. These scripts are useful for understanding basic cryptographic methods such as Caesar cipher, one-time pad, and other encryption techniques.

## Table of Contents

- [Getting Started](#getting-started)
- [File Descriptions](#file-descriptions)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Getting Started

Each script in this repository is standalone and can be executed independently. Ensure Python is installed on your system and follow the instructions under [Usage](#usage) to run each script.

## File Descriptions

1. **3_a_Caesar_encryption.py**: This script implements a Caesar encryption function, shifting letters by a specified number of positions.

2. **3_Caesar_encryption.py**: Similar to `3_a_Caesar_encryption.py`, this script also performs Caesar encryption but may have variations in implementation or usage.

3. **4_Caesar_decryption.py**: This script is used for decrypting text encrypted with the Caesar cipher. It reverses the shift applied during encryption.

4. **5_one_time_pad.py**: Implements the one-time pad encryption method, where each character in the plaintext is combined with a random key character. This method is theoretically unbreakable if the key is truly random and as long as the plaintext.

5. **7_Caesar_with_public_key.py**: A modified version of the Caesar cipher that incorporates a public key mechanism for encryption.

6. **8_Caesar_decipher.py**: This script attempts to decipher text encoded with the Caesar cipher, likely implementing frequency analysis or brute-force methods.

7. **9_faktoriazation.py**: Contains a function for calculating factorials, which might be used as part of a cryptographic process or for other mathematical applications.

## Requirements

- Python 3.x

No additional libraries are required beyond Python's standard library.

## Usage

To run any script, open a terminal or command prompt and navigate to the directory containing the scripts. Then execute a script with:

```bash
python script_name.py
