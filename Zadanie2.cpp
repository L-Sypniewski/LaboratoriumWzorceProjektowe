#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

class Klawiatura
{
    vector<class Klawisz *> rejestrObserwatorow;
    static Klawiatura *shared;
    unsigned keyPressed;
    Klawiatura()
    {
        keyPressed = 0;
    };

  public:
    void setPressedKey(unsigned u);
    unsigned getPressedKey();
    int rejestrSize();
    void zarejestrujObserwatora(Klawisz *klawisz);
    void usunObserwatora(Klawisz *klawisz);
    void notify();

    static Klawiatura *getInstance()
    {
        {
            if (shared == NULL)
            {
                shared = new Klawiatura();
                cout << "Stworzono klawiature";
                return shared;
            }
            else
            {
                std::cout << "Nie stworzono klawiatury - instancja juz istnieje";
                return shared;
            }
        }
    }
};

class Klawisz
{
  private:
    bool wasPressed;

  public:
    unsigned key;
    Klawisz(unsigned key)
    {
        this->key = key;
    };

    void update();
    void registerToSubject(Klawiatura *keyboard);
};

//################## Klawiatura
int Klawiatura::rejestrSize()
{
    return rejestrObserwatorow.size();
}

unsigned Klawiatura::getPressedKey()
{
    return keyPressed;
}

void Klawiatura::setPressedKey(unsigned u)
{
    this->keyPressed = u;
    notify();
}

void Klawiatura::notify()
{
    for (int i = 0; i < rejestrObserwatorow.size(); i++)
    {
        Klawisz klawisz = *rejestrObserwatorow[i];
        if (klawisz.key == this->keyPressed)
        {
            this->usunObserwatora(&klawisz);
            klawisz.update();
        }
    }
}
void Klawiatura::usunObserwatora(Klawisz *klawisz)
{
    for (int i = 0; i < rejestrObserwatorow.size(); i++)
    {
        if (rejestrObserwatorow[i]->key == klawisz->key)
        {
            rejestrObserwatorow.erase(rejestrObserwatorow.begin() + i);
            usunObserwatora(klawisz);
        }
    }
}

void Klawiatura::zarejestrujObserwatora(Klawisz *klawisz)
{
    rejestrObserwatorow.push_back(klawisz);
}

//################## Klawisz
void Klawisz::update()
{
    {
        std::cout << "\n"
                  << "Zostalem wcisniety i wyrejestrowany: " << key << "\n";
    }
}

void Klawisz::registerToSubject(Klawiatura *keyboard)
{
    keyboard->zarejestrujObserwatora(this);
};


Klawiatura *Klawiatura::shared(0);

//################## main()
int main()
{
    Klawiatura keyboard = *Klawiatura::getInstance();
    keyboard.notify();

    Klawisz k1(32);
    Klawisz k2(1);
    Klawisz k3(35);
    Klawisz k4(47);
    Klawisz k5(19);

    k1.registerToSubject(&keyboard);
    k2.registerToSubject(&keyboard);
    k3.registerToSubject(&keyboard);
    k4.registerToSubject(&keyboard);
    keyboard.zarejestrujObserwatora(&k5);

    int counter = 0;
    while (keyboard.rejestrSize() != 0)
    {
        keyboard.setPressedKey(rand() % 50 + 1);
        cout << "Iteracja " << counter << "\n"
             << "Pressed key: " << keyboard.getPressedKey() << "\n\n";
        keyboard.notify();
        counter++;
    }

    return 0;
}
