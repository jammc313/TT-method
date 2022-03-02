import sys
import gzip
import get_file_name
from zipfile import ZipFile


def get_var_form(a_list):
    for x in a_list:
        d=x.split('=')
        if d[0]=='VariantType':
            return d[1]
    return ''

def check_if_missingness(a_list):
    for x in a_list:
        d=x.split(':')
        if d[0]=='./.':
            return 'missingness'
    return ''

def parse_var_genotypes(a_list):
    b_list=[]
    for x in a_list:
        d=x.split(':')
        if d[0]=='./.':
            return 'missingness'
        b_list.append(d[0])
    return b_list

# For vcfs produced by GATK pipeline, may need to alter depending on FORMAT field 
def get_genotype(a_list):
    b_geno=''
    coverage=0
    for x in a_list:
        d=x.split(':')
        if d[0]=='./.':
            return [0,'']
        b_geno=d[0]
        if len(d)>2:
            if d[2]=='.':
                return [0,'']
            coverage+=int(d[2])
        else:
            coverage+=int(d[1])
    return [coverage,b_geno]



def orient_and_get_count(genotype,ref_nt,alt_nt,anc_nt):
    if genotype.count('2')>0:
        print('BAD orient',genotype,ref_nt,alt_nt,anc_nt)
        input()
    if alt_nt=='.':
        if ref_nt==anc_nt:
            return 0
        else:
            return 2
    else:
        if ref_nt==anc_nt:
            return genotype.count('1')
        else:
            return genotype.count('0')


def check_if_ok_and_get_var_form(anc_nt,ref_nt1,ref_nt2,alt_nt1,alt_nt2):
    set1=set([anc_nt,ref_nt1,ref_nt2,alt_nt1,alt_nt2]).difference('.')
    if set1.issubset(nt_set):
        if len(set1)==1:
            return 'OK_NO_VARIATION'
        if len(set1)==2:
            if alt_nt1=='.' and alt_nt2=='.':
                return 'OK_NO_VARIATION'
            else:
                return 'OK_POLY'
    return ''



def get_sample_conf(der_count1,der_count2):
    if der_count1+der_count2==0:
        return 0
    if der_count1+der_count2==4:
        return 0
    if der_count1+der_count2==1:
        if der_count1==1:
            return 1
        else:
            return 2
    if der_count1+der_count2==2:
        if der_count1==2:
            return 3
        if der_count2==2:
            return 4
        else:
            return 5
    if der_count1+der_count2==3:
        if der_count1==2:
            return 6
        else:
            return 7
    print('THIS SHOULD NEVER HAPPEN')
    return 100

def check_if_pass_coverage(a_coverage,LOW_COV_THRESH,HIGH_COV_THRESH):
    if (a_coverage>LOW_COV_THRESH and a_coverage<HIGH_COV_THRESH):
        return 1
    else:
        return 0


def make_out_str(a_list):
    b_str=''
    for x in a_list:
        b_str+=str(x)+','
    return b_str[:-1]


######### User should edit file paths below to point to ancestral state files and vcfs #############
ancPath='/proj/ancestral_states'
vcf_path='/proj/allsite_vcfs'
####################################################################################################

arg_list=sys.argv
the_chr=arg_list[1]
ind1=arg_list[2]
ind2=arg_list[3]

##########################
##########################

#Get file name function to use ind1 ind2 etc
outPATH='DIR_counts_per_5cm_TT'

file_dict=get_file_name.get_name_file_dict()
vcf_file_one=vcf_path+'/'+file_dict[ind1]
vcf_fileOne=vcf_file_one.split('.vc')
vcf_file1=vcf_fileOne[0] + the_chr + '.vc' + vcf_fileOne[1]

vcf_file_two=vcf_path+'/'+file_dict[ind2]
vcf_fileTwo=vcf_file_two.split('.vc')
vcf_file2=vcf_fileTwo[0] + the_chr + '.vc' + vcf_fileTwo[1]

##########################
##########################


NUCL=['A','C','G','T']
nt_set=set(NUCL)
ANCESTRAL_FILTER=['A','C','G','T']


############################## User consider coverage thresholds to filter sites #############################
LOW_COV_THRESH=10
HIGH_COV_THRESH=500
####################################################################################################

win_start=0
win_step=5000000 #(corresponds to about 5 cM)
win_end=win_start+win_step


out_dict={(win_start,win_end):{'A':[0,0,0,0,0,0,0,0,0],'C':[0,0,0,0,0,0,0,0,0],'G':[0,0,0,0,0,0,0,0,0],'T':[0,0,0,0,0,0,0,0,0]}}


with ZipFile(ancPath+'/Ancestral_states.zip', 'r') as z:
    with z.open('Ancestral_states/chr'+the_chr+'.txt','r') as anc_file:
        with gzip.open(vcf_file1,'rt',encoding='utf-8') as myf1:
            with gzip.open(vcf_file2,'rt',encoding='utf-8') as myf2:
                l1='##'
                while l1[0]=='#':
                    l1=myf1.readline()
                l2='##'
                while l2[0]=='#':
                    l2=myf2.readline()
                anc_l=anc_file.readline()
                while l1 and l2 and anc_l:
                    vcf_data1=l1.strip().split()
                    vcf_data2=l2.strip().split()
                    anc_d=anc_l.decode('utf-8').strip().split()                      
                    vcf_pos1=vcf_data1[1]
                    vcf_pos2=vcf_data2[1]
                    anc_pos=anc_d[0]
                    
                    while not vcf_pos1 == vcf_pos2 == anc_pos:  # loop through to sync vcf and ancestral file positions. Break if end-of-file occurs.
                        if int(vcf_pos1) == min(int(vcf_pos1), int(vcf_pos2), int(anc_pos)):
                            l1 = myf1.readline()
                        elif int(vcf_pos2) == min(int(vcf_pos1), int(vcf_pos2), int(anc_pos)):
                            l2 = myf2.readline()
                        elif int(anc_pos) == min(int(vcf_pos1), int(vcf_pos2), int(anc_pos)):
                            anc_l = anc_file.readline()
                        if l1 and l2 and anc_l:
                            vcf_data1 = l1.strip().split()
                            vcf_pos1 = vcf_data1[1]
                            vcf_data2 = l2.strip().split()
                            vcf_pos2 = vcf_data2[1]
                            anc_d = anc_l.decode('utf-8').strip().split()
                            anc_pos = anc_d[0]
                        else:
                            break                                                                        
                    if not anc_pos==vcf_pos1==vcf_pos2:
                        break
                        
                    at_pos=int(float(anc_pos))
                    while at_pos>win_end:
                        win_start+=win_step
                        win_end+=win_step
                        #print(win_start,win_end)
                        out_dict.update({(win_start,win_end):{'A':[0,0,0,0,0,0,0,0,0],'C':[0,0,0,0,0,0,0,0,0],'G':[0,0,0,0,0,0,0,0,0],'T':[0,0,0,0,0,0,0,0,0]}})
                    anc_support=anc_d[2]
                    if anc_support=='3': # only consider positions where ancestral state is same in all 3 apes
                        qual1=vcf_data1[5]
                        qual2=vcf_data2[5]
                        if not '.' in [qual1,qual2]:
                            flag1=vcf_data1[6]
                            flag2=vcf_data2[6]
##############################USER CONSIDER IF YOU WANT OTHER FILTERS#############################
                            if (flag1 in ['PASS','.']) and (flag2 in ['PASS','.']):
###########################################################
                                anc_nt=anc_d[1]
                                ref_nt1=vcf_data1[3]
                                alt_nt1=vcf_data1[4]
                                ref_nt2=vcf_data2[3]
                                alt_nt2=vcf_data2[4]
                                [coverage1,genotype1]=get_genotype(vcf_data1[9:])

                                try:
                                    [coverage2,genotype2]=get_genotype(vcf_data2[9:])
                                except ValueError:
                                    print(vcf_pos2, vcf_data2[9:])
##############################CONSIDER IF YOU WANT OTHER FILTERS#############################
                                if check_if_pass_coverage(coverage1,LOW_COV_THRESH,HIGH_COV_THRESH) and check_if_pass_coverage(coverage2,LOW_COV_THRESH,HIGH_COV_THRESH):
###########################################################
                                    if anc_nt in ANCESTRAL_FILTER:
                                        var_form=check_if_ok_and_get_var_form(anc_nt,ref_nt1,ref_nt2,alt_nt1,alt_nt2)
                                        if not var_form=='':
                                            if var_form=='OK_NO_VARIATION':
                                                if ref_nt1==anc_nt:
                                                    out_dict[(win_start,win_end)][anc_nt][0]+=1
                                                else:
                                                    out_dict[(win_start,win_end)][anc_nt][8]+=1
                                            elif var_form=='OK_POLY':
                                                der_count1=orient_and_get_count(genotype1,ref_nt1,alt_nt1,anc_nt)
                                                der_count2=orient_and_get_count(genotype2,ref_nt2,alt_nt2,anc_nt)
                                                out_dict[(win_start,win_end)][anc_nt][get_sample_conf(der_count1,der_count2)]+=1
                    l1=myf1.readline()
                    l2=myf2.readline()
                    anc_l=anc_file.readline()

outf=open(outPATH+'/chr'+the_chr+'_'+ind1+'_vs_'+ind2+'.txt','w')

for a_tuple in sorted(out_dict.keys()):
    out_str=str(a_tuple[0])+','+str(a_tuple[1])
    for nt in NUCL:
        out_str+='\t'+nt+':'+make_out_str(out_dict[a_tuple][nt])
    outf.write(out_str+'\n')
outf.close()


