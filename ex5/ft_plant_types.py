class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_basic_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(self.name + " is blooming beautifully!")

    def get_info(self):
        return (
            f"{self.name} (Flower): "
            f"{self.height}cm, {self.age} days, {self.color} color"
        )


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter + 28
        print(self.name + " provides " + str(shade) +
              " square meters of shade")

    def get_info(self):
        return (
            f"{self.name} (Tree): "
            f"{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"{self.name} (Vegetable): "
            f"{self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )

    def nutrition_info(self):
        print(self.name + " is rich in " + self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    plants = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    ]

    for plant in plants:
        print(plant.get_info())

        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            plant.nutrition_info()
