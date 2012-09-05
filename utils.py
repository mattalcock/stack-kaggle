import scipy as sp

def logloss(act, pred):
    """ Vectorised computation of logloss """
    
    #cap in official Kaggle implementation, 
    #per forums/t/1576/r-code-for-logloss
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    
    #compute logloss function (vectorised)
    ll = sum(   act*sp.log(pred) + 
                sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
    ll = ll * -1.0/len(act)
    return ll

def mc_logloss(act, pred):
    ll = logloss(act, pred)
    return sum(ll)*1.0/len(ll)

if __name__=="__main__":

    act = [[1,0], [1,0], [1,0], [0,1], [0,1], [0,1]]
    pred = [[0.5,0.5], [0.1,0.9], [0.01,0.99], [0.9,0.1], [0.75,0.25], [0.001,0.999]]
    print mc_logloss(act, pred)