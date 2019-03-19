using System.Collections.Generic;
namespace Zadanie3
{
    public interface IObserwator
    {
        void update();
        void registerToSubject(ISubject subject);
    }

    public interface ISubject 
    {
        IList<IObserwator> ListaObserwatorow { get; }
        void zarejestrujObserwatora(IObserwator obserwator);
        void usunObserwatora(IObserwator obserwator); 
        void notify();
    }
}