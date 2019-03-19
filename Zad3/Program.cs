using System;

namespace Zadanie3
{
    class Program
    {
        static void Main(string[] args)
        {
            Klawiatura keyboard = Klawiatura.Shared;
            Klawiatura keyboard2 = Klawiatura.Shared;
            keyboard.notify();

            ObservableKlawisz k1 = new Klawisz(1);
            ObservableKlawisz k2 = new Klawisz(2);
            ObservableKlawisz k3 = new Klawisz(3);
            ObservableKlawisz k4 = new Klawisz(4);
            ObservableKlawisz k5 = new Klawisz(5);

           
            ObservableKlawisz dec1 = new Dekorator(k1, "?");
            ObservableKlawisz dec2 = new Dekorator(dec1, "?");

            ObservableKlawisz dec3 = new Dekorator(k2, "!");

            dec2.registerToSubject(keyboard);
            dec3.registerToSubject(keyboard);
            k3.registerToSubject(keyboard2);
            k4.registerToSubject(keyboard);
            k5.registerToSubject(keyboard);

            int counter = 0;
            var random = new Random();
            while (keyboard.rejestrSize() != 0)
            {
                keyboard.setPressedKey((uint)random.Next(21));
                System.Console.WriteLine($"\n Iteracja {counter}\n Pressed key: {keyboard.getPressedKey()}\n\n");
                keyboard.notify();
                counter++;
            }
        }
    }
}