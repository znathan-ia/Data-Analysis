
# -*- coding: utf-8 -*-
from scipy.stats import ttest_ind

class Base:
    def __init__(self, h0, h1, test_name, alpha, pvalue, test_type):
        self.h0 = h0
        self.h1 = h1
        self.test_name = test_name
        self.alpha = 0.05
        self.pvalue = pvalue
        self.test_type = test_type
        
    def check_data(x):
        quantitative, qualitative = bool
        if isinstance(x,(int, float)):          
            return quantitative
        elif isinstance(x, (str, bool, list)):           
            return qualitative
    
    
    def result(self):
        print("La nature du test est" % (self.test_name))
        print("Le parametre aplha est" % (self.alpha))
        print("L'hypothese h0 est" % (self.h0))
        print("L'hypothese h1 est" % (self.h1))
        print("La description du test est" % (self.test_type))
        
class T_de_student(Base):
    def __init__(self, h0, h1, test_name, alpha, pvalue, test_type, stat):
        Base.__init(self, h0, h1, test_name, alpha, pvalue, test_type)
        self.x = []
        self.y = []
        self.stat = stat            
            
    def test_de_student(self, X,Y):
        self.x = X       
        self.y = Y              
        self.stat, self.pvalue = ttest_ind(X,Y)
            
        
            
