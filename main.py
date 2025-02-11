#!/usr/bin/env python3
__version__ = "1.1.0"

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Add two numbers from the command line."
    )
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")
    # Adding a --version flag that prints the program name and version
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )

    args = parser.parse_args()
    result = args.a + args.b + 2
    print(f"The sum of {args.a} and {args.b} is {result}")


if __name__ == "__main__":
    main()
