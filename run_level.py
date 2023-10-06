import flywheel
from flywheel_gear_toolkit import GearToolkitContext

def get_hierarchy(fw, d):


    hierarchy = {
        "group": None,
        "project_label": None,
        "subject_label": None,
        "session_label": None,
    
	
    }

    
    destination = fw.get(d)

    hierarchy["group"] = destination.parents["group"]
    for level in ["project", "subject", "session"]:
        container = fw.get(destination.parents[level])
        hierarchy[f"{level}_label"] = container.label

    return hierarchy