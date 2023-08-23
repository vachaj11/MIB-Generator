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


def delete_empty(table):
    """Delete empty entries in arrays to be made tables, so they trigger appropriate warnings."""
    for i in range(len(table)):
        dic = {}
        for l in table[i]:
            if table[i][l] not in {"", None}:
                dic[l] = table[i][l]
        table[i] = dic


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
    """Take all constructed packets/calibrations/commands and call generation scripts for each table."""
    one_generate(calibrations["mcfs"], "mcf")
    one_generate(calibrations["lgfs"], "lgf")
    one_generate(calibrations["txfs"], "txf")
    two_generate(calibrations["txfs"], "txp")
    one_generate(calibrations["cafs"], "caf")
    two_generate(calibrations["cafs"], "cap")
    one_generate(Tm_packets, "pid")
    one_generate(Tm_packets, "pic")
    one_generate(Tm_packets, "tpcf")
    two_generate(Tm_packets, "pcf")
    two_generate(Tm_packets, "plf")
    two_generate(Tm_packets, "cur")
    two_generate(Tm_packets, "vpd")
    one_generate([Tc_head], "tcp")
    two_generate([Tc_head], "pcpc")
    two_generate([Tc_head], "pcdf")
    one_generate(Tc_packets, "ccf")
    two_generate(Tc_packets, "cpc")
    two_generate(Tc_packets, "cdf")


def one_generate(lists, name):
    """Transform the given 1D object into universal generation array."""
    rows = []
    for i in lists:
        rows.append(vars(i)[name])
    delete_empty(rows)
    generate(name, rows)


def two_generate(lists, name):
    """Transform the given 2D object into universal generation array."""
    rows = []
    for i in lists:
        for l in vars(i)[name]:
            rows.append(l)
    delete_empty(rows)
    generate(name, rows)
