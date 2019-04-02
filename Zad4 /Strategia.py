class BicycleDeliveryStrategy:
    def deliver(self):
        print("Delivered by bicycle!")


class PublicTransportDeliveryStrategy:
    def deliver(self):
        print("Delivered by public transport!")


class TaxiDeliveryStrategy:
    def deliver(self):
        print("Delivered by taxi!")


class DeliverContext:
    def __init__(self, deliveryStrategy):
        self.deliveryStrategy = deliveryStrategy

    def DeliverProduct(self):
        self.deliveryStrategy.deliver()


money = input("Type in money available: ")
time = input("Type in time available: ")
value = input("Type in product value: ")

if money >= 0 and money < 3:
    context = DeliverContext(BicycleDeliveryStrategy())
elif money >= 3 and money < 20:
    context = DeliverContext(BicycleDeliveryStrategy(
    )) if value < 0.25 and time > 30 else DeliverContext(PublicTransportDeliveryStrategy())
elif money >= 20:
    if value > 0.75:
        context = DeliverContext(TaxiDeliveryStrategy())
    elif value >= 0.25:
        if time > 30:
            context = DeliverContext(BicycleDeliveryStrategy())
        else:
            context = DeliverContext(PublicTransportDeliveryStrategy())
    else:
        context = DeliverContext(BicycleDeliveryStrategy(
        )) if value < 0.25 and time > 30 else DeliverContext(PublicTransportDeliveryStrategy())


context.DeliverProduct()
