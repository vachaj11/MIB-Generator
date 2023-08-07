"""This module serves the purpose of storing various data that would otherwise cluster the code elsewhere."""
pid = [
    {"name": "PID_TYPE", "type": ["n", 3], "mandatory": True},
    {"name": "PID_STYPE", "type": ["n", 3], "mandatory": True},
    {"name": "PID_APID", "type": ["n", 5], "mandatory": True},
    {"name": "PID_PI1_VAL", "type": ["n", 10], "mandatory": False},
    {"name": "PIC_PI2_VAL", "type": ["n", 10], "mandatory": False},
    {"name": "PID_SPID", "type": ["n", 10], "mandatory": True},
    {"name": "PID_DESCR", "type": ["c", 64], "mandatory": False},
    {"name": "PID_UNIT", "type": ["c", 8], "mandatory": False},
    {"name": "PID_TPSD", "type": ["n", 10], "mandatory": False},
    {"name": "PID_DFHSIZE", "type": ["n", 12], "mandatory": True},
    {"name": "PID_TIME", "type": ["c", 1], "mandatory": False},
    {"name": "PID_INTER", "type": ["n", 8], "mandatory": False},
    {"name": "PID_VALID", "type": ["c", 1], "mandatory": False},
    {"name": "PID_CHECK", "type": ["n", 1], "mandatory": False},
    {"name": "PID_EVENT", "type": ["c", 1], "mandatory": False},
    {"name": "PIC_EVID", "type": ["c", 17], "mandatory": False},
]
pic = [
    {"name": "PIC_TYPE", "type": ["n", 3], "mandatory": True},
    {"name": "PIC_STYPE", "type": ["n", 3], "mandatory": True},
    {"name": "PIC_PI1_OFF", "type": ["n", 5], "mandatory": True},
    {"name": "PIC_PI1_WID", "type": ["n", 3], "mandatory": True},
    {"name": "PIC_PI2_OFF", "type": ["n", 5], "mandatory": True},
    {"name": "PIC_PI2_WID", "type": ["n", 3], "mandatory": True},
    {"name": "PIC_APID", "type": ["n", 5], "mandatory": False},
]
tpcf = [
    {"name": "TPCF_SPID", "type": ["n", 10], "mandatory": True},
    {"name": "TPCF_NAME", "type": ["c", 12], "mandatory": False},
    {"name": "TPCF_SIZE", "type": ["n", 8], "mandatory": False},
]
pcf = [
    {"name": "PCF_NAME", "type": ["c", 8], "mandatory": True},
    {"name": "PCF_DESCR", "type": ["c", 24], "mandatory": False},
    {"name": "PCF_PID", "type": ["n", 10], "mandatory": False},
    {"name": "PCF_UNIT", "type": ["c", 4], "mandatory": False},
    {"name": "PCF_PTC", "type": ["n", 2], "mandatory": True},
    {"name": "PCF_PFC", "type": ["n", 5], "mandatory": True},
    {"name": "PCF_WIDTH", "type": ["n", 6], "mandatory": False},
    {"name": "PCF_VALID", "type": ["c", 8], "mandatory": False},
    {"name": "PCF_RELATED", "type": ["c", 8], "mandatory": False},
    {"name": "PCF_CATEG", "type": ["c", 1], "mandatory": True},
    {"name": "PCF_NATUR", "type": ["c", 1], "mandatory": True},
    {"name": "PCF_CURTX", "type": ["c", 10], "mandatory": False},
    {"name": "PCF_INTER", "type": ["c", 1], "mandatory": False},
    {"name": "PCF_USCON", "type": ["c", 1], "mandatory": False},
    {"name": "PCF_DECIM", "type": ["n", 3], "mandatory": False},
    {"name": "PCF_PARVAL", "type": ["c", 14], "mandatory": False},
    {"name": "PCF_SUBSYS", "type": ["c", 8], "mandatory": False},
    {"name": "PCF_VALPAR", "type": ["n", 5], "mandatory": False},
    {"name": "PCF_SPTYPE", "type": ["c", 1], "mandatory": False},
    {"name": "PCF_CORR", "type": ["c", 1], "mandatory": False},
    {"name": "PCF_OBTID", "type": ["n", 5], "mandatory": False},
    {"name": "PCF_DARC", "type": ["c", 1], "mandatory": False},
    {"name": "PCF_ENDIAN", "type": ["c", 1], "mandatory": False},
    {"name": "PCF_DESCR2", "type": ["c", 256], "mandatory": False},
]
plf = [
    {"name": "PLF_NAME", "type": ["c", 8], "mandatory": True},
    {"name": "PLF_SPID", "type": ["n", 10], "mandatory": True},
    {"name": "PLF_OFFBY", "type": ["n", 5], "mandatory": True},
    {"name": "PLF_OFFBI", "type": ["n", 1], "mandatory": True},
    {"name": "PLF_NBOCC", "type": ["n", 4], "mandatory": False},
    {"name": "PLF_LGOCC", "type": ["n", 5], "mandatory": False},
    {"name": "PLF_TIME", "type": ["n", 9], "mandatory": False},
    {"name": "PLF_TDOCC", "type": ["n", 9], "mandatory": False},
]
mcf = [
    {"name": "MCF_IDENT", "type": ["c", 10], "mandatory": True},
    {"name": "MCF_DESCR", "type": ["c", 32], "mandatory": False},
    {"name": "MCF_POL1", "type": ["c", 14], "mandatory": True},
    {"name": "MCF_POL2", "type": ["c", 14], "mandatory": False},
    {"name": "MCF_POL3", "type": ["c", 14], "mandatory": False},
    {"name": "MCF_POL4", "type": ["c", 14], "mandatory": False},
    {"name": "MCF_POL5", "type": ["c", 14], "mandatory": False},
]
txf = [
    {"name": "TXF_NUMBR", "type": ["c", 10], "mandatory": True},
    {"name": "TXF_DESCR", "type": ["c", 32], "mandatory": False},
    {"name": "TXF_RAWFMT", "type": ["c", 1], "mandatory": True},
    {"name": "TXF_NALIAS", "type": ["n", 3], "mandatory": False},
]
txp = [
    {"name": "TXP_NUMBR", "type": ["c", 10], "mandatory": True},
    {"name": "TXP_FROM", "type": ["c", 14], "mandatory": True},
    {"name": "TXP_TO", "type": ["c", 14], "mandatory": True},
    {"name": "TXP_ALTXT", "type": ["c", 14], "mandatory": True},
]
caf = [
    {"name": "CAF_NUMBR", "type": ["c", 10], "mandatory": True},
    {"name": "CAF_DESCR", "type": ["c", 32], "mandatory": False},
    {"name": "CAF_ENGFMT", "type": ["c", 1], "mandatory": True},
    {"name": "CAF_RAWFMT", "type": ["c", 1], "mandatory": True},
    {"name": "CAF_RADIX", "type": ["c", 1], "mandatory": False},
    {"name": "CAF_UNIT", "type": ["c", 4], "mandatory": False},
    {"name": "CAF_NCURVE", "type": ["n", 13], "mandatory": False},
    {"name": "CAF_INTER", "type": ["c", 1], "mandatory": False},
]
cap = [
    {"name": "CAP_NUMBR", "type": ["c", 10], "mandatory": True},
    {"name": "CAP_XVALS", "type": ["c", 14], "mandatory": True},
    {"name": "CAP_YVALS", "type": ["c", 14], "mandatory": True},
]
lgf = [
    {"name": "LGF_IDENT", "type": ["c", 10], "mandatory": True},
    {"name": "LGF_DESCR", "type": ["c", 32], "mandatory": False},
    {"name": "LGF_POL1", "type": ["c", 14], "mandatory": True},
    {"name": "LGF_POL2", "type": ["c", 14], "mandatory": False},
    {"name": "LGF_POL3", "type": ["c", 14], "mandatory": False},
    {"name": "LGF_POL4", "type": ["c", 14], "mandatory": False},
    {"name": "LGF_POL5", "type": ["c", 14], "mandatory": False},
]
sizes = {
    "uint8_t": 8,
    "uint16_t": 16,
    "uint32_t": 32,
    "uint64_t": 64,
    "unsigned int": 32,
    "enum": 32,
}
tables_format = {
    "pic": pic,
    "pid": pid,
    "pcf": pcf,
    "tpcf": tpcf,
    "plf": plf,
    "mcf": mcf,
    "txf": txf,
    "txp": txp,
    "caf": caf,
    "cap": cap,
    "lgf": lgf,
}
uint_pfc = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 24, 32, 48, 64]
