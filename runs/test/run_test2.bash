#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:10:00
#PBS -o ./data/test2.out
#PBS -N test2

# echo "Running job on $HOST - " `date` 
# echo "prout"
# run_prog -tmp $TMPDIR -in $HOME/my_input -out $WORKDIR/my_output 


# cd $TMPDIR

module load python/3.4.0a1 

python3.4 $HOME/coev_hydra.py 
#-out $TMPDIR/test2
# cd $TMPDIR
# gzip test2.out

# mv ./test2.out.gz $HOME/

# CLeanup my temporary space:

# Make sure that I am still in my temporary space:

# cd $TMPDIR 
# echo "Done"
# Delete everything

#/bin/rm -r *