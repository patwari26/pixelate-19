import cv2 as cv
import numpy as np
import time
import serial
import urllib.request as ur
import math
import forward
# url='http://192.168.137.116:8080/shot.jpg'
# def captu():
# 	imgr = ur.urlopen(url)
# 	imgNp=np.array(bytearray(imgr.read()),dtype=np.uint8)
# 	img=cv.imdecode(imgNp,-1)
# 	return img

cap=cv.VideoCapture(1)
cap.set(3,960)
cap.set(4,1280)
#print(ser.name)

re,frame=cap.read()
# cv.imshow("gb",frame)
a=frame.copy()
#a=cv.imread("aaa1.jpg")
#cv.imshow("ada",a)
pi=math.pi
n=10
#***
# RED TRIANGLE = 1
# RED SQUARE = 2
# RED CIRCLE = 3
# YELLOW TRIANGLE = 4
# YELLOW SQUARE = 5
# YELLOW CIRCLE = 6
#***INTIALIZING MATRIX***#
A=[]
G=[]
ini=0
for i in range(n):
	A.append([])
	G.append([])
	for j in range(n):
		A[i].append(0)
		G[i].append(0)
#***RED COLOR*****#
cro=cv.selectROI("im2",a,False)
crod=a[cro[1]:cro[1]+cro[3],cro[0]:cro[0]+cro[2]]
# kernel = np.ones((5,5),np.float32)/25
# crod = cv.filter2D(crod,-1,kernel)
h,w,dep=crod.shape
print(h,w)
y1=h//9+3
x1=w//9+3
r=cv.selectROIs("image",crod,False)
t=0
pinky=[]

ree=37
yee=28
pee=30
bee=30
perfect=[]
midix=h//9
midiy=w//9

for i in range(10):
	for j in range(10):
		G[i][j]=[midiy//2+j*w//9,i*h//9+midix//2]
for ri in r:
	# if(t==9 or t==6):
	# 	continue
	print("hello")
	b=crod[ri[1]:ri[1]+ri[3],ri[0]:ri[0]+ri[2]]
	if(t==0):
		lr=np.array([b[:,:,0].min()-ree,b[:,:,1].min()-ree,b[:,:,2].min()-ree])
		ur=np.array([b[:,:,0].max()+ree,b[:,:,1].max()+ree,255])
	elif(t==3):
		lr=np.array([b[:,:,0].min()-yee,b[:,:,1].min()-yee,b[:,:,2].min()-yee])
		ur=np.array([b[:,:,0].max()+yee,b[:,:,1].max()+yee,b[:,:,2].max()+yee])
	elif(t==6):
		lr=np.array([b[:,:,0].min()-pee,b[:,:,1].min()-pee,b[:,:,2].min()-pee])
		#ur=[166,147,194]
		ur=np.array([b[:,:,0].max()+pee,b[:,:,1].max()+pee,b[:,:,2].max()+pee])
		pink_low=lr
		pink_high=ur
	else:
		#lr=np.array[68,112,196]
		#ur=np.array[68,113,200]
		lr=np.array([b[:,:,0].min()-bee,b[:,:,1].min()-bee,b[:,:,2].min()-bee])
		#ur=[58,122,157]
		ur=np.array([b[:,:,0].max()+bee,b[:,:,1].max()+bee,b[:,:,2].max()+bee])
		brown_low=lr
		brown_high=ur
	print(lr,ur)
	thresh_red=cv.inRange(crod,lr,ur)
	_, threshold = cv.threshold(thresh_red, 240, 255, cv.THRESH_BINARY)
	kernel = np.ones((7,7),np.uint8)
	threshold = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
	_,contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	font = cv.FONT_HERSHEY_COMPLEX
	fsize=0.5
	cv.imshow("Dadadad",threshold)
	cv.waitKey(0)
	cv.destroyAllWindows()
	
	for cnt in contours:
		approx = cv.approxPolyDP(cnt, 0.03*cv.arcLength(cnt, True), True)
		cv.drawContours(crod, [approx], 0, (0), 5)
		x=approx.ravel()[0]
		y=approx.ravel()[1]
		M=cv.moments(cnt)
		area = cv.contourArea(cnt)
		if(M['m00']!=0 and area>=80):
			gx=M['m10']//M['m00']
			gy=M['m01']//M['m00']
			if(t==6):
				botu=[gx,gy]
				continue
			elif(t==9):
				botd=[gx,gy]
				continue
			#print(gx,gy,len(approx))
			cy=int(gx//y1)
			cx=int(gy//x1)
			G[cx][cy]=[gx,gy]
			if(A[cx][cy]!=0):
				perfect.append([cx,cy])
			if(len(approx)==3):
				A[cx][cy]=1+t
				cv.putText(crod, "Triangle", (x, y), font, fsize, (0))
			elif len(approx) == 4:
				A[cx][cy]=2+t
				cv.putText(crod, "Rectangle", (x, y), font, fsize, (0))
			else:
				A[cx][cy]=3+t
				cv.putText(crod,"Circle",(x,y),font,fsize,(0))
	t+=3
	# cv.imshow("cc",threshold)
	# cv.imshow("cc1",a)
	# cv.waitKey(0)
	# cv.destroyAllWindows()
print("Here are the bot centroids:")
print(botu,botd)

#####################################


for i in perfect:
	A[i[0]][i[1]]=4


#manual centroids


#####################################

for i in range(n):
	for j in range(n):
		print(G[i][j],end=" ")
	print("")
cv.imshow("cc",thresh_red)
cv.imshow("cc1",a)
cv.waitKey(0)
cv.destroyAllWindows()

#a=[[1,2,3,4,5],[6,7,8,9,1],[1,2,3,4,5],[2,3,4,5,5],[2,3,4,5,6]]


for i in range(9):
	for j in range(9):
		print(A[i][j],end=" ")
	print(" ")


###############################

def bot_vector():
	ret,ss=cap.read()
	
	global cro
	crod=ss[cro[1]:cro[1]+cro[3],cro[0]:cro[0]+cro[2]]
	# cv.imshow("dada1",crod)
	# cv.waitKey(0)
	# kernel = np.ones((5,5),np.float32)/25
	# crod = cv.filter2D(crod,-1,kernel)
	thresh_red=cv.inRange(crod,pink_low,pink_high)
	print("dadada :",pink_low,pink_high)
	#thresh_red=cv.inRange(crod,lr,ur)
	_, threshold = cv.threshold(thresh_red, 240, 255, cv.THRESH_BINARY)
	kernel = np.ones((7,7),np.uint8)
	threshold = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
	_,contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	# cv.imshow("dada",threshold)
	# cv.waitKey(0)

	for cnt in contours:
		M=cv.moments(cnt)
		area = cv.contourArea(cnt)
		if(M['m00']!=0 and area>=80):
			gx=M['m10']//M['m00']
			gy=M['m01']//M['m00']
			botu=[gx,gy]
	
	thresh_red=cv.inRange(crod,brown_low,brown_high)
	_,contours,hie = cv.findContours(thresh_red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		M=cv.moments(cnt)
		area = cv.contourArea(cnt)
		if(M['m00']!=0 and area>=80):
			gx=M['m10']//M['m00']
			gy=M['m01']//M['m00']
			botd=[gx,gy]
	#cv.imshow("ada",threshold)
	botv=[botu[0]-botd[0],botu[1]-botd[1]]
	print("botv :",botu,botd,botv)
	centi=[(botu[0]+botd[0])//2,(botu[1]+botd[1])//2]
	print(centi)
	return botv,centi



def cross_product(v2,v1):
	mag=0
	mag=v2[0]*v1[1]-v2[1]*v1[0]
	siz=(math.sqrt(v1[0]*v1[0]+v1[1]*v1[1]))*(math.sqrt(v2[0]*v2[0]+v2[1]*v2[1]))
	if siz==0:
		return 0
	return mag/siz


def dist(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

#############

a=A.copy()

# print(a)
edge=[]
for i in range(81):
	edge.append([])
for i in range(8):
	edge[i].append(i+1)
for i in range(8):
	edge[i*9+8].append((i+1)*9+8)
for i in range(8):
	edge[80-i].append(79-i)
for i in range(8):
	edge[(i+1)*9].append(i*9)
for i in range(4):
	edge[20+i].append(20+i+1)
for i in range(4):
	edge[i*9+24].append((i+1)*9+24)
for i in range(4):
	edge[60-i].append(59-i)
for i in range(4):
	edge[(i+1)*9+20].append(i*9+20)
# edge[4].append(13);
# edge[13].append(22);edge[13].append(4);edge[22].append(13)
edge[36].append(37);edge[37].append(38);edge[37].append(36);edge[38].append(37)
edge[44].append(43);edge[43].append(42);edge[43].append(44);edge[42].append(43)
edge[76].append(67);edge[67].append(58);edge[67].append(76);edge[58].append(67)
edge[22].remove(23)
edge[22].append(31)
edge[13].append(22)
# for i in edge:
# 	print(i)
x=53
mydir=[0,1]
vis=[]
parent=[]
t=0
for i in range(81):
	vis.append(0)
	parent.append(0)
while(x!=31):
	xip=x
	for i in range(81):
		vis[i]=0
	y=int(input())
	l=[]
	j=0
	indi=x//9
	indj=x%9
	l.append(x)
	count=0
	while(len(l)!=j):
		vis[l[j]]=1
		if(a[l[j]//9][l[j]%9]==y and count!=0):
			indi=l[j]//9
			indj=l[j]%9
			break
		count+=1
		for jj in edge[l[j]]:
			if(vis[jj]==1):
				continue
			l.append(jj)
			parent[jj]=l[j]
		j+=1
		if(t==0):
			edge[4].append(13)
			edge[4].remove(5)
			t=1
	mypath=[]
	xi=indi*9+indj
	while(xi!=x):
		mypath.append([xi//9,xi%9])
		xi=parent[xi]
	mypath.reverse()
	mypathdir=[]
	for i in mypath:
		# print(xip)
		# print(xip//5+mydir[0],i[0])
		if xip//9+mydir[0]==i[0] and xip%9+mydir[1]==i[1]:
			mypathdir.append("F")
		else:
			if(mydir[0]*(i[0]-xip//9)==-1 or mydir[1]*(i[1]-xip%9)==-1):
				mypathdir.append("R")
				mypathdir.append("R")
				mypathdir.append("F")
			else:
				mypathdir.append("R")
				mypathdir.append("F")
			# print(i[0],xip//5)
			mydir[0]=i[0]-xip//9
			mydir[1]=i[1]-xip%9
		xip=i[0]*9+i[1]
	x=indi*9+indj
	# print(mypath)
	print(mypathdir)

	#G[1][1]=[355,225]

#def move_to(x,y):
	#mypath=[[1,1]]
	#mypathdir=['F']


	#botv=[botu[0]-botd[0],botu[1]-botd[1]]
	#centi=[(botu[0]+botd[0])//2,(botu[1]+botd[1])//2]
	ii=0
	w=0
	for q in mypathdir:
		# botv,centi=bot_vector(ss)
		# next_block_x=G[j[0]][j[1]][0]
		# next_block_y=G[j[0]][j[1]][1]
		# move_to(next_block_x,next_block_y)
		# pathv=[next_block_x-centi[0],next_block_y-centi[1]]
		#sintheta=0
		# sintheta=cross_product(pathv,botv)
		if(q=='F'):
			jii=mypath[ii]
			ret,ss=cap.read()
			#ss=captu()
			botv,centi=bot_vector()
			xc='k'
			next_block_x=G[jii[0]][jii[1]][0]
			next_block_y=G[jii[0]][jii[1]][1]
			print("next:",end=" ")
			print(next_block_x,next_block_y)
			while(dist(centi[0],centi[1],next_block_x,next_block_y)>20):
				#after forward
				ret,ss=cap.read()
				#ss=captu()
				botv,centi=bot_vector()
				next_block_x=G[jii[0]][jii[1]][0]
				next_block_y=G[jii[0]][jii[1]][1]				
				pathv=[next_block_x-centi[0],next_block_y-centi[1]]
				sintheta=cross_product(pathv,botv)
				#while()
				print("pathvector :",pathv,botv,centi)
				print("sintheta :",sintheta)
				while((sintheta>0.3) or sintheta<-0.3):
					print("sintheta :",sintheta)
					botv,centi=bot_vector()
					next_block_x=G[jii[0]][jii[1]][0]
					next_block_y=G[jii[0]][jii[1]][1]				
					pathv=[next_block_x-centi[0],next_block_y-centi[1]]
					sintheta=cross_product(pathv,botv)
					if(sintheta>0.3):
						print('l')
						forward.ligh()
						#time.sleep(0.1)
					elif(sintheta<-0.3):
						print('r')
						forward.righ()
				#ret,ss=cap.read()
				print('f')
				forward.forw()
				#after forward
				#ret,ss=cap.read()
				#ss=captu()
				botv,centi=bot_vector()
				next_block_x=G[jii[0]][jii[1]][0]
				next_block_y=G[jii[0]][jii[1]][1]			
				pathv=[next_block_x-centi[0],next_block_y-centi[1]]
				sintheta=cross_product(pathv,botv)
			print('s')
			ii+=1
		if(q=='R' and mypathdir[w+1]!='R'):
			ret,ss=cap.read()
			#ss=captu()
			botv,centi=bot_vector()
			next_block_x=G[jii[0]][jii[1]][0]
			next_block_y=G[jii[0]][jii[1]][1]
			pathv=[next_block_x-centi[0],next_block_y-centi[1]]
			sintheta=cross_product(pathv,botv)
			while((sintheta>0.3) or sintheta<-0.3):
					botv,centi=bot_vector()
					next_block_x=G[jii[0]][jii[1]][0]
					next_block_y=G[jii[0]][jii[1]][1]				
					pathv=[next_block_x-centi[0],next_block_y-centi[1]]
					sintheta=cross_product(pathv,botv)
					if(sintheta<-0.4):
						print('r')
						forward.righ()
					elif(sintheta>0.4):
						print('l')
						forward.ligh()
		if(q=='R' and mypathdir[w+1]=='R'):
			print('r')
			forward.fullright()
			# botv,centi=bot_vector()
			# next_block_x=G[j[0]][j[1]][0]
			# next_block_y=G[j[0]][j[1]][1]
			# pathv=[next_block_x-centi[0],next_block_y-centi[1]]
			# sintheta=cross_product(pathv,botv)
			# while((sintheta>0.4) or sintheta<-0.4):
			# 		botv,centi=bot_vector()
			# 		next_block_x=G[j[0]][j[1]][0]
			# 		next_block_y=G[j[0]][j[1]][1]				
			# 		pathv=[next_block_x-centi[0],next_block_y-centi[1]]
			# 		sintheta=cross_product(pathv,botv)
			# 		if(sintheta<-0.3):
			# 			print('r')
			# 			forward.righ()
			# 		elif(sintheta>0.1):
			# 			print('l')
			# 			forward.ligh()

		w+=1