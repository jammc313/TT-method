def filter_list(g,n,a_list,site_counts):
    b_list=[]
    b_snps=[]
    num_rem_wins=0
    num_rem_snps=0
    for i in range(g):
        a_count=site_counts[i]
        try:
            b_list.append(1.0*float(a_list[i]))
            b_snps.append(a_count)
        except:
            num_rem_wins+=1
            num_rem_snps+=a_count
    return [g-num_rem_wins,n-num_rem_snps,b_list,b_snps]



#######REQUIRES NO SECTIONS WITH NO SNPs ARE USED
#######'snp_counts' ARE THE NUMBER OF SNPs REMOVED FOR EACH JACK KNIFE CALCULATION
def get_WBJ_mean_var(g,n,obs_mean,a_list,site_counts):
    a_mean=0
    if obs_mean=='NA':
        return ('NA','NA','NA')
    else:
        obs_mean=1.0*float(obs_mean)
        #print  'BEFORE',[g,n,a_list,site_counts]
        [g,n,a_list,site_counts]=filter_list(g,n,a_list,site_counts)
        #print  'AFTER',[g,n,a_list,site_counts]
        for i in range(g):
            a_count=1.0*site_counts[i]
            a_term=1.0-1.0*(a_count/n)
            a_mean+=a_term*a_list[i]
        a_mean=g*obs_mean-a_mean
        a_var=0
        for i in range(g):
            a_count=1.0*site_counts[i]
            hj=1.0*n/a_count
            a_term=hj*obs_mean-(hj-1.0)*a_list[i]-a_mean
            a_var+=a_term*a_term/(hj-1.0)
        a_var=a_var/g
        return (str(obs_mean),str(a_mean),str(a_var))





