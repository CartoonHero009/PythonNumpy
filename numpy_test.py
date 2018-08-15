#coding=utf-8

import numpy as np

def appendFn ():
  np1 = np.array([1, 2, 3])
  np2 = np.array([3, 4, 5])
  # 陣列相加
  print(np1 + np2) # [4 6 8]
  # 顯示相關資訊
  print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別

# 形状变化的原则是数组元素不能发生改变
def reShapeFn ():
  np1 = np.array([1, 2, 3, 4, 5, 6])
  np1 = np1.reshape([2, 3])
  print(np1)
  print(np1.ndim, np1.shape, np1.dtype) # 2 (2, 3) int64

def reshapeAuto():
    npz = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])
    print(npz.reshape(-1))
    print(npz.reshape(-1,1))
    print(npz.reshape(2,-1))
    #print(npz.transpose)

def complexArray():
    c1 = np.array([(1.1, 1.2, 1.3), (2.1, 2.2, 2.3)], dtype=complex)
    print("c1=>{0}".format(c1))
    print()
    c2 = np.array([2.1+6j, 3.2+9j, 4.3+12j])
    print("c2=>{0}".format(c2))
def zeroArray():
    zeros = np.zeros( (3, 5) )
    print("zeros=>{0}".format(zeros))
def onesArray():
    nes = np.ones( (3, 5) )
    print("ones=>{0}".format(ones))
def arrangeArray():
    r1 = np.arange(25, 30, .5)
    print("r1=>{0}".format(r1))
def line():
    lin = np.linspace(3, 5, 9)
    print("lin=>\n{0}".format(lin))

reShapeFn()



