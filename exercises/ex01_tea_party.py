"""Calculating the amount of tea bags, treats, and money needed for a tea party."""

__author__ = "730775500"


def main_planner(guests: int) -> None:
    """Brings all the function together"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags:" + str(tea_bags(people=guests)))
    print("Treats:" + str(treats(people=guests)))
    print("Cost:$" + str((cost(tea_bags(people=guests), treats(people=guests)))))


# The cost should be calling both function


def tea_bags(people: int) -> int:
    """2 tea bags per person"""
    return people * 2


def treats(people: int) -> int:
    """1.5 treats for each tea a guest drink."""
    return int(tea_bags(people=people) * 1.5)


# people should be equal to people to show the people in both function


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating the total cost of the tea party"""
    return float(tea_count * 0.5 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
