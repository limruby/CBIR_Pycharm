from main import Main
from searcher import Searcher
import argparse
import cv2

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True, help="Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required= True, help="Path to the query image")
ap.add_argument("-r", "--result-path", required=True, help="Path to the result path")
args = vars(ap.parse_args())

# initialize img descriptor
cd = Main((8, 12, 3))

# load tge query image and describe
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display query
# Create window with freedom of dimensions
cv2.namedWindow("Query", cv2.WINDOW_NORMAL)
cv2.imshow("Query", query)

# loop the results
for(score, resultID) in results:
    result = cv2.imread(args["result_path"] + "/" + resultID)
    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.imshow("Result", result)
    cv2.waitKey(0)