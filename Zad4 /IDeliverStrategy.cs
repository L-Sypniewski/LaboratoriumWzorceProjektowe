namespace Zad4
{
    public interface IDeliveryStrategy
    {
        void Deliver();
    }

    public class BicycleDeliveryStrategy : IDeliveryStrategy
    {
        public void Deliver()
        {
            System.Console.WriteLine("Delivered by bicycle!");
        }
    }

    public class PublicTransportDeliveryStrategy : IDeliveryStrategy
    {
        public void Deliver()
        {
            System.Console.WriteLine("Delivered by public transport!");
        }
    }

    public class TaxiDeliveryStrategy : IDeliveryStrategy
    {
        public void Deliver()
        {
            System.Console.WriteLine("Delivered by taxi!");
        }
    }
}