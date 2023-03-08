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
SERVER_PATH = "https://spacecapades.shotgrid.autodesk.com"
SCRIPT_NAME = 'Python Script'
SCRIPT_KEY = 'ytKsey6jgrhlbwxjeuwwlyw)u'

# --------------------------------------
# Main
# --------------------------------------
if __name__ == '__main__':

    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    # --------------------------------------
    # Create a bunch of Assets with data
    # --------------------------------------

    batch_data = []
    batch_props = ['Suitcase', 'Deckchair_F', 'Deckchair_B', 'Tongue', 'Sunglasses_F',
                        'Sunglasses_B', 'Egg']

    for p in batch_props:
        data = {
            'project': {"type":"Project","id": 122},
            'code': p,
            'sg_asset_type' : 'Prop'
        }
        batch_data.append({"request_type": "create", "entity_type": "Asset", "data": data})
    result = sg.batch(batch_data)
    pprint(result)
