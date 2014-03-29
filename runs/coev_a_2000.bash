#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=60:00:00
#PBS -o coev_a_2000.out
#PBS -N coev_a

module load python/3.4.0a1 

python3.4 $HOME/coev_hydra_2000.py 
