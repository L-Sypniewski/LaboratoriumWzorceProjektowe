from typing import List
import random

class Klawiatura:

    shared = None

    class __Klawiatura:

         keyPressed = None 

         def __init__(self):
             pass

    def __init__(self):
        if not Klawiatura.shared:
            Klawiatura.shared = Klawiatura.__Klawiatura()

class Klawisz:
    value: int = 0
    __wasPressed: bool = False
    
    def __init__(self, keyValue):
        self.value = keyValue

    def checkIfPressed(self, klawiatura: Klawiatura):
        if not self.__wasPressed:
            print("Sprawdzenie czy klawisz {} zostal wcisniety\n".format(self.value))
            if self.value == klawiatura.keyPressed.value:
                print("Klawisz {} zostal wcisniety\n".format(self.value))
                self.__wasPressed = True
                return self.__wasPressed
            else:
                return self.__wasPressed
        else:
            return self.__wasPressed

def areAllKeysPressed(klawisze: List[Klawisz], klawiatura: Klawiatura):
    areAllKeysPressed: bool = True
    for klawisz in klawisze:
        if not klawisz.checkIfPressed(klawiatura):
            areAllKeysPressed = False
    return areAllKeysPressed

if __name__ == '__main__':
    klawiatura = Klawiatura().shared
    klawiatura.keyPressed = Klawisz(0)

    k1 = Klawisz(18)
    k2 = Klawisz(45)
    k3 = Klawisz(4)
    k4 = Klawisz(23)
    k5 = Klawisz(1)

    klawisze = [k1, k2, k3, k4, k5]
    counter = 0
    while(not areAllKeysPressed(klawisze, klawiatura)):
        klawiatura.keyPressed = Klawisz(random.randint(1, 50))
        print("\nIteracja {} \nWcisniety klawisz: {} \n".format(counter, klawiatura.keyPressed.value))
        counter += 1


    # print(klawiatura)
    # klawiatura.keyPressed = Klawisz(233223)
    # print(str(klawiatura.keyPressed.value))

    # klaw2 = Klawiatura().shared
    # print(klaw2)
    # print(Klawiatura().shared.keyPressed)
