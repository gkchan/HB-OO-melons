import random
import datetime

"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Splurge pricing: chooses value between 5 and 9 for melon price"""

        base_price = random.randint(5, 9)

        # Adding Rush Hour Prices: use datetime library.
        # Get time and weekday from datetime.datetime/date.method.
        # Use the if statement to check and add charge:
        # Add time zone to get correct time?
        # https://docs.python.org/2/library/datetime.html
        # http://fellowship.hackbrightacademy.com/materials/f18k/exercises/oo-melons/further-study.html

            # if  and:
            #     base_price += 4

        if self.species == "christmas":
            base_price *= 1.5

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
   
    order_type = "domestic"
    tax = 0.08

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Add flat fee to small international orders"""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3
        
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""

    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        """Record that an inspection has passed"""

        self.passed_inspection = passed


