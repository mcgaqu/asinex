#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from websites import WEBSITES
SITE_DIR = Path(__file__).resolve(strict=True).parent
SITE_NAME = os.path.basename(SITE_DIR)

def main(params):
    """Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djengine.settings')
    # print('PARAMS MAIN: ', params)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(params)


if __name__ == '__main__':
     # main()

    print('ARGUMENTOS = ', sys.argv) # ['manage.py, <site_name>, 'runserver'/...]
    if (len(sys.argv) > 1) and (sys.argv[1] in WEBSITES):
        print('extraer SITE_NAME de los parámetros')
       
        SITE_NAME = sys.argv[1]
        print('websites.%s.settings' % SITE_NAME)
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websites.%s.settings' % SITE_NAME)
        main([sys.argv[0]] + sys.argv[2:]) 

    elif (len(sys.argv) > 1) and (sys.argv[1] == 'b2bengine'):
        # extraer "engine" de los parámetros
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b2bengine.settings' % SITE_NAME)
        main([sys.argv[0]] + sys.argv[2:])
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % SITE_NAME)
        main(sys.argv)





