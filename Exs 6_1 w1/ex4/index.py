import is_number
import math
import trigonometry


def input_data ():
    while(True):
        input_x = input('enter x: ')

        # NOTE: i check and convert x to radians number
        if (is_number.calc(x=input_x, is_int=False)):

            input_x = math.radians(float(input_x))
        else:
            print('x must be radian')
            continue
        
        # HACK: im placing loop2 for checking n number 
        while(True):
            input_n = input('enter n: ')
            if (is_number.calc(x=input_n, is_int=True) == False):
                print('n must be int')
                continue
            else: 
                input_n = int(input_n)
                break
        
        user_choice  = input('sin | cos | sinh | cosh: ')

        if (user_choice == 'sin'): print(f'{trigonometry.calc_sin(x=input_x, n=input_n)}')
        elif (user_choice == 'cos'): print(f'{trigonometry.calc_cos(x=input_x, n=input_n)}')
        elif (user_choice == 'sinh'): print(f'{trigonometry.calc_sinh(x=input_x, n=input_n)}')
        elif (user_choice == 'cosh'): print(f'{trigonometry.calc_cosh(x=input_x, n=input_n)}') 
        else: print('not supported') 
