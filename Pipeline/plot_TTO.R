source('my_R_plot_funcs.R')

myCombine=function(X1,X2){return (paste(X1,X2,sep=' - '))}

myCutAtBorder=function(x,low,high){
	bVal=x
	if (x<low){bVal=low}
	if (x>high){bVal=high}
	return(bVal)
}

doAllBranchPlotVertical=function(Param1,Param2,Param3,Param4,Param5,Param6,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText){

	theY1=as.numeric(Param1$wbj_mean)
	lowY1=as.numeric(Param1$wbj_mean)-2.0*sqrt(as.numeric(Param1$wbj_var))
	highY1=as.numeric(Param1$wbj_mean)+2.0*sqrt(as.numeric(Param1$wbj_var))
	theB1=as.numeric(Param3$wbj_mean)
	lowB1=as.numeric(Param3$wbj_mean)-2.0*sqrt(as.numeric(Param3$wbj_var))
	highB1=as.numeric(Param3$wbj_mean)+2.0*sqrt(as.numeric(Param3$wbj_var))
	theC1=as.numeric(Param5$wbj_mean)
	lowC1=as.numeric(Param5$wbj_mean)-2.0*sqrt(as.numeric(Param5$wbj_var))
	highC1=as.numeric(Param5$wbj_mean)+2.0*sqrt(as.numeric(Param5$wbj_var))

	theY2=as.numeric(Param2$wbj_mean)
	lowY2=as.numeric(Param2$wbj_mean)-2.0*sqrt(as.numeric(Param2$wbj_var))
	highY2=as.numeric(Param2$wbj_mean)+2.0*sqrt(as.numeric(Param2$wbj_var))
	theB2=as.numeric(Param4$wbj_mean)
	lowB2=as.numeric(Param4$wbj_mean)-2.0*sqrt(as.numeric(Param4$wbj_var))
	highB2=as.numeric(Param4$wbj_mean)+2.0*sqrt(as.numeric(Param4$wbj_var))
	theC2=as.numeric(Param6$wbj_mean)
	lowC2=as.numeric(Param6$wbj_mean)-2.0*sqrt(as.numeric(Param6$wbj_var))
	highC2=as.numeric(Param6$wbj_mean)+2.0*sqrt(as.numeric(Param6$wbj_var))

	allY=c(theY1,theY2)
	lowallY=c(lowY1,lowY2)
	highallY=c(highY1,highY2)
	allB=c(theB1,theB2)
	lowB=c(lowB1,lowB2)
	highB=c(highB1,highB2)
	allC=c(theC1,theC2)
	lowC=c(lowC1,lowC2)
	highC=c(highC1,highC2)

	p1_names=c(as.character(Param1$pop1),as.character(Param2$pop2))
	p2_names=c(as.character(Param1$pop2),as.character(Param2$pop1))
	branch_names=c(as.character(Param1$branch),as.character(Param2$branch))

	theX=seq(1,length(allY))
	theOrder=rev(order(allY))

        allY=allY[theOrder]
        lowallY=lowallY[theOrder]
        highallY=highallY[theOrder]

        allB=allB[theOrder]
        lowB=lowB[theOrder]
        highB=highB[theOrder]

        allC=allC[theOrder]
        lowC=lowC[theOrder]
        highC=highC[theOrder]

        p1_names=p1_names[theOrder]
        p2_names=p2_names[theOrder]
        branch_names=branch_names[theOrder]

	#par(xaxt='n',yaxt='n',xpd=NA,bty='n')
	par(yaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))

	#plot(allB,theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab=paramName)
	plot(allB,theX,type='n',xlim=c(yLow,yHigh),ylab='',xlab='',xaxt='n')

	segments(0,0,0,length(theOrder),col='black',lty=1)
	A=1000*c(-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000)/transformScale
	B=A-(50000/transformScale)
	segments(A,rep(0,length(A)),A,rep(length(theOrder),length(A)),col='black',lty=3)
	segments(B,rep(0,length(B)),B,rep(length(theOrder),length(B)),col='grey',lty=3)

	points(allB,theX,pch=5,cex=0.6,col=sapply(branch_names,myGetBranchColor))
	segments(lowB,theX,highB,col=sapply(branch_names,myGetBranchColor))

	points(allC,theX,pch=4,cex=0.6,col=sapply(branch_names,myGetBranchColor))
	segments(lowC,theX,highC,col=sapply(branch_names,myGetBranchColor))

	points(allY,theX,pch=3,cex=0.6,col=sapply(branch_names,myGetBranchColor))
	segments(lowallY,theX,highallY,col=sapply(branch_names,myGetBranchColor))

        text(lowC-0.1*(yHigh-yLow),theX,mapply(myCombine,X1=p1_names,X2=p2_names),srt=0,cex=popTextSize,col='black')

	if (doPlotTranformAxis==1){
		par(new=T)
		plot(allY,theX,type='n',xlab='',ylab='',xlim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=1)
		mtext(side=1,line=3,transformText)
		#axis(side=3)
		#mtext(side=3,line=3,transformText)
	}
}


doAllBranchPlotHorizontal=function(Param1,Param2,Param3,Param4,yLow,yHigh,popTextSize,doPlotLegend,paramName,doPlotTranformAxis,tranformScale,transformText,Correction1,Correction2){

	theY1=Correction1*as.numeric(Param1$wbj_mean)
	lowY1=Correction1*as.numeric(Param1$wbj_mean)-2.0*sqrt(as.numeric(Param1$wbj_var))
	highY1=Correction1*as.numeric(Param1$wbj_mean)+2.0*sqrt(as.numeric(Param1$wbj_var))
	theB1=Correction2*as.numeric(Param3$wbj_mean)
	lowB1=Correction2*as.numeric(Param3$wbj_mean)-2.0*sqrt(as.numeric(Param3$wbj_var))
	highB1=Correction2*as.numeric(Param3$wbj_mean)+2.0*sqrt(as.numeric(Param3$wbj_var))

	theY2=Correction1*as.numeric(Param2$wbj_mean)
	lowY2=Correction1*as.numeric(Param2$wbj_mean)-2.0*sqrt(as.numeric(Param2$wbj_var))
	highY2=Correction1*as.numeric(Param2$wbj_mean)+2.0*sqrt(as.numeric(Param2$wbj_var))
	theB2=Correction2*as.numeric(Param4$wbj_mean)
	lowB2=Correction2*as.numeric(Param4$wbj_mean)-2.0*sqrt(as.numeric(Param4$wbj_var))
	highB2=Correction2*as.numeric(Param4$wbj_mean)+2.0*sqrt(as.numeric(Param4$wbj_var))

	allY=c(theY1,theY2)
	lowallY=c(lowY1,lowY2)
	highallY=c(highY1,highY2)
	allB=c(theB1,theB2)
	lowB=c(lowB1,lowB2)
	highB=c(highB1,highB2)

	p1_names=c(as.character(Param1$pop1),as.character(Param2$pop2))
	p2_names=c(as.character(Param1$pop2),as.character(Param2$pop1))
	branch_names=c(as.character(Param1$branch),as.character(Param2$branch))

	theX=seq(1,length(allY))
	theOrder=rev(order(allY))

        allY=allY[theOrder]
        lowallY=lowallY[theOrder]
        highallY=highallY[theOrder]

        allB=allB[theOrder]
        lowB=lowB[theOrder]
        highB=highB[theOrder]

        p1_names=p1_names[theOrder]
        p2_names=p2_names[theOrder]
        branch_names=branch_names[theOrder]

	#par(xaxt='n',yaxt='n',xpd=NA,bty='n')
	par(xaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))

	plot(theX,allB,type='n',ylim=c(yLow,yHigh),ylab='',xlab='',yaxt='n')

	segments(0,0,length(theOrder),0,col='black',lty=1)
	A=1000*c(100,200,300,400,500,600,700,800,900,1000,1100,1200)/transformScale
	B=A-(50000/transformScale)
	segments(rep(0,length(A)),A,rep(length(theOrder),length(A)),A,col='black',lty=3)
	segments(rep(0,length(B)),B,rep(length(theOrder),length(B)),B,col='grey',lty=3)

	points(theX,allB,pch=4,cex=0.8,col=sapply(branch_names,myGetBranchColor))
	segments(theX,lowB,theX,highB,col=sapply(branch_names,myGetBranchColor))
	
	points(theX,allY,pch=3,cex=0.8,col=sapply(branch_names,myGetBranchColor))
	segments(theX,lowallY,theX,highallY,col=sapply(branch_names,myGetBranchColor))

	if (min(lowallY)<min(lowB)){
		text(theX,lowallY-0.1*(yHigh-yLow),mapply(myCombine,X1=p1_names,X2=p2_names),srt=90,cex=popTextSize,col='black')
	} else {
		text(theX,lowB-0.1*(yHigh-yLow),mapply(myCombine,X1=p1_names,X2=p2_names),srt=90,cex=popTextSize,col='black')
	}
	if (doPlotTranformAxis==1){
		par(new=T)
		plot(theX,allY,type='n',xlab='',ylab='',ylim=c(transformScale*yLow,transformScale*yHigh),axes=F)
		axis(side=2)
		mtext(side=2,line=3,transformText)
	}
}

###############CONDITIONING ON AN OUTGROUP##################################

pdf('DIR_plots/div_estimates_TTO.pdf',width=7,height=13)
Param1=read.table('DIR_estimates_TTO/J1_cond.res',header=T)
Param2=read.table('DIR_estimates_TTO/J2_cond.res',header=T)
Param3=read.table('DIR_estimates_TTO/B1_cond.res',header=T)
Param4=read.table('DIR_estimates_TTO/B2_cond.res',header=T)
Param5=read.table('DIR_estimates_TTO/T1_cond.res',header=T)
Param6=read.table('DIR_estimates_TTO/T2_cond.res',header=T)
#yLow=-0.000125
#yHigh=0.00045
yLow=-0.0000
yHigh=0.00015
popTextSize=0.4
transformScale=assumedGen/assumedMut
#transformText=paste('years w mu=',as.character(assumedMut),' and gen time=',as.character(assumedGen),sep='')
transformText='time in years'
doAllBranchPlotVertical(Param1,Param2,Param3,Param4,Param5,Param6,yLow,yHigh,popTextSize,1,'T',1,tranformScale,transformText)
#legend('right',legend=c('non-African','out-of-Africa','West/East Afr split','Mbuti split','Khoe-San split','Archaic split','Neand/Denis split','Mandenka-Yoruba'),pch=19,col=c('pink','purple','skyblue','red','green','black','grey','blue'),bty='n',cex=0.7)
legend('right',legend=c('Linear estimation','Correcting with tau3','time to first coalescent event in ancestral pop'),pch=c(3,4,5),bty='n',cex=0.8)
dev.off()


pdf('DIR_plots/tau_estimates_cond.pdf',width=7,height=13)
Param1=read.table('DIR_estimates_TTO/tau3_1_cond.res',header=T)
Param2=read.table('DIR_estimates_TTO/tau3_2_cond.res',header=T)
Param3=read.table('DIR_estimates_TTO/tau2_1_cond.res',header=T)
Param4=read.table('DIR_estimates_TTO/tau2_2_cond.res',header=T)
yLow=0
yHigh=0.0005
popTextSize=0.4
transformScale=assumedGen/assumedMut
#transformText=paste('years w mu=',as.character(assumedMut),' and gen time=',as.character(assumedGen),sep='')
transformText='time in years'
doAllBranchPlotHorizontal(Param1,Param2,Param3,Param4,yLow,yHigh,popTextSize,1,'T',1,tranformScale,transformText,3,1)
legend('top',legend=c('3tau3','tau2'),pch=c(3,4),bty='n',cex=1)
dev.off()


##########################################################################


