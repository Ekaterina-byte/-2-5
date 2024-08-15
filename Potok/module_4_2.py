def test_function():
    def inner_function():
        def print_function():
            print('Я в области видимости функции test_function')
        print(print_function())
    inner_function()
test_function()






