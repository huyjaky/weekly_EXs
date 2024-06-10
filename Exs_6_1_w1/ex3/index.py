import is_number
import loss


def input_data():
    while True:

        num_samples = input(
            "Input number of samples ( integer number ) which are generated : "
        )

        if is_number.calc(num_samples, is_int=True) == False:
            print("number of samples must int")
            continue

        num_samples = int(num_samples)

        loss_name = input("Input loss name (MAE | MSE | RMSE) :")

        if (loss_name == 'MAE'): loss.calc_MAE(num_samples)
        elif (loss_name == 'MSE'): loss.calc_MSE(num_samples)
        elif (loss_name == 'RMSE'): loss.calc_RMSE(num_samples)
        else:
            print('loss method not supported')
            continue

input_data()