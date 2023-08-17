

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = list(skus)
    pricing = Pricing()
    basket = Basket(skus)
    return pricing.get_price(basket.items)


class Basket:
    def __init__(self, skus):
        self.items = {}
        for sku in skus:
            if sku not in self.items:
                self.items[sku] = 1
            else:
                self.items[sku] += 1


class Pricing:
    def __init__(self):
        self.prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }
        self.promotions = {
            'A': {
                    5: 200,
                    3: 130,
                },
            'B': {2: 45},
        }
        self.cross_promotions = {
            'E': {2: "B"},
        }        
    
    def apply_cross_promotions(self, items):
        for sku, promotion in self.cross_promotions.items():
            if sku not in items:
                continue
            for quantity, other_sku in promotion.items():
                if other_sku not in self.items:
                    continue
                total_items = self.items[sku]
                free_items = total_items // quantity
                self.items[other_sku] = max(0, self.items[other_sku] - free_items)
        return items
    
    def get_price(self, items):
        items = self.apply_cross_promotions(items)
        total = 0
        for sku, quantity in items.items():
            item_price = self.get_price_for_item(sku, quantity)
            if item_price == -1:
                return -1
            total += item_price
        return total      


    def get_price_for_item(self, sku, quantity):
        if sku not in self.prices:
            return -1
        total = 0
        while quantity > 0:
            used_offer = False
            if sku in self.promotions:
                for amount, price in self.promotions[sku].items():
                    if amount <= quantity:
                        total += price
                        quantity -= amount
                        used_offer = True
                        break
            if used_offer:
                continue
            if quantity > 0:
                total += self.prices[sku]
                quantity -= 1
            
        return total      


