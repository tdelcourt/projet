#!/bin/bash -l 

qsub coev_b_2000.bash  
qsub coev_b_4000.bash  
qsub coev_b_3000.bash  
qsub coev_b_5000.bash  
qsub drift_b_2000.bash  
qsub drift_b_4000.bash  
qsub drift_b_3000.bash  
qsub drift_b_5000.bash
qsub hetero_b_2000.bash
qsub hetero_b_3000.bash
qsub hetero_b_4000.bash
qsub hetero_b_5000.bash