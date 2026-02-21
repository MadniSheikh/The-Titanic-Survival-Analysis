import pandas as pd
import numpy as np

def extractTitle(X):

    if isinstance(X, pd.DataFrame):
        X = X.iloc[:, 0]
    
    NameTitle = X.apply(lambda x: x.split(",")[1].split()[0])

    result_df = pd.DataFrame(
        {
            'NameTitle': NameTitle
        }, index=X.index                            ##I did this because there were inconsistences in row indices that lead to error
    )

    return result_df

def ageCategory2(x):                                                 #Green
    if x<7:
        return "Childrens"
    elif x<20:
        return "teen"
    elif x<40:
        return "Peak"
    elif x<60:
        return "Senior"
    else:
        return "old"
    

def extractAgeCategory(X):

    if isinstance(X, pd.DataFrame):
        X = X.iloc[:, 0]
    
    AgeCategory = X.apply(ageCategory2)

    result_df = pd.DataFrame(
        {
            'AgeCategory': AgeCategory
        }, index=X.index
    )

    return result_df

def fam_category(s):                                        ##Green
    if s == 0:
        return "Alone"
    elif 0<s<4:
        return "Small_fam"
    else:
        return "Big_fam"

def famCategory(X):
    
    FamSize = X.iloc[:, 0] + X.iloc[:, 1]

    FamSize = FamSize.apply(fam_category)

    result_df = pd.DataFrame(
        {
            'FamSize': FamSize
        }, index=X.index
    )

    return result_df

def ticketCategory(X):

    if isinstance(X, pd.DataFrame):
        X = X.iloc[:, 0]

    TicketCat = X.apply(lambda s: s.split()[0])
    TicketCat = np.where(TicketCat.str.isdigit(), "NA", TicketCat) 

    result_df = pd.DataFrame(
        {
            'TicketCat': TicketCat
        }, index=X.index
    )

    return result_df 

def cabinCategory(X):

    if isinstance(X, pd.DataFrame):
        X = X.iloc[:, 0]
    
    CabinCategory = X.str[0]
    CabinCategory = np.where(CabinCategory.str.isdigit(), "NA", CabinCategory)

    result_df = pd.DataFrame(
        {
            'CabinCategory': CabinCategory
        }, index=X.index
    )

    return result_df 