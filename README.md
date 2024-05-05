# Find the Encryption Key

A program to find the encryption key given a known plaintext and ciphertext pair. The hint for the key is that it is an english word less than 16 characters. This program utilizes the pycryptodome package to invoke OpenSSL calls to encrypt/decrypt plaintext and ciphertext with a list of english words and compare the output plaintext or ciphertext to the originals. If a match is found, then we know we have found the key. 

### MacOS/Linux

First, clone the repository or download/extract the files. Then, it is recommended to go to the project directory and create a virtual environment as follows: 

```
python<version> -m venv <name-for-venv>
```

Then, we need to activate the venv by running:

```
source <name-for-venv>/bin/activate
```

Now that the virtual environment is enabled in the terminal, we need to install the packages required by the program that reside in requirements.txt. To do so, we can run the following command:

```
pip install -r requirements.txt
```

To run the experiment, we can enter one of the following:

```
python find_key.py
```
```
python3 find_key.py
```
```
<name-for-venv>/bin/python find_key.py
```

# Usage
Once the program begin, trials will begin to come in showing the output of the encryption of plaintext and decryption of ciphertext using the list of english words. This can be visually compared in each trial to the expected outputs. The program will stop once the key has been found.
