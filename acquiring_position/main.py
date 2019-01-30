"""
Modeling to estimate the victms' positions in Brumadinho
Underdevelopment: 
    Rafael Pinheiro*, Bruno Turrim*
    Alexandre Rodrigues*, Isabela Stevani*
    Andre, Marconi*, Leonardo Carvalho*
    *Lab de Automacao e Controle, Electric Engineering, Poli-USP - SP Brazil

    Thamires Chagas**
    **ITA, Brazil

    Jean Matias***
    ***Tyndal National Institute, UCC - Cork, Ireland
"""
import numpy as np
from scipy.integrate import cumtrapz
import utm

# Initial position - Transform Geo coords to UTM coords.

# If we need arrays: uncomment the next 3 lines and comment the next 2
    # some more changes are expected to be done to match the
    # variable types
# latArr = [-20]; lonArr = [-44]
# utmArr = np.array([ utm.from_latlon(lat, lon) for lat, lon in zip(latArr, lonArr) ])
# x0, y0, utmZoneNumber, utmZoneLetter = (utmArr[:,i] for i in range(utmArr.shape[1]))

# Example: 
lat, lon = -20., -44.
x0, y0, utmZoneNumber, utmZoneLetter = utm.from_latlon(lat, lon)

#############################################################
# Get the waste vectorial velocity field 
# Or get the vectorial velocity from CFD simulation
#############################################################

#############################################################
# Calculate the drift velocity of objects submerged in the waste
# and obtain the vectorial accelaration: accelarationX, accelarationY
#############################################################

#############################################################
# Classical mechnics: 
# Calculates position from the drift accleration after two integrations
# The first approach uses a 2D model
#############################################################

accelelationX = np.array([
    1.45, 1.79, 4.02, 7.15, 11.18, 16.09, 21.90, 29.05, 29.05,
    29.05, 29.05, 29.05, 22.42, 17.9, 17.9, 17.9, 17.9, 14.34, 
    11.01, 8.9, 6.54, 2.03, 0.55, 0
])
accelelationY = np.array([
    1.45, 1.79, 4.02, 7.15, 11.18, 16.09, 21.90, 29.05, 29.05,
    29.05, 29.05, 29.05, 22.42, 17.9, 17.9, 17.9, 17.9, 14.34, 
    11.01, 8.9, 6.54, 2.03, 0.55, 0
])

# time = 24 #seconds or min?

# Integrate on the x direction
velocityX = cumtrapz(accelelationX)
# Integrate on the x direction
velocityY = cumtrapz(accelelationY)

# Integrate velocity to get x position
positionX = cumtrapz(velocityX)
# Integrate velocity to get y position
positionY = cumtrapz(velocityY)

# Insert initial position 
positionX = np.concatenate([[x0], positionX])
positionY = np.concatenate([[y0], positionY])

# Using cumulative sum instead of for
positionX = np.cumsum(positionX)
positionY = np.cumsum(positionY)

# Gets latitute and longitude of an object in the fluid waste
lat, lon = utm.to_latlon(positionX[-1], positionY[-1], utmZoneNumber, utmZoneLetter)

