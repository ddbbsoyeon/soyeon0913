        for i, b in enumerate(self.boxes[0]):
            if self.scores[0][i] >= 0.6:
                if self.classes[0][i] in self.category_index.keys():
                    class_name = self.category_index[self.classes[0][i]]['name']
                    self.e_list.append(class_name)
                    if class_name == 'person':
                        x, y = self.boxes[0][i][1], self.boxes[0][i][0]
                        w, h = self.boxes[0][i][3] - self.boxes[0][i][1], self.boxes[0][i][2] - self.boxes[0][i][0]
                        coord = (x, y, w, h)
                        self.fxy_list.append(coord)
                        
                        
                        
                        
    if 'person' in self.e_list:
        if trackers.isFirst or counter%15 == 0:
                try:
                    trackers.settings(detection.fxy_list, detection.frame)
                    #now = 0
                    counter = counter + 1
                except Exception as e:
                    print(str(e))
                    continue
        elif len(detection.fxy_list) != 0 and detection.ret and detection.video.isOpened():
                 try:
                     trackers.updatebox(detection.frame)
                     #tracker.update(detection.frame, detection.ret)
                     counter = counter + 1
                 except Exception as e:
                     print(str(e))
                     continue
