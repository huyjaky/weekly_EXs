relu_data_env = []

def calc(list_data):
    global relu_data_env

    for x in list_data:
        if (x <= 0):
            relu_data_env.append(0)
        else:
            relu_data_env.append(x)

    return relu_data_env
