class Tp1:
    """
    This method is designed to gets the triple of a number
    @:param operand: integer to triple
    @:return : operand * 3
    """
    def triple(self, operand):
        return operand * 3


    """
    This method is designed to test if a number is divisible by two
    @:param operand : integer to test
    @:return : true it's divisible. In all other case, false
    """
    def is_peer(self, operand):
        if operand % 2 == 0:
            return True
        else:
            return False
