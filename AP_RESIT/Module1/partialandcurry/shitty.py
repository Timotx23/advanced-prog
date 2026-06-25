import argparse

from data import *
from functools import partial

# The product prices listed in the products list are the initial values before any VAT or discount applied.
# Some products should be taxed with a standard and others with a reduced VAT.

# This assignment is to develop a python program which can output a price overview. This overview consists of many different manupilations of prices per country, different user types, etc.

# 1. First let's create a fomula that can be applied in general.
# A typical formula to do so is the following:
# final price = (original product * vat) - discount
# the discount is generally computed either based on some percentage e.g., 20% off or based on a flat rate, e.g. EUR10 off. Members have a discount as well.
# 1.1. let's compute first the discount based on the price, the member type and the time of the year.
def curried_discount(member_discount):
    # Write your code here:
    def price(price):
        def time_of_year(toy):
            return 
            

        return time_of_year
    return price



# 1.2. Now let's compute the final price based on the VAT and the discount computed above.
def curried_final_price(vat):
    # Write your code here:
    def calculate(price):
        ...
    return calculate


# 1.3. Let's combine both functions into one that can compute the final price based on all parameters.
def curried_calculate_final_price(product_price):
    # Write your code here:
    
    def with_vat(vat):
        #curri
        def member_discount(memberdiscount):
            def seasonal_discount(seasonaldiscount):
                def additional_flat_discount(additionalflatdiscount):
                    final_price = (product_price* vat)
                    if memberdiscount:
                        final_price -= final_price*memberdiscount
                    if seasonaldiscount:
                        final_price -= seasonaldiscount
                    if additionalflatdiscount:
                        final_price -= additionalflatdiscount
                    return final_price
                    
                return additional_flat_discount
            return seasonal_discount
        return member_discount

    return with_vat

# 1.4. Let's create some functions to compute the final price for a product depending on its type.

# 1.4.1. Let's create a function calledcalculate_final_price that uses the curried function above to compute the final price for a product depending on its type.
def calculate_final_price_standard(product_price, country, member_discount, seasonal_discount, additional_flat_discount):
    return curried_calculate_final_price(product_price)(standard_vat[country])(member_discount)(seasonal_discount)(additional_flat_discount)

def calculate_final_price_reduced(product_price, country, member_discount, seasonal_discount, additional_flat_discount):
    return curried_calculate_final_price(product_price)(reduced_vat[country])(member_discount)(seasonal_discount)(additional_flat_discount)

# 1.4.2 Create a function called calculate_final_price_bg_standard that uses the curried function above to compute the final price for a product in Bulgaria.
def calculate_final_price_bg_standard(product_price, member_discount, seasonal_discount, additional_flat_discount):
    # Complete the return statement
    return 

# As well as a function called calculate_final_price_bg_reduced that uses the curried function above to compute the final price for a product in Bulgaria.
def calculate_final_price_bg_reduced(product_price, member_discount, seasonal_discount, additional_flat_discount):
    # Complete the return statement
    return 

# 1.4.3. Can you do the same with a partial function instead of a curried function?
calculate_final_price_bg_standard_partial = # Write your code here (1 line)
calculate_final_price_bg_reduced_partial = # Write your code here (1 line)

# 1.5. Now let's create a function that applies either the reduced or the standard VAT in Bulgaria based on the product category using map.
def compute_final_price_bg(product, member_discount, seasonal_discount, additional_flat_discount):
    category = # Write a lambda function here to get the category from the product
    price = # Write a lambda function here to get the price from the product
    
    if category(product) in reduced_vat_categories:
        return calculate_final_price_bg_reduced(price(product), member_discount, seasonal_discount, additional_flat_discount)
    
    return calculate_final_price_bg_standard(price(product), member_discount, seasonal_discount, additional_flat_discount)


# 2. Now let's create a function that can output the final prices for all products in a given country for a given member type, seasonal discount and additional flat discount using a list comprehension.
def price_overview_comprehension(country, member_type, seasonal_month, additional_flat_discount):
    name = # Write a lambda function here to get the name from the product
    category = # Write a lambda function here to get the category from the product
    price = # Write a lambda function here to get the price from the product

    member_discount = members[member_type]
    seasonal_discount = seasonal_discounts[seasonal_month]["discount"]
    
    standard_final_prices = # Write a list comprehension here to compute final prices for products with standard VAT
    reduced_final_prices = # Write a list comprehension here to compute final prices for products with reduced VAT

    return standard_final_prices + reduced_final_prices

# 3. Let's create a function that can output the final prices for all products in a given country, for a given member type, seasonal discount and additional flat discount using map and filter.
def price_overview_map_filter(country, member_type, seasonal_month, additional_flat_discount):
    name = # Write a lambda function here to get the name from the product
    category = # Write a lambda function here to get the category from the product
    price = # Write a lambda function here to get the price from the product

    member_discount = members[member_type]
    seasonal_discount = seasonal_discounts[seasonal_month]["discount"]
    
    standard_products = # Write a filter function here to get products with standard VAT
    reduced_products = # Write a filter function here to get products with reduced VAT
    
    standard_final_prices = # Write a map function here to compute final prices for standard_products
    reduced_final_prices = # Write a map function here to compute final prices for reduced_products

    return standard_final_prices + reduced_final_prices

# 4. Let's create a set comprehension that outputs all product categories that have final prices above EUR500 in a country for golden members in February with an additional flat discount of EUR10. We also want to use closures and partial application where possible.
def expensive_categories(country):
    name = lambda x: x[0]
    category = lambda x: x[1]
    price = lambda x: x[2]

    member_discount = members["golden"]
    seasonal_discount = lambda x: seasonal_discounts[x]["discount"]
    additional_flat_discount = 10

    # Create a partial function for calculating final prices in Germany for golden members during holiday season with an additional flat discount of EUR10
    f = # Write your code here
    
    # Compare the above to an equivalent lambda function:
    f = lambda product_price: calculate_final_price_standard(product_price, country, member_discount,  seasonal_discount("February"), additional_flat_discount)

    # Use a set comprehension to get all categories with final prices above EUR500
    expensive_categories = # Write a set comprehension here to get categories with final prices above EUR500

    return expensive_categories

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input arguments for the expensive category check.")
    parser.add_argument("country", type=str, default="Germany", help="Country name")
    # parser.add_argument("member_type", type=str, default="golden", help="Member type (golden, silver, bronze)")
    # parser.add_argument("seasonal_discount", type=str, default="January", help="Seasonal discount month")
    # parser.add_argument("additional_flat_discount", type=float, default=10.0, help="Additional flat discount in EUR")
    args = parser.parse_args() 
    
    print(expensive_categories(args.country))

    # Example usage:
    # python HW_module1_part2_iterators_advanced.py "Germany"

