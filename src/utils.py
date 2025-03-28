import folium
import datetime

def addTitle(map, title):
    text = """
    <div style='position:absolute; top:5px;left:50px;z-index:10000;background-color:#ffffffBB;padding:15px;'>
        <h3 style="font-size:16px;margin:0;padding:0"><b>{}</b></h3>
    </div>
    """.format(title)

    map.get_root().html.add_child(folium.Element(text))

# Convert current to only time like the others
def dt_to_time(dt):
    dt = datetime.datetime.strptime(dt[:-6], '%Y-%m-%d %H:%M:%S.%f')
    return dt.time()

def time_to_time(dt):
    return datetime.datetime.strptime(dt, '%H:%M:%S.%f').time()


def time_to_time_str(dt):
    return datetime.datetime.strptime(dt, '%H:%M:%S.%f').strftime('%H:%M')

# Calculate difference between time_reference and given time
def calculate_difference_to_timereference(dt, time_reference):
    diff = datetime.datetime.combine(datetime.date.min, dt) - datetime.datetime.combine(datetime.date.min, time_reference)
    return round(diff.total_seconds() / 60)

def categorize_time_to_half_hour_numerical(dt):
    h = dt.hour
    if dt.minute < 30:
        return h
    else:
        return h + 0.5
    
def categorize_time_to_half_hour(dt):
    h = dt.hour
    if dt.minute < 30:
        return f"{h:02d}:00 - {h:02d}:30"
    else:
        return f"{h:02d}:30 - {h+1:02d}:00"  
    
def categorize_time_to_6min_numerical(dt_str):
    dt = datetime.datetime.strptime(dt_str, '%H:%M')
    h = dt.hour
    m = dt.minute
    return h + (m // 6) * 0.1    

def categorize_time_to_6min(dt_str):
    dt = datetime.datetime.strptime(dt_str, '%H:%M')
    h = dt.hour
    m = dt.minute
    start_minute = (m // 6) * 6
    end_minute = start_minute + 6
    return f"{h:02}:{start_minute:02} - {h:02}:{end_minute:02}"