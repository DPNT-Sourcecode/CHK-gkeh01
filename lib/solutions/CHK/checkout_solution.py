

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
            'D': 15,
            'E': 40,
            'F': 10,
            'G': 20,
            'H': 10,
            'I': 35,
            'J': 60,
            'K': 80,
            'L':90,
            'M':15,
            'N':40,
            'O':10,
            'P':50,
            'Q':30,
            'R':50,
            'S':20,
            'T':20,
            'U':40,
            'V':50,
            'W':20,
            'X':17,
            'Y':20,
            'Z':21
        }     
        self.promotions = {
            'A': {
                    5: 200,
                    3: 130,
                },
            'B': {2: 45},
            'H': {
                10: 80,
                5: 45,
            },
            'K': {2: 150},
            'P': {5: 200},
            'Q': {3: 80},
            'V': {
                3: 130,
                2: 90
            },            
        }
        self.cross_promotions = {
            'E': {2: "B"},
            'F': {2: "F"},
            'N': {3: "M"},
            'R': {3: "Q"},
            'U': {3: "U"}
        } 
        self.bundle_promotions = {
            'XSTYZ': {3: 45}
        }               
    
    def apply_bundle_promotions(self, items):
        total = 0
        for skus, promotions in self.bundle_promotions.items():
            skus = list(skus)
            total_amount = 0
            for sku in skus:
                if sku in items:
                    total_amount += items[sku]
            for promotion_amount, promotion_price in promotions.items():
                times_used = total_amount // promotion_amount
                total += times_used * promotion_price
                to_be_taken = promotion_amount * times_used
                for i in range(to_be_taken):
                    for sku in skus:
                        if items[sku] == 0:
                            continue
                        items[sku] -=1
                        break
        return total, items
            
    def apply_cross_promotions(self, items):
        for sku, promotion in self.cross_promotions.items():
            if sku not in items:
                continue
            for quantity, other_sku in promotion.items():
                if other_sku not in items:
                    continue
                total_items = items[sku]
                if other_sku == sku:
                    bought = 0
                    for i in range(total_items):
                        bought += 1
                        if bought == quantity and i < total_items - 1:
                            items[other_sku] = max(0, items[other_sku] - 1)
                            bought = -1
                else:
                    free_items = total_items // quantity
                    items[other_sku] = max(0, items[other_sku] - free_items)
        return items
    
    def get_price(self, items):
        items = self.apply_cross_promotions(items)
        items, total = self.apply_bundle_promotions(items)
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
