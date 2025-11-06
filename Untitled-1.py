"""
Argparse Teaching Module
------------------------

This module demonstrates how to use argparse for command-line arguments in Python.
"""

import argparse

def main():
    # 1. Create the ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Demo: argparse teaching module"
    )

    # 2. Add arguments
    parser.add_argument("name", type=str, help="Your name (required)")
    parser.add_argument("age", type=int, help="Your age (required)")
    parser.add_argument("--active", action="store_true", help="Are you active? (optional flag)")

    # 3. Parse arguments from the command line
    args = parser.parse_args()

    # 4. Use the arguments
    print(f"Name: {args.name}")
    print(f"Age: {args.age}")
    print(f"Active: {args.active}")

if __name__ == "__main__":
    main()