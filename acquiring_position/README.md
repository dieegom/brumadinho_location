# Position Modeling

The acquiring position folder contains the modeling to try to estimate the position of the victims bodies or animals drifted by the mud. 
This approach aims to construct a vectorial field of the mud's drift force running off down the valey. 

From this force vectorial field, it is possible to calculate the accelaration vectorial field and after integration processes possible final positions of the bodies can be estimated considering their initial position. 

One of the possible ways to get the initial position is from GPS geolocation of the victms' cell phones at the time of the Dam burst. 

# The code

The oiginal code was written in MATLAB and then translated to Python. 

The [main.py](./main.py) file gets the geolocation coordinates and converts to x and y positions, which are used as boundary conditions.

After two integrations of the acceleration field, the code calculates the position field of the body. 

In this first approach, two ramdom acceleration arrays (2D - modeling - x and y) are used to test the code. 


