from .biz_actions import ac_load_inidata, ac_dataload_run


def get_app_actions(index=None):
    dev = {
        'Website': [
            ac_load_inidata
        ],
        'Dataload': [
            ac_dataload_run,
         ]
    }
    if not index:
        return dev
    elif not index in dev.keys():
        return None
    return dev[index]


