# This SLURM submission script counts sample configurations with conditioning on an outgroup. It implements 'count_sample_confs_per_ind_TTO.py' for all
# 22 autosomes, and for as many pairwise individual comparisons as you choose.
# 'Ind' is a keyword representing the full vcf filenames and paths, and is assigned by the USER in 'get_file_name.py'.
# In the example below, jobs will be submitted to count sample configurations for 6 pairwise comparisons in total: Ind1 vs Ind2, Ind1 vs Ind3, Ind2 vs Ind3 while conditioning on each of the supplied outgroups.

declare -a ind=(Ind1 Ind2 Ind3)
declare -a ind_outgrp=(Neanderthal Denisovan)

for chr in {1..22}; do
    for (( i = 0; i < ${#ind[@]}; ++i )); do
        for (( j = i+1; j < ${#ind[@]}; ++j )); do
	        for (( k = 0; k < ${#ind_outgrp[@]}; ++k )); do
            (echo '#!/bin/bash -l'
echo "python count_sample_confs_per_ind_TTO.py ${chr} ${ind[i]} ${ind[j]} ${ind_outgrp[k]}
exit 0") | sbatch -p core -t 1-00:00:00 -A snic2021-1 -J ${chr}_${ind[i]}_${ind[j]}_${ind_outgrp[k]} -e DIR_error_TTO/${chr}_${ind[i]}_${ind[j]}_${ind_outgrp[k]}.error
done
done
done
done


