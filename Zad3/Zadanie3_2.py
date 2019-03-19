
import random


class Klawiatura:

    shared = None

    class __Klawiatura:
        rejestrObserwatorow = []
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
    value = 0
    __wasPressed = False

    def __getMessage(self):
        return "Zostalem wcisniety i wyrejestrowany: {}".format(self.value)


    def __init__(self, keyValue):
        self.value = keyValue

    def update(self):
        print(self.__getMessage())

    def zarejestrujDoSubjecta(self, klawiatura):
        klawiatura.zarejestrujObserwatora(self)

class Dekorator:
    def __init__(self, klawisz, string):
        self.klawisz = klawisz
        self.value = klawisz.value
        self.string = string

    def update(self):
        self.klawisz.update()
        print(self.string)

    def zarejestrujDoSubjecta(self, klawiatura):
        klawiatura.zarejestrujObserwatora(self)




def areAllKeysPressed(klawisze, klawiatura):
    areAllKeysPressed = True
    for klawisz in klawisze:
        if not klawisz.checkIfPressed(klawiatura):
            areAllKeysPressed = False
    return areAllKeysPressed


if __name__ == '__main__':
    klawiatura = Klawiatura().shared
    klawiatura.keyPressed = Klawisz(0)

    k1 = Klawisz(1)
    k2 = Klawisz(2)
    k3 = Klawisz(3)
    k4 = Klawisz(4)
    k4 = Dekorator(k4, "!")
    k5 = Klawisz(5)
    k5 = Dekorator(k5,"#")
    k3 = Dekorator(k3,"@")
    k3 = Dekorator(k3,"*")

    k1.zarejestrujDoSubjecta(klawiatura)
    k2.zarejestrujDoSubjecta(klawiatura)
    k3.zarejestrujDoSubjecta(klawiatura)
    k4.zarejestrujDoSubjecta(klawiatura)
    klawiatura.zarejestrujObserwatora(k5)

    counter = 0
    while(klawiatura.rejestrSize() != 0):
        klawiatura.keyPressed = Klawisz(random.randint(1, 6))
        print("\nIteracja {} \nWcisniety klawisz: {}".format(
            counter, klawiatura.keyPressed.value))
        klawiatura.notify()
        counter += 1
