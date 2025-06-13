#!/usr/bin/env python3
"""
Example application to demonstrate mdump functionality
"""

def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"


def main():
    """Main entry point"""
    name = input("What's your name? ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
