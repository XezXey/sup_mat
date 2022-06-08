import cv2
import glob
import os

for f1 in glob.glob("./Tennis_dat/all_frame/*"):
  if not os.path.isdir(f1): continue
  print(os.path.basename(f1))
  os.makedirs("clips/" + os.path.basename(f1), exist_ok=True)
  for f2 in glob.glob(f1 + "/*"):
    print(os.path.basename(f2))
    os.makedirs("clips/" + os.path.basename(f1) + "/" + os.path.basename(f2), exist_ok=True)
    for f3 in glob.glob(f2 + "/raw/*.jpg"):
      print(f3)
      im = cv2.imread(f3)
      re = cv2.resize(im, (0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
      fn = os.path.basename(f3)
      fn = "%04d.jpg" % int(fn.split("_")[0].replace("f", ""))
      cv2.imwrite("clips/" + os.path.basename(f1) + "/" + os.path.basename(f2) + "/" + fn, re)
  #print(re.shape)
  #print(os.path.basename(f))
  #print(glob.glob(f + "/raw/*.jpg"))
