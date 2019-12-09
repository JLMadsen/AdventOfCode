HEIGHT = 6
WIDTH = 25
SIZE = HEIGHT*WIDTH

def checkCorruption(codedImage) -> []:
    codedImage = list(map(int, codedImage))

    # get layers
    layers = []
    prev = 0
    for step in range(SIZE, len(codedImage), SIZE):
        layers.append(codedImage[prev:step])
        prev = step

    # count 0's 1's and 2's
    count = []
    for i in range(len(layers)):
        count.append([0,0,0])
        for j in layers[i]:
            count[i][j] += 1

    # find lowest 0's and get sum om 1's * 2's
    result = [SIZE,0]
    for c in count:
        if c[0] < result[0]:
            result = [c[0], c[1]*c[2]]
        
    print('CheckSum =',result[1])

    return layers

def printImage(image) -> None:
    for row in image:
        print(row)

def decodeImage(layers) -> []:
    image = [[-1]*WIDTH]*HEIGHT

    try:
        for layer in layers:
            j = 0
            for i in range(len(layer)):
                if image[j][i] != -1: continue
                if i != 0 and i % WIDTH == 0:j += 1
                i = i % WIDTH

                if layer[i] == 2: continue
                image[j][i] = layer[i]
    except:
        print(i,j)
        printImage(image)
        return

    printImage(image)

def main() -> None:
    codedImage = open('input/day8input.txt').read()

    print('Part 1')
    layers = checkCorruption(codedImage)

    print('Part 2')
    decodeImage(layers)

if __name__ == '__main__':
    main()