#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=17:00:00
#PBS -o drift_a.out
#PBS -N drift_a


module load python/3.4.0a1 

python3.4 $HOME/drift_hydra.py
