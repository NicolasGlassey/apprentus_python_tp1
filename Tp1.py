import math


class Tp1:
    # region Bonus

    """
    This method is designed to gets the sum of 2 numbers
    @:param number1:
    @:param number2:
    @:return : sum of number1 and number2
    """

    def add(self, number1, number2):
        return number1 + number2

    """
    This method is designed to gets the subtract a number to another one
    @:param number1: 
    @:param number2: 
    @:return : the result of number1 - number2
    """

    def subtract(self, number1, number2):
        return number1 - number2

    """
    This method is designed to gets the average a 3 numbers
    @:param number1 : 
    @:param number2 : 
    @:param number3 : 
    @:return : the average
    """

    def average(self, numbers):
        return sum(numbers) / len(numbers)

    """
    This method is designed to gets the triple of a number
    @:param number: integer to triple
    @:return : number * 3
    """

    # endregion Bonus

    def triple(self, number):
        return number * 3

    """
    This method is designed to test if a number is peer
    @:param number1 : number to test
    @:return : true if the number is peer. false in all other cases.
    """

    def is_peer(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

    """
    This method is designed to realize multiplications
    @:param multiplier :
    @:param multiplicand:
    @:return : the multiplication's result
    """

    def multiply(self, multiplier, multiplicand):
        return multiplier * multiplicand

    """
    This method is designed to generate a list of peer number
    @:param range_upper_limit :
    @:return a list of peer numbers (from 0 to range_upper_limit)
    https://www.w3schools.com/python/python_lists.asp
    """

    def unpair_range(self, range_upper_limit):
        list_of_numbers = []
        for current_number in range(1, range_upper_limit):
            if not self.is_peer(current_number):
                list_of_numbers.append(current_number)
        return list_of_numbers
    """
    This method is designed to generate a list of pair, triplied
    @:param range_upper_limit :
    @:return a list of peer numbers triplied (from 0 to range_upper_limit)
    https://www.w3schools.com/python/python_lists.asp
    """

    def triple_range(self, range_upper_limit):
        list_of_triple_range = []
        for number in range(1, range_upper_limit):
            # TODO - Bug fix
            self.multiply(number, 3)
            list_of_triple_range.append(number)
        return list_of_triple_range

    """
    This method is designed to get the factorial of a number
    @:param number :
    @:return the factorial of a number
    """

    def factorial(self, number):
        return math.factorial(number)


    """
    This method is designed to convert a list of number in a list of number and boolean (true, false if peer)
    @:param list of numbers : sample (1, 4, 3, 7)
    @:return the list : sample ((1, False), (4, True), (3, False), (7, False))
    https://www.programiz.com/python-programming/tuple
    """

    def integer_to_boolean(self, numbers):
        list_of_tuples = []
        for single_number in numbers:
            if single_number % 2 == 0:
                list_of_tuples.append((single_number, True))
            else:
                list_of_tuples.append((single_number, False))
        return list_of_tuples


    """
    This method is designed to get the population's average by city
    @:param cities : sample ('Zürich', 409241), ('Genève', 200548), ('Basel', 171513), ('Bern', 133798)
    @:return population average by city : sample 210801
    https://www.programiz.com/python-programming/tuple
    """

    def population_average_by_city(self, cities):
        # TODO - Camel case... 
        list_of_Populations = []
        for single_tuple in cities:
            list_of_Populations.append(single_tuple[1])
        return sum(list_of_Populations)/len(list_of_Populations)

    """
    This method is designed to find a first bigger value from a minimal in a given list
    @:param numbers : sample [7, 1, 4, 0]
    @:param min_value : sample 3
    @:return either the value found (sample : 4), or "None"
    https://www.programiz.com/python-programming/tuple
    """

    def find_value_bigger_than_minimal(self, numbers, min_value):
        # sort the list https://www.programiz.com/python-programming/methods/list/sort

        # loop on each list's item and find the next value bigger than the min_value

        raise Exception
