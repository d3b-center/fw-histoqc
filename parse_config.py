from typing import Tuple
from flywheel_gear_toolkit import GearToolkitContext


def parse_config(x):
 with x as gtk_context:
    
    api_key_in=(gtk_context.get_input('api-key'))
    fw =api_key_in['key']
    destination_id = gtk_context.destination["id"]

    return (fw,destination_id)