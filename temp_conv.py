convert = input('What temperature units you want to convert: Celsius -> Fahrenheit or Fahrenheit -> Celsius: ')


def temp_converter(convert):
    conv = convert
    if conv == 'Fahrenheit':
        temp_f = input('Temperature in Fahrenheit: ')

        def f_to_c(temp_f):
            c_temp = (int(temp_f) - 32) * 5 / 9
            return c_temp

        f_in_celsius = f_to_c(temp_f)
        print(f_in_celsius)

    if conv == 'Celsius':
        temp_c = input('Temperature in Celsius: ')

        def c_to_f(temp_c):
            f_temp = int(temp_c) * (9 / 5) + 32
            return f_temp

        c_in_fahrenheit = c_to_f(temp_c)
        print(c_in_fahrenheit)

    return f'Conversion completed from {conv}'


print(temp_converter(convert))