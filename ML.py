import numpy as np
import cv2
import mediapipe as mp
from PIL import Image


filepath = 'D:/Server/'

def ML():
    path = filepath+'Android/Sample.jpg'

    img = cv2.imread(path)

    max_num_hands = 1

    rps_gesture = {0:'rock', 5:'paper', 9:'scissors'}

    # MediaPipe hands model
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=max_num_hands,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    file = np.genfromtxt('gesture_train.csv', delimiter=',')
    angle = file[:,:-1].astype(np.float32)
    label = file[:, -1].astype(np.float32)
    knn = cv2.ml.KNearest_create()
    knn.train(angle, cv2.ml.ROW_SAMPLE, label)

    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks is not None:
      for res in result.multi_hand_landmarks:
          joint = np.zeros((21, 3))
          for j, lm in enumerate(res.landmark):
              joint[j] = [lm.x, lm.y, lm.z]

          # Compute angles between joints
          v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
          v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
          v = v2 - v1 # [20,3]
          # Normalize v
          v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

          # Get angle using arcos of dot product
          angle = np.arccos(np.einsum('nt,nt->n',
              v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:],
              v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

          angle = np.degrees(angle) # Convert radian to degree

          # Inference gesture
          data = np.array([angle], dtype=np.float32)
          ret, results, neighbours, dist = knn.findNearest(data, 3)
          idx = int(results[0][0])
          print(idx)
          # Draw gesture result
          if idx in rps_gesture.keys():
              cv2.putText(img, text=rps_gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
      f = open(filepath+"python/hand.txt", "w")
      print(joint)
      f.write(rps_gesture[idx])
      joint_list=joint.tolist()
      save_joint=""
      save_joint=''.join(str(joint_list))
      f.write('\n')
      f.write(save_joint)

      f.close()