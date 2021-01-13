import os
import wbj
from math import log

def sum_over_all_nt(a_d):
	m0=0
	m1=0
	m2=0
	m3=0
	m4=0
	m5=0
	m6=0
	m7=0
	m8=0
	for a_nt_c in a_d:
		nt=a_nt_c[0]
		temp=a_nt_c[2:].split(',')
		if nt in ['A','C','G','T']:
			m0+=int(temp[0])
			m1+=int(temp[1])
			m2+=int(temp[2])
			m3+=int(temp[3])
			m4+=int(temp[4])
			m5+=int(temp[5])
			m6+=int(temp[6])
			m7+=int(temp[7])
			m8+=int(temp[8])

	#print(a_d)
	#print(m1,m2,m3,m4,m5,m6,m7,m0,m8)
	#input()
	return (m1,m2,m3,m4,m5,m6,m7,m0+m8)

def get_count_list(file_list):
	count_list=[]
	for f in file_list:
		myf=open('DIR_counts_per_5cm_TT/'+f,'r')
		for a_l in myf:
			d=a_l.split()
			counts=sum_over_all_nt(d[1:])
			if sum(counts)>0:
				count_list.append(counts)
		myf.close()
	b_list=[]
	return count_list

def estimate_param(in_tuple):
	(n1,n2,n3,n4,n5,n6,n7,n0)=in_tuple
	n_tot=1.0*sum(in_tuple)
	alfa1=2.0*n5/(n5+2.0*n6)
	alfa2=2.0*n5/(n5+2.0*n7)

	mu_t1_t2_diff=1.0*(n3-n4+0.5*(n1+n6-n2-n7))/n_tot

	thetaA=(3.0/n_tot)*(n5+2.0*n6)*(n5+2.0*n7)/(8.0*n5)

	mu_t1_p1=1.0*n3+0.5*n1
	mu_t1_p2=(n5+2.0*n6)*(n5+6.0*n7)/(8.0*n5)
	mu_t1=(mu_t1_p1-mu_t1_p2)/n_tot

	mu_t2_p1=1.0*n4+0.5*n2
	mu_t2_p2=(n5+6.0*n6)*(n5+2.0*n7)/(8.0*n5)
	mu_t2=(mu_t2_p1-mu_t2_p2)/n_tot

	if n5<2*n6:
		drift1=-1.0*log(alfa1)
		theta1=mu_t1/drift1
		the_nom=2.0*n6*(n1+n7)-1.0*n5*(n1+4.0*n3-n7)
		the_den=2.0*(2.0*n6-1.0*n5)*n_tot
		mu_nu1=the_nom/the_den
		the_nom=(2.0*n6+n5)*(n5*(8.0*n3+2.0*n7+n5)-2.0*n6*(6.0*n7+n5))
		the_den=(2.0*n6-n5)*(n5*(4.0*n1+8.0*n3-6.0*n7-n5)-2.0*n6*(6.0*n7+n5))
		W1ratio=the_nom/the_den
		logpt=1.0/(log(2.0*n5)-log(2.0*n6+n5))
		pt1=(2.0*n7+n1)*(2.0*n6+n5)/(2.0*n6-n5)
		pt2=(2.0*n3-n1)/logpt
		pt3=(2.0*n6+n5)*(6.0*n7+n5)/(4.0*n5)
		pt4=4.0*n5/(2.0*n6-n5)
		D1=(pt1+pt2-(pt3*(pt4+logpt)))/(2.0*n_tot)

	else:
		drift1='NaN'
		theta1='NaN'
		mu_nu1='NaN'
		W1ratio='NaN'
		D1='NaN'

	if n5<2*n7:
		drift2=-1.0*log(alfa2)
		theta2=mu_t2/drift2
		the_nom=2.0*n7*(n2+n6)-1.0*n5*(n2+4.0*n4-n6)
		the_den=2.0*(2.0*n7-1.0*n5)*n_tot
		mu_nu2=the_nom/the_den

		the_nom=(2.0*n7+n5)*(n5*(8.0*n4+2.0*n6+n5)-2.0*n7*(6.0*n6+n5))
		the_den=(2.0*n7-n5)*(n5*(4.0*n2+8.0*n4-6.0*n6-n5)-2.0*n7*(6.0*n6+n5))
		W2ratio=the_nom/the_den

		logpt=1.0/(log(2.0*n5)-log(2.0*n7+n5))
		pt1=(2.0*n6+n2)*(2.0*n7+n5)/(2.0*n7-n5)
		pt2=(2.0*n4-n2)/logpt
		pt3=(6.0*n6+n5)*(2.0*n7+n5)/(4.0*n5)
		pt4=4.0*n5/(2.0*n7-n5)
		D2=(pt1+pt2-(pt3*(pt4+logpt)))/(2.0*n_tot)

	else:
		drift2='NaN'
		theta2='NaN'
		mu_nu2='NaN'
		W2ratio='NaN'
		D2='NaN'
##################METHOD Schlebusch et al 2012 ############
	Ccount1=1.0*n3+0.5*n6
	D1orD2count1=0.5*n5+1.0*n7
	Ccount2=1.0*n4+0.5*n7
	D1orD2count2=0.5*n5+1.0*n6
	P1=-log((3.0/2.0)*D1orD2count1/(D1orD2count1+Ccount1))
	P2=-log((3.0/2.0)*D1orD2count2/(D1orD2count2+Ccount2))
	P1_time=P1*thetaA
	P2_time=P2*thetaA
###################METHOD Schlebusch et al 2012 ############
###################Fst############
	Fst=(2.0*n3+2.0*n4-1.0*n5)/(1.0*n1+1.0*n2+2.0*n3+2.0*n4+1.0*n5+1.0*n6+1.0*n7)
###################Fst############
	return [alfa1,alfa2,thetaA,mu_t1,mu_t2,mu_nu1,mu_nu2,mu_t1_t2_diff,drift1,drift2,theta1,theta2,W1ratio,W2ratio,D1,D2,P1,P2,P1_time,P2_time,Fst]





def get_res(raw_data):
	obs_d=[]
	for i in range(len(raw_data[0])):
		obs_d.append(0)
	for a_tuple in raw_data:
		for i in range(len(a_tuple)):
			obs_d[i]+=a_tuple[i]
	[obs_alfa1,obs_alfa2,obs_thetaA,obs_mu_t1,obs_mu_t2,obs_mu_nu1,obs_mu_nu2,obs_mu_diff_t1_t2,obs_drift1,obs_drift2,obs_theta1,obs_theta2,obs_W1ratio,obs_W2ratio,obs_D1,obs_D2,obs_P1,obs_P2,obs_P1_time,obs_P2_time,obs_Fst]=estimate_param(obs_d)
	l_alfa1=[]
	l_alfa2=[]
	l_thetaA=[]
	l_mu_t1=[]
	l_mu_t2=[]
	l_mu_nu1=[]
	l_mu_nu2=[]
	l_mu_diff_t1_t2=[]
	l_drift1=[]
	l_drift2=[]
	l_theta1=[]
	l_theta2=[]
	l_W1ratio=[]
	l_W2ratio=[]
	l_D1=[]
	l_D2=[]
	l_P1=[]
	l_P2=[]
	l_P1_time=[]
	l_P2_time=[]
	l_Fst=[]
	num_sites=[]
	g=0
	n=0
	for a_t in raw_data:
		if sum(a_t)>0:
			g+=1
			n+=sum(a_t)
			local_tuple=(obs_d[0]-a_t[0],obs_d[1]-a_t[1],obs_d[2]-a_t[2],obs_d[3]-a_t[3],obs_d[4]-a_t[4],obs_d[5]-a_t[5],obs_d[6]-a_t[6],obs_d[7]-a_t[7])
			[alfa1,alfa2,thetaA,mu_t1,mu_t2,mu_nu1,mu_nu2,mu_diff_t1_t2,drift1,drift2,theta1,theta2,W1ratio,W2ratio,D1,D2,P1,P2,P1_time,P2_time,Fst]=estimate_param(local_tuple)
			l_alfa1.append(alfa1)
			l_alfa2.append(alfa2)
			l_thetaA.append(thetaA)
			l_mu_t1.append(mu_t1)
			l_mu_t2.append(mu_t2)
			l_mu_nu1.append(mu_nu1)
			l_mu_nu2.append(mu_nu2)
			l_mu_diff_t1_t2.append(mu_diff_t1_t2)
			l_drift1.append(drift1)
			l_drift2.append(drift2)
			l_theta1.append(theta1)
			l_theta2.append(theta2)
			l_W1ratio.append(W1ratio)
			l_W2ratio.append(W2ratio)
			l_D1.append(D1)
			l_D2.append(D2)
			l_P1.append(P1)
			l_P2.append(P2)
			l_P1_time.append(P1_time)
			l_P2_time.append(P2_time)
			l_Fst.append(Fst)
			#num_sites.append(sum(local_tuple))
			num_sites.append(sum(a_t))

	b_res=[wbj.get_WBJ_mean_var(g,n,obs_alfa1,l_alfa1,num_sites)]
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_alfa2,l_alfa2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_thetaA,l_thetaA,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_mu_t1,l_mu_t1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_mu_t2,l_mu_t2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_mu_nu1,l_mu_nu1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_mu_nu2,l_mu_nu2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_mu_diff_t1_t2,l_mu_diff_t1_t2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_drift1,l_drift1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_drift2,l_drift2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_theta1,l_theta1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_theta2,l_theta2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_W1ratio,l_W1ratio,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_W2ratio,l_W2ratio,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_D1,l_D1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_D2,l_D2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_P1,l_P1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_P2,l_P2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_P1_time,l_P1_time,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_P2_time,l_P2_time,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_Fst,l_Fst,num_sites))
	return b_res




def get_estimates(file_dict):
	b_dict={}
	for a_tuple in file_dict.keys():
		print(a_tuple)
		file_list=file_dict[a_tuple]
		b_dict.update({a_tuple:get_res(get_count_list(file_list))})
	return b_dict

def get_branch_name(i1,i2):
    #print(i1,i2, ('Kankanaey' in i1) ,('Kankanaey' in i2))
    #input()
    if ('Kankanaey' in i1) or ('Kankanaey' in i2):
        if ('Kankanaey' in i1) and ('Kankaaney' in i2):
            return 'withinKankanaey_branch'
        else:
            return 'Kankanaey_branch'
    return 'unspecified_branch'


####################
all_files_dict={}
temp=os.listdir('DIR_counts_per_5cm_TT')
for x in temp:
	if x[:len('chr')]=='chr':
		d=x.split('_')
		pop_tuple=(d[1],d[3][:-len('.txt')])
        	#print(pop_tuple,d)
        	#input()
		if not pop_tuple in all_files_dict.keys():
			all_files_dict.update({pop_tuple:[]})
		all_files_dict[pop_tuple].append(x)

for a_tuple in all_files_dict.keys():
	if not len(all_files_dict[a_tuple])==22:
		print(a_tuple,len(all_files_dict[a_tuple]))
		print(sorted(all_files_dict[a_tuple]))
		print('Not 22 chroms')
		input()
#print('tot comparisons',len(all_files_dict.keys()))

################

outPATH='DIR_estimates_TT'

alfa1_out=open(outPATH+'/alfa1.res','w')
alfa2_out=open(outPATH+'/alfa2.res','w')
thetaA_out=open(outPATH+'/thetaA.res','w')
mu_t1_out=open(outPATH+'/mu_t1.res','w')
mu_t2_out=open(outPATH+'/mu_t2.res','w')
mu_nu1_out=open(outPATH+'/mu_nu1.res','w')
mu_nu2_out=open(outPATH+'/mu_nu2.res','w')
mu_diff_t1_t2_out=open(outPATH+'/mu_diff_t1_t2.res','w')
drift1_out=open(outPATH+'/drift1.res','w')
drift2_out=open(outPATH+'/drift2.res','w')
theta1_out=open(outPATH+'/theta1.res','w')
theta2_out=open(outPATH+'/theta2.res','w')
W1ratio_out=open(outPATH+'/W1ratio.res','w')
W2ratio_out=open(outPATH+'/W2ratio.res','w')
D1_out=open(outPATH+'/D1.res','w')
D2_out=open(outPATH+'/D2.res','w')
P1_out=open(outPATH+'/P1.res','w')
P2_out=open(outPATH+'/P2.res','w')
P1_time_out=open(outPATH+'/P1_time.res','w')
P2_time_out=open(outPATH+'/P2_time.res','w')
Fst_out=open(outPATH+'/Fst.res','w')



header= '\t'.join(['branch','pop1','pop2','obs_mean','wbj_mean','wbj_var'])+'\n'

alfa1_out.write(header)
alfa2_out.write(header)
thetaA_out.write(header)
mu_t1_out.write(header)
mu_t2_out.write(header)
mu_nu1_out.write(header)
mu_nu2_out.write(header)
mu_diff_t1_t2_out.write(header)
drift1_out.write(header)
drift2_out.write(header)
theta1_out.write(header)
theta2_out.write(header)
W1ratio_out.write(header)
W2ratio_out.write(header)
D1_out.write(header)
D2_out.write(header)
P1_out.write(header)
P2_out.write(header)
P1_time_out.write(header)
P2_time_out.write(header)
Fst_out.write(header)


a_res_dict=get_estimates(all_files_dict)
for a_comp in a_res_dict.keys():
	(p1,p2)=a_comp
	print(p1,'vs',p2)
	br=get_branch_name(p1,p2)
	[alfa1,alfa2,thetaA,mu_t1,mu_t2,mu_nu1,mu_nu2,mu_diff_t1_t2,drift1,drift2,theta1,theta2,W1ratio,W2ratio,D1,D2,P1,P2,P1_time,P2_time,Fst]=a_res_dict[a_comp]
	alfa1_out.write('\t'.join([br,p1,p2,alfa1[0],alfa1[1],alfa1[2]])+'\n')
	alfa2_out.write('\t'.join([br,p1,p2,alfa2[0],alfa2[1],alfa2[2]])+'\n')
	thetaA_out.write('\t'.join([br,p1,p2,thetaA[0],thetaA[1],thetaA[2]])+'\n')
	mu_t1_out.write('\t'.join([br,p1,p2,mu_t1[0],mu_t1[1],mu_t1[2]])+'\n')
	mu_t2_out.write('\t'.join([br,p1,p2,mu_t2[0],mu_t2[1],mu_t2[2]])+'\n')
	mu_nu1_out.write('\t'.join([br,p1,p2,mu_nu1[0],mu_nu1[1],mu_nu1[2]])+'\n')
	mu_nu2_out.write('\t'.join([br,p1,p2,mu_nu2[0],mu_nu2[1],mu_nu2[2]])+'\n')
	mu_diff_t1_t2_out.write('\t'.join([br,p1,p2,mu_diff_t1_t2[0],mu_diff_t1_t2[1],mu_diff_t1_t2[2]])+'\n')
	drift1_out.write('\t'.join([br,p1,p2,drift1[0],drift1[1],drift1[2]])+'\n')
	drift2_out.write('\t'.join([br,p1,p2,drift2[0],drift2[1],drift2[2]])+'\n')
	theta1_out.write('\t'.join([br,p1,p2,theta1[0],theta1[1],theta1[2]])+'\n')
	theta2_out.write('\t'.join([br,p1,p2,theta2[0],theta2[1],theta2[2]])+'\n')
	W1ratio_out.write('\t'.join([br,p1,p2,W1ratio[0],W1ratio[1],W1ratio[2]])+'\n')
	W2ratio_out.write('\t'.join([br,p1,p2,W2ratio[0],W2ratio[1],W2ratio[2]])+'\n')
	D1_out.write('\t'.join([br,p1,p2,D1[0],D1[1],D1[2]])+'\n')
	D2_out.write('\t'.join([br,p1,p2,D2[0],D2[1],D2[2]])+'\n')
	P1_out.write('\t'.join([br,p1,p2,P1[0],P1[1],P1[2]])+'\n')
	P2_out.write('\t'.join([br,p1,p2,P2[0],P2[1],P2[2]])+'\n')
	P1_time_out.write('\t'.join([br,p1,p2,P1_time[0],P1_time[1],P1_time[2]])+'\n')
	P2_time_out.write('\t'.join([br,p1,p2,P2_time[0],P2_time[1],P2_time[2]])+'\n')
	Fst_out.write('\t'.join([br,p1,p2,Fst[0],Fst[1],Fst[2]])+'\n')

alfa1_out.close()
alfa2_out.close()
thetaA_out.close()
mu_t1_out.close()
mu_t2_out.close()
mu_nu1_out.close()
mu_nu2_out.close()
mu_diff_t1_t2_out.close()
drift1_out.close()
drift2_out.close()
theta1_out.close()
theta2_out.close()
W1ratio_out.close()
W2ratio_out.close()
D1_out.close()
D2_out.close()
P1_out.close()
P2_out.close()
P1_time_out.close()
P2_time_out.close()
Fst_out.close()
