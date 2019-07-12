import time
import datetime

from django.http import request

order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-7:]
date = datetime.datetime.now()


