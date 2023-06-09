def minTimeToVisitAllPoints(self, points):
        if len(points)==1:
            return 0
        elif len(points)==2:
            maximaXorY=max(abs(points[0][0]-points[1][0]), abs(points[0][1]-points[1][1]))
            return maximaXorY
        else:
            return self.minTimeToVisitAllPoints(points[1:])+self.minTimeToVisitAllPoints(points[:2])