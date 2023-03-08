#!/usr/bin/env python

# --------------------------------------
# Imports
# --------------------------------------
import shotgun_api3
from pprint import pprint # useful for debugging

# --------------------------------------
# Globals
# --------------------------------------
# make sure to change this to match your ShotGrid server and auth credentials.
SERVER_PATH = "https://spacecapades.shotgrid.autodesk.com/"
SCRIPT_NAME = 'Python Script'
SCRIPT_KEY = 'ytKsey6jgrhlbwxjeuwwlyw)u'

# --------------------------------------
# Main
# --------------------------------------
if __name__ == '__main__':

    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    # --------------------------------------
    # Create a Shot with data
    # --------------------------------------
    
    batch_data = []
    for i in range (1, 35):
        #print("%02d0" %i)
        data = {
            'project': {"type":"Project","id": 122},
            'code': 'SC_SQ%02d0' %i,
            'sg_status_list': 'ip'
        }
        batch_data.append({"request_type": "create", "entity_type": "Sequence", "data": data})
    result = sg.batch(batch_data)
    pprint(result)
