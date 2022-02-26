"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self,species,qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        if self.species == 'Christmas':
            base_price = 5*1.5
        else:
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price

    def mark_shipped(self):
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"   #class attributes
    tax = 0.08  #class attributes
    # def __init__(self, species, qty):
    #     self.order_type = "domestic"
    #     self.tax = 0.08

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    #     self.order_type = "domestic"
    #     self.tax = 0.08

    #def get_total(self):
       #"""Calculate price, including tax."""

       #base_price = 5
        #total = (1 + self.tax) * self.qty * base_price

        #return total

    #def mark_shipped(self):
       # """Record the fact than an order has been shipped."""

        #self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
    

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17

    def get_total(self, is_Christmas):
        """Calculate price, including tax."""
        super().get_total(self,is_Christmas)
        if self.qty <10 and is_Christmas:
            base_price = base_price+3
        #elif self.qty<10:
            #base_price = base_price+3
    

        #base_price = 5
        #total = (1 + self.tax) * self.qty * base_price

        #return total

   # def mark_shipped(self):
       # """Record the fact than an order has been shipped."""

       # self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
