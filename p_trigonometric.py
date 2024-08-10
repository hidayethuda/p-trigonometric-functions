import numpy as np


class p_trigonometric:
    
    
    def __init__(self, p):
        if p >= 0:
            raise ValueError('p must be negative')
        else:
            self.p = p
             
    def cosp(self,tetha):
        value = np.cos(tetha * np.sqrt(abs(self.p)))
        return value
     
    def sinp(self,tetha):
        value = (1 / np.sqrt(abs(self.p))) * np.sin(tetha * np.sqrt(abs(self.p)))
        return value       
    
    def tanp(self,tetha):
        value = self.sinp(tetha) / self.cosp(tetha)
        return value
    
    def asinp(self,tetha):
        value = (1 / np.sqrt(abs(self.p))) * np.arcsin(tetha * np.sqrt(abs(self.p)))
        return value  
    
    def acosp(self,tetha):
        value = (1 / np.sqrt(abs(self.p))) * np.arccos(tetha)
        return value         
    
    def atanp(self,tetha):
        tetha = (1 / np.sqrt(abs(self.p))) * np.arctan(tetha* np.sqrt(abs(self.p)))
        return tetha
    
            




