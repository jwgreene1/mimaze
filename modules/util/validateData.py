import logging
from voluptuous import Schema, Required as req, All, Length, Range, error, Any

# Create logger
module_logger = logging.getLogger('modules.validateData')

schemaWallSegment = ({
    req('x1'): All(int, Range(min=-128, max=128)),
    req('y1'): All(int, Range(min=-128, max=128)),
    req('z1'): All(int, Range(min=-128, max=128)),
    req('x2'): All(int, Range(min=-128, max=128)),
    req('y2'): All(int, Range(min=-128, max=128)),
    req('z2'): All(int, Range(min=-128, max=128)),
    req('blockType'): All(int, Range(min=0, max=128)),
    req('blockData'): All(int, Range(min=0, max=10))
})

schemaWall = Schema({
    req('segments'): [schemaWallSegment],
    req('direction'): Any('N', 'S', 'E', 'W')
})

schemaPyramidSegment = Schema({
    req('stepWidth'): All(int, Range(min=1, max=127)),
    req('stepHeight'): All(int, Range(min=1, max=127)),
    req('blockType'): All(int, Range(min=0, max=128)),
    req('blockData'): All(int, Range(min=0, max=128)),
    req('height'): All(int, Range(min=1, max=256))
})

schemaPyramidCenter = Schema({
    req('x'): All(int, Range(min=-128, max=128)),
    req('y'): All(int, Range(min=-128, max=128)),
    req('z'): All(int, Range(min=-128, max=128))
})

schemaPyramid = Schema({
    req('segments'): [schemaPyramidSegment],
    req('baseWidth'): All(int, Range(min=4, max=256)),
    req('center'): schemaPyramidCenter
})

def validateWall(data):
    try:
        print('  validating schemaWall: ', schemaWall(data))
        module_logger.info('  validating schemaWall: ', schemaWall(data))

    except error.MultipleInvalid as e:
        print('Error validating wall data: ', e)
        module_logger.error('Error validating wall data: ', e)

def validatePyramid(data):
    try:
        print('  validating schemaPyramid: ', schemaPyramid(data))
        module_logger.info('  validating schemaWall: ', schemaPyramid(data))

    except error.MultipleInvalid as e:
        print('Error validating Pyramid data: ', e)
        module_logger.error('Error validating Pyramid data: ', e)
