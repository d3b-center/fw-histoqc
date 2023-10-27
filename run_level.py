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

def get_acq(fi,group_name, project_label,sub_label,ses_label,names):

  ses=fi.lookup(f'{group_name}/{project_label}/{sub_label}/{ses_label}')
  for acq in ses.acquisitions.iter():
    acq_label = acq.label
    acq_id = acq.id
    for file_obj in acq.files:
        if (file_obj.name==names):
          print(acq_id)
    return acq_id

  

 