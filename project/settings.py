import os


REPO_NAME = 'blog'
DEBUG = True
APP_DIR = os.path.dirname(os.path.abspath(__file__))

FREEZER_DESTINATION = PROJECT_ROOT = os.path.dirname(APP_DIR)
FREEZER_BASE_URL = 'http://localhost/{}'.format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False

FLATPAGES_MARKDOWN_EXTENSIONS = []
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
