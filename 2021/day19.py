
# https://en.wikipedia.org/wiki/Cross_product
# https://en.wikipedia.org/wiki/Change_of_basis
# https://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm

"""

the scanners do not know their own position.
the scanners also don't know their rotation or facing direction

This region can be reconstructed by finding pairs of scanners that have overlapping detection regions such that there are at least 12 beacons

"""
# 24 different orientations
def rotations(x, y, z):
    for dx in [1, -1]:
        for dy in [1, -1]:
            for dz in [1,  -1]:
                yield x*dx, y*dy, z*dz

def mean(points):
    lower_x = min(map(lambda p: p[0], points))
    lowey_y = min(map(lambda p: p[1], points))
    lower_z = min(map(lambda p: p[2], points))

    normalized_points = list(map(lambda x, y, z: [x-lower_x, y-lowey_y, z-lower_z], points))

    x_sum = sum(map(lambda p: p[0], normalized_points))
    y_sum = sum(map(lambda p: p[1], normalized_points))
    z_sum = sum(map(lambda p: p[2], normalized_points))

    mean = x_sum / len(points) + y_sum / len(points) + z_sum / len(points)

    return mean 



if __name__ == "__main__":
    with open('input/day19.txt') as f:
        content = f.read().split('\n')[:-1]

        scanners = []
        for line in content:
            if 'scanner' in line:
                scanners.append([])
            else:
                if line:
                    scanners[-1].append([*map(int, line.split(','))])

    

