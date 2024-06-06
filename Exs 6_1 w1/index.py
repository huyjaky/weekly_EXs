import relu
import sigmoid

data_env = []


def input_data():
    global data_env

    # loop 1: input dimension data
    while True:
        try:

            dimension_data = int(input("Enter dimension list: "))

            count_loop2 = 0
            # loop 2: append data to list
            while True:
                for i in range(dimension_data):
                    try:
                        temp = float(input(f"location {i+1}: "))
                        data_env.append(temp)
                        
                        # end loops condition
                        if count_loop2 == dimension_data-1:
                            return
                        count_loop2 += 1

                    except:
                        print("input must float or int")
                        continue

        except:
            print("input must int")
            continue


input_data()

print(f'relu {relu.calc(data_env)}')
print(f'sigmoid {sigmoid.calc(data_env)}')
