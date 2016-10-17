import sys
import logging
import modules.util.util as util
import modules.util.validateData as validate


def createPyramid():
    p = Pyramid()
    p.buildPyramid(util.readJsonFile("../../db/pyramid.json"))

class Pyramid:

    def __init__(self):
        self.logger = logging.getLogger('modules.draw.pyramid')
        self.logger.info('  pyramid.init')

    def buildPyramid(self, data):

        validate.validatePyramid(data)
        center = data.get('center')
        baseWidth = data.get('baseWidth')

        for segment in data.get('segments'):
            baseWidth = self.buildPyramidSegment(segment, center, baseWidth)
            center['y'] += segment['height']

    def buildPyramidSegment(self, segment, center, baseWidth):

        print("Building segment: ", segment, ", center: ", center, ", baseWidth: ", baseWidth)

        x1 = center['x'] - (baseWidth / 2)
        x2 = center['x'] + (baseWidth / 2)
        z1 = center['z'] - (baseWidth / 2)
        z2 = center['z'] + (baseWidth / 2)
        stepWidth = segment['stepWidth']
        stepHeight = segment['stepHeight']
        stepCounter = 0
        counter = 1

        for y in range(center['y'], center['y'] + segment['height']):
            print("%d. x1: %d, z1: %d, x2: %d, z2: %d, y: %d" % (counter,x1, z1, x2, z2, y))
            stepCounter += 1

            if(stepCounter == stepHeight):
                stepCounter = 0
                x1 = x1 + stepWidth
                x2 = x2 - stepWidth
                z1 = z1 + stepWidth
                z2 = z2 - stepWidth
                baseWidth -= stepWidth * 2

            counter += 1

        return baseWidth


if __name__ == "__main__":
    sys.exit(createPyramid())