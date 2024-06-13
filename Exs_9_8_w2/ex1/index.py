import is_number
import node


def calc_max_in_window(head, tail, lst_data):
    return max(lst_data[head:tail])


def move_window(window_size, lst_data):
    lst_result = []
    current_position = 0

    # HACK: loop until we not enough data to find
    while current_position + window_size - 1 < len(lst_data):

        lst_result.append(
            calc_max_in_window(
                current_position, current_position + window_size, lst_data=lst_data
            )
        )
        current_position += 1

    print(lst_result)


def input_data():
    lst_data = []

    # NOTE: verified input
    dimension_ll = input("Enter Dimension LL: ")

    if is_number.calc(dimension_ll, is_int=True) == False:
        print("Dimension must int")
        return

    window_size = input("Enter Window Size: ")

    if is_number.calc(window_size, is_int=True) == False:
        print("window size must int")
        return

    # NOTE: convert type of input data
    dimension_ll = int(dimension_ll)
    window_size = int(window_size)

    countdown = dimension_ll
    while countdown != 0:
        temp = input("Enter Data: ")

        if is_number.calc(temp) == False:
            print("Data must float or int")
            continue

        lst_data.append(float(temp))
        countdown -= 1
    move_window(window_size=window_size, lst_data=lst_data)


input_data()
