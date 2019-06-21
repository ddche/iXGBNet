from dream5.iXGBNet_dream5 import *
import pandas as pd

# for i in [1,3]:
#     # Read data
#     file_ss = "data/steadystate_data/dream5_net{}_steadystate.csv".format(i)
#     data_ss = pd.read_csv(file_ss).to_numpy()
#
#     # Compute weights of gene regulatory network
#     vv = main(data_ss, 1000)
#
#     # Export result
#     df = pd.DataFrame(vv)
#     df.to_csv("result/dream5_d{}.csv".format(i), index=False)

from  scipy.io  import loadmat
# d = loadmat('net1_VIM_0621.mat')
# d1 = d['VIM1']
# df = pd.DataFrame(d1)
# df.to_csv("result/dream5_d1.csv", index=False)

d = loadmat('net3_VIM_0621.mat')
d3 = d['VIM3']
df = pd.DataFrame(d3)
df.to_csv("result/dream5_d3.csv", index=False)