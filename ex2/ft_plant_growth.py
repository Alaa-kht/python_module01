"""track how plants change and provide operatin to modify their state."""


class Plant:
    def __init__(self, name: str, height: int, Age: int) -> None:
        self.name = name
        self.height = height
        self.Age = Age
    """track multiple plant with  their information.storing and display data
        for several plants efficiently"""

    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.Age += 1

    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    print(rose.get_info)
    init_height = rose.height
    for _ in range(7):
        rose.grow()
        rose.age_one_day()
    print("=== Day 7 ===")
    print(rose.get_info())
    print("Growth this week: " + str(rose.height - init_height) + "cm")
