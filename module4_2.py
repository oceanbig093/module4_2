def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
inner_function() #не вызывается, так как находится только в области видимости функции тест