"""My first Challenge Question in COMP110!"""

__author__ = "730775500"


def mimic(message: str) -> str:
    """Mimic whatever is typed in"""
    return message


def main() -> None:
    """Calling the mimic function"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
