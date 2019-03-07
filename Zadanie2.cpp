#include <iostream>
#include <stdlib.h>

using namespace std;

class klawiatura
{
  private:
    static klawiatura *single;
    klawiatura()
    {
        keyPressed = 0;
    }

  public:
    unsigned keyPressed;
    static klawiatura *getInstance()
    {
        {
            if (single == NULL)
            {
                single = new klawiatura();
                return single;
            }
            else
            {
                return single;
            }
        }
    }
};

class klawisz
{
  private:
    static const int interval = 1000;
    bool wasPressed;

  public:
    unsigned key;

    klawisz(unsigned key)
    {
        this->wasPressed = false;
        this->key = key;
    }

    bool checkIfPressed(klawiatura keyboard)
    {
        if (!wasPressed)
        {
            cout << "Checking if key with value " << key << " has been pressed"
                 << "\n";
            if (key == keyboard.keyPressed)
            {
                cout << "Key with value " << key << " has been pressed"
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

#ifdef _WIN32
#include <windows.h>

void sleep(unsigned milliseconds)
{
    Sleep(milliseconds);
}
#endif

klawiatura *klawiatura::single(0);
int main()
{
    klawiatura keyboard = *klawiatura::getInstance();
    klawisz k1 = klawisz(2);
    klawisz k2 = klawisz(5);
    klawisz k3 = klawisz(14);
    klawisz k4 = klawisz(16);
    klawisz k5 = klawisz(20);

    int counter = 0;

    while (true)
    {
        int keypressed = rand() % 20 + 1;
        keyboard.keyPressed = keypressed;

        bool isK1Pressed = k1.checkIfPressed(keyboard);
        bool isK2Pressed = k2.checkIfPressed(keyboard);
        bool isK3Pressed = k3.checkIfPressed(keyboard);
        bool isK4Pressed = k4.checkIfPressed(keyboard);
        bool isK5Pressed = k5.checkIfPressed(keyboard);

        if (isK1Pressed && isK2Pressed && isK3Pressed && isK4Pressed && isK5Pressed)
        {
            break;
        }

        cout << "Iteracja " << counter << "\n";
        counter++;
    }
    return 0;
}