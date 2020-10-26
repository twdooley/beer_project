import numpy as np
import pandas as pd

def get_stats():
    og = float(input("Enter Original Gravity: "))
    fg = float(input("Enter Final Gravity: "))
    abv = float(input("Enter ABV: "))
    srm = float(input("Enter SRM: "))
    ibu = float(input("Enter IBU: "))
    bugu = float(ibu/((og -.999999999)*1000))
    hopcm = float(input("On a scale of 1-100, how hoppy is this beer? : "))
    
    array = np.array([og, fg, abv, srm, ibu, bugu, hopcm])
    df = pd.DataFrame(array, index = ['og', 'fg', 'abv', 'srm', 'ibu', 'bugu', 'hopcmp']).T

    return df