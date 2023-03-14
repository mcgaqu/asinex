from .load_actions import load_rols


def get_job_actions():
    return [


    ]

def get_call_actions():
    return [
        
    ]


def get_app_actions(index=None):
    dev = {
        'Group': [

        ],
        'User' : [


        ]

    }
    if not index:
        return dev
    elif not index in dev.keys():
        return None
    return dev[index]
