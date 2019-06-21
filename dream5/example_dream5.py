from dream5.iXGBNet_dream5 import *
import pandas as pd

for i in [1,3]:
    # Read data
    file_ss = "data/steadystate_data/dream5_net{}_steadystate.csv".format(i)
    data_ss = pd.read_csv(file_ss).to_numpy()

    # Compute weights of gene regulatory network
    vv = main(data_ss, 1000)

    # Export result
    df = pd.DataFrame(vv)
    df.to_csv("result/dream5_d{}.csv".format(i), index=False)

