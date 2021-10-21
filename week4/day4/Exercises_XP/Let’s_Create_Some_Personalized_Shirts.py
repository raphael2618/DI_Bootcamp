def make_shirt(size, message):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')


def make_shirt(size='large', message='I love Python!'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
