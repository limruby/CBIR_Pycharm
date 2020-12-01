# CBIR_Pycharm

Please donwload several library packages: cv2, imutils, numpy, opencv_python, pip

To run the program, first upload all the images into the "dataset" folder.

Then, open the terminal and issue the following command:

python index.py --dataset dataset --index index.csv 

Next, upload your query images into the "queries" folder.

Then, open the terminal and issue the following command:

python query.py --index index.csv --query "queries\yourimagename.jpg" --result-path dataset

Please remember to index your images whenever you have upload the images.

python query.py --index index.csv --query "queries\6.jpg" --result-path dataset

The code is from Adrian Rosebrock, https://www.pyimagesearch.com/
