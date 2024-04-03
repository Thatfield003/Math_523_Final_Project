# Math_523_Final_Project
Created by Tad Hatfield and Tanner Byer

INTRODUCTION:

White mold sclerotia, also known as Sclerotinia sclerotiorum, is a fungus with a large economic impact on soybean production worldwide. The fungus lives in the soil and can survive there for very long periods of time. When conditions are right, the fungus will sprout up to release ascospores from structures known as apothecia. These ascospores will flow up into the canopy and infect soybean stems. Epidemics typically occur when soybeans start to canopy around flowering. This is because this fungus prefers cool temperatures and moist conditions that arise when canopies form. Previous studies have found that a 10% increase in white mold incidence would result in a mean yield reduction of 5% (Lehner 2017).
	In this, we model the yield of soybeans as a function of white mold population, weed population, soybean seeding population, fungicide use, and herbicide use. 
If epidemics could be predicted, the expense of routine fungicide applications could be eliminated or reduced while maintaining crop integrity and yield. 

RESEARCH QUESTIONS: 

What is the minimal amount of fungicide and pesticide to apply to soybean plants to minimize crop and weed presence while maximizing crop output? Is there a reliable way to forecast potential epidemics of white mold?

PREVIOUS RESEARCH/MODELS: 

Fungicides are effective at mitigating white mold outbreaks but are not 100% effective (Leaher, 2017). Previous research has focused on determining the efficacy of varied fungicides to reduce the incidence of white mold in different climates (WUTZKI 2016). Optimal fungicide application time is another area of research interest in the fight against Sclerotinia sclerotiorum. 

OUR MODEL: 

We use difference equations to model white mold’s effect on soybean crop yield. The mold in the next season is a function of the mold in the previous season that survives the winter and propagates based on the canopy formed(p+wt). We assume that a certain amount of fungicide will be applied based on the amount observed by farmers in the previous season. Weeds are modeled as a function of the total germinating seeds from the previous year that survived the winter. We assume that a certain amount of herbicide will be applied based on the weeds observed in the previous season, and the presence of crops limits the available resources for weeds to grow. The total crop yield from the season is a function of the total soybeans produced, offset by weeds and mold that develop during the season. We assume that if too many soybean plants are produced in a season, the crop yield will start to diminish as there is a finite amount of resources in the soil. 

We assume that there is consistent soil moisture and temperature from year to year - other factors affecting mold propagation (Hunter, 1981). 

In our closed system, we consider a farm of 100 acres where in an ideal year, 50 bushels of soybeans are produced per acre. We assume on each acre that (100,000 - 190,000) - (Tad add reference) soybean plants grow. Based on current trends in soybean profits, this earns the farmer $450 per acre. Therefore, for 100 acres of soybeans, the estimated annual revenue, assuming no mold infestation, is $45,000. 
Add information about water hemp weed propagation.
