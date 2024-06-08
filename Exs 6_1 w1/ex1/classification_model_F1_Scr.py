import sigmoid
import is_number

# set up env vars
tp_env = None
fp_env = None
fn_env = None

err_logs = []

def calc_precision(tp_env, fp_env):
    return tp_env/ (tp_env + fp_env)


def calc_recall(tp_env, fn_env):
    return tp_env/ (tp_env + fn_env)


def calc_f1_scrs(calc_precision, calc_recall):
    return 2 * ((calc_precision*calc_recall) / (calc_precision + calc_recall))

def input_data():
    global tp_env
    global fp_env
    global fn_env
    global err_logs

    while True:
        # print current values and catch errs 
        print(f""" exercise1 ( tp ={catch_err('tp')} , fp ={fp_env} , fn ={fn_env}) """)
        print(f""" exercise1 ( tp ={tp_env} , fp ={catch_err('fp')} , fn ={fn_env}) """)
        print(f""" exercise1 ( tp ={tp_env} , fp ={fp_env} , fn ={catch_err('fn')}) """)

        # conditions break or continue inf loop 
        if (
            isinstance(tp_env, float)
            == True & isinstance(fp_env, float)
            == True & isinstance(fn_env, float)
            == True
        ):
            break
        else:
            
            if len(err_logs) == 1:
                print(f"{err_logs[0]} must be greater than zero")
            elif len(err_logs) > 1:
                noti_err = " and ".join(err_logs)
                print(noti_err)

            # reset env
            tp_env = "Null"
            fp_env = "Null"
            fn_env = "Null"
            err_logs = []
            continue

    return


def catch_err(sequence_err):
    global tp_env
    global fp_env
    global fn_env
    global err_logs

    while(True):
        
        temp = input(f'enter {sequence_err}: ')
        if (is_number.calc(temp) == False):
            print(f'{sequence_err} must be int')
            
        convert_to_int = float(temp)

        # overwrite env vars
        if sequence_err == "tp":
            tp_env = convert_to_int
        if sequence_err == "fp":
            fp_env = convert_to_int
        if sequence_err == "fn":
            fn_env = convert_to_int

        if (convert_to_int <= 0):
            err_logs.append(sequence_err)

        return convert_to_int

    return

input_data()

precision_env = calc_precision(tp_env=tp_env, fp_env=fp_env)
recall_env = calc_recall(tp_env=tp_env, fn_env=fn_env)
f1_scrs_env = calc_f1_scrs(calc_precision=precision_env, calc_recall=recall_env)

print(f'precision is {precision_env}')
print(f'recall is {recall_env}')
print(f'f1-score is {f1_scrs_env}')

