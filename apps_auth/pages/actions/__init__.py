# from .load_actions 
from apps_admin.main1.actions import (
    ac_save_records, ac_delete_records,
    ac_deactivate_records, ac_activate_records,
    ac_lock_records, ac_unlock_records
)
from .biz_actions import  ac_create_i18n
from .load_actions import ac_gen_page

def get_job_actions():
    return [
        
    ]

def get_call_actions(index=None):
    return [
        ac_gen_page,
        ac_create_i18n,

    ]

def get_app_actions(index=None):
    dev = {
		'Page': [
            ac_gen_page,
			ac_create_i18n,

            ac_deactivate_records, ac_activate_records,
            ac_lock_records, ac_unlock_records
		],
		'PageI18n':[
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