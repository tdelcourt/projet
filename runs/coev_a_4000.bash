#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=120:00:00
#PBS -o coev_a_4000.out
#PBS -N coev_a

module load python/3.4.0a1 

python3.4 $HOME/coev_hydra_4000.py 
