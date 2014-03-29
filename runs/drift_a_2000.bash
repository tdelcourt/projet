#!/bin/bash -l

#PBS -l nodes=1:ppn=1

#PBS -o drift_a_2000.out
#PBS -N drift_a_2000


module load python/3.4.0a1 

python3.4 $HOME/drift_hydra_2000.py
