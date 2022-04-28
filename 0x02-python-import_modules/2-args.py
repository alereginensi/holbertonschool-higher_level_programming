#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(f"0 arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
        print(f"{len(argv) - 1}: {argv[1]}")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for n in range(1, len(argv)):
            print(f"{n}: {argv[n]}")
