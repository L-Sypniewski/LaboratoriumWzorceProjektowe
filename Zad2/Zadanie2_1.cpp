#include <iostream>
#include <stdlib.h>

using namespace std;

class Klawiatura
{
  private:
    static Klawiatura *shared;
    Klawiatura()
    {
        keyPressed = 0;
    }

  public:
    unsigned keyPressed;
    static Klawiatura *getInstance()
    {
        {
            if (shared == NULL)
            {
                shared = new Klawiatura();
                return shared;
            }
            else
            {
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
        this->wasPressed = false;
        this->key = key;
    }

    bool checkIfPressed(Klawiatura keyboard)
    {
        if (!wasPressed)
        {
            cout << "Sprawdzenie czy klawisz " << key << " zostal wcisniety"
                 << "\n";
            if (key == keyboard.keyPressed)
            {
                cout << "Klawisz  " << key << " zostal wcisniety"
                     << "\n";
                wasPressed = true;
                return wasPressed;
            }
            else
            {
                return wasPressed;
            }
        }
        else
        {
            return wasPressed;
        }
    }
};

bool areAllKeysPressed(Klawisz klawisze[], int size, Klawiatura keyboard)
{
    bool allKeysPressed = true;
    for (int i = 0; i < size; i++)
    {
        if (!klawisze[i].checkIfPressed(keyboard))
        {
            allKeysPressed = false;
        }
    }
    return allKeysPressed;
}

Klawiatura *Klawiatura::shared(0);
int main()
{
    Klawiatura keyboard = *Klawiatura::getInstance();
    Klawisz k1 = Klawisz(18);
    Klawisz k2 = Klawisz(45);
    Klawisz k3 = Klawisz(4);
    Klawisz k4 = Klawisz(23);
    Klawisz k5 = Klawisz(1);

    const int arrayLength = 5;
    Klawisz klawisze[arrayLength] = {k1, k2, k3, k4, k5};

    int counter = 0;
    while (!areAllKeysPressed(klawisze, arrayLength, keyboard))
    {
        keyboard.keyPressed = rand() % 50 + 1;
        cout << "\n\nIteracja " << counter << "\n"
             << "Wcisniety klawisz: " << keyboard.keyPressed << "\n";
        counter++;
    }
    return 0;
}
