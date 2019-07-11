import numpy as np 
import cv2

img=cv2.imread('pixelate_ps.jpeg')

fromcenter=False
r=cv2.selectROI("image",img,fromcenter)  #(x,y,w,h)
b=img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]  #(y:y+h , x:x+w)
#b is the cropped image
#print(r)
#cv.imshow("cropped",b)

test=img

lr=np.array([b[:,:,0].min()-40,b[:,:,1].min()-40,b[:,:,2].min()-40])
ur=np.array([b[:,:,0].max()+40,b[:,:,1].max()+40,b[:,:,2].max()+40])
print(lr,ur)
new1=cv2.inRange(img,lr,ur)   #new1 is binary image
cv2.imshow("new1",new1)
cv2.waitKey(0)
cv2.destroyAllWindows()

a=np.zeros((9,9))
print(img.shape)

#  SIGN CONVENTION
# 1- Red triangle
# 2- Red SQuare
# 3- Red circle
# 4- Yellow triangle
# 5- Yellow square
# 6- Yellow circle
# 7- Black arrow
# 8- Home

a[4][4]=8
a[0][4]=7
a[4][0]=7
a[8][4]=7
a[4][8]=7

'''
#            SHAPE DETECTION USING CONTOURS APPROXIMATION
#finding contours on the binary image
_, contours ,_ = cv2.findContours(new1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#drawing contours on original image
print(len(contours))
count=0
for c in contours:
	area=cv2.contourArea(c)
	if(area>150):
		count=count+1
		M = cv2.moments(c)
		approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True) #approximating contours
		cv2.drawContours(img, [approx], 0, (0,0,0), 2)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
		print(len(approx))   #yahan approx ki jagah cnt rakhne pe not useful numbers
		#4 wala square, 3 wala triangle, 16 ya near wale circle
		if(len(approx)==3):
			print('Triangle')
			cv2.putText(img, "triangle", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
		elif(len(approx)==4):
			print('Square')
			cv2.putText(img, "square", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
		elif(len(approx)>10):
			print('Circle')
			cv2.putText(img, "circle", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
		else:
			print('no idea')
			cv2.putText(img, "no idea", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
print(count)

cv2.imshow('contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

w1=961/9
w2=959/9
print(w1,w2)

#         SHAPE DETECTION USING BOUNDING BOX AREA
_, contours ,_ = cv2.findContours(new1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#drawing contours on original image
print(len(contours))
count=0
for c in contours:
	area=cv2.contourArea(c)
	if(area>200):
		count=count+1
		approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True) #approximating contours
		cv2.drawContours(img, [approx], 0, (0,0,0), 2)
		area_shape=cv2.contourArea(c)
		x,y,w,h=cv2.boundingRect(c)
		area_rect=w*h
		ratio=area_shape/area_rect
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		cv2.circle(img, (cX, cY), 5, (0, 0, 0), -1)
		#print(ratio)
		if(ratio<0.6 and ratio>0.4):
			print('Triangle')
			cv2.putText(img, "triangle", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
			a[int(cY//w2)][int(cX//w1)]=1
		elif(ratio<=1 and ratio>0.9):
			print('Square')
			cv2.putText(img, "square", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
			a[int(cY//w2)][int(cX//w1)]=2
		elif(ratio<0.9 and ratio>0.7):
			print('Circle')
			cv2.putText(img, "circle", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
			a[int(cY//w2)][int(cX//w1)]=3
		else:
			print('no idea')
			cv2.putText(img, "no idea", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
print(count)
print("nxt")

cv2.imshow("immm",test)


#      FOR YELLOW
fromcenter=False
r=cv2.selectROI("image1",test,fromcenter)  #(x,y,w,h)
b=img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]  #(y:y+h , x:x+w)
ll=np.array([b[:,:,0].min()-40,b[:,:,1].min()-40,b[:,:,2].min()-40])
ul=np.array([b[:,:,0].max()+40,b[:,:,1].max()+40,b[:,:,2].max()+40])
print(ll,ul)
new2=cv2.inRange(test,ll,ul)   #new1 is binary image
cv2.imshow("new2",new2)
cv2.waitKey(0)
cv2.destroyAllWindows()
_, contours ,_ = cv2.findContours(new2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#drawing contours on original image
print(len(contours))
count=0
for c in contours:
	area=cv2.contourArea(c)
	if(area>200):
		count=count+1
		approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True) #approximating contours
		cv2.drawContours(img, [approx], 0, (0,0,0), 2)
		area_shape=cv2.contourArea(c)
		x,y,w,h=cv2.boundingRect(c)
		area_rect=w*h
		ratio=area_shape/area_rect
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		cv2.circle(img, (cX, cY), 5, (0, 0, 0), -1)
		#print(ratio)
		if(ratio<0.6 and ratio>0.4):
			print('Triangle')
			cv2.putText(img, "triangle", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
			a[int(cY//w2)][int(cX//w1)]=4
		elif(ratio<=1 and ratio>0.9):
			print('Square')
			cv2.putText(img, "square", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
			a[int(cY//w2)][int(cX//w1)]=5
		elif(ratio<0.9 and ratio>0.7):
			print('Circle')
			cv2.putText(img, "circle", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
			a[int(cY//w2)][int(cX//w1)]=6
		else:
			print('no idea')
			cv2.putText(img, "no idea", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
print(count)


for i in range(9):
	for j in range(9):
		print(a[i][j],end='  ')
	print(end='\n')
	print(end='\n')

print("****************")
cv2.imshow('contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np

#       PATH SEARCHING ON MATRIX A
work=np.zeros((9,9));
work[4][0]=1;work[3][0]=2;work[2][0]=3;work[1][0]=4;
for j in range(9):
	work[0][j]=(j+5)
for i in range(1,9):
	work[i][8]=(i+13)
work[8][7]=22;work[8][6]=23;work[8][5]=24;work[8][4]=25;
work[8][3]=26;work[8][2]=27;work[8][1]=28;work[8][0]=29;
work[7][0]=30;work[6][0]=31;work[5][0]=32;
work[4][1]=33;work[1][4]=34;work[4][7]=35;work[7][4]=36;
work[4][2]=37;work[3][2]=38;
for j in range(2,7):
	work[2][j]=(j+37)
for i in range(3,7):
	work[i][6]=(i+41)
work[6][5]=48;work[6][4]=49;work[6][3]=50;work[6][2]=51;
work[5][2]=52;work[4][3]=53;work[3][4]=54;work[4][5]=55;
work[5][4]=56;work[4][4]=57;

nodes=57
edges=64

v=[]
for i in range(58):
	v.append([])
for i in range(1,33):
	if((i+1)%32!=0):
		v[i].append((i+1)%32)
	else:
		v[i].append(i+1)
for i in range(38,52):
	v[i].append(i+1)
v[52].append(37)
#bidirected nodes
#v[1].append(33)
#v[33].append(1)
v[33].append(37)
v[37].append(33)
v[9].append(34)
v[34].append(9)
v[34].append(41)
v[41].append(34)
v[17].append(35)
v[35].append(17)
v[35].append(45)
v[45].append(35)
v[25].append(36)
v[36].append(25)
v[36].append(49)
v[49].append(36)
v[37].append(53)
v[53].append(57)

for i in range(9):
	for j in range(9):
		print(work[i][j],end='  ')
	print(end='\n')
	print(end='\n')

for i in range(len(v)):
	if(len(v[i])==0):
		continue;
	print(i,": ",end=" ")
	for j in range(len(v[i])):
		print(v[i][j],end=" ")
	print("")

#print(v)


#BFS FUNCTION
c=[]
done=0
def bfs(x,vis,p,aux):
	global c
	global a
	global done
	c=[]
	c.append(x)
	pat=[]
	while(len(c)):
		s=c[0]
		wi=-1
		if(s!=x or done==2):
			pat.append(s)
			for i in range(9):
				if(wi!=-1):
					done =1
					break
				for j in range(9):
					if(work[i][j]==s):
						wi=i
						wj=j
						break
			if(a[wi][wj]==p):
				#print(wi,wj)
				return pat
		c.remove(c[0])
		if(len(v[s])==2):
			return pat
		for i in v[s]:
			print("i am goin in queue",i,v[s],c)
			c.append(i)


#PATH PRINTING
t=3
while(t):
	t-=1
	p=int(input())
	start=1
	vis=[]
	for i in range(100):
		vis.append(0)
	done=0
	pat=bfs(start,vis,p,[])
	if(done==0):
		done =2
		q1=bfs(v[pat[len(pat)-1]][0],vis,p,pat)
		q2=bfs(v[pat[len(pat)-1]][1],vis,p,pat)
		if(len(q1)>len(q2)):
			pat=q2
		else:
			pat=q1
	start=pat[len(pat)-1]
	print(start)
	print(*pat)