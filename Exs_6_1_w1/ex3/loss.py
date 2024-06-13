import random
import math


def export_process(predict, target, loss_name, sample, loss):
    print(
        f"loss name: {loss_name}, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}"
    )


def create_predict_loss():
    predict = random.uniform(0, 10)
    target = random.uniform(0, 10)
    return {"predict": predict, "target": target}


def calc_mae(n):
    count_top = 0
    for i in range(n):
        x_i = create_predict_loss()
        temp = abs(x_i.get("target") - x_i.get("predict"))
        count_top += temp

        export_process(
            predict=x_i.get("predict"),
            target=x_i.get("target"),
            loss_name="MAE",
            sample=i,
            loss=temp,
        )
    print(f"final MAE: {count_top/n}")


def calc_mse(n):
    count_top = 0
    for i in range(n):
        x_i = create_predict_loss()
        temp = (x_i.get("target") - x_i.get("predict")) ** 2
        count_top += temp

        export_process(
            predict=x_i.get("predict"),
            target=x_i.get("target"),
            loss_name="MSE",
            sample=i,
            loss=temp,
        )
    print(f"final MSE: {count_top/n}")


def calc_rmse(n):
    count_top = 0
    for i in range(n):
        x_i = create_predict_loss()
        temp = (x_i.get("target") - x_i.get("predict")) ** 2
        count_top += temp

        export_process(
            predict=x_i.get("predict"),
            target=x_i.get("target"),
            loss_name="MSE",
            sample=i,
            loss=temp,
        )

    print(f"final RMSE: {math.sqrt(count_top/n)}")

calc_mae(2)

