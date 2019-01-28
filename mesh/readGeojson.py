## get coordinates of the mud are from .geojson file
## create script file for generating 2D mesh in Gmsh

import json

###########################
###########################
## parameter to be modified

inFileGeojson = 'export.geojson'
outFileTxt = 'coords.txt'
outFileGeo = 'scriptGmsh.geo'

cellSize = 1.     ## size of cells in the mesh (in units of lat/lon)

##########################
###########################



##########################
##########################

## get coordinates
with open(inFileGeojson) as f:
    data = json.load(f)
coords = data['features'][0]['geometry']['coordinates'];

print ' ** Coordinates read from ', inFileGeojson

##########################
##########################

## write raw txt file with coordinates
f = open(outFileTxt, 'w')

for p in coords:
    f.write('%f %f\n' %(p[0],p[1]))
f.close()

print ' ** Coordinates written to ', outFileTxt

##########################
##########################

## write script for generating mesh in Gmsh
lC = len(coords)

f = open(outFileGeo,'w')

f.write("//GMSH script - Brumadinho\n\n")
f.write("size = %f;\n\n" %(cellSize));

for i in range(lC):
    f.write("Point(%d) = {%f, %f, 0., size};\n" %(i+1, coords[i][0], coords[i][1]));

f.write("\n");

for i in range(lC - 1):
    f.write('Line(%d) = {%d, %d};\n' %(i+1, i+1, i+2));
f.write('Line(%d) = {%d, %d};\n' %(lC, lC, 1));

f.write("\n");

f.write("Line Loop(1) = {");
for i in range(lC - 1):
    f.write("%d, " %(i+1));
f.write("%d};\n\n" %(lC));

f.write("\n");

f.write("Plane Surface(1) = 1;")

f.close();
print ' ** GMSH script written to ', outFileGeo





