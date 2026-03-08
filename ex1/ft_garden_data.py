"""track multiple plant with  their information.
    storing and display data for several plants efficiently"""


class Plant:
    def __init__(self, name: str, height: int, Age: int) -> None:
        self.name = name
        self.height = height
        self.Age = Age

    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    print(p1.get_info())
    p2 = Plant("Sunflower", 80, 45)
    print(p2.get_info())
    p3 = Plant("Cactus", 15, 120)
    print(p3.get_info())
