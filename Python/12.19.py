name = input('Введите ваше ФИО:  ')

def print_msg(msg):
    """This is the outer enclosing function"""
    def printer():
        """This is the nested function"""
        print(msg, name)

    return printer  

Hi = print_msg("Здравствуйте, студент")
bb = print_msg("До свидания, студент")

Hi()
bb()
