# PyRot - A simple Python ROT bruteforce utility

PyRot is a tiny utility that will attempt to bruteforce simple ROT ciphers.  

Simply put, it will try to rotate the cipher text in a loop, increasing the rotations each time, and then try and compare the result with a dictionary (a small one is included). 

## Installation

```bash
$ git clone https://github.com/e4ld3rs0n/PyRot.git

$ cd PyRot

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

$ python3 pyrot.py
```

## Usage
`./pyrot [-h] [-f FILE | -s STRING] [-v] [-d DICTIONARY] [--version]`

| Option     | Description                         |
|------------|-------------------------------------|
| -h         | Show the help screen and exit       |
| -f FILE    | Read cipher text from a file        |
| -s STR     | Read cipher text as an argument     |
| -v         | Verbose mode, show all ROT attempts |
| -d DICT    | Use a custom dictionary             |
| --versiion | Show script version and exit        | 

## Example

```bash
$./pyrot.py -s "Tqxxa, Iadxp! Ftue ue mz qjmybxq"                  

Encoded string: Tqxxa, Iadxp! Ftue ue mz qjmybxq

Found the following solutions: 
[+] ROT14 = Hello, World! This is an example

```

