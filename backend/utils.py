import numpy as np
from scipy import interpolate


X = np.linspace(-20.139558, -20.115769, 1000)
Y = np.linspace(-44.141856, -44.099738, 1000)
Z = np.array([100.0, 50.0, 50.0, 25, 100.0])

DAM = [-20.119026, -44.119985]
X, Y = np.meshgrid(X, Y)

NPTS = 5
PX, PY = np.random.choice(X, NPTS), np.random.choice(Y, NPTS)

X_POINTS = np.array([-20.115769, -20.115769, -20.129558, -20.129558])
Y_POINTS = np.array([-44.141856, -44.119738, -44.141856, -44.119738])

Z1 = np.array([np.random.random() * 100 for X, Y in zip(X_POINTS, Y_POINTS)])
Z2 = interpolate.griddata((X_POINTS, Y_POINTS), Z1, (X, Y), method='nearest')

MAP = [(X, Y, Z) for X, Y, Z in zip(X, Y, Z2)]


class Position:
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def calc_vector(self):
        v_pos_x, v_pos_y = (self.lat - DAM[0], self.lng - DAM[1])
        d = np.sqrt((v_pos_x ** 2 + v_pos_y ** 2))

        print(v_pos_x, v_pos_y, d)

        xf = self.lat + v_pos_x
        yf = self.lng + v_pos_y

        return xf, yf


def return_vector(request_latitude, request_longitude):
    if request_latitude and request_longitude:
        return Position(request_latitude, request_longitude).calc_vector()
    return None
