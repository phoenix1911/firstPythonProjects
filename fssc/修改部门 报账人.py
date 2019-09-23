from fssc.util import fieldStringBuilder


def one(s):
    list = s.split("\t")
    writrSql("'" + list[0].strip() + "'", list[1].strip(), list[2].strip())


def many(claim_num, dept, emp):
    writrSql(fieldStringBuilder(claim_num).strip(), dept.strip(), emp.strip())


def writrSql(claim_num, dept, emp):
    select_sql = """SELECT
    ccch.claim_num 报账单编号
    ,(SELECT ccch.unit_code from hr_org_unit_b ccch where ccch.unit_id = ccch.creation_dept_id) 创建部门
    --,(SELECT ccch.unit_code from hr_org_unit_b ccch where ccch.unit_id = ccch.opr_depart_id) 报账部门
    ,(SELECT he.employee_code from hr_employee he where he.employee_id = ccch.opr_employee_id) 报账人
    --,(SELECT he.employee_code from hr_employee he where he.employee_id = ccch.USE_EMPLOYEE_ID) 创建人姓名
    ,(SELECT he.name from hr_employee he where he.employee_id = ccch.opr_employee_id) 报账人
    --,(SELECT he.name from hr_employee he where he.employee_id = ccch.USE_EMPLOYEE_ID) 创建人姓名
    ,(SELECT ccch.name from hr_org_unit_b ccch where ccch.unit_id = ccch.creation_dept_id) 创建部门
    --,(SELECT ccch.name from hr_org_unit_b ccch where ccch.unit_id = ccch.opr_depart_id) 报账部门
    FROM cmf_clm_claim_headers        ccch  -- 报账单头表
    WHERE ccch.claim_num IN(""" + claim_num + """);
    """

    update_sql = """
UPDATE cmf_clm_claim_headers ccch SET"""
    if len(dept) > 0:
        update_sql += """
    ccch.opr_depart_id    =(SELECT hou.unit_id FROM hr_org_unit_b hou WHERE hou.unit_code = '""" + dept + """'),
    ccch.CREATION_DEPT_ID =(SELECT hou.unit_id FROM hr_org_unit_b hou WHERE hou.unit_code = '""" + dept + """'),"""
    if len(emp) > 0:
        update_sql += """
    ccch.OPR_EMPLOYEE_ID  =(SELECT he.employee_id FROM hr_employee he WHERE he.employee_code = '""" + emp + """'),
    ccch.USE_EMPLOYEE_ID  =(SELECT he.employee_id FROM hr_employee he WHERE he.employee_code = '""" + emp + """'),"""
    update_sql += """
    ccch.last_update_date = sysdate
WHERE ccch.claim_num IN(""" + claim_num + """);
    """
    writerfile(select_sql + "\n\n" + update_sql + "\n\n" + select_sql)


def writerfile(sql):
    file = open(
        "C:\\Users\\JiaLong\\.DataGrip2019.1\\config\\consoles\\db\\3ee2783f-bed1-4f15-8bcf-f9fb492ab541\\u_部门 报账人.sql",
        mode='w', encoding='utf-8')
    file.write(sql)
    file.close()


one("""303227QC2900001130	00320027006600000000	32233939
""")


# many("", "", "")
