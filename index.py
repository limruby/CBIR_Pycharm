from main import Main
import argparse
import glob
import cv2

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help= "Path to the directory that contains imgs to be indexed")
ap.add_argument("-i", "--index", required=True, help= "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize colour descriptor
cd = Main((8, 12, 3))

# open output index file for writing
output = open(args["index"], "w")

# use glob to grab img file and loop over time
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract img ID from img path and load the img itself
    imageID = imagePath[imagePath.rfind("\\") + 1:]
    image = cv2.imread(imagePath)

    # describe img
    features = cd.describe(image)

    # write features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()
