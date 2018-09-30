# Getting Started
checkMatch.py is used to find the similarity between two document.
isHooper.py gives us the probablity that how likely jobseeker will dropout.

# Prerequisite
Some python module that are required.
**isHopper.py**
  -dateutil
  - docx

**checkMatch.py**
- TfidfVectorizer
- cosine_similarity
- docx

# Installing
- pip install python-docx
- pip install python-dateutil
- pip install numpy scipy scikit-learn

# How to use 
NOTE : Make sure you have the dataset folder in the same directory as this file
##### checkMatch.py
1. python checkMatch.py
2. Then enter the names of file whom you want to compare

# Example
Let if jobseeker's resume file name is ved.docx and and employer's requirement file name is employer.docx
**isHopper.py**
1. python3 isHopper.py
2. ved.docx
It will give you number between 0 to 4.

**checkMatch.py**
You should run this code where you have saved all files. 
1. python3 checkMatch.py

##### isHopper.py
1. python3 isHopper.py
2. Then enter the resume name without the extension.

# Author
- Parth goyal
- Mayank mussadi

# Licence 
This project is licensed under the MIT License.

```
