import os
from screeninfo import get_monitors
def findnumber(a):
    for i, c in enumerate(a):
        if c.isdigit():
            return c
def scoreCalculator(firstscore,secondscore):
        arr=[
            [2,4,6],
            [4,6,8],
            [6,8,10],
            [8,10,12]
        ]
        return arr[int(firstscore)-1][int(secondscore)-1]
def scoreCalculator2(firstscore):
    arr=[
        [1,4,9,16]
    ]
    return arr[0][int(firstscore)-1]
def CalculateBackB1(A,B1,H,J):
    return scoreCalculator(H,A)+scoreCalculator(J,A)+scoreCalculator(H,J)+scoreCalculator(J,B1)
def CalculateBackB3(A,B3,H,J):
    return scoreCalculator(H,A)+scoreCalculator(J,A)+scoreCalculator(H,J)+scoreCalculator(H,int(B3)-2)+scoreCalculator(J,int(B3)-2)
def CalculateShoulderArm(C,D,H,J):
    return scoreCalculator(H,C)+scoreCalculator(J,C)+scoreCalculator(H,J)+scoreCalculator(H,D)+scoreCalculator(J,D)
def CalculateWristHand(E,F,K,J):
    return scoreCalculator(K,F)+scoreCalculator(J,F)+scoreCalculator(K,J)+scoreCalculator(K,E)+scoreCalculator(J,E)
def CalculateNeck(G,J,L):
    return scoreCalculator(J,G)+scoreCalculator(J,L)
def CalculateDriving(M):
    return scoreCalculator2(M)
def CalculateVibration(N):
    return scoreCalculator2(N)
def CalculateWorkPace(P):
    return scoreCalculator2(P)
def CalculateStress(Q):
    return scoreCalculator2(Q)
def CreateFilePath():
    home_dir = os.path.expanduser("~")
    file_path_to_HEC = os.path.join(home_dir, "AppData/Local/HEC Calculator")
    if not os.path.exists(file_path_to_HEC):
        os.makedirs(file_path_to_HEC)
    return home_dir, file_path_to_HEC
def ScreenSize():
    return [(m.width, m.height) for m in get_monitors() if m.is_primary][0]