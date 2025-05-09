#!/usr/bin/env python3

from convert_crocolake_obs import ObsSequence

LAT0 = 5
LAT1 = 50
LON0 = -90
LON1 = -30

selected_variables = [
    "DB_NAME",
    "JULD",
    "LATITUDE",
    "LONGITUDE",
    "PRES",
    "TEMP",
    "PRES_QC",
    "TEMP_QC",
    "PRES_ERROR",
    "TEMP_ERROR",
]

db_filters = [
    ("LATITUDE",'>',LAT0),
    ("LATITUDE",'<',LAT1),
    ("LONGITUDE",'>',LON0),
    ("LONGITUDE",'<',LON1),
    ("PRES",'<',1e30),
    ("PRES",'>',-1e30),
    ("TEMP",">",20.5),
    ("TEMP","<",21)
]

obsSeq = ObsSequence(
    "PHY",
    ["ARGO","GLODAP","SprayGliders"],
    "/path/to/crocolake/",
    selected_variables,
    db_filters
)
obsSeq.write_obs_seq()
