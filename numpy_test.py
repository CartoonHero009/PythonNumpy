#coding=utf-8

import numpy as np

def appendFn ():
  np1 = np.array([1, 2, 3])
  np2 = np.array([3, 4, 5])
  # 陣列相加
  print(np1 + np2) # [4 6 8]
  # 顯示相關資訊
  print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別

def reShapeFn ():
  np1 = np.array([1, 2, 3, 4, 5, 6])
  np1 = np1.reshape([2, 3])
  print(np1)
  print(np1.ndim, np1.shape, np1.dtype) # 2 (2, 3) int64


reShapeFn()


