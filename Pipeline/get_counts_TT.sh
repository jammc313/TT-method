# This SLURM submission script counts sample configurations without conditioning on an outgroup. It implements 'count_sample_confs_per_ind_TT.py' for all
# 22 autosomes, and for as many pairwise individual comparisons as you choose.
# 'Ind' is a keyword representing the full vcf filenames and paths, which is assigned by the USER in 'get_file_name.py'.
# In the example below, jobs will be submitted to count sample configurations for 3 pairwise comparisons: Ind1 vs Ind2, Ind1 vs Ind3, Ind2 vs Ind3.

declare -a ind=(Ind1 Ind2 Ind3)

for chr in {1..22}; do
    for (( i = 0; i < ${#ind[@]}; ++i )); do
        for (( j = i+1; j < ${#ind[@]}; ++j )); do
	    (echo '#!/bin/bash -l'
echo "python count_sample_confs_per_ind_TT.py ${chr} ${ind[i]} ${ind[j]}
exit 0") | sbatch -p core -t 1-00:00:00 -A snic2021-01 -J ${chr}_${ind[i]}_${ind[j]} -e DIR_error/${chr}_${ind[i]}_${ind[j]}.error
done
done
done


