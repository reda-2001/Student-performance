import pandas as pd
import numpy as np
import scipy.stats as stats

class two_sample_t_test:
    
    def __init__(self,groupA,groupB,equal_variance=bool):
        self.groupA = groupA
        self.groupB = groupB
        self.equal_variance = equal_variance
        self.groupA_mean = self.groupA.mean()
        self.groupB_mean = self.groupB.mean()
        self.groupA_var = pow(self.groupA.describe().loc['std'],2)
        self.groupB_var = pow(self.groupB.describe().loc['std'],2)
        self.nA = len(groupA)
        self.nB = len(groupB)
        
    
        
    def t_test(self):
        
        if(self.equal_variance == False):
                    
            t_statistic = (self.groupA_mean-self.groupB_mean)/(np.sqrt((self.groupA_var/self.nA)+(self.groupB_var/self.nB)))
            
            df_num = pow((self.groupA_var/self.nA)+(self.groupB_var/self.nB),2)
            df_denum = pow(self.groupA_var/self.nA,2)/((self.nA)-1)+pow(self.groupB_var/self.nB,2)/(self.nB-1)
            degree_of_freedom = df_num/df_denum 
            
            p_value = stats.t.sf(t_statistic,degree_of_freedom)*2
            
        
        else:
            t_statistic_num  =(self.groupA_mean-self.groupB_mean)*np.sqrt(self.nA+self.nB-2)
            t_statistic_denum = np.sqrt(((self.nA-1)*self.groupA_var+(self.nB-1)*self.groupB_var)*((1/self.nA)+(1/self.nB)))
            
            t_statistic = t_statistic_num/t_statistic_denum
            
            degree_of_freedom = self.nA+self.nB-2
            
            p_value = stats.t.sf(t_statistic,degree_of_freedom)*2
            
        return t_statistic , p_value
            
    