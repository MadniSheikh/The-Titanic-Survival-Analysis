import pandas as pd
import numpy as np

def extractTitle(X):
    
    NameTitle = X.apply(lambda x: x.split(",")[1].split()[0])

    result_df = pd.DataFrame(
        {
            'NameTitle': NameTitle
        }
    )

    return result_df

def ageCategory(x):                                                             ##RED ONE HAS BEEN PICKED
    if x<15:
        return "Childrens"
    elif x<35:
        return "Adults"
    elif x<60:
        return "Middle"
    else:
        return "old"
    

def extractAgeCategory(X):
    
    AgeCategory = X.apply(ageCategory)

    result_df = pd.DataFrame(
        {
            'AgeCategory': AgeCategory
        }
    )

    return result_df

def famCategory(X):
    
    FamSize = X.iloc[:, 0] + X.iloc[:, 1]

    result_df = pd.DataFrame(
        {
            'FamSize': FamSize
        }
    )

    return result_df

def ticketCategory(X):
    TicketCat = X.apply(lambda s: s.split()[0])
    TicketCat = np.where(TicketCat.str.isdigit(), "NA", TicketCat) 

    result_df = pd.DataFrame(
        {
            'TicketCat': TicketCat
        }
    )

    return result_df 

def cabinCategory(X):
    
    CabinCategory = X.str[0]
    CabinCategory = np.where(CabinCategory.str.isdigit(), "MISSING", CabinCategory)

    result_df = pd.DataFrame(
        {
            'CabinCategory': CabinCategory
        }
    )

    return result_df 