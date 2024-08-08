#!/usr/bin/env python3
import sys
import os
import json
import glob
from google.cloud import vision
from google.cloud import storage

bucket_name='BUCKET-NAME' # BUCKET-NAME
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'PATH/TO/YOUR/ServiceAccountKey.json' # PATH/TO/YOUR/ServiceAccountKey.json

class ocr:
    def __init__(self):
        pass

    def scan(self):
        pass

if __name__ == '__main__':
    ocr()
