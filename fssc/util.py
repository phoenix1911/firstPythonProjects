def fieldStringBuilder(field):
    a_field = field.split("\n")
    field = ""
    for i in range(len(a_field) - 1):
        a_field[i] = "'" + a_field[i].strip() + "'" + '\n'
        field += a_field[i] + ","
    return field[0:len(field) - 1]

