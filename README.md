Programming language: Python 3.5.2 
Use Python3 to run each file except for tabular_to_CSV.py (use Python).

Public Packages: scikit-learn, pandas, numpy, scipy, matplotlib

Structure of Source Code Directory: There are 3 sub directories as follows with the list of files in it:
1. Data Extraction: tabular_to_CSV.py, venue_score.csv, venue_h5Index_final.csv, reduce_dataset.py, reduced_acm_citation.csv, final_data_generator.py
acm_output.txt [1] and acm_citation.csv (in Drive)
2. Final Dataset: final_dataset.csv, test5kdata.csv
3. Algorithms: final_dataset.csv, test5kdata.csv, knnAndMLR.py

1. Data Extraction

tabular_to_CSV.py file: (Use Python for this) 
	Input: acm_output.txt (download the dataset from ArtMiner[1])
	Output: acm_citation.csv
	Run Command: python tabular_to_CSV.py
	Description: This file [2] will take .txt file as an input obtained from ArtMiner and will convert it into .csv file. It takes several minutes to run.

2. Reduction of DataSet

reduce_dataset.py file:
   Input: venue_h5Index_final.csv and acm_citation.csv (Output of previous step)
   Output: reduced_acm_citation.csv
   Run Command: python3 reduce_dataset.py
   Description: There are 32 venues listed in venue_score.csv which is used to filter out all the authors from acm_citation.csv (reduction of the dataset size from 2.2M to 0.9M i.e. the resultant belongs to only those 32 venues). It takes several hours to run.

3. Creation of Final Dataset

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

4. Training Model

For Multinomial Logistic Regression and KNN Classifier, knn_AndMLR.py file:
   Input: final_dataset.csv, test5kdata.csv
   Output: output.txt, fig1.pdf (Resultant Output Graph will be generated)
   Run Command: python3 knn_AndMLR.py
	Description:  Both the models are implemented in the same file. The dataset is trained with the multinomial logistic regression algorithm and KNN Classifier where K=5 and there are 9 classes used for classification. From the resultant graph, we can say the KNN Classifier results into better accuracy than Multinomial Logistic Regression for the given dataset. 

REFERENCES
1. Paper-Citation Dataset: [DOI]: http://aminer.org/lab-datasets/citation/DBLP_citation_Sep_2013.rar
2. Text to CSV: [DOI]: https://www.snip2code.com/Snippet/1084356/parse-aminer-s-dblp-dataset-(https---ami
