class ShippingService:
    @staticmethod
    def ship_items(shippables):
        print("** Shipment notice **")
        total_weight = 0
        for item in shippables:
            print(f"{item['quantity']}x {item['product'].get_name()} {item['product'].get_weight()*item['quantity']}g")
            total_weight += item['product'].get_weight() * item['quantity']
        print(f"Total package weight {total_weight/1000:.1f}kg")