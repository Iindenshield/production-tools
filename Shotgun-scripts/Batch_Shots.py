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
    last_seq = input('If the first shot isnt the sequence first shot, enter last sequence {code: code_value, id: id_value, type: Sequence}. Otherwise enter -')
    if last_seq == '-':
        last_seq = {}
    for i in range (2, 35):
        #print("%02d0" %i)
        filters = [['code', 'is', 'SC_SQ%02d0' %i]]
        code_field = ['code']
        seq = sg.find_one('Sequence',filters, code_field)
        #pprint(seq)
        if seq != None:
            last_seq = seq 
            #pprint('SEQ EXISTS \n')
            #pprint(last_seq)
        data = {
            'project': {"type":"Project","id": 122},
            'code': last_seq['code'] + '_SH%02d0' %i,
            'sg_status_list': 'ip',
            'sg_shot_type' : 'Full CG',
            'sg_sequence' : {'type' : 'Sequence', 'id' : last_seq['id']}
        }
        batch_data.append({"request_type": "create", "entity_type": "Shot", "data": data})
    result = sg.batch(batch_data)