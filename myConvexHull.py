import numpy as np

def determinant(p1, p2, p3):
    return p1[1]*p2[2] + p3[1]*p1[2] + p2[1]*p3[2] - p3[1]*p2[2] - p2[1]*p1[2] - p1[1]*p3[2]

def leftOrRight(p1, p2, p3):
    det = determinant(p1, p2, p3)
    if (det > 0):
        return "left"
    elif (det < 0):
        return "right"
    else:
        return "inline"

def divide(points, p1, pn):
    left = np.empty((0, 3))
    right = np.empty((0, 3))
    if (p1 is None or pn is None):
        return left, right
    for point in points:
        if (not (point[0] == p1[0] or point[0] == pn[0])):
            loc = leftOrRight(p1, pn, point)
            if (loc == "left"):
                left = np.append(left, np.array([point]), axis=0)
            elif (loc == "right"):
                right = np.append(right, np.array([point]), axis=0)
        # points where loc == "inline", p1, and pn is ignored since they can't form hull
    return left, right

def distance(p1, p2, px):
    A = p1[2]-p2[2]
    B = p2[1]-p1[1]
    C = p1[1]*p2[2]-p2[1]*p1[2]
    return abs(A*px[1] + B*px[2] + C)/((A*A + B*B)**(1/2))

def angle(p1, pmax, pn):
    pA = np.array(p1)
    pB = np.array(pmax)
    pC = np.array(pn)
    vectBA = pA - pB
    vectBC = pC - pB

    return (np.degrees(np.arccos((vectBA @ vectBC)/(np.linalg.norm(vectBA) * np.linalg.norm(vectBC)))))

def myConvexHull2(p1, pn, part, leftRightPos):
    cvHull = np.empty((0, 2))
    if (not(np.size(part))):
        # kasus jika kosong
        return [[p1[0], pn[0]]]
    else:
        # choose a farthest point to p1pn line (pmax)
        dist_pmax = -1
        pmax = None
        idx_pmax = 0
        ctr = 0
        for point in part:
            temp_dist = distance(p1, pn, point)
            if (temp_dist > dist_pmax):
                dist_pmax = temp_dist
                pmax = point
                idx_pmax = ctr
            elif (temp_dist == dist_pmax and not(pmax is None)):
                if (angle(p1, point, pn) > angle(p1, pmax, pn)):
                    dist_pmax = temp_dist
                    pmax = point
                    idx_pmax = ctr
            ctr += 1
        if (not(pmax is None)):
            # maximum is found
            part = np.delete(part, idx_pmax, axis=0)
            # divide to two parts, only take the outer points
            p1pmaxleft, p1pmaxright = divide(part, p1, pmax)
            pmaxpnleft, pmaxpnright = divide(part, pmax, pn)
            if (leftRightPos == "left"):
                cvHull = np.append(cvHull, np.array(myConvexHull2(p1, pmax, p1pmaxleft, "left")), axis=0)
                cvHull = np.append(cvHull, np.array(myConvexHull2(pmax, pn, pmaxpnleft, "left")), axis=0)
            elif (leftRightPos == "right"):
                cvHull = np.append(cvHull, np.array(myConvexHull2(p1, pmax, p1pmaxright, "right")), axis=0)
                cvHull = np.append(cvHull, np.array(myConvexHull2(pmax, pn, pmaxpnright, "right")), axis=0)
        return cvHull

def numTitik(points):
    tempPoints = np.empty((0, 3))
    for i in range(len(points)):
        tempPoints = np.append(tempPoints, np.array([[i, points[i][0], points[i][1]]]), axis=0)
    return tempPoints

def myConvexHull(points):
    points = numTitik(points)
    cvHull = np.empty((0, 2))
    # sort points
    points = points[np.lexsort((points[:,2], points[:,1]))]
    # p1 and pn, leftmost and rightmost points respectively
    p1 = points[0]
    pn = points[-1]
    
    if (not(np.size(points))):
        # kasus kosong
        return [[p1[0], pn[0]]]
    else:
        left, right = divide(points, p1, pn)
        cvHull = np.append(cvHull, np.array(myConvexHull2(p1, pn, left, "left")), axis=0)
        cvHull = np.append(cvHull, np.array(myConvexHull2(p1, pn, right, "right")), axis=0)
        return cvHull