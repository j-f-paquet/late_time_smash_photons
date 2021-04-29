#!/bin/bash
#SBATCH -c 1
#SBATCH --mem=0
#SBATCH --time=8000:00
#SBATCH --account=def-gale

cd /project/def-gale/paquet/smash_photons/rhic_final_hydros/photons_T110-150_nx200_before10fm

icpc -O3 photon.cpp rates.cpp

time ./a.out
