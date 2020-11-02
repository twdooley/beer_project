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

Beer styles were reduced to four 'superstyles' in order to make classification possible. <br>
![https://github.com/twdooley/beer_project/blob/master/images/4styles.svg](https://github.com/twdooley/beer_project/blob/master/images/4styles.svg) <br>

The first model I built focused only on back of bottle, numerical data to classify a beer. The ROC Curve pictured below shows good results. However, this should be obvious. Beer styles as marketed might be decided after the beer is manufactured. In other words, perhaps I was aiming for a Pale Ale and its a bit bitter, so lets call it an IPA. <br>
![https://github.com/twdooley/beer_project/blob/master/images/ROCquant.svg](https://github.com/twdooley/beer_project/blob/master/images/ROCquant.svg)
<br>
Another model was built to demonstrate the effect hops have on the classification of a beer. The Hops model considered over 40 strains of hop plant. The ROC Curve is found below. <br>
![https://github.com/twdooley/beer_project/blob/master/images/ROCHops.jpg](https://github.com/twdooley/beer_project/blob/master/images/ROCHops.jpg)
<br>

Finally, the most interesting model I built was the BRO: Beer Review Organizer. <br>

The BRO operates as a basic NLP vectorizer and one-hot encodes common descriptors of beer. This effort requires more polish but at this point shows decent results. The Forest model in this individual stacked model is demonstrated with a confusion matrix, below.

![https://github.com/twdooley/beer_project/blob/master/images/broForest.jpg](https://github.com/twdooley/beer_project/blob/master/images/broForest.jpg)
<br>
----------------------------
### **Conclusion**
<br>

The web apps have provided some classification clarity to the styles of beer. IPA is indeed an increasingly nebulous classification. I believe my Hops model shows a very clear picture of the aromatic effect of certain hop strains on the consideration of a style. American and New Zealand hops predominate the class, regardless of the other methods and numerical features. 

Please see the attached .pdf for examples of the web app as I work on deploying them for public use. 
----------------------------
### **Further Considerations** 
<br> 
As mentioned, closer study of the BRO with more advanced NLP methods would be helpful. 
I would also like to deploy the model apps for use by the interested general public. 
