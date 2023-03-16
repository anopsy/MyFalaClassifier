# Program To Read video
# and Extract Frames
import cv2
import os

directory= '\home\anopsy\data\frames'

# Function to extract frames
def FrameCapture(path, x):
    # Path to video file
    vidObj = cv2.VideoCapture(path)
    # Used as counter variable
    count = 0
    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        if success != 1:
            break
        
        # Saves the frames with frame-count
        name = directory + "{x}frame{count}.jpg".format(x= x, count=count)
        cv2.imwrite(name, image)
        count += 1
        print(count)
    vidObj.release()


# Driver Code
if __name__ == '__main__':
    walk_dir = os.getcwd()
    i = 0

for root, subdirs, files in os.walk(walk_dir):
    for file in files:
        i += 1
        if (file.split(".")[-1].lower() == 'mp4'):
            filePath = os.path.join(root, file)
            print(filePath)
            if os.path.isfile(filePath):
	            # Calling the function
                FrameCapture(filePath,i )
            else:
                continue
# When everything done, release the capture
#cap.release()
#cv.destroyAllWindows()