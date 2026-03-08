class Plant:
    def __init__(self, name: str, height: int, Age: int) -> None:
        self.name = name
        self.height = height
        self.Age = Age
    """track multiple plant with  their information.
        storing and display data for several plants efficiently"""
    def get_info(self):
        return (f"{self.name} {self.height}cm, {self.Age} days")


if __name__ == "__main__":
    Plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in Plants:
        print("Created: ", plant.get_info())
    print("\nTotal plants created:", len(Plants))
