import math

elu_data_env = []

def calc_elu(list_data):
    global elu_data_env

    for x in list_data:
        if (x <= 0):
            temp = 0.01*(math.e**x-1)
            elu_data_env.append(temp)
        else:
            relu_data_env.append(x)

    return elu_data_env
