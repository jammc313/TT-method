def get_group_name_dict():
    b_dict={'Mbuti':[]}
    b_dict['Mbuti'].append(('Mbuti1','Mbuti1.AllSites.A3.vqsred_chr.vcf.gz'))
    b_dict['Mbuti'].append(('Mbuti2','Mbuti2.AllSites.A3.vqsred_chr.vcf.gz'))

    b_dict.update({'French':[]})
    b_dict['French'].append(('French1','French1.AllSites.A3.vqsred_chr.vcf.gz'))
    b_dict['French'].append(('French2','French2.AllSites.A3.vqsred_chr.vcf.gz'))

    b_dict.update({'Papuan':[]})	
    b_dict['Papuan'].append(('Papuan1','Papuan1.AllSites.A3.vqsred_chr.vcf.gz'))
    b_dict['Papuan'].append(('Papuan2','Papuan2.AllSites.A3.vqsred_chr.vcf.gz'))
    
    b_dict.update({'Archaic':[]})       
    b_dict['Archaic'].append(('Neanderthal','AltaiNea.hg19_1000g.dq.bqual.RG.realn-snpAD_chr.vcf.gz'))
    b_dict['Archaic'].append(('Denisovan','T_hg19_1000g.bqual.RG.realn-snpAD_chr.vcf.gz'))
    
    b_dict.update({'BaalitoBay':[]})    
    b_dict['BaalitoBay'].append(('baa001','baa001-dr_90perc_libr_160609.merge.hs37d5.fa.bqual.RG.realn.UG.recode_chr.vcf.gz'))
    
    return b_dict

def get_name_file_dict():
    a_dict=get_group_name_dict()
    b_dict={}
    for x in a_dict.keys():
        for a_tuple in a_dict[x]:
            b_dict.update({a_tuple[0]:a_tuple[1]})
            #b_dict.update({a_tuple[0]+'_'+x:a_tuple[1]})
    return b_dict


if __name__=='__main__':
    a_dict=get_name_file_dict()
    for x in a_dict.keys():
        print(x,a_dict[x])
