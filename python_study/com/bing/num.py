
import numpy as np;
from numpy.lib.shape_base import tile






if __name__ == '__main__':
     aa1 = np.array([[1,2], [7,8], [11,12],[12,12]])
     print aa1
     print aa1.shape
     print aa1[0]
     group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
     print group
     aa=(2,4)
     bb = tile(aa,(4,1))
     print aa1
     print bb
     cc = bb - aa1
     print cc
     dd=cc**2
     print 'dd is '+ dd
     ee=dd**0.5
     print  ee

     print ee
     print ee.argsort();  
     dd = ee.argsort()  
     labels=['A','B','C','D']
     
     print dd[0]
     voteIlabel = labels[dd[0]] 
     
     
    