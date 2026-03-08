""" create a secure system that protects and encapsulates sensitive data."""


class SecurePlant:
    def __init__(self, name) -> None:
        self.name = name
        self._height = 0
        self._age = 0

    def set_height(self, height):
        if height < 0:
            print("\nInvalid operation attempted: height " + str(height) +
                  "cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print("Height updated:", str(self._height) + "cm [OK]")

    def set_age(self, age):
        if age < 0:
            print("\nInvalid operation attempted: age" + str(age) +
                  "days [ REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print("Age updated: ", str(self._age) + " days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_info(self):
        return (
            self.name + " (" +
            str(self._height) + "cm, " +
            str(self._age) + " days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print("Plant created:", plant.name)

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)

    print("\nCurrent plant:", plant.get_info())
