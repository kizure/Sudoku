#!/usr/bin/python
# -*- coding:utf-8 -*-
import string
import copy
import time

#数独求解程序
class SodukuStack:
    is_right=False
    lCurrS=[]
    def __init__(self, arr):
        self.current=arr

    def resolve(self):
        lSolverStack=[self.current]
        while len(lSolverStack)>0:
            lCurrSolution=lSolverStack.pop()
            for row in lCurrSolution:
                outLine=''
                for number in row:
                    outLine=outLine + "%d" % number +' '
            isResult=True
            #用于存放当前最少候选数列表
            lMinAvailableNumber=range(1,10)
            #当前最少候选数所在位置
            lMinAvailableNumberX=0
            lMinAvailableNumberY=0
            for idx in range(81):
                i=idx%9
                j=idx//9
                if lCurrSolution[i][j]==0:
                    isResult=False
                    #计算当前位置可以放置的数字列表
                    lCurrAvailableNumber=[i for i in range(1,10)]
                    #如果同一行中存在相同元素，则排除
                    for x in range(9):
                        if lCurrAvailableNumber.count(lCurrSolution[i][x])>0:
                            lCurrAvailableNumber.remove(lCurrSolution[i][x])
                    #如果同一列中存在相同元素，则排除
                    for y in range(9):
                        if lCurrAvailableNumber.count(lCurrSolution[y][j])>0:
                            lCurrAvailableNumber.remove(lCurrSolution[y][j])
                    #如果当前位置所在的小九宫格中存在相同元素，则排除
                    for x in range(i//3*3,i//3*3+3):
                        for y in range(j//3*3,j//3*3+3):
                            if lCurrAvailableNumber.count(lCurrSolution[x][y])>0:
                                lCurrAvailableNumber.remove(lCurrSolution[x][y])
                    #如果当前单元格中可选数字个数最少，则保留
                    if len(lCurrAvailableNumber)<len(lMinAvailableNumber):
                        lMinAvailableNumber=copy.deepcopy(lCurrAvailableNumber)
                        lMinAvailableNumberX=i
                        lMinAvailableNumberY=j

                    if len(lMinAvailableNumber)==0:
                        break
            #若当前位置存在可选数字，则将当前位置的所有可选数字，依次作为临时解，并存入堆栈
            if len(lMinAvailableNumber)>0:
                for number in lMinAvailableNumber:
                    lNewSolution=copy.deepcopy(lCurrSolution)
                    lNewSolution[lMinAvailableNumberX][lMinAvailableNumberY]=number
                    lSolverStack.append(lNewSolution)
            if isResult:
                self.lCurrS=lCurrSolution
                self.is_right=isResult
                return

    def display(self):
            """打印矩阵"""
            for row in self.lCurrS:
                outLine=''
                for number in row:
                    outLine=outLine + "%d" % number +' '
                print(outLine)
