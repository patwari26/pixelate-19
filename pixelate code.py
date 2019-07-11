import cv2 as cv
import numpy as np
import time
import serial
import math
cap=cv.VideoCapture(1)
ser= serial.Serial('COM11',9600)
print(ser.name)
#a=cv.imread("aaa1.jpg")
re,frame=cap.read()
a=frame.copy()
#cv.imshow("ada",a)

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
h,w,dep=crod.shape
print(h,w)
y1=h//5+5
x1=w//5+5
r=cv.selectROIs("image",crod,False)
t=0
pinky=[]
ree=37
yee=37
pee=16
bee=16
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
	
	for cnt in contours:
		approx = cv.approxPolyDP(cnt, 0.03*cv.arcLength(cnt, True), True)
		cv.drawContours(crod, [approx], 0, (0), 5)
		x=approx.ravel()[0]
		y=approx.ravel()[1]
		M=cv.moments(cnt)
		area = cv.contourArea(cnt)
		if(M['m00']!=0 and area>=100):
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
for i in range(n):
	for j in range(n):
		print(A[i][j],end=" ")
	print("")
cv.imshow("cc",threshold)
cv.imshow("cc1",a)
cv.waitKey(0)
cv.destroyAllWindows()

#a=[[1,2,3,4,5],[6,7,8,9,1],[1,2,3,4,5],[2,3,4,5,5],[2,3,4,5,6]]


###############################

def bot_vector(ss):
	global cro
	alp=ss[cro[1]:cro[1]+cro[3],cro[0]:cro[0]+cro[2]]
	thresh_red=cv.inRange(crod,pink_low,pink_high)
	_, threshold = cv.threshold(thresh_red, 240, 255, cv.THRESH_BINARY)
	kernel = np.ones((5,5),np.uint8)
	threshold = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
	_,contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		M=cv.moments(cnt)
		area = cv.contourArea(cnt)
		if(M['m00']!=0 and area>=100):
			gx=M['m10']//M['m00']
			gy=M['m01']//M['m00']
			botu=[gx,gy]
	thresh_red=cv.inRange(crod,brown_low,brown_high)
	_, threshold = cv.threshold(thresh_red, 240, 255, cv.THRESH_BINARY)
	kernel = np.ones((5,5),np.uint8)
	threshold = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
	_,contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		M=cv.moments(cnt)
		area = cv.contourArea(cnt)
		if(M['m00']!=0 and area>=100):
			gx=M['m10']//M['m00']
			gy=M['m01']//M['m00']
			botd=[gx,gy]
	cv.imshow("ada",threshold)
	botv=[botu[0]-botd[0],botu[1]-botd[1]]
	centi=[(botu[0]+botd[0])//2,(botu[1]+botd[1])//2]

	return botv,centi



def cross_product(v2,v1):
	mag=0
	mag=v2[0]*v1[1]-v2[1]*v1[0]
	#siz=(math.sqrt(v1[0]*v1[0]))*(math.sqrt(v2[0]*v2[0]))
	siz=(math.sqrt(v1[0]*v1[0]+v1[1]*v1[1]))*(math.sqrt(v2[0]*v2[0]+v2[1]*v2[1]))
	if(siz==0):
		return 0
	return mag/siz


def dist(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

#############

a=A.copy()
edge=[]
for i in range(25):
	edge.append([])
edge[0].append(1);edge[1].append(2);edge[2].append(3);edge[3].append(4);edge[4].append(9);
edge[9].append(14);edge[14].append(19);edge[19].append(24);edge[24].append(23);edge[23].append(22);
edge[22].append(21);edge[21].append(20);edge[20].append(15);edge[15].append(10);edge[10].append(5);edge[5].append(0);
# edge[2].append(7);edge[7].append(2);edge[14].append(13);edge[13].append(14);edge[22].append(17);edge[17].append(22);

for i in a:
	for j in range(len(i)):
		print(i[j],end=" ")
	print("")

pi=math.pi

x=10
mydir=[-1,0]
vis=[]
parent=[]
t=0
for i in range(25):
	vis.append(0)
	parent.append(0)
while(x!=11):
	xip=x
	for i in range(25):
		vis[i]=0
	y=int(input())
	l=[]
	j=0
	indi=x//5
	indj=x%5
	l.append(x)
	count=0
	while(len(l)!=j):
		vis[l[j]]=1
		if(a[l[j]//5][l[j]%5]==y and count!=0):
			indi=l[j]//5
			indj=l[j]%5
			break
		count+=1
		for jj in edge[l[j]]:
			if(vis[jj]==1):
				continue
			l.append(jj)
			parent[jj]=l[j]
		j+=1
		if(t==0):
			edge[10].append(11)
			edge[10].remove(5)
			t=1
	mypath=[]
	xi=indi*5+indj
	while(xi!=x):
		mypath.append([xi//5,xi%5])
		xi=parent[xi]
	mypath.reverse()
	mypathdir=[]
	for i in mypath:
		# print(xip)
		# print(xip//5+mydir[0],i[0])
		if xip//5+mydir[0]==i[0] and xip%5+mydir[1]==i[1]:
			mypathdir.append("F")
		else:
			if(mydir[0]*(i[0]-xip//5)==-1 or mydir[1]*(i[1]-xip%5)==-1):
				mypathdir.append("R")
				mypathdir.append("R")
				mypathdir.append("F")
			else:
				mypathdir.append("R")
				mypathdir.append("F")
			# print(i[0],xip//5)
			mydir[0]=i[0]-xip//5
			mydir[1]=i[1]-xip%5
		xip=i[0]*5+i[1]
	x=indi*5+indj
	print(mypath)
	print(mypathdir)


#def move_to(x,y):



	#botv=[botu[0]-botd[0],botu[1]-botd[1]]
	#centi=[(botu[0]+botd[0])//2,(botu[1]+botd[1])//2]
	i=0
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
			j=mypath[i]
			ret,ss=cap.read()
			#ss=captu()
			botv,centi=bot_vector(ss)
			next_block_x=G[j[0]][j[1]][0]
			next_block_y=G[j[0]][j[1]][1]

			while(dist(centi[0],centi[1],next_block_x,next_block_y)>10):
				#after forward
				ret,ss=cap.read()
				#ss=captu()
				botv,centi=bot_vector()
				next_block_x=G[j[0]][j[1]][0]
				next_block_y=G[j[0]][j[1]][1]				
				pathv=[next_block_x-centi[0],next_block_y-centi[1]]
				sintheta=cross_product(pathv,botv)
				#while()
				while((sintheta>0.18) or sintheta<-0.18):
					ret,ss=cap.read()
					botv,centi=bot_vector()
					next_block_x=G[j[0]][j[1]][0]
					next_block_y=G[j[0]][j[1]][1]				
					pathv=[next_block_x-centi[0],next_block_y-centi[1]]
					sintheta=cross_product(pathv,botv)
					if(sintheta<-0.1):
						ser.write(b'r')
						print('r')
						#time.sleep(0.1)
						ser.write(b's')
						print('s')
					elif(sintheta>0.1):
						ser.write(b'l')
						print('l')
						#time.sleep(0.1)
						ser.write(b's')
						print('s')
				#ret,ss=cap.read()
				ser.write(b'f')
				print('f')
				time.sleep(0.2)
				ser.write(b's')
				print('s')
				#after forward
				ret,ss=cap.read()
				#ss=captu()
				botv,centi=bot_vector(ss)
				next_block_x=G[j[0]][j[1]][0]
				next_block_y=G[j[0]][j[1]][1]				
				pathv=[next_block_x-centi[0],next_block_y-centi[1]]
				sintheta=cross_product(pathv,botv)
			i+=1
		if(q=='R' and mypathdir[w+1]!='R'):
			ret,ss=cap.read()
			#ss=captu()
			botv,centi=bot_vector(ss)
			next_block_x=G[j[0]][j[1]][0]
			next_block_y=G[j[0]][j[1]][1]
			pathv=[next_block_x-centi[0],next_block_y-centi[1]]
			sintheta=cross_product(pathv,botv)
			while((sintheta>0.18) or sintheta<-0.18):
					ret,ss=cap.read()
					botv,centi=bot_vector()
					next_block_x=G[j[0]][j[1]][0]
					next_block_y=G[j[0]][j[1]][1]				
					pathv=[next_block_x-centi[0],next_block_y-centi[1]]
					sintheta=cross_product(pathv,botv)
					if(sintheta<-0.1):
						ser.write(b'r')
						print('r')
						#time.sleep(0.1)
						ser.write(b's')
						print('s')
					elif(sintheta>0.1):
						ser.write(b'l')
						print('l')
						#time.sleep(0.1)
						ser.write(b's')
						print('s')
		if(q=='R' and mypathdir[w+1]=='R'):
			ser.write(b'r')
			time.sleep(0.3)
			ser.write(b's')
			ret,ss=cap.read()
			#ss=captu()
			botv,centi=bot_vector(ss)
			next_block_x=G[j[0]][j[1]][0]
			next_block_y=G[j[0]][j[1]][1]
			pathv=[next_block_x-centi[0],next_block_y-centi[1]]
			sintheta=cross_product(pathv,botv)
			while((sintheta>0.18) or sintheta<-0.18):
					ret,ss=cap.read()
					botv,centi=bot_vector(ss)
					next_block_x=G[j[0]][j[1]][0]
					next_block_y=G[j[0]][j[1]][1]				
					pathv=[next_block_x-centi[0],next_block_y-centi[1]]
					sintheta=cross_product(pathv,botv)
					if(sintheta<-0.12):
						ser.write(b'r')
						print('r')
						time.sleep(0.1)
						ser.write(b's')
						print('s')
					elif(sintheta>0.12):
						ser.write(b'l')
						print('l')
						time.sleep(0.1)
						ser.write(b's')
						print('s')

		w+=1
	ser.write(b's')
ser.write(b's')