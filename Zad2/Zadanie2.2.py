from typing import List
import random


class Klawiatura:

    shared = None

    class __Klawiatura:
        rejestrObserwatorow: List[any] = []
        keyPressed = None

        def __init__(self):
            pass

        def setPressedKey(self, klawisz):
            self.keyPressed = klawisz

        def rejestrSize(self):
            return len(self.rejestrObserwatorow)

        def zarejestrujObserwatora(self, klawisz):
            self.rejestrObserwatorow.append(klawisz)

        def usunObserwatora(self, klawisz):
            for obserwator in self.rejestrObserwatorow:
                if obserwator.value == klawisz.value:
                    self.rejestrObserwatorow.remove(obserwator)
                    self.usunObserwatora(klawisz)

        def notify(self):
            for obserwator in self.rejestrObserwatorow:
                if obserwator.value == self.keyPressed.value:
                    self.usunObserwatora(obserwator)
                    obserwator.update()

    def __init__(self):
        if not Klawiatura.shared:
            Klawiatura.shared = Klawiatura.__Klawiatura()


class Klawisz:
    value: int = 0
    __wasPressed: bool = False

    def __init__(self, keyValue):
        self.value = keyValue

    def update(self):
        print("Zostalem wcisniety i wyrejestrowany: {} \n".format(self.value))

    def zarejestrujDoSubjecta(self, klawiatura):
        klawiatura.zarejestrujObserwatora(self)


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

    k1.zarejestrujDoSubjecta(klawiatura)
    k2.zarejestrujDoSubjecta(klawiatura)
    k3.zarejestrujDoSubjecta(klawiatura)
    k4.zarejestrujDoSubjecta(klawiatura)
    klawiatura.zarejestrujObserwatora(k5)

    counter = 0
    while(klawiatura.rejestrSize() != 0):
        klawiatura.keyPressed = Klawisz(random.randint(1, 50))
        print("\nIteracja {} \nWcisniety klawisz: {}".format(
            counter, klawiatura.keyPressed.value))
        klawiatura.notify()
        counter += 1
