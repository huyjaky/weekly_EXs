import md_nre

def input_data():
    # WARNING: im pretty lazy so i did not do check 
    input_y = float(input('enter y: '))
    input_y_hat = float(input('enter y^: '))
    input_n = int(input ('enter n: '))
    input_p = int(input ('enter p: '))

    print(f'md_nre_single_sample ( y ={input_y} , y_hat ={input_y_hat} , n ={input_n} , p ={input_p})')
    print(md_nre.calc(y=input_y, y_hat=input_y_hat, n=input_n, p=input_p))

input_data()
