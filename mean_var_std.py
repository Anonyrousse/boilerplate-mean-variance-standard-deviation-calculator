import numpy as np

def calculate(list):
    longueur = len(list)
    if longueur <9 :
        return "List must contain nine numbers."
    else : 
        A = np.array(list).reshape(3, 3) #conversion liste en numpy array 3D
        moyenne1 = np.mean(A, axis =(0))
        moyenne2 = np.mean(A, axis =(1))
        moyenneF = np.mean(A)
        var1 = np.var(A, axis =(0))
        var2 = np.var(A, axis =(1))
        varF = np.var(A)
        standard_Deviation1 = A.std(axis =(0))
        standard_Deviation2 = A.std(axis =(1))
        standard_DeviationF = A.std()
        max1 = np.max(A, axis =(0))
        max2 = np.max(A, axis =(1))
        maxF = np.max(A)
        min1 = np.min(A, axis =(0))
        min2 = np.min(A, axis =(1))
        minF = np.min(A)
        somme_totale1 = np.sum(A, axis =(0)) 
        somme_totale2 = np.sum(A, axis =(1)) 
        somme_totaleF = np.sum(A) 
        calculations = dict()
        calculations = {
        "mean": [moyenne1.tolist(),moyenne2.tolist(),moyenneF.tolist()],
        "variance": [var1.tolist(),var2.tolist(),varF.tolist()],
        "standard deviation": [standard_Deviation1.tolist(),standard_Deviation2.tolist(),standard_DeviationF.tolist()],
        "max": [max1.tolist(),max2.tolist(),maxF.tolist()],
        "min": [min1.tolist(),min2.tolist(),minF.tolist()],  
        "sum": [somme_totale1.tolist(),somme_totale2.tolist(),somme_totaleF.tolist()], 
            }       
        return calculations



print(calculate([0,1,2,3,4,5,6,7,8]))

print(calculate([0,1,2,3,4,5,6,7]))