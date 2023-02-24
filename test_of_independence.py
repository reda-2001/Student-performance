import pandas as pd
class chi_square_test:
    def __init__(self,row,column):
        self.column = column
        self.row = row
    
    def contingency_table(self):
        contingency_table = pd.crosstab(self.row,self.column,margins=True)
        return contingency_table
    
    def observed_values(self):
        observed_values = []
        for i in range(len(self.row.value_counts())):
            for j in range(len(self.column.value_counts())):
                observed_values.append(self.contingency_table().iloc[i][0:len(self.column.value_counts())].values[j])
        return observed_values
    
    def expected_values(self):
        total = self.contingency_table().loc['All','All']
        expected_values = []
        for i in range(len(self.row.value_counts())):
            row_total = self.contingency_table().iloc[i]['All']
            for j in range(len(self.column.value_counts())):
                col_total = self.contingency_table().iloc[:,j]['All']
                expected_values.append(col_total*row_total/total)
        return expected_values
    
    def chi_squared_value(self):
        
        chi_squared_value = sum([(self.observed_values()[i]-self.expected_values()[i])**2/self.expected_values()[i] for i in                                 range(len(self.expected_values()))])
        
        return chi_squared_value
        
        
        
        
        
        
        
        