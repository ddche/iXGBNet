from dream5.iXGBNet_dream5 import *
import pandas as pd

for i in [1,3]:
    # Read data
    file_tm = "data/steadystate_data/dream5_net{}_steadystate.csv".format(i)
    tm = pd.read_csv(file_tm).to_numpy()
    file_ko = "data/knockout_data/dream5_net{}_knockout.csv".format(i)
    ko = pd.read_csv(file_ko).to_numpy()

    # Compute weights of gene regulatory network
    # vv = main(tm, 10, 2, 0.45, 1000, ko)

    # Export result
    df = pd.DataFrame(ko)
    df.to_csv("result/dream5_d{}.csv".format(i), index=False)

