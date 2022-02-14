#! /usr/bin/python3

import argparse
import plistlib

def byteStringProcessor(_bytes):
    print("{ length = ", end="")
    length = len(_bytes)
    print(length, end=" ")

    if length < 32:
        print("bytes = 0x", end="")
        print(_bytes.hex())
    else:
        record = _bytes.hex()
        print("bytes = 0x", end="")
        print(record[:8] + " " + record[8:16] + " " + record[16:24] + " " + record[24:32] + " ... " + record[-16:-8] + " " + record[-8:])
    print(" }")

def printStructure(key, series):
    print("  " + key + " => {",)
    index = 0
    for item in series:
        print("    " + str(index) + " => ", end="")
        if isinstance(item, bytes):
            byteStringProcessor(item)
        else:
            print(item)
        index += 1
        pass
    print("  }")

def argumentHander():
    parser = argparse.ArgumentParser(prog="plutil")
    parser.add_argument('file', nargs='+', help='Property List fie')
    args = parser.parse_args()

    return args.file[0]

def main():
    _file = argumentHander()

    with open(_file, 'rb') as fp:
        pl = plistlib.load(fp)

        for key in pl.keys():
            printStructure(key, pl[key])

if __name__ == '__main__':
    main()
