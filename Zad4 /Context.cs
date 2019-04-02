namespace Zad4
{
    public class DeliverContext
    {
        private readonly IDeliveryStrategy deliveryStrategy;

        public DeliverContext(IDeliveryStrategy deliveryStrategy)
        {
            this.deliveryStrategy = deliveryStrategy;
        }

        public void DeliverProduct()
        {
            deliveryStrategy.Deliver();
        }

    }
}