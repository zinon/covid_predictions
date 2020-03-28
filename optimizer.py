

import numpy as np
import proc as xp
import optparam as op
import prophet_trainer as pt

ds = xp.DataLoader().train_ds_confirmed
tb = xp.DataLoader().table
floor_points = [0, 10e3, 20e3, 50e3]
cap_lower = 800e3
cap_upper = 1200e3
cap_step = 100e3
cap_benchpoints = np.arange(cap_lower,
                            cap_upper+1,
                            cap_step).tolist()
seasonality_modes = ['multiplicative', 'additive']
future_periods = [21]
#changepoint_prior_scales = [0.05, 0.1, 0.5]
changepoint_prior_scales = [0.05]
interval_widths = [0.90, 0.95]

print("Logistic scan points:", cap_benchpoints)

#create set of params
optparams = []
for cap in cap_benchpoints:
    for floor in floor_points:
        for smode in seasonality_modes:
            for periods in future_periods:
                for cpps in changepoint_prior_scales:
                    for iw in interval_widths:
                        p = op.Param(rmse = 0.,
                                     floor = floor,
                                     cap = cap,
                                     smode = smode,
                                     periods = periods,
                                     cpps = cpps,
                                     iw = iw)
                    optparams.append( p )

trains = []
for op in optparams:
    trains.append( pt.ProphetTrainer(op, ds, tb) )

trains.sort(key=lambda x : x.param.rmse, reverse=False)   

for t in trains:
    print(t.param)

#print("Best params:", optparams[0])
