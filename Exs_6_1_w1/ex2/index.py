import relu
import sigmoid
import is_number
import elu

data_env = []


def input_data():
    global data_env

    # NOTE: loop 1: input dimension data
    while True:
        dimension_data = input("Enter dimension list: ")

        if is_number.calc(dimension_data, is_int=True) == False:
            print("input must int")
            continue

        # NOTE: loop 2: append data to list
        for i in range(int(dimension_data)):

            # catching err point until user enter right data
            while True:
                temp = input(f"location {i+1}: ")

                if is_number.calc(temp) == False:
                    print("input must float or int")
                else:
                    data_env.append(float(temp))
                    break
        return


input_data()


def export_result():
    while True:
        user_choice = input(
            """Input activation Function ( sigmoid*1 | relu*2 | elu*3 ) : """
        )
        if user_choice == "sigmoid" or user_choice == "1":
            print(f"sigmoid {sigmoid.calc(data_env)}") 
            break
        if user_choice == "relu" or user_choice == "2":
            print(f"sigmoid {relu.calc(data_env)}")
            break
        if user_choice == "elu" or user_choice == "3":
            print(f"sigmoid {elu.calc(data_env)}")
            break
        print(f'{user_choice} is not supportted')
