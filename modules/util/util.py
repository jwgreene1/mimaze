#!/usr/bin/python

import logging
import json

# Create logger
module_logger = logging.getLogger('modules.util.util')

def readJsonFile(filename):
    module_logger.info(u'  util.readJsonFile - Reading JSON file: {0:s}'.format(filename))

    with open(filename) as data_file:
        data = json.load(data_file)

    return data


if __name__ == '__main__':
    print('util called as script')
    module_logger.info('  util default code')
