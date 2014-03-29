#!/bin/bash -l 

qsub coev_c_2000.bash  
qsub coev_c_4000.bash  
qsub coev_c_3000.bash  
qsub coev_c_5000.bash  
qsub drift_c_2000.bash  
qsub drift_c_4000.bash  
qsub drift_c_3000.bash  
qsub drift_c_5000.bash
qsub hetero_c_2000.bash
qsub hetero_c_3000.bash
qsub hetero_c_4000.bash
qsub hetero_c_5000.bash