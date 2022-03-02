import os
import sys
import wbj
from math import log


def make_string(a_l):
	b_l=[]
	for x in a_l:
		b_l.append(str(x))
	return b_l

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

        #print a_d
        #print (m1,m2,m3,m4,m5,m6,m7,m0,m8)
        #raw_input()
	return (m1,m2,m3,m4,m5,m6,m7,m0+m8)

def do_inverse(in_tuple):
	(m10,m01,m20,m02,m11,m21,m12,m00)=in_tuple
	return (m01,m10,m02,m20,m11,m12,m21,m00)


def get_count_list(file_list):
	count_list=[]
	for f in file_list:
		myf=open(f,'r')
		for a_l in myf:
			d=a_l.split()
			counts=sum_over_all_nt(d[1:])
			count_list.append(counts)
		myf.close()
	b_list=[]
	return count_list

def get_inverse_count_list(file_list):
	count_list=[]
	for f in file_list:
		myf=open(f,'r')
		for a_l in myf:
			d=a_l.split()
			counts=sum_over_all_nt(d[1:])
			count_list.append(do_inverse(counts))
		myf.close()
	b_list=[]
	return count_list

def get_cond_estimates(in_tuple):
	(m10,m01,m20,m02,m11,m21,m12,m00)=in_tuple
	m_tot=1.0*sum(in_tuple)

	alfa1=1.0*(m10+m12+m11)/(m10+2.0*m20+m21+0.5*m11)
	alfa2=1.0*(m01+m21+m11)/(m01+2.0*m02+m12+0.5*m11)

	test1=(2.0*m10+m11)/(2.0*m01+m11)-(2.0*m12+m11)/(2.0*m21+m11)
	test2=((m10-m01)+2.0*(m20-m02)+(m21-m12))/m_tot

	return [alfa1,alfa2,test1,test2]


def estimate_param(in_tuple,cond_in_tuple):
	[alfa1,alfa2,test1,test2]=get_cond_estimates(cond_in_tuple)
	(m10,m01,m20,m02,m11,m21,m12,m00)=in_tuple
	m_tot=1.0*sum(in_tuple)
	if alfa1*alfa2>0:
		y=(9.0*m11)/(m_tot*2.0*alfa1*alfa2)
		tau2_1=(3.0* (2.0*alfa1*m21-(1.0-alfa1)*m11) ) /(m_tot*2.0*alfa1*alfa2)
		tau2_2=(3.0* (2.0*alfa2*m12-(1.0-alfa2)*m11) ) /(m_tot*2.0*alfa1*alfa2)
		tau3_1=((5.0-2.0*alfa1)*m11-4.0*alfa1*m21 ) /(m_tot*2.0*alfa1*alfa2)
		tau3_2=((5.0-2.0*alfa2)*m11-4.0*alfa2*m12 ) /(m_tot*2.0*alfa1*alfa2)
		B1=(0.5*m10+m20+0.5*m21+0.25*m11-(5.0*m11/(4.0*alfa1*alfa2)) )/m_tot
		B2=(0.5*m01+m02+0.5*m12+0.25*m11-(5.0*m11/(4.0*alfa1*alfa2)) )/m_tot
		#T1=B1-(y/18.0)
		#T2=B2-(y/18.0)
		#T1=B1-0.25*(tau3_1+tau3_2)
		#T2=B2-0.25*(tau3_1+tau3_2)
		#mean_B=0.5*(B1+B2)
		mean_tau_3=0.5*(tau3_1+tau3_2)
		mean_tau_2=0.5*(tau2_1+tau2_2)
		T1=B1-0.5*mean_tau_3
		T2=B2-0.5*mean_tau_3
		J1=B1-(3.0*mean_tau_3)*(3.0*mean_tau_3)/(6.0*mean_tau_2)
		J2=B2-(3.0*mean_tau_3)*(3.0*mean_tau_3)/(6.0*mean_tau_2)
	else:
		y='NaN'
		tau2_1='NaN'
		tau2_2='NaN'
		tau3_1='NaN'
		tau3_2='NaN'
		B1='NaN'
		B2='NaN'
		T1='NaN'
		T2='NaN'
		J1='NaN'
		J2='NaN'
	U1=(0.5*(1.0-alfa1)*m10-alfa1*m20+0.5*(1.0-alfa2)*m12 +0.25*(2.0-alfa2)*m11 )/m_tot
	U2=(0.5*(1.0-alfa2)*m01-alfa2*m02+0.5*(1.0-alfa1)*m21 +0.25*(2.0-alfa1)*m11 )/m_tot
	if alfa1<1:
		#V1=(0.5*m10-(alfa1/(1.0-alfa1))*m20+0.5*((1.0-alfa2)/(1.0-alfa1))*m12 +0.25*((2.0-alfa2)/(1.0-alfa1))*m11 )/m_tot
		V1=(0.5*m10-  (alfa1/(1.0-alfa1))*m20  +0.5*m12/(1.0-alfa1)  )/m_tot
	else:
		V1='NaN'
	if alfa2<1:
		#V2=(0.5*m01-(alfa2/(1.0-alfa2))*m02+0.5*((1.0-alfa1)/(1.0-alfa2))*m21 +0.25*((2.0-alfa1)/(1.0-alfa2))*m11 )/m_tot
		V2=(0.5*m01-(alfa2/(1.0-alfa2))*m02+0.5*m21/(1.0-alfa2))/m_tot

	else:
		V2='NaN'
	tau_test=y-1.5*(tau2_1+tau2_2)

	return [alfa1,alfa2,test1,test2,y,tau2_1,tau2_2,tau3_1,tau3_2,B1,B2,U1,U2,V1,V2,tau_test,T1,T2,J1,J2]

def get_res(raw_data,cond_raw_data):
	obs_d=[]
	for i in range(len(raw_data[0])):
		obs_d.append(0)
	for a_tuple in raw_data:
		for i in range(len(a_tuple)):
			obs_d[i]+=a_tuple[i]
	obs_cond_d=[]
	for i in range(len(cond_raw_data[0])):
		obs_cond_d.append(0)
	for a_tuple in cond_raw_data:
		for i in range(len(a_tuple)):
			obs_cond_d[i]+=a_tuple[i]
	[obs_alfa1,obs_alfa2,obs_test1,obs_test2,obs_y,obs_tau2_1,obs_tau2_2,obs_tau3_1,obs_tau3_2,obs_B1,obs_B2,obs_U1,obs_U2,obs_V1,obs_V2,obs_tau_test,obs_T1,obs_T2,obs_J1,obs_J2]=estimate_param(obs_d,obs_cond_d)
	l_alfa1=[]
	l_alfa2=[]
	l_test1=[]
	l_test2=[]
	l_y=[]
	l_tau2_1=[]
	l_tau2_2=[]
	l_tau3_1=[]
	l_tau3_2=[]
	l_B1=[]
	l_B2=[]
	l_U1=[]
	l_U2=[]
	l_V1=[]
	l_V2=[]
	l_tau_test=[]
	l_T1=[]
	l_T2=[]
	l_J1=[]
	l_J2=[]
	num_sites=[]
	g=0
	n=0
	for i in range(len(cond_raw_data)):
		a_t=raw_data[i]
		a_cond_t=cond_raw_data[i]
		if sum(a_t)>0:
			g+=1
			n+=sum(a_t)
			local_tuple=(obs_d[0]-a_t[0],obs_d[1]-a_t[1],obs_d[2]-a_t[2],obs_d[3]-a_t[3],obs_d[4]-a_t[4],obs_d[5]-a_t[5],obs_d[6]-a_t[6],obs_d[7]-a_t[7])
			local_cond_tuple=(obs_cond_d[0]-a_cond_t[0],obs_cond_d[1]-a_cond_t[1],obs_cond_d[2]-a_cond_t[2],obs_cond_d[3]-a_cond_t[3],obs_cond_d[4]-a_cond_t[4],obs_cond_d[5]-a_cond_t[5],obs_cond_d[6]-a_cond_t[6],obs_cond_d[7]-a_cond_t[7])
			[alfa1,alfa2,test1,test2,y,tau2_1,tau2_2,tau3_1,tau3_2,B1,B2,U1,U2,V1,V2,tau_test,T1,T2,J1,J2]=estimate_param(local_tuple,local_cond_tuple)
			l_alfa1.append(alfa1)
			l_alfa2.append(alfa2)
			l_test1.append(test1)
			l_test2.append(test2)
			l_y.append(y)
			l_tau2_1.append(tau2_1)
			l_tau2_2.append(tau2_2)
			l_tau3_1.append(tau3_1)
			l_tau3_2.append(tau3_2)
			l_B1.append(B1)
			l_B2.append(B2)
			l_U1.append(U1)
			l_U2.append(U2)
			l_V1.append(V1)
			l_V2.append(V2)
			l_tau_test.append(tau_test)
			l_T1.append(T1)
			l_T2.append(T2)
			l_J1.append(J1)
			l_J2.append(J2)

			num_sites.append(sum(a_t))
	b_res=[wbj.get_WBJ_mean_var(g,n,obs_alfa1,l_alfa1,num_sites)]
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_alfa2,l_alfa2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_test1,l_test1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_test2,l_test2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_y,l_y,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_tau2_1,l_tau2_1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_tau2_2,l_tau2_2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_tau3_1,l_tau3_1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_tau3_2,l_tau3_2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_B1,l_B1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_B2,l_B2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_U1,l_U1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_U2,l_U2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_V1,l_V1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_V2,l_V2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_tau_test,l_tau_test,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_T1,l_T1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_T2,l_T2,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_J1,l_J1,num_sites))
	b_res.append(wbj.get_WBJ_mean_var(g,n,obs_J2,l_J2,num_sites))
	b_res.append(make_string(obs_d))
	return b_res



def get_estimates(file_dict,cond_file_dict):
	b_dict={}
	tot_tuples=len(cond_file_dict.keys())
	at_tuple=0
	for a_tuple in cond_file_dict.keys():
		at_tuple+=1
		print(a_tuple,'num',at_tuple,'out of',tot_tuples)
		cond_file_list=cond_file_dict[a_tuple]
		cond_count_list=get_count_list(cond_file_list)
		if a_tuple in file_dict.keys():
			file_list=file_dict[a_tuple]
			count_list=get_count_list(file_list)
		elif (a_tuple[1],a_tuple[0]) in file_dict.keys():
			file_list=file_dict[(a_tuple[1], a_tuple[0])]
			count_list=get_inverse_count_list(file_list)
		b_dict.update({a_tuple:get_res(count_list,cond_count_list)})
	return b_dict


def get_branch_name(i1,i2):
	if ('Kankanaey' in i1) or ('Kankanaey' in i2):
		if ('Kankanaey' in i1) and ('Kankanaey' in i2):
			return 'withinKankanaey_branch'
		else:
			return 'Kankanaey_branch'
	return 'unspecified_branch'

### Assign outgroup individual
arg_list=sys.argv
THE_COND=arg_list[1]

### Specify path to DIR containing counts for this outgroup
COND_in_path='DIR_counts_per_5cm_TTO_'+THE_COND
COND_file_dict={}
temp=os.listdir(COND_in_path)
for x in temp:
	if x[:len('chr')]=='chr':
		d=x.split('_')
		#print(d)
		pop_tuple=(d[1],d[3]))
		#print(pop_tuple=)
		#input()
		if not pop_tuple in COND_file_dict.keys():
			COND_file_dict.update({pop_tuple:[]})
		COND_file_dict[pop_tuple].append(COND_in_path+'/'+x)


### Specify path to DIR containing TT counts
file_dict={}
in_path='DIR_counts_per_5cm_TT'
all_files=os.listdir(in_path)
for x in all_files:
	if x[:len('chr')]=='chr':
		d=x.split('_')
		#print(d)
		pop_tuple=(d[1],d[3][:-len('.txt')])
		#print(pop_tuple)
		#input()
		if not pop_tuple in file_dict.keys():
			file_dict.update({pop_tuple:[]})
		file_dict[pop_tuple].append(in_path+'/'+x)



all_comps=file_dict.keys()
for x in sorted(all_comps):
	if x in COND_file_dict.keys():
		if not len(file_dict[x])==22 and len(COND_file_dict[x])==22:
			print(x,len(file_dict[x]),'conditional data:',len(COND_file_dict[x]))
			#print file_dict[x][:3]
			input()
	elif (x[1],x[0]) in COND_file_dict.keys():
		if not len(file_dict[x])==22 and len(COND_file_dict[(x[1],x[0])])==22:
			print(x,len(file_dict[x]),'conditional data (other order of pops):',len(COND_file_dict[(x[1],x[0])]))
			#print file_dict[x][:3]
			input()
	else:
		print(x,'not in conditional data')
		input()

outPATH='DIR_estimates_TTO'+THE_COND+'_res'

alfa1_out=open(outPATH+'/alfa1_cond.res','w')
alfa2_out=open(outPATH+'/alfa2_cond.res','w')
test1_out=open(outPATH+'/test1_cond.res','w')
test2_out=open(outPATH+'/test2_cond.res','w')
y_out=open(outPATH+'/y_cond.res','w')
tau2_1_out=open(outPATH+'/tau2_1_cond.res','w')
tau2_2_out=open(outPATH+'/tau2_2_cond.res','w')
tau3_1_out=open(outPATH+'/tau3_1_cond.res','w')
tau3_2_out=open(outPATH+'/tau3_2_cond.res','w')
B1_out=open(outPATH+'/B1_cond.res','w')
B2_out=open(outPATH+'/B2_cond.res','w')
U1_out=open(outPATH+'/U1_cond.res','w')
U2_out=open(outPATH+'/U2_cond.res','w')
V1_out=open(outPATH+'/V1_cond.res','w')
V2_out=open(outPATH+'/V2_cond.res','w')
tau_test_out=open(outPATH+'/tau_test_cond.res','w')
T1_out=open(outPATH+'/T1_cond.res','w')
T2_out=open(outPATH+'/T2_cond.res','w')
J1_out=open(outPATH+'/J1_cond.res','w')
J2_out=open(outPATH+'/J2_cond.res','w')

m_counts_out=open(outPATH+'/m_counts_cond.res','w')


header= '\t'.join(['branch','pop1','pop2','obs_mean','wbj_mean','wbj_var'])+'\n'
alfa1_out.write(header)
alfa2_out.write(header)


test1_out.write(header)
test2_out.write(header)
y_out.write(header)
tau2_1_out.write(header)
tau2_2_out.write(header)
tau3_1_out.write(header)
tau3_2_out.write(header)

B1_out.write(header)
B2_out.write(header)
U1_out.write(header)
U2_out.write(header)
V1_out.write(header)
V2_out.write(header)
tau_test_out.write(header)
T1_out.write(header)
T2_out.write(header)
J1_out.write(header)
J2_out.write(header)

m_counts_out.write(','.join(['branch','pop1','pop2','m10','m01','m20','m02','m11','m21','m12','m00'])+'\n')

a_res_dict=get_estimates(file_dict,COND_file_dict)
for a_comp in sorted(a_res_dict.keys()):
	print(a_comp)
	[p1,p2]=a_comp
	a_br=get_branch_name(p1,p2)
	[alfa1,alfa2,test1,test2,y,tau2_1,tau2_2,tau3_1,tau3_2,B1,B2,U1,U2,V1,V2,tau_test,T1,T2,J1,J2,m_counts]=a_res_dict[a_comp]
	alfa1_out.write('\t'.join([a_br,p1,p2,alfa1[0],alfa1[1],alfa1[2]])+'\n')
	alfa2_out.write('\t'.join([a_br,p1,p2,alfa2[0],alfa2[1],alfa2[2]])+'\n')

	test1_out.write('\t'.join([a_br,p1,p2,test1[0],test1[1],test1[2]])+'\n')
	test2_out.write('\t'.join([a_br,p1,p2,test2[0],test2[1],test2[2]])+'\n')

	y_out.write('\t'.join([a_br,p1,p2,y[0],y[1],y[2]])+'\n')

	tau2_1_out.write('\t'.join([a_br,p1,p2,tau2_1[0],tau2_1[1],tau2_1[2]])+'\n')
	tau2_2_out.write('\t'.join([a_br,p1,p2,tau2_2[0],tau2_2[1],tau2_2[2]])+'\n')
	tau3_1_out.write('\t'.join([a_br,p1,p2,tau3_1[0],tau3_1[1],tau3_1[2]])+'\n')
	tau3_2_out.write('\t'.join([a_br,p1,p2,tau3_2[0],tau3_2[1],tau3_2[2]])+'\n')
	B1_out.write('\t'.join([a_br,p1,p2,B1[0],B1[1],B1[2]])+'\n')
	B2_out.write('\t'.join([a_br,p1,p2,B2[0],B2[1],B2[2]])+'\n')
	U1_out.write('\t'.join([a_br,p1,p2,U1[0],U1[1],U1[2]])+'\n')
	U2_out.write('\t'.join([a_br,p1,p2,U2[0],U2[1],U2[2]])+'\n')
	V1_out.write('\t'.join([a_br,p1,p2,V1[0],V1[1],V1[2]])+'\n')
	V2_out.write('\t'.join([a_br,p1,p2,V2[0],V2[1],V2[2]])+'\n')
	tau_test_out.write('\t'.join([a_br,p1,p2,tau_test[0],tau_test[1],tau_test[2]])+'\n')
	T1_out.write('\t'.join([a_br,p1,p2,T1[0],T1[1],T1[2]])+'\n')
	T2_out.write('\t'.join([a_br,p1,p2,T2[0],T2[1],T2[2]])+'\n')
	J1_out.write('\t'.join([a_br,p1,p2,J1[0],J1[1],J1[2]])+'\n')
	J2_out.write('\t'.join([a_br,p1,p2,J2[0],J2[1],J2[2]])+'\n')
	m_counts_out.write(','.join([a_br,p1,p2]+m_counts)+'\n')

alfa1_out.close()
alfa2_out.close()
test1_out.close()
test2_out.close()
y_out.close()
tau2_1_out.close()
tau2_2_out.close()
tau3_1_out.close()
tau3_2_out.close()
B1_out.close()
B2_out.close()
U1_out.close()
U2_out.close()
V1_out.close()
V2_out.close()
tau_test_out.close()
T1_out.close()
T2_out.close()
J1_out.close()
J2_out.close()

m_counts_out.close()
