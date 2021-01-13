# This SLURM submission script counts sample configurations without conditioning on an outgroup. It implements 'count_sample_confs_per_ind_TT.py' for all
# 22 autosomes, and for as many pairwise individual comparisons as you choose.
# 'Ind1' is a keyword for the full vcf filenames and paths, and is assigned in 'get_file_name.py'.
# In the example below, jobs will be submitted to count sample configurations for 3 pairwise comparisons: Ind1 vs Ind2, Ind1 vs Ind3, Ind2 vs Ind3.

declare -a ind_1=(Ind1 Ind2 Ind3)
declare -a ind_2=(Ind1 Ind2 Ind3)

for chr in {1..22}; do
    for (( i = 0; i < ${#ind_1[@]}; ++i )); do
        for (( j = i+1; j < ${#ind_2[@]}; ++j )); do
	    (echo '#!/bin/bash -l'
echo "python count_sample_confs_per_ind_TT.py ${chr} ${ind_1[i]} ${ind_2[j]}
exit 0") | sbatch -p core -t 4-00:00:00 -A snic2021-01 -J ${chr}_${ind_1[i]}_${ind_2[j]} -e DIR_error/${chr}_${ind_1[i]}_${ind_2[j]}.error
done
done
done


