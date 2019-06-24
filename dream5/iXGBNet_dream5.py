import numpy as np
import xgboost as xgb
import operator
import re
import math
import time

def main(data_ss, iter_num):
    """
    Inferring gene regulatory networks (GRNs) from gene expression data using an integrative XGBoost-based method.

    Args:

        data_ss: Steady-state experimental data.
        iter_num: Number of iterations in XGBoost model.

    Returns:

        vim: A matrix recording the weights of regulatory network.

    """
    time_start = time.time()

    # Compute the weights of gene regulatory network using XGBoost.
    feature_num = np.shape(data_ss)[1]
    vv = xgboost_weight(data_ss, feature_num, iter_num)
    vv = np.transpose(vv)

    # Normalize inferred GRN matrix by row with L2-norm method.
    vim = normalized_l2norm(vv)

    # Use a statistical technology to refine the inferred GRN.
    statis = statistical_method(vim)
    vim = vim * statis

    # Compute the running time
    time_end = time.time()
    print('totally cost', time_end - time_start)

    return vim


def xgboost_weight(data, subprob_num, iter_num):
    """
    Compute the weights of gene regulatory network using XGBoost.

    Args:

        data: Experimental data.
        subprob_num: Number of subproblems.
        iter_num: Number of iterations.

    Returns:

        vim: The matrix recording the weights of regulatory network after using XGBoost.

    """

    vim = np.zeros((data.shape[1], subprob_num)).tolist()  # vim: weights of Regulatory network
    for i in range(0, data.shape[1]):
        print("----------------------------------------------------------------", i,
              "----------------------------------------------------------------")

        # split train and test data set
        y = data[:, i]
        if i == 0:
            x = data[:, 1:subprob_num]
        elif i < subprob_num:
            x = np.hstack((data[:, 0:i], data[:, i + 1:subprob_num]))
        else:
            x = data[:, 0:subprob_num]

        # Build model
        params = {

            'booster': 'gbtree',
            'gamma': 0.2,
            'max_depth': 4,
            'min_child_weight': 4,
            'lambda': 1,
            'subsample': 0.7,
            'colsample_bytree': 0.9,
            'silent': 1,
            'eta': 0.0008
        }

        dtrain = xgb.DMatrix(x, y)
        plst = params.items()
        model = xgb.train(plst, dtrain, iter_num)

        # Compute and sort feature importance
        importance = model.get_fscore()
        importance = sorted(importance.items(), key=operator.itemgetter(1), reverse=True)

        # Convert the importance list to matrix weights
        for j in range(0, len(importance)):
            num = re.findall(r'\d+', importance[j][0])
            num = np.array(num)
            num = np.core.defchararray.strip(num, '()')
            num = int(num)
            if i >= subprob_num - 1:
                fea_num = num
            else:
                if num < i:
                    fea_num = num
                else:
                    fea_num = num + 1
            vim[i][fea_num] = importance[j][1]

    return vim


def normalized_l2norm(x):
    # Normalize matrix by row with L2-norm method.
    n = np.shape(x)[0]
    y = np.power(x, 2)
    w = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            x_sum = sum(y[i, :])
            w[i, j] = y[i, j] / math.sqrt(x_sum)
    return w


def statistical_method(x):
    # Use a statistical technology to further refine the inferred GRN.
    n = np.shape(x)[0]
    vv = np.var(x, axis=1, ddof=1)
    w = np.zeros((n, n))
    for i in range(n):
        w[i, :] = vv[i]
    return w