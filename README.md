# NFC-tag-reader

Given an NFC tag, parses the tag id and displays it in binary.

## Usage

To get started, execute the commands below at a command prompt.
Ensure that the processor on the system is an ARM processor and not an Intel processor.
If it is not an ARM processor, the assembled code cannot be run.

$ git clone https://github.com/DMevada/NFC-tag-reader.git
$ cd NFC-tag-reader
$ as -o first.o first.s
$ gcc -o first first.o
$ python control.py
