# Lighthouse :  Guiding Scholars to Directed Pathway for Higher Impact

## Problem
It is extremely important to learn from the history for making the progress in an efficient manner. This is particularly true for the emerging scholars who want to leave the utmost impact quickly in their early phase of the career. Thanks to the increased computed resources, it has become possible to mine the neat out of the available enormous data related to the research done to date. Although there are several works that make scholarly predictions, they mainly operate on the individual scholarly work, and typically predict the impact only after the work is published. However, this barely guides the scholar to increase his impact.

## solution 
We advocate for recommending scholars some publication pattern to be followed such that they can quickly achieve their target impact stage (i.e. higher citations). we introduce LightHouse to direct the scholars toward their desired pathway. First, the author-centric databases are created from the scratch, based on the paper-centric data available from the ArtMiner. Our datasets include the extraction and computation of custom features, tailored to our author-centric approach. Then, the supervised learning strategies such as multinomial regression or nearest neighbor classification are applied. The classification models are trained on the data up to the year 2008. The test data always consists information up to the year 2013 and is at least 10% of the training data. Evaluating the classification models on the rich author-centric test dataset (of several thousand scholars) show that for (real-time) undergone scholarly patterns, LightHouse predicts the outcome correctly for the majority of the authors (about 78%). We show the accuracy of different classification models and show how Lighthouse can successfully predict the outcomes for scholars of different domains.



## Environment
Python 3.5.2 
Use Python3 to run each file except for tabular_to_CSV.py (use Python).

## Public Packages
scikit-learn, pandas, numpy, scipy, matplotlib

## Structure of Source Code Directory: 
There are 3 sub directories as follows with the list of files in it:
1. Data Extraction: tabular_to_CSV.py, venue_score.csv, venue_h5Index_final.csv, reduce_dataset.py, reduced_acm_citation.csv, final_data_generator.py
acm_output.txt [1] and acm_citation.csv (in Drive)
2. Final Dataset: final_dataset.csv, test5kdata.csv
3. Algorithms: final_dataset.csv, test5kdata.csv, knnAndMLR.py

## Data Extraction

tabular_to_CSV.py file: (Use Python for this) 
	Input: acm_output.txt (download the dataset from ArtMiner[1])
	Output: acm_citation.csv
	Run Command: python tabular_to_CSV.py
	Description: This file [2] will take .txt file as an input obtained from ArtMiner and will convert it into .csv file. It takes several minutes to run.

## Reduction of DataSet

reduce_dataset.py file:
   Input: venue_h5Index_final.csv and acm_citation.csv (Output of previous step)
   Output: reduced_acm_citation.csv
   Run Command: python3 reduce_dataset.py
   Description: There are 32 venues listed in venue_score.csv which is used to filter out all the authors from acm_citation.csv (reduction of the dataset size from 2.2M to 0.9M i.e. the resultant belongs to only those 32 venues). It takes several hours to run.

## Creation of Final Dataset

For Training Dataset, final_data_generator.py file:
   Input: venue_h5Index_final.csv, reduced_acm_citation.csv, venue_score.csv
   Output: final_dataset.csv
   Run Command: python3 final_data_generator.py
   Description: Training Dataset consists of the dataset till year 2008


For Testing Dataset, final_data_generator.py file:
   Input: venue_h5Index_final.csv, reduced_acm_citation.csv, venue_score.csv 
   Output: test5kdata.csv
   Run Command: python3 final_data_generator.py
   Description: The same file is used by changing years to 2013 and limiting entries to 5000 as well as hanging the name of output file to test5kdata.csv.

## Training Model

For Multinomial Logistic Regression and KNN Classifier, knn_AndMLR.py file:
   Input: final_dataset.csv, test5kdata.csv
   Output: output.txt, fig1.pdf (Resultant Output Graph will be generated)
   Run Command: python3 knn_AndMLR.py
	Description:  Both the models are implemented in the same file. The dataset is trained with the multinomial logistic regression algorithm and KNN Classifier where K=5 and there are 9 classes used for classification. From the resultant graph, we can say the KNN Classifier results into better accuracy than Multinomial Logistic Regression for the given dataset. 

## REFERENCES
1. Paper-Citation Dataset: [DOI]: http://aminer.org/lab-datasets/citation/DBLP_citation_Sep_2013.rar
2. Text to CSV: [DOI]: https://www.snip2code.com/Snippet/1084356/parse-aminer-s-dblp-dataset-(https---ami
