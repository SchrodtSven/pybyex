from datetime import datetime

# timestamp is number of seconds since 1970-01-01 
#
# timestamp = 1545730073
timestamp = 1751935680
timestamp = 1325412060
# convert the timestamp to a datetime object in the local timezone
dt_object = datetime.fromtimestamp(timestamp)

# print the datetime object and its type
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))


