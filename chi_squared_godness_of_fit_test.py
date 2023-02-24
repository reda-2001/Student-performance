import pandas as pd
import numpy as np
import scipy.stats as stats

class chi_squared_godness_of_fit_test:
    
    def __init__(self,column):
        self.column = pd.Series(column)
 
    def bin_information(self):
        hist , bin_edges = np.histogram(self.column,bins='auto')
        return hist , bin_edges
    
    def mean(self):
        mean = 0
        for i in range(len(self.bin_information()[0])):
            mean += ((self.bin_information()[1][i+1]+self.bin_information()[1][i])/2)*self.bin_information()[0][i]
        mean = mean / len(self.column)
        return mean
        
    def std(self):
        variance = 0
        for i in range(len(self.bin_information()[0])):
            variance += pow(((self.bin_information()[1][i+1]+self.bin_information()[1][i])/2)-self.mean(),2)*self.bin_information()[0][i]                            
        variance = variance / (len(self.column)-1)
        std = np.sqrt(variance)
        return std
    
    def values(self):
        
        values = []
        for i in range(1,len(self.bin_information()[1])-1):
            values.append(self.bin_information()[1][i])
        return values
    
    def z_scores(self,values):
        z_score = (values-self.mean())/self.std()
        return z_score
        
 
    def probability(self,z_score):
                                
        prob = []
        prob.append(stats.norm.cdf(z_score[0]))
        for i in range(len(z_score)-1):
            prob.append(stats.norm.cdf(z_score[i+1]) - stats.norm.cdf(z_score[i]))
        prob.append(1-stats.norm.cdf(z_score[-1]))
        return prob

    def expected_frequencies(self,prob):
        expected_frequencies = []
        for i in range(len(self.bin_information()[0])):
            expected_frequencies.append(prob[i]*len(self.column))
        return expected_frequencies

    def chi_squared_statistic(self,expected_frequencies):
        chi_squared_statistic =0
        for i in range(len(self.bin_information()[0])):
            chi_squared_statistic += pow((self.bin_information()[0][i]-expected_frequencies[i]),2)/expected_frequencies[i]                       
        return chi_squared_statistic
            
    def p_value(self,chi_squared_statistic):
        p_value = stats.distributions.chi2.sf(chi_squared_statistic,len(self.bin_information()[0])-3)
        return p_value