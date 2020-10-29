# Beer Classification
## Timothy W. Dooley (LASSO)
## Metis
## Contents 
The main notebook of model creation is found in this directory as `model_building.ipynb`. <br>
The scraping file is called `fresh_beer.py`. The website, BrewersFriend.com, does not permit fast scraping. <br> 

### **Problem**
-------------------------------
The India Pale Ale (IPA) is a beer style of incredible popularity. Beer brewers have scrambled in recent years to produce new variations of the style and fill shelves with IPAs. As such, the purist definition of IPA as a slightly hoppier pale ale has been considerably stretched. <br>
In order to 'democratically' confer with the beer world at large, I scraped recipes of craft devotees from BrewersFriend.com. The 27,000+ recipes required extensive cleaning and encoding but provided a useful database from which to build a number of models. These models provide some insight into the various components that make up a particular style, especially the IPA. 
***Objective:*** Understand beer classifications through the production of numerous machine learning models built from scraped recipes from BrewersFriend.com.
### **Methods**
----------------------------
The 27,000+ recipes were scraped using BeautifulSoup and Requests. The file `fresh_beer.py` provides a file for scraping.<br>
Extensive cleaning of user input was required. Much of this cleaning can be found in `FSM_merge.ipynb` 


