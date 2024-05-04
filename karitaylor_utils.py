''' Module 1 - This module provides a reusable byline for the author's services. '''

# Import Dependencies
import statistics


def main():

    # Define Variables
    company_name: str = 'Designs by KB Designs'
    company_description: str = 'Small town t-shirt business'
    number_of_employees: int = 2
    has_etsy_store: bool = True
    average_etsy_rating: float = 4.8 
    etsy_rating_list: list = [4.0, 5.0, 5.0, 5.0, 5.0]
    physical_items_offered: list = ['short sleeve', 'long sleeve',     'sweatshirts', 'hoodies']
    offers_free_shipping: bool = False
    digital_forms_offered: list = ['svg', 'png', 'eps', 'dxf']

    # Calculate Descriptive Statistics
    smallest = min(etsy_rating_list)
    largest = max(etsy_rating_list)
    total = sum(etsy_rating_list)
    number_of_reviews = len(etsy_rating_list)
    mean = statistics.mean(etsy_rating_list)
    median = statistics.median(etsy_rating_list)
    mode = statistics.mode(etsy_rating_list)
    SD = statistics.stdev(etsy_rating_list)

    # Define Formatted Strings
    employee_number_string: str = f"Number of Employees: {number_of_employees}"
    etsy_store_string: str = f"Etsy Store: {has_etsy_store}"
    etsy_rating_string: str = f"Average Etsy Rating: {average_etsy_rating}"
    free_shipping_string: str = f"Free Shipping: {offers_free_shipping}"

    stats_string: str = f"""
        Descriptive Statistics for our Etsy Ratings:
        lowest rating: {smallest}
        highest rating: {largest}
        total: {total}
        number of reviews: {number_of_reviews}
        mean: {mean}
        median: {median}
        mode: {mode}
        standard Deviation: {SD}
        """

    # Define Byline String
    byline: str = f"""
        {company_name}
        {employee_number_string}
        {etsy_store_string}
        {etsy_rating_string}
        {free_shipping_string}
        {physical_items_offered}
        {digital_forms_offered}
        {stats_string}
        """

    print(company_name)
    print(company_description)
    print(employee_number_string)
    print(etsy_store_string)
    print(etsy_rating_string)
    print("Physical Items Offered:", physical_items_offered)
    print("Digital Forms Offered:", digital_forms_offered)
    print(stats_string)

# print(byline)

# Conditional Script Execution
if __name__ == '__main__':
    main()
