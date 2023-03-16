import shutil
import cv2
import os
directory = '/home/anopsy/data/frames/crop'
directoryGood = '/home/anopsy/data/frames/goodwaves'
directoryBad = '/home/anopsy/data/frames/badwaves'
directoryRemoved = '/home/anopsy/data/frames/removed'

countgood = 379
countbad = 1639
countdunno = 1

for filename in sorted(os.listdir(directory)):
    cv2.destroyAllWindows()
    if filename.endswith('.jpg'):
        img=cv2.imread(os.path.join(directory, filename))
        cv2.imshow(filename, img)
        key=cv2.waitKey(0)
        oldname= directory+ '/' + filename
        if key==ord('1'):
            print('good wave')
            newname= directoryGood + '/goodwave{}.jpg'.format(countgood)
            shutil.move(oldname, newname)
            countgood+=1
        elif key==ord('0'):
            print('bad wave')
            newname= directoryBad + '/badwave{}.jpg'.format(countbad)
            shutil.move(oldname, newname)
            countbad+=1
        elif key==ord('d'):
            print('removed')
            newname=directoryRemoved + '/dunno{}.jpg'.format(countdunno)
            shutil.move(oldname, newname)
            countdunno+=1
    else:
        continue
