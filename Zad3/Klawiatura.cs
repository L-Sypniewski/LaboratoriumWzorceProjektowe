using System.Collections.Generic;

namespace Zadanie3
{
    public class Klawiatura : ISubject
    {
        public IList<IObserwator> ListaObserwatorow { get; set; } = new List<IObserwator>();

        private static Klawiatura shared = null;
        public static Klawiatura Shared
        {
            get
            {
                if (shared == null)
                {
                    shared =  new Klawiatura();
                    return shared;
                } else 
                {
                    return shared;
                }
            }
        }
        uint keyPressed = 0;

        public int rejestrSize()
        {
            return ListaObserwatorow.Count;
        }

        public uint getPressedKey()
        {
            return keyPressed;
        }

        public void setPressedKey(uint u)
        {
            keyPressed = u;
            notify();
        }

        private Klawiatura()
        {
            System.Console.WriteLine("Stworzono klawiature");
        }

        public void notify()
        {
            for (int i = 0; i < ListaObserwatorow.Count; i++)
            {
                IObserwator obserwator = ListaObserwatorow[i];

                ObservableKlawisz klawisz = obserwator as ObservableKlawisz;
                if (klawisz != null && klawisz.key == keyPressed)
                {
                    usunObserwatora(klawisz);
                    obserwator.update();
                }
            }
        }

        public void usunObserwatora(IObserwator obserwator)
        {
            ListaObserwatorow.Remove(obserwator);
            // for (int i = 0; i < ListaObserwatorow.Count; i++)
            // {
            //     ObservableKlawisz klawisz = obserwator as ObservableKlawisz;
            //     ObservableKlawisz klawiszZListy = ListaObserwatorow[i] as ObservableKlawisz;
            //     if (klawisz != null && klawiszZListy != null && klawisz.key == klawiszZListy.key)
            //     {
            //         ListaObserwatorow.RemoveAt(i);
            //     }
            // }
        }

        public void zarejestrujObserwatora(IObserwator obserwator)
        {
            ListaObserwatorow.Add(obserwator);
        }
    }
}