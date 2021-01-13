source('my_R_plot_funcs.R')

myCombine=function(X1,X2){return (paste(X1,X2,sep=' - '))}

myCutAtBorder=function(x,low,high){
	bVal=x
	if (x<low){bVal=low}
	if (x>high){bVal=high}
	return(bVal)
}

doAllBranchPlotvminus1=function(Param1,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText,doPlotSD){
	theY1=as.numeric(Param1$wbj_mean)
	lowY1=as.numeric(Param1$wbj_mean)-2.0*sqrt(as.numeric(Param1$wbj_var))
	highY1=as.numeric(Param1$wbj_mean)+2.0*sqrt(as.numeric(Param1$wbj_var))
	allY=theY1
	lowallY=lowY1
	highallY=highY1
	p1_names=as.character(Param1$pop1)
	p2_names=as.character(Param1$pop2)
	branch_names=as.character(Param1$branch)
	theX=seq(1,length(allY))
	theOrder=rev(order(allY))
	par(yaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))
	#print(branch_names[theOrder])	
	plot(allY[theOrder],theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab=paramName)
	points(allY[theOrder],theX,pch='+',cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor))
	#points(allY[theOrder],theX,pch='+',cex=0.6,col='black')
	segments(0,0,0,length(theOrder),col='black',lty=1)
	A=10000*c(-2,-1,0,1,2,3,4,5,6,7,8)/transformScale
	#B=A-1000*(2.5/transformScale)
	segments(A,rep(0,length(A)),A,rep(length(theOrder),length(A)),col='black',lty=3)
	#segments(B,rep(0,length(B)),B,rep(length(theOrder),length(B)),col='grey',lty=3)
	if (doPlotSD==1){
		segments(lowallY[theOrder],theX,highallY[theOrder],col=sapply(branch_names[theOrder],myGetBranchColor))
		#segments(lowallY[theOrder],theX,highallY[theOrder],col='black')
	}
	text(highallY[theOrder]+0.07*(yHigh-yLow),theX,p1_names[theOrder],srt=0,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(lowallY[theOrder]-0.07*(yHigh-yLow),theX,p2_names[theOrder],srt=0,cex=popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doPlotTranformAxis==1){
		par(new=T)
		plot(allY,theX,type='n',xlab='',ylab='',xlim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=3)
		mtext(side=3,line=3,transformText)
	}
}


doAllBranchPlotv0=function(Param1,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText,doPlotSD){
	theY1=as.numeric(Param1$wbj_mean)
	lowY1=as.numeric(Param1$wbj_mean)-2.0*sqrt(as.numeric(Param1$wbj_var))
	highY1=as.numeric(Param1$wbj_mean)+2.0*sqrt(as.numeric(Param1$wbj_var))
	allY=theY1
	lowallY=lowY1
	highallY=highY1
	p1_names=as.character(Param1$pop1)
	p2_names=as.character(Param1$pop2)
	branch_names=as.character(Param1$branch)
	theX=seq(1,length(allY))
	theOrder=rev(order(allY))
	par(yaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))
	plot(allY[theOrder],theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab=paramName)
	points(allY[theOrder],theX,pch='+',cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor))
	A=1000*c(0,5,10,15,20)/transformScale
	B=A-1000*(2.5/transformScale)
	segments(A,rep(0,length(A)),A,rep(length(theOrder),length(A)),col='black',lty=3)
	segments(B,rep(0,length(B)),B,rep(length(theOrder),length(B)),col='grey',lty=3)

	if (doPlotSD==1){
		segments(lowallY[theOrder],theX,highallY[theOrder],col=sapply(branch_names[theOrder],myGetBranchColor))
	}
	text(highallY[theOrder]+0.07*(yHigh-yLow),theX,p1_names[theOrder],srt=0,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(lowallY[theOrder]-0.07*(yHigh-yLow),theX,p2_names[theOrder],srt=0,cex=popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doPlotTranformAxis==1){
		par(new=T)
		plot(allY,theX,type='n',xlab='',ylab='',xlim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=3)
		mtext(side=3,line=3,transformText)
	}
}


doAllBranchPlot=function(Param1,Param2,Param3,Param4,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText){
	theY1=as.numeric(Param1$wbj_mean)
	lowY1=as.numeric(Param1$wbj_mean)-2.0*sqrt(as.numeric(Param1$wbj_var))
	highY1=as.numeric(Param1$wbj_mean)+2.0*sqrt(as.numeric(Param1$wbj_var))
	theB1=as.numeric(Param3$wbj_mean)
	lowB1=as.numeric(Param3$wbj_mean)-2.0*sqrt(as.numeric(Param3$wbj_var))
	highB1=as.numeric(Param3$wbj_mean)+2.0*sqrt(as.numeric(Param3$wbj_var))

	if (Param2=='None'){
		allY=theY1
		lowallY=lowY1
		highallY=highY1
		allB=theB1
		lowB=lowB1
		highB=highB1
		p1_names=as.character(Param1$pop1)
		p2_names=as.character(Param1$pop2)
		branch_names=as.character(Param1$branch)

	}else{

		theY2=as.numeric(Param2$wbj_mean)
		lowY2=as.numeric(Param2$wbj_mean)-2.0*sqrt(as.numeric(Param2$wbj_var))
		highY2=as.numeric(Param2$wbj_mean)+2.0*sqrt(as.numeric(Param2$wbj_var))
		theB2=as.numeric(Param4$wbj_mean)
		lowB2=as.numeric(Param4$wbj_mean)-2.0*sqrt(as.numeric(Param4$wbj_var))
		highB2=as.numeric(Param4$wbj_mean)+2.0*sqrt(as.numeric(Param4$wbj_var))

		allY=c(theY1,theY2)
		lowallY=c(lowY1,lowY2)
		highallY=c(highY1,highY2)
		allB=c(theB1,theB2)
		lowB=c(lowB1,lowB2)
		highB=c(highB1,highB2)
		p1_names=c(as.character(Param1$pop1),as.character(Param2$pop2))
		p2_names=c(as.character(Param1$pop2),as.character(Param2$pop1))
		branch_names=c(as.character(Param1$branch),as.character(Param2$branch))
	}


	theX=seq(1,length(allY))
	theOrder=rev(order(allY))
	par(yaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))

	plot(allB[theOrder],theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab='',xaxt='n')

	segments(0,0,0,length(theOrder),col='black',lty=1)
	A=1000*c(-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000)/transformScale
	B=A-(50000/transformScale)
	segments(A,rep(0,length(A)),A,rep(length(theOrder),length(A)),col='black',lty=3)
	segments(B,rep(0,length(B)),B,rep(length(theOrder),length(B)),col='grey',lty=3)
	points(allB[theOrder],theX,pch=5,cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor))
	segments(lowB[theOrder],theX,highB[theOrder],col=sapply(branch_names[theOrder],myGetBranchColor))
	points(allY[theOrder],theX,pch=3,cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor))
	segments(lowallY[theOrder],theX,highallY[theOrder],col=sapply(branch_names[theOrder],myGetBranchColor))
	#text(highallY[theOrder]+0.07*(yHigh-yLow),theX,p1_names[theOrder],srt=0,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
        #text(lowallY[theOrder]-0.07*(yHigh-yLow),theX,p2_names[theOrder],srt=0,cex=popTextSize,col=sapply(p2_names[theOrder],myGetColor))
        text(lowallY[theOrder]-0.1*(yHigh-yLow),theX,mapply(myCombine,X1=p1_names[theOrder],X2=p2_names[theOrder]),srt=0,cex=popTextSize,col='black')

	#text(allMax[theOrder]+0.07*(yHigh-yLow),theX,p1_names[theOrder],srt=0,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	#text(allMin[theOrder]-0.07*(yHigh-yLow),theX,p2_names[theOrder],srt=0,cex=0.7*popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doPlotTranformAxis==1){
		par(new=T)
		plot(allY,theX,type='n',xlab='',ylab='',xlim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=1)
		mtext(side=1,line=3,transformText)
	}
	return (0)
}


doAllBranchPlotV3=function(Param1,Param2,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText,doPlotSD){
	theY1=Param1$wbj_mean
	lowY1=Param1$wbj_mean-2.0*sqrt(Param1$wbj_var)
	highY1=Param1$wbj_mean+2.0*sqrt(Param1$wbj_var)

	if (Param2=='None'){
		allY=theY1
		lowallY=lowY1
		highallY=highY1
		p1_names=as.character(Param1$pop1)
		p2_names=as.character(Param1$pop2)
		branch_names=as.character(Param1$branch)

	}else{
		theY2=Param2$wbj_mean
		lowY2=Param2$wbj_mean-2.0*sqrt(Param2$wbj_var)
		highY2=Param2$wbj_mean+2.0*sqrt(Param2$wbj_var)
		allY=c(theY1,theY2)
		lowallY=c(lowY1,lowY2)
		highallY=c(highY1,highY2)
		p1_names=c(as.character(Param1$pop1),as.character(Param2$pop2))
		p2_names=c(as.character(Param1$pop2),as.character(Param2$pop1))
		branch_names=c(as.character(Param1$branch),as.character(Param2$branch))
	}
	theOrder=NULL
	br_names_unique=unique(branch_names)
	#br_names_unique=c("withinArchaic_branch","Archaic_branch","KSP_branch","pygmy_branch","WesternAfr_branch","ooAfr_branch","nonAfrican_branch")
	for (i in 1:length(br_names_unique)){
		aBr=as.character(br_names_unique[i])
		temp1=NULL
		temp2=NULL
		for (j in 1:length(p1_names)){
			if (branch_names[j]==aBr){
				temp1=c(temp1,allY[j])
				temp2=c(temp2,j)
			}	
		}
		tempOrder=order(temp1)
		theOrder=c(theOrder,temp2[tempOrder])
		
	}
	theX=seq(1,length(allY))
	#theOrder=rev(order(allY))
	#theOrder1=order(p1_names)
	#theOrder2=order(branch_names)
	#theOrder=theOrder1[theOrder2]
	par(yaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))

	if (doPlotSD==1){
		plot(allY[theOrder],theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab=paramName)
		segments(c(0,1),c(0,0),c(0,1),c(length(theOrder),length(theOrder)),col='grey',lty=1)
		points(allY[theOrder],theX,pch='+',cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor))
		segments(lowallY[theOrder],theX,highallY[theOrder],col=sapply(branch_names[theOrder],myGetBranchColor))
	}else{
		plot(allY[theOrder],theX,pch=19,cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor),xlim=c(yLow,yHigh),ylab='',xlab=paramName)
	}
	text(highallY[theOrder]+0.05*(yHigh-yLow),theX,p1_names[theOrder],srt=0,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(lowallY[theOrder]-0.05*(yHigh-yLow),theX,p2_names[theOrder],srt=0,cex=0.7*popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doPlotTranformAxis==1){
		par(new=T)
		plot(allY,theX,type='n',xlab='',ylab='',xlim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=3)
		mtext(side=3,line=3,transformText)
	}
	return (0)
}

doAllBranchPlotV4=function(Param1,Param2,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText,doPlotSD){
	theY1=Param1$wbj_mean
	lowY1=Param1$wbj_mean-2.0*sqrt(Param1$wbj_var)
	highY1=Param1$wbj_mean+2.0*sqrt(Param1$wbj_var)

	if (Param2=='None'){
		allY=theY1
		lowallY=lowY1
		highallY=highY1
		p1_names=as.character(Param1$pop1)
		p2_names=as.character(Param1$pop2)
		branch_names=as.character(Param1$branch)

	}else{
		theY2=Param2$wbj_mean
		lowY2=Param2$wbj_mean-2.0*sqrt(Param2$wbj_var)
		highY2=Param2$wbj_mean+2.0*sqrt(Param2$wbj_var)
		allY=c(theY1,theY2)
		lowallY=c(lowY1,lowY2)
		highallY=c(highY1,highY2)
		p1_names=c(as.character(Param1$pop1),as.character(Param2$pop2))
		p2_names=c(as.character(Param1$pop2),as.character(Param2$pop1))
		branch_names=c(as.character(Param1$branch),as.character(Param2$branch))
	}
	theX=seq(1,length(allY))
	theOrder=rev(order(allY))
	#theOrder=order(p1_names)
	par(yaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))
	plot(allY[theOrder],theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab=paramName)
	points(allY[theOrder],theX,pch='+',cex=0.6,col=sapply(branch_names[theOrder],myGetBranchColor))
	#A=1000*c(-1000,0,1000)/transformScale
	#A=1000*c(-1500,-1000,-500,0,500,1000,1500)/transformScale
	A=1000*c(750,1000,1250,1500,1750,2000)/transformScale
	segments(A,rep(0,length(A)),A,rep(length(theOrder),length(A)),col='grey',lty=1)
	#segments(0,0,0,length(theOrder),col='black',lty=1)
	if (doPlotSD==1){
		segments(lowallY[theOrder],theX,highallY[theOrder],col=sapply(branch_names[theOrder],myGetBranchColor))
	}
	text(highallY[theOrder]+0.05*(yHigh-yLow),theX,p1_names[theOrder],srt=0,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(lowallY[theOrder]-0.05*(yHigh-yLow),theX,p2_names[theOrder],srt=0,cex=0.7*popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doPlotTranformAxis==1){
		par(new=T)
		plot(allY,theX,type='n',xlab='',ylab='',xlim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=3)
		mtext(side=3,line=3,transformText)
	}
	return (0)
}


print('time diff')
pdf('DIR_plots/time_difference.pdf',width=7,height=10)
Param1=read.table('DIR_estimates_v2/mu_diff_t1_t2.res',header=T)
yLow=-0.00001
yHigh=0.000033
popTextSize=0.6
transformScale=assumedGen/assumedMut
transformText=paste('years w mu=',as.character(assumedMut),' and gen time=',as.character(assumedGen),sep='')
doAllBranchPlotvminus1(Param1,yLow,yHigh,popTextSize,1,'scaled time difference',1,transformScale,transformText,1)
#legend('topright',legend=c('non-African','out-of-Africa','West/East Afr split','Mbuti split','Khoe-San split','Archaic split','Neand/Denis split','Mandenka-Yoruba'),pch=19,col=c('pink','purple','skyblue','red','green','black','grey','blue'),bty='n',cex=0.7)
dev.off()

print('T')
pdf('DIR_plots/mu_t.pdf',width=7,height=10)
Param1=read.table('DIR_estimates_v2/mu_t1.res',header=T)
Param2=read.table('DIR_estimates_v2/mu_t2.res',header=T)
yLow=-0.00008
yHigh=0
popTextSize=0.4
transformScale=assumedGen/assumedMut
transformText=paste('years w mu=',as.character(assumedMut),' and gen time=',as.character(assumedGen),sep='')
doAllBranchPlotV4(Param1,Param2,yLow,yHigh,popTextSize,1,'T',1,tranformScale,transformText,1)
dev.off()

print('theta')
pdf('DIR_plots/thetaA.pdf',width=7,height=10)
Param1=read.table('DIR_estimates_v2/thetaA.res',header=T)
yLow=0
yHigh=0.0005
popTextSize=0.5
transformScale=1/(2*assumedMut)
transformText=paste('diploid population size assuming mu=',as.character(assumedMut),sep='')
doAllBranchPlotv0(Param1,yLow,yHigh,popTextSize,1,expression(paste(theta)),1,transformScale,transformText,1)
#legend('center',legend=c('non-African','out-of-Africa','West/East Afr split','Mbuti split','Khoe-San split','Archaic split','Neand/Denis split','Mandenka-Yoruba'),pch=19,col=c('pink','purple','skyblue','red','green','black','grey','blue'),bty='n',cex=0.7)
dev.off()

print('alpha')
pdf('DIR_plots/alpha.pdf',width=7,height=10)
Param1=read.table('DIR_estimates_v2/alfa1.res',header=T)
Param2=read.table('DIR_estimates_v2/alfa2.res',header=T)
yLow=0.8
yHigh=1
popTextSize=0.3
transformScale=assumedGen/assumedMut
transformText=paste('years w mu=',as.character(assumedMut),' and gen time=',as.character(assumedGen),sep='')
doAllBranchPlotV3(Param1,Param2,yLow,yHigh,popTextSize,1,'P(no coalescence before split)',0,tranformScale,transformText,1)
#legend('left',legend=c('non-African','out-of-Africa','West/East Afr split','Mbuti split','Khoe-San split','Archaic split','Neand/Denis split','Mandenka-Yoruba'),pch=19,col=c('pink','purple','skyblue','red','green','black','grey','blue'),bty='n',cex=0.7)
dev.off()

print('V')
pdf('DIR_plots/mu_nu.pdf',width=7,height=10)
Param1=read.table('DIR_estimates_v2/mu_nu1.res',header=T)
Param2=read.table('DIR_estimates_v2/mu_nu2.res',header=T)
yLow=-0.0002
yHigh=0.0002
popTextSize=0.4
transformScale=assumedGen/assumedMut
transformText=paste('years w mu=',as.character(assumedMut),' and gen time=',as.character(assumedGen),sep='')
doAllBranchPlotV4(Param1,Param2,yLow,yHigh,popTextSize,1,'V',1,tranformScale,transformText,1)
#legend('topright',legend=c('non-African','out-of-Africa','West/East Afr split','Mbuti split','Khoe-San split','Archaic split','Neand/Denis split','Mandenka-Yoruba'),pch=19,col=c('pink','purple','skyblue','red','green','black','grey','blue'),bty='n',cex=0.7)
dev.off()







