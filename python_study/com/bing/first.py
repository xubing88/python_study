# -*- coding: utf-8 -*-
'''
Created on Sep 16, 2010
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

@author: bing
'''
import kNN;
import requests

##看高手写代码，不然好多东西都不知道怎么用，原来可以这么用，这就叫跟高手过招，天天搞自己的一亩半分田 没意思
##第一个class
class myclass():
    def __init__(self,name,age):##初始化发放
        self.name=name
        self.age=age
    
    def get_age(self):##定义函数
        print self.age
    '''raise用法'''
    def testException(self,num):
        if num>10:
            raise NumException()

class NumException():
    def _init_(self):
        print 'exception'
        
if __name__ == '__main__':
    group, labels = kNN.createDataSet()
    result = kNN.classify0([1,3], group, labels, 3)
    print result
    ##测试requests库
    r = requests.get('http://www.baidu.com', auth=('user', 'pass'))
    print r.status_code
    print r.text
    #print r.headers['content-type'] 
    '''
    :param  a  value;
    :param  b  value b;
    '''
    myobj = myclass(age = 18,name= 'bing')##根据名字匹配，而不是顺序
    print myobj.age;
    myobj.get_age()
    myobj.testException(12)   #测试异常  2
    
