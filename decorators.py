def outer_function():
    message = 'hii'

    def inner_function():
        print(message)

    return inner_function()

outer_function()
 