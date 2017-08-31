class BinHeap:
    def __int__(self):
        self.headList=[0]
        self.currentSize=0
    #新节点"上浮"
    def percUp(self,i):
        while i //2>0:
            if self.headList[i]<self.headList[i//2]:
                tmp=self.headList[i//2]
                self.headList[i//2]=self.headList[i]
                self.headList[i]=tmp
            i=i//2
    #插入新节点
    def insert(self,k):
        self.headList.append(k)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)
    #最后一个节点接替第一个节点的位置后下沉
    def percDown(self,i):
        while (i*2)<self.currentSize:
            mc=self.minChild(i)
            if self.headList[i]>self.headList[mc]:
                tmp=self.headList[i]
                self.headList[i]=self.headList[mc]
                self.headList[mc]=tmp
            i=mc
    #找到当前时刻最小的子结点
    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.headList[i*2]<self.headList[i*2+1]:
                return i*2
            else:
                return i*2+1
    #取出根节点
    def delMin(self):
        retval=self.headList[1]
        self.headList[1]=self.headList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.headList.pop()
        self.percDown(1)
        return retval
    #从无序列表建立堆
    def buildHeap(self,alist):
        i=len(alist)
        self.currentSize=len(alist)
        self.headList=[0]+alist[:]
        while i>0:
            self.percDown(i)
            i-=1

i=[1,9,5,6,2,3]

bh=BinHeap()
bh.buildHeap(i)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())