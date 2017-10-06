dic = {
    "2017.09.30.(토)" : {"h.m.s" : "12:00:00 기준" },
    "2017.09.31.(토)" : {"h.m.s" : "12:00:00 기준" }
}

for key, value in dic.items():
    print( "key : ", key , " / value : ", value["h.m.s"] )