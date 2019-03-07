from enum import Enum

class Key(Enum):
    Key1 = 1,
    Key2 = 2,
    Key3 = 3,
    Key4 = 4,
    Key5 = 5

class klawiatura:

    shared = None

    class __klawiatura:
        keyPressed = None 

        def __init__(self):
            pass

    def __init__(self):
        if not klawiatura.shared:
            klawiatura.shared = klawiatura.__klawiatura()


klaw = klawiatura()

print(klaw.shared.keyPressed)
klaw.shared.keyPressed = Key.Key1

klaw2 = klawiatura()
print(klaw2.shared.keyPressed)