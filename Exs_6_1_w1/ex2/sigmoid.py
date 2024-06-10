import math

sigmoid_data_env = []

def calc(list_data):
    global sigmoid_data_env

    for x in list_data:
        x_temp = float(x)
        sigmoid_data_env.append(1 / (1 + math.e**(-x_temp) ))

    return sigmoid_data_env