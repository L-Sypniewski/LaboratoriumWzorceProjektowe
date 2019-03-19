namespace Zadanie3
{
    public interface ObservableKlawisz : IKlawisz, IObserwator
    {

    }
    public interface IKlawisz
    {
        string message();
        uint key { get; }
    }
    public class Klawisz : ObservableKlawisz
    {
        private bool wasPressed { get; set; } = false;

        public uint key { get; }
        public Klawisz(uint key)
        {
            this.key = key;
        }

        public void update()
        {
            System.Console.Write(message());
        }

        public void registerToSubject(ISubject subject)
        {
            subject.zarejestrujObserwatora(this);
        }

        public string message()
        {
            return $"\n Zostalem wcisniety i wyrejestrowany {key}";
        }
    }
    public class Dekorator : ObservableKlawisz
    {
        public ObservableKlawisz baseKlawisz;
        private readonly string suffix;

        public uint key { get { return baseKlawisz.key; } }

        public Dekorator(ObservableKlawisz baseKlawisz, string suffix)
        {
            this.baseKlawisz = baseKlawisz;
            this.suffix = suffix;
        }

        public string message()
        {
            var str = baseKlawisz.message();
            return str + suffix + "\n";
        }

        public void update()
        {
            baseKlawisz.update();
            System.Console.Write(suffix);
        }

        public void registerToSubject(ISubject subject)
        {
            subject.zarejestrujObserwatora(this);
        }
    }

}