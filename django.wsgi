#!/Users/aneeptandel/Sites/frank/env/bin/python

import os
import sys

sys.path.append("/Users/aneeptandel/Sites/frank/env/lib/python3.7/site-packages")
sys.path.append("/Users/aneeptandel/Sites/frank/v3/cogofly/")

os.environ["DJANGO_SETTINGS_MODULE"] = "cogofly.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
