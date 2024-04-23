
from apps_admin.main1.actions import (
    ac_save_records, ac_delete_records,
    ac_deactivate_records, ac_activate_records,
    ac_lock_records, ac_unlock_records
)
from .biz_actions import ac_expand_layout, ac_create_i18n, ac_expand_component_layout 
from .load_actions import ac_gen_page

def get_job_actions():
    return [
        
    ]

def get_call_actions(index=None):
    return [
        ac_expand_layout,
        ac_create_i18n,
        ac_expand_component_layout
    ]

def get_app_actions(index=None):
    dev = {
        'Component': [
            ac_deactivate_records, ac_activate_records,
            ac_lock_records, ac_unlock_records       
        ],
		'Layout': [
            ac_expand_layout,
			ac_create_i18n,
            # ac_expand_component_layout,
            ac_deactivate_records, ac_activate_records,
            ac_lock_records, ac_unlock_records,
            ac_gen_page
		],
		'LayoutI18n':[
			# ac_save_records, # los datos-factor de la hoja de calculo
            ac_deactivate_records, ac_activate_records,
            ac_lock_records, ac_unlock_records
		],
    }
    if not index:
        return dev
    elif not index in dev.keys():
        return None
    return dev[index]