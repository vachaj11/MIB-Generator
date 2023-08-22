"""This module serves the purpose of generating MIB databases from inputed objects and checking their validity."""
import data.longdata as longdata
import parsing.load as load

out_path = load.out_dir


def list_to_mib(lis):
    """Convert a 2D list of values into a string formatted as MIB ASCII file."""
    rowstr = []
    for row in lis:
        rowstr.append("\t".join(row))
    out = "\n".join(rowstr)
    return out


def save_mib(mib, name):
    """Save the string-MIB database into the specified folder."""
    path = out_path + "/" + name + ".dat"
    fil = open(path, "w")
    fil.write(mib)
    fil.close()


def check(value, typ):
    """Check whether the given value matches the given type."""
    if len(value) > typ[1]:
        return False
    if typ[0] == "n":
        try:
            x = int(value)
        except:
            return False
    if typ[0] == "c":
        if (not value.isascii()) or bool({'"', "&", "<", ">"} & set(value)):
            return False
    return True


def exclude_repetition(table, typ):
    """Check whether there is any repetition in columns where entries should be unique and if so, delete additional rows."""
    constraints = longdata.unique_entries[typ]
    redundance = set()
    for i in constraints:
        bare_table = []
        for l in table:
            bare_table.append([l[x - 1] for x in i])
        for x in range(len(bare_table)):
            for y in range(len(bare_table)):
                if (
                    bare_table[x] == bare_table[y]
                    and y > x
                    and "".join(bare_table[x]) != ""
                ):
                    redundance.add(y)
    if redundance:
        print(
            "Warn.:\tFound repetition in table "
            + typ
            + ". Deleting rows: "
            + str(redundance)[1:-1]
            + ". (This is to be expected for some tables like pic.)"
        )
    indexes = sorted(list(redundance), reverse=True)
    for i in indexes:
        table.pop(i)


def generate(table_type, source):
    """From a list of entries (per rows) generate and save a MIB database of a given type."""
    columns = longdata.tables_format[table_type]
    table = []
    row_ind = 1
    for i in source:
        row = []
        for l in columns:
            if l["name"] in i.keys():
                val = str(i[l["name"]])
                row.append(val)
                if not check(val, l["type"]):
                    print(
                        "Warn.:\tThe value in table "
                        + table_type
                        + ", column "
                        + l["name"]
                        + ", row "
                        + str(row_ind)
                        + " doesn't have the required type."
                    )
                    print("\tValue: " + str(val) + "; Type: " + str(l["type"]))
            else:
                row.append("")
                if l["mandatory"]:
                    print(
                        "Warn.:\tMissing a mandatory entry in table "
                        + table_type
                        + ", column "
                        + l["name"]
                        + ", row "
                        + str(row_ind)
                        + "."
                    )

        table.append(row)
        row_ind += 1
    exclude_repetition(table, table_type)
    mib = list_to_mib(table)
    save_mib(mib, table_type)


def generation_hub(Tm_packets, Tc_packets, calibrations, Tc_head):
    mcf_generate(calibrations["mcfs"])
    txf_generate(calibrations["txfs"])
    txp_generate(calibrations["txfs"])
    caf_generate(calibrations["cafs"])
    cap_generate(calibrations["cafs"])
    lgf_generate(calibrations["lgfs"])
    pid_generate(Tm_packets)
    pic_generate(Tm_packets)
    tpcf_generate(Tm_packets)
    pcf_generate(Tm_packets)
    plf_generate(Tm_packets)
    cur_generate(Tm_packets)
    vpd_generate(Tm_packets)
    tcp_generate([Tc_head])
    pcpc_generate([Tc_head])
    ccf_generate(Tc_packets)
    cpc_generate(Tc_packets)
    


def pid_generate(packets):
    rows = []
    for i in packets:
        rows.append(i.pid)
    generate("pid", rows)


def pic_generate(packets):
    rows = []
    for i in packets:
        rows.append(i.pic)
    generate("pic", rows)


def tpcf_generate(packets):
    rows = []
    for i in packets:
        rows.append(i.tpcf)
    generate("tpcf", rows)


def pcf_generate(packets):
    rows = []
    for i in packets:
        for l in i.pcf:
            rows.append(l)
    generate("pcf", rows)


def plf_generate(packets):
    rows = []
    for i in packets:
        for l in i.plf:
            rows.append(l)
    generate("plf", rows)


def cur_generate(packets):
    rows = []
    for i in packets:
        for l in i.cur:
            rows.append(l)
    generate("cur", rows)


def mcf_generate(mcfs):
    rows = []
    for i in mcfs:
        rows.append(i.mcf)
    generate("mcf", rows)


def txf_generate(txfs):
    rows = []
    for i in txfs:
        rows.append(i.txf)
    generate("txf", rows)


def txp_generate(txfs):
    rows = []
    for i in txfs:
        for l in i.txp:
            rows.append(l)
    generate("txp", rows)


def lgf_generate(lgfs):
    rows = []
    for i in lgfs:
        rows.append(i.lgf)
    generate("lgf", rows)


def caf_generate(cafs):
    rows = []
    for i in cafs:
        rows.append(i.caf)
    generate("caf", rows)


def cap_generate(cafs):
    rows = []
    for i in cafs:
        for l in i.cap:
            rows.append(l)
    generate("cap", rows)


def vpd_generate(packets):
    rows = []
    for i in packets:
        for l in i.vpd:
            rows.append(l)
    generate("vpd", rows)
    
def tcp_generate(packets):
    rows = []
    for i in packets:
        rows.append(i.tcp)
    generate("tcp", rows)

def pcpc_generate(packets):
    rows = []
    for i in packets:
        for l in i.pcpc:
            rows.append(l)
    generate("pcpc", rows)
    
def ccf_generate(packets):
    rows = []
    for i in packets:
        rows.append(i.ccf)
    generate("ccf", rows)
    
def cpc_generate(packets):
    rows = []
    for i in packets:
        for l in i.cpc:
            rows.append(l)
    generate("cpc", rows)
