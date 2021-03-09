#!/bin/bash
#SBATCH -c 1
#SBATCH --mem=0
#SBATCH --time=800:00
#SBATCH --account=def-gale

cd /project/def-gale/paquet/smash_photons/rhic_final_hydros/photons_T140-150_nx200_before1fm

icpc -O3 photon.cpp rates.cpp

time ./a.out
