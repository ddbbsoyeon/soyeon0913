import cv2

class multitracker():
    def __init__(self):
        self.multitrackers = cv2.MultiTracker_create()
        self.bboxes = []
        self.prev = []
        self.over = False
        self.id = 0
        self.isFirst = True

    def settings(self, coord, frame):
        if not self.isFirst:
            self.multitrackers = cv2.MultiTracker_create()
        else:
            self.isFirst = False
        self.prev = []
        for i in coord:
            i0, i2 = int(i[0] * 1280), int(i[2] * 1280)
            i1, i3 = int(i[1] * 800), int(i[3] * 800)
            #trackers.add(tracker, frame, box)
            #roi = frame[x:x + h, y:y + w]
            #roi = frame[i0: i0 + i3, i1: i1 + i2]
            window = (i0, i1, i2, i3)
            self.prev.append(window)
            csrt = cv2.TrackerCSRT_create()
            self.multitrackers.add(csrt, frame, window)
            print("init =", self.prev)

    def updatebox(self, frame):
        '''
            for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        :return:
        '''
        #(success, boxes) = trackers.update(frame)
        self.id = 0
        (success, boxes) = self.multitrackers.update(frame)
        #prev와 boxes의 길이를 비교해 그 차이 만큼 boxes의 끝 원소들 --
        temp = []
        for box in boxes:
            #[x0, y0, w0, h0] = [int(k) for k in self.prev[self.id]]
            [x, y, w, h] = [int(v) for v in box]
            temp.append(box.tolist())
            #self.prev[self.id] = [x, y, w, h]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #if y - y0 >= 20:
            #    self.over = True
            #self.id += 1
        #self.prev = boxes
        #self.prev = boxes2
        self.prev = temp
        print(self.prev)
        #print("prev = ", self.prev)
