import random
import math


def export_process(predict, target, loss_name, sample, loss):
    print(
        f"loss name: {loss_name}, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}"
    )
    return


def create_predict_loss():
    predict = random.uniform(0, 10)
    target = random.uniform(0, 10)
    return {"predict": predict, "target": target}


def calc_MAE(n):
    count_Top = 0
    for i in range(n):
        x_i = create_predict_loss()
        count_Top += abs(x_i.get("target") - x_i.get("predict"))

        export_process(
            predict=x_i.get("predict"),
            target=x_i.get("target"),
            loss_name="MAE",
            sample=i,
            loss=count_Top / (i + 1),
        )
    print(f"final MAE: {count_Top/n}")
    return


def calc_MSE():
    count_Top = 0
    for i in range(n):
        x_i = create_predict_loss()
        count_Top += (x_i.get("target") - x_i.get("predict")) ** 2

        export_process(
            predict=x_i.get("predict"),
            target=x_i.get("target"),
            loss_name="MSE",
            sample=i,
            loss=count_Top / (i + 1),
        )
    print(f"final MSE: {count_Top/n}")
    return


def calc_RMSE(n):
    count_Top = 0
    for i in range(n):
        x_i = create_predict_loss()
        count_Top += (x_i.get("target") - x_i.get("predict")) ** 2

        export_process(
            predict=x_i.get("predict"),
            target=x_i.get("target"),
            loss_name="MSE",
            sample=i,
            loss=count_Top / (i + 1),
        )

    print(f"final RMSE: {math.sqrt(count_Top/n)}")
    return
