class Documentation:

    def inputMethod(self):
        """
        The input() function allows a user to insert a value into a program.
        input() returns a string value. You can convert the contents of an input using any data type.
        This example takes the email from the user and return it."""
        email = input("Enter your email address: ")
        print("To confirm, is your email address:", email)

    print(inputMethod.__doc__)

    def __abs__(self):
        """
        The abs() function returns the absolute value of the given number.
        If the number is a complex number, abs() returns its magnitude.


        abs() method takes a single argument:

        num - a number whose absolute value is to be returned. The number can be:
        - integer
        - floating number
        - complex number


        In this example, we have convert -20 to his absolute means 20.
        """
        number = -20
        absolute_number = abs(number)
        print(absolute_number)

    print(__abs__.__doc__)

    def __int__(self):
        """
        The int() method can be used to convert a string to an integer value in Python.

        int() takes in two parameters: the string to convert into an integer and the base you want your data to be
        represented in. The second parameter is optional.
        In this example, we have convert a string into a int and check the result with type method.
        """
        stringTest = "test"
        print(type(stringTest))
        stringConvertToInt = int(stringTest)
        print(type(stringConvertToInt))

    print(__int__.__doc__)
