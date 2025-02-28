import folium

def addTitle(map, title):
    text = """
    <div style='position:absolute; top:5px;left: 50%;transform: translateX(-50%);z-index:10000;background-color:#ffffffBB;padding:15px;'>
        <h3 style="font-size:16px;margin:0;padding:0"><b>{}</b></h3>
    </div>
    """.format(title)

    map.get_root().html.add_child(folium.Element(text))