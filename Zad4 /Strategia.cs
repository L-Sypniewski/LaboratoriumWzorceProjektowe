using System;

namespace Zad4
{
    class Program
    {
        static void Main(string[] args)
        {
            Decimal money;
            double time;
            double value;

            DeliverContext context = null;

            System.Console.WriteLine("Type in money available: ");
            money = Convert.ToDecimal(Console.ReadLine());
            System.Console.WriteLine("Type in time available: ");
            time = Convert.ToDouble(Console.ReadLine());
            System.Console.WriteLine("Type in product value: ");
            value = Convert.ToDouble(Console.ReadLine());

            switch (money)
            {
                case Decimal d when (money >= 0 && money < 3):
                    context = new DeliverContext(new BicycleDeliveryStrategy());
                    break;
                case Decimal d when (money >= 3 && money < 20):
                    context = value < 0.25 && time > 30 ? new DeliverContext(new BicycleDeliveryStrategy()) : new DeliverContext(new PublicTransportDeliveryStrategy());
                    break;
                case Decimal d when (money >= 20):
                    if (value > 0.75)
                    {
                        context = new DeliverContext(new TaxiDeliveryStrategy());
                    }
                    else if (value >= 0.25)
                    {
                        if (time > 30)
                        {
                            context = new DeliverContext(new BicycleDeliveryStrategy());
                        }
                        else
                        {
                            context = new DeliverContext(new PublicTransportDeliveryStrategy());
                        }
                    }
                    else
                    {
                        context = value < 0.25 && time > 30 ? new DeliverContext(new BicycleDeliveryStrategy()) : new DeliverContext(new PublicTransportDeliveryStrategy());
                    }
                    break;
            }

            context.DeliverProduct();
        }
    }
}
