"""'dryh', 'lact', 'clone', 'juicy', 'dank', 'wedding', 'whisk', 'trop',\
              'award', 'best', 'smoke', 'roast', 'thick',\
              'heavy', 'stfruit', 'hazy', 'pheno', 'banana','clove', \
              'bitter','puree','lovehop', \
              'strong', 'dry', 'sweet'"""
import numpy as np
import pandas as pd
def search_desc(entry):
    """Creates an np.array from a string description of a beer for use in model to predict beer style."""
    dryh = 0
    lact = 0
    clone = 0
    juicy = 0
    dank = 0
    wedding = 0
    whisk = 0
    trop = 0
    award = 0
    best = 0
    smoke = 0
    roast = 0
    thick = 0
    heavy = 0
    stfruit = 0
    hazy = 0
    pheno = 0
    banana = 0
    clove = 0
    bitter = 0
    puree = 0
    lovehop = 0
    strong= 0
    dry = 0
    sweet = 0
    sour = 0
    dark = 0
    pine = 0
    sticky = 0
    foam = 0
    hoppy = 0
    biscuit = 0
    ester = 0
    straw = 0
    choco = 0
    coffee = 0
    malt = 0
    agg = 0
    balance = 0
    cmpl = 0
    crisp = 0
    smooth = 0
    diac = 0
    apple = 0
    floral = 0
    fruity = 0
    robust = 0
    wood = 0
    vanilla = 0
    cherry = 0
    funk = 0
    grapef = 0
    solvent = 0
    check = entry.lower()
    if 'dry hop' in check or 'dryhop' in check:
        dryh += 1
    if 'lactose' in check:
        lact += 1
    if 'clone' in check:
        clone += 1
    if 'juicy' in check or 'juice' in check:
        juicy += 1
    if 'dank' in check or 'cannabis' in check or 'marijuana' in check or '420' in check or 'resin' in check or 'pine' in check:
        dank += 1
    if 'wedding' in check or 'marriage' in check:
        wedding += 1
    if 'whisky' in check or 'whiskey' in check:
        whisk +=1
    if 'tropical' in check:
        trop += 1
    if 'award' in check or 'champion' in check:
        award += 1
    if 'best' in check:
        best += 1
    if 'smoke' in check or 'smoky' in check or 'campfire' in check or 'fire' in check or 'scotch' in check or 'peat' in check:
        smoke += 1
    if 'roast' in check:
        roast += 1
    if 'thick' in check:
        thick += 1
    if 'heavy' in check:
        heavy += 1
    if 'stonefruit' in check or 'stone fruit' in check or 'peach' in check or 'apricot' in check:
        stfruit += 1
    if 'hazy' in check or 'haze' in check:
        hazy += 1
    if 'pheno' in check:
        pheno += 1
    if 'banana' in check:
        banana += 1
    if 'clove' in check:
        clove += 1
    if 'bitter' in check:
        bitter += 1
    if 'puree' in check:
        puree += 1
    if 'hop love' in check or 'love hop' in check:
        lovehop += 1
    if 'strong' in check or 'booz' in check:
        strong += 1
    if 'bone' in check or 'dry' in check:
        dry += 1
    if 'sweet' in check:
        sweet += 1
    if 'sour' in check or 'acid' in check or 'pucker' in check:
        sour +=1
    if 'dark' in check or 'black' in check or 'brown' in check:
        dark +=1
    if 'pine ' in check:
        pine +=1
    if 'sticky' in check:
        sticky +=1
    if 'foam' in check or 'head' in check:
        foam +=1
    if 'hoppy' in check:
        hoppy += 1
    if 'biscuit' in check:
        biscuit += 1
    if 'ester' in check:
        ester +=1
    if 'straw' in check:
        straw +=1
    if 'choco' in check:
        choco +=1
    if 'coffee' in check:
        coffee += 1
    if 'mango' in check or 'papaya' in check or 'citr' in check or 'orange' in check or 'pineapple' in check or 'lemon' in check:
        trop +=1
    if 'malt' in check or 'backbone' in check:
        malt += 1
    if 'aggresive' in check:
        agg += 1
    if 'balance' in check:
        balance += 1
    if 'complex' in check or 'complicated' in check:
        cmpl +=1
    if 'crisp' in check:
        crisp += 1
    if 'smooth' in check:
        smooth += 1
    if 'diac' in check:
        diac += 1
    if 'apple' in check or 'pear' in check:
        apple += 1
    if 'floral' in check or 'flower' in check:
        floral += 1
    if 'fruity' in check:
        fruity += 1
    if 'robust' in check:
        robust += 1
    if 'wood' in check or 'oak' in check:
        wood += 1
    if 'vanill' in check:
        vanilla += 1
    if 'cherr' in check:
        cherry += 1
    if 'funk' in check or 'barn' in check or 'blanket' in check:
        funk += 1
    if 'grapef' in check:
        grapef += 1
    if 'solv' in check:
        solvent += 1
    res_list = [dryh, lact, clone, juicy, dank, wedding, whisk, trop, award, best, smoke, roast, thick,heavy, stfruit, hazy, pheno,
                banana,clove, bitter,puree,lovehop,strong, dry, sweet, sour, dark, pine, sticky, foam, hoppy, biscuit, ester, straw, choco, coffee,
                malt, agg, balance, cmpl, crisp, smooth, diac, apple, floral, fruity, robust, wood, vanilla, cherry, funk, grapef, solvent]
    resparray = np.asarray(res_list)
    response = pd.DataFrame(resparray, index = ['dryh', 'lact', 'clone', 'juicy', 'dank', 'wedding', 'whisk', 'trop',
       'award', 'best', 'smoke', 'roast', 'thick', 'heavy', 'stfruit', 'hazy',
       'pheno', 'banana', 'clove', 'bitter', 'puree', 'lovehop', 'strong',
       'dry', 'sweet', 'sour', 'dark', 'pine', 'sticky', 'foam', 'hoppy',
       'bisc', 'ester', 'straw', 'choco', 'coffee', 'malt', 'agg', 'balance',
       'complex', 'crisp', 'smooth', 'diac', 'apple', 'floral', 'fruity',
       'robust', 'wood', 'vanilla', 'cherry', 'funk', 'grapef', 'solvent']).T
    #'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f29', 'f30', 'f31', 'f32', 'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f39', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47', 'f48', 'f49', 'f50', 'f51', 'f52']).T
    return response
