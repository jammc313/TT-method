assumedMut=1.25e-8
assumedGen=30


myFilterAllArchaic=function(a_param){
	Den=a_param$pop1=='Denisovan'|a_param$pop2=='Denisovan'
	Neand=a_param$pop1=='Neandertal'|a_param$pop2=='Neandertal'
	myFilter=!(Den|Neand)
	return (a_param[myFilter,])
}

myFilterDenNeand=function(a_param){
	RemComps1=a_param$pop1 %in% c('Neanderthal','Neandertal')&a_param$pop2=='Denisovan'
	RemComps2=a_param$pop1=='Denisovan'&a_param$pop2 %in% c('Neanderthal','Neandertal')
	myFilter=!(RemComps1|RemComps2)
	return (a_param[myFilter,])
}

myFilterNoDenNeand=function(a_param){
	RemComps1=a_param$pop1 %in% c('Neandertal','Denisovan')
	RemComps2=a_param$pop2 %in% c('Neandertal','Denisovan')
	myFilter=!(RemComps1|RemComps2)
	return (a_param[myFilter,])
}

myFilterAtLeastOneDenNeand=function(a_param){
	RemComps1=a_param$pop1 %in% c('Neandertal','Denisovan')
	RemComps2=a_param$pop2 %in% c('Neandertal','Denisovan')
	myFilter=(RemComps1|RemComps2)
	return (a_param[myFilter,])
}

myFilter0or2Archaic=function(a_param){
	RemComps1=a_param$pop1 %in% c('Neandertal','Denisovan')
	RemComps2=a_param$pop2 %in% c('Neandertal','Denisovan')
	myFilter1=(RemComps1&RemComps2)
	myFilter2=((!RemComps1)&(!RemComps2))
	myFilter=(myFilter1|myFilter2)
	return (a_param[myFilter,])
}

myFilterOnlyHGDP=function(a_param){
	HGDP=c('San','Dinka','French','Sardinian','Yoruba','Dai','Mbuti','Papuan','Han','Karitiana','Mandenka')
	noKSP=(a_param$pop1 %in% HGDP & a_param$pop2 %in% HGDP)
	return (a_param[noKSP,])
}

myFilterOnlyHGDPorArch=function(a_param){
	HGDP=c('San','Dinka','French','Sardinian','Yoruba','Dai','Mbuti','Papuan','Han','Karitiana','Mandenka','Neandertal','Denisovan')
	arch=c('Neandertal','Denisovan')
	temp=c(HGDP,arch)
	noKSP=(a_param$pop1 %in% temp & a_param$pop2 %in% temp)
	return (a_param[noKSP,])
}

myFilterNoKSPbranch=function(a_param){
	HGDP_noSan=c('Dinka','French','Sardinian','Yoruba','Dai','Mbuti','Papuan','Han','Karitiana','Mandenka')
	noKSP=(a_param$pop1 %in% HGDP_noSan & a_param$pop2 %in% HGDP_noSan)
	return (a_param[noKSP,])
}

myFilterWithinArchAndNoKSPbranch=function(a_param){
	HGDP_noSan=c('Dinka','French','Sardinian','Yoruba','Dai','Mbuti','Papuan','Han','Karitiana','Mandenka')
	noKSP=(a_param$pop1 %in% HGDP_noSan & a_param$pop2 %in% HGDP_noSan)
	arch=c('Neandertal','Denisovan')
	withinArch=(a_param$pop1 %in% arch & a_param$pop2 %in% arch)
	myFilter=(noKSP|withinArch)
	
	return (a_param[myFilter,])
}


myFilterWithinArchAndNoKSPbranchAndNoMbuti=function(a_param){
	HGDP_noSanMbuti=c('Dinka','French','Sardinian','Yoruba','Dai','Papuan','Han','Karitiana','Mandenka')
	noKSPMbuti=(a_param$pop1 %in% HGDP_noSanMbuti & a_param$pop2 %in% HGDP_noSanMbuti)
	arch=c('Neandertal','Denisovan')
	withinArch=(a_param$pop1 %in% arch & a_param$pop2 %in% arch)
	myFilter=(noKSPMbuti|withinArch)
	
	return (a_param[myFilter,])
}

myFilterOnlyNonAfr=function(a_param){
	#NonAfr=c('French','Sardinian','Dai','Papuan','Han','Karitiana')
	NonAfr=c('French','Sardinian','Dai','Han','Karitiana')
	NonAfrFilter=(a_param$pop1 %in% NonAfr & a_param$pop2 %in% NonAfr)
	return (a_param[NonAfrFilter,])
}

myGetBranchColor=function(x){
        x=as.character(x)
	#print(x)
        bCol='yellow'
        if (x=='withinArchaic_branch'){
                bCol='grey60'
        } else  if (x=='Archaic_branch'){
                bCol='black'
        } else  if (x=='ooAfr_branch'){
                bCol='purple'
        } else  if (x=='WesternAfr_branch'){
                bCol='skyblue'
        } else  if (x=='KSP_branch'){
                bCol='green'
        } else  if (x=='pygmy_branch'){
                bCol='red'
        } else  if (x=='NorthernKSP_branch'){
                bCol='blue'
        } else  if (x=='nonAfrican_branch'){
                bCol='pink'
        } else  if (x=='withinWesternAfr_branch'){
                bCol='blue'
        }
	return (bCol)
}


myGetColor=function(x){
	x=as.character(x)
        bCol='black'
	if (strsplit(x,'')[[1]][length(strsplit(x,'')[[1]])] %in% c('1','2','3','4','5')){
		x=paste(strsplit(x,'')[[1]][1:length(strsplit(x,'')[[1]])-1],collapse='')
	}
        if (x %in% c('Neanderthal','Neandertal')){
                bCol='black'
        } else  if (x=='Denisovan'){
                bCol='grey60'
        } else  if (x %in% c('Nama','Karretjie')){
                bCol='darkgreen'
        } else  if (x %in% c('Juhoansi','Xun','San')){
                bCol='lightgreen'
        } else  if (x %in% c('GuiGhanaKgal')){
                bCol='green'
        } else  if (x %in% c('Mbuti')){
                bCol='red'
        } else  if (x %in% c('Mandenka','Yoruba')){
                bCol='yellow4'
        } else  if (x %in% c('Dinka')){
                bCol='darkblue'
        } else  if (x %in% c('French','Sardinian')){
                bCol='skyblue'
        } else  if (x %in% c('Papuan')){
                bCol='magenta'
        } else  if (x %in% c('Han','Dai')){
                bCol='purple'
        } else  if (x %in% c('Karitiana')){
                bCol='pink2'
        }
	return (bCol)
}




plotParam=function(Param1,Param2,yLow,yHigh,theOrder,doLegend,yText,popTextSize){
	par(xaxt='n',xpd=NA,bty='n')
	theX=seq(1,length(Param1$wbj_mean))
	theY1=Param1$wbj_mean

	lowY1=Param1$wbj_mean-2.0*sqrt(Param1$wbj_var)
	highY1=Param1$wbj_mean+2.0*sqrt(Param1$wbj_var)
	theY2=Param2$wbj_mean
	lowY2=Param2$wbj_mean-2.0*sqrt(Param2$wbj_var)
	highY2=Param2$wbj_mean+2.0*sqrt(Param2$wbj_var)
	p1_names=Param1$pop1
	p2_names=Param1$pop2



	plot(theX,theY1[theOrder],pch=19,cex=0.5,col='blue',ylim=c(yLow,yHigh),xlab='pop2',ylab=yText,main='pop1',font.main=1,cex.main=1)
	segments(0,0,length(theX),0,lty=3)
	segments(theX,lowY1[theOrder],theX,highY1[theOrder],col='blue')

	points(theX,theY2[theOrder],pch=19,cex=0.5,col='red')
	segments(theX,lowY2[theOrder],theX,highY2[theOrder],col='red')


	text(theX,1.01*yHigh,p1_names[theOrder],srt=90,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(theX,yLow,p2_names[theOrder],srt=90,cex=popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doLegend==1){
		legend('center',legend=c('pop1','pop2'),pch=19,col=c('blue','red'))
	}	
	return(0)
}




plotParam2axis=function(Param1,Param2,yLow,yHigh,theOrder,doLegend,yText,popTextSize,transformScale,transformText){
	par(xaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))
	theX=seq(1,length(Param1$wbj_mean))
	theY1=Param1$wbj_mean

	lowY1=Param1$wbj_mean-2.0*sqrt(Param1$wbj_var)
	highY1=Param1$wbj_mean+2.0*sqrt(Param1$wbj_var)
	theY2=Param2$wbj_mean
	lowY2=Param2$wbj_mean-2.0*sqrt(Param2$wbj_var)
	highY2=Param2$wbj_mean+2.0*sqrt(Param2$wbj_var)
	p1_names=Param1$pop1
	p2_names=Param1$pop2

	plot(theX,theY1[theOrder],pch=19,cex=0.5,col='blue',ylim=c(yLow,yHigh),xlab='pop2',ylab=yText,main='pop1',font.main=1,cex.main=1)
	#segments(0,0,length(theX),0,lty=3)
	segments(theX,lowY1[theOrder],theX,highY1[theOrder],col='blue')

	points(theX,theY2[theOrder],pch=19,cex=0.5,col='red')
	segments(theX,lowY2[theOrder],theX,highY2[theOrder],col='red')


	text(theX,1.01*yHigh,p1_names[theOrder],srt=90,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(theX,yLow,p2_names[theOrder],srt=90,cex=popTextSize,col=sapply(p2_names[theOrder],myGetColor))
	if (doLegend==1){
		legend('center',legend=c('pop1','pop2'),pch=19,col=c('blue','red'))
	}	

	par(new=T)
	plot(theX,theY1[theOrder],pch=19,cex=0.5,type='n',xlab='',ylab='',ylim=c(transformScale*yLow,transformScale*yHigh),axes=F)
	axis(side=4)
	mtext(side=4,line=3,transformText)
	return(0)
}


plot1Param2axis=function(Param1,ParamCol,yLow,yHigh,theOrder,doLegend,yText,popTextSize,transformScale,transformText){
	par(xaxt='n',xpd=NA,bty='n')
	par(mar = c(5,5,5,5))
	theX=seq(1,length(Param1$wbj_mean))
	theY1=Param1$wbj_mean

	lowY1=Param1$wbj_mean-2.0*sqrt(Param1$wbj_var)
	highY1=Param1$wbj_mean+2.0*sqrt(Param1$wbj_var)
	p1_names=Param1$pop1
	p2_names=Param1$pop2

	plot(theX,theY1[theOrder],pch=19,cex=0.5,col=ParamCol,ylim=c(yLow,yHigh),xlab='pop2',ylab=yText,main='pop1',font.main=1,cex.main=1)
	segments(theX,lowY1[theOrder],theX,highY1[theOrder],col=ParamCol)



	text(theX,1.01*yHigh,p1_names[theOrder],srt=90,cex=popTextSize,col=sapply(p1_names[theOrder],myGetColor))
	text(theX,yLow,p2_names[theOrder],srt=90,cex=popTextSize,col=sapply(p2_names[theOrder],myGetColor))

	par(new=T)
	plot(theX,theY1[theOrder],pch=19,cex=0.5,type='n',xlab='',ylab='',ylim=c(transformScale*yLow,transformScale*yHigh),axes=F)
	axis(side=4)
	mtext(side=4,line=3,transformText)
	return(0)
}



