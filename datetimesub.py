#!/usr/bin/env python 
from datetime import datetime
start_date = datetime.strptime('2018-06-08 09:05:55', "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime('2018-06-08 09:06:55', "%Y-%m-%d %H:%M:%S")
print abs(end_date-start_date)
