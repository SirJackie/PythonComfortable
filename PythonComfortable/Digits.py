class Digits:
    @staticmethod
    def NDigitsMaximum(n):
        return int("9" * n)

    @staticmethod
    def ToNDigitsString(i, n):
        return "0" * (n - len(str(i))) + str(i)
