tp_env = "Null"
fp_env = "Null"
fn_env = "Null"

err_logs = []


def input_data():
    global tp_env
    global fp_env
    global fn_env
    global err_logs

    while True:

        err_logs = []

        print(f""" exercise1 ( tp ={catch_err('tp')} , fp ={fp_env} , fn ={fn_env}) """)
        print(f""" exercise1 ( tp ={tp_env} , fp ={catch_err('fp')} , fn ={fn_env}) """)
        print(f""" exercise1 ( tp ={tp_env} , fp ={fp_env} , fn ={catch_err('fn')}) """)

        if (
            isinstance(tp_env, int)
            == True & isinstance(fp_env, int)
            == True & isinstance(fn_env, int)
            == True
        ):
            break
        else:
            if len(err_logs) == 1:
                print(f"{err_logs[0]} must be int")
            elif len(err_logs) > 1:
                noti_err = " and ".join(err_logs)
                print(noti_err)

            #ERROR: change type of err_logs to dict make it ez write logs for each errs

            elif (tp_env <= 0 | fn_env <= 0 | fp_env <= 0): print('')
            # reset vars
            tp_env = "Null"
            fp_env = "Null"
            fn_env = "Null"
            continue

    return


def catch_err(sequence_err):
    global tp_env
    global fp_env
    global fn_env
    global err_logs

    temp = input()
    try:
        convert_to_int = int(temp)

        # overwrite env vars
        if sequence_err == "tp":
            tp_env = convert_to_int
        if sequence_err == "fp":
            fp_env = convert_to_int
        if sequence_err == "fn":
            fn_env = convert_to_int

        return convert_to_int

    except:
        err_logs.append(sequence_err)
        return temp
    return


input_data()

print(tp_env)
print(fp_env)
print(fn_env)
print(err_logs)
# if (isinstance('null', int) == True): print('dung ma')


def calc_precision():

    return


def calc_recall():

    return


def calc_f1_scrs():

    return
