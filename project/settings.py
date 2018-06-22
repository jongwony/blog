import os


def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))


REPO_NAME = 'blog'
DEBUG = True
APP_DIR = os.path.dirname(os.path.abspath(__file__))
FREEZER_DESTINATION = PROJECT_ROOT = parent_dir(APP_DIR)
FREEZER_BASE_URL = 'http://localhost/{}'.format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'

