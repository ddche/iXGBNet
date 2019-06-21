from dream4.iXGBNet_dream4 import *
import pandas as pd

# for i in range(1, 2):
#     # Read data
#     file_tm = "data/timeseries_data/insilico_size100_{}_timeseries.csv".format(i)
#     tm = pd.read_csv(file_tm).to_numpy()
#     file_ko = "data/knockout_data/insilico_size100_{}_knockout.csv".format(i)
#     ko = pd.read_csv(file_ko).to_numpy()
#
#     # Compute weights of gene regulatory network
#     vv = main(tm, 10, 2, 0.45, 1000, ko)
#
#     # Export result
#     df = pd.DataFrame(vv)
#     df.to_csv("result/dream4_d{}.csv".format(i), index=False)
from scipy.io import loadmat

n = loadmat('data/dream4_zscore.mat')
# n = loadmat('/home/cdd/share/xgb/dream4_zscore.mat')
d1 = n['nn1']
d2 = n['nn2']
d3 = n['nn3']
d4 = n['nn4']
d5 = n['nn5']
# print(type(d1))


# Export the matrix of weigths
# df1 = pd.DataFrame(d1)
# df1.to_csv("/home/cdd/share/xgb/dream5_net1.csv", index=False)  # 按指定列名顺序输出df
#
# df3 = pd.DataFrame(d3)
# df3.to_csv('/home/cdd/share/xgb/dream5_net3.csv', index=False)
#
# df4 = pd.DataFrame(d4)
# df4.to_csv('/home/cdd/share/xgb/dream5_net4.cav', index=False)
