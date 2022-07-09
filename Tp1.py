class Tp1:
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
    This method is designed to gets the triple of a number
    @:param number: integer to triple
    @:return : number * 3
    """

    def triple(self, number):
        return number * 3

    """
    This method is designed to gets the average a 3 numbers
    @:param number1 : 
    @:param number2 : 
    @:param number3 : 
    @:return : the average
    """

    def average(self, number1, number2, number3):
        return (number1 + number2 + number3) / 3

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
