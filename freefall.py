# Author: Pak Lim
# Date: Jan 19, 2018
# Code to generate sudeo experiment 
# Experiment: Five measurement of time on free fall metal ball

import numpy as np
import random
from datetime import datetime
random.seed(datetime.now())

y0 = 0.3
Nstep = 50

g = 9.81
del_y = 0.005
y_min = y0-del_y
N_y = 2*del_y/Nstep

file = open("testrun.txt","w")
for i in range(5):
    k = random.randint(1,Nstep)
    y_est = y_min + k*N_y
    del_t = np.sqrt(2*y_est/g)

    print("step= ", i, " rand.num= ", k, "   del_t = ", del_t)
    file.write('%.4f' % del_t )
    file.write("\n")
file.close()
