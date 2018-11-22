def isIntrusion(colist, x, y):
    #colist = [x1, y1, x2, y2] : 가상 펜스 좌표 리스트
    #x, y = 입력받은 좌표 값
    #x2 > x1
    warning = False
    gr = (colist[3] - colist[1]) / (colist[2] - colist[0])  # 기울기
    yinter = -1 * gr * colist[0] + colist[1]  # y절편
    yout = gr * x + yinter
    if y < yout: #꼭지점이 경계선 위에 있을 때
            warning = True
    return warning

class fence():
    #check fence warning
    def fence_check(self, fxy_list, frame):
        self.fence_warning = False
        self.colist = [38, 660, 1174, 374]
        f_stat = True
        for i, b in enumerate(fxy_list): #객체 상자 좌표 리스트에서
            stat = []
            for m in range(0, len(fxy_list[i]), 2):
                stat.append(isIntrusion(self.colist, fxy_list[i][m], fxy_list[i][m + 1])) #좌표 계산
            for k in stat:
                f_stat = f_stat and k
        if f_stat:
            self.fence_warning = True