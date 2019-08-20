"""一个字符串跨多行"""
claim_num = "303825R03190731005"
s = """
SELECT CPL.Recipient_Account_Type,cpl.*
 FROM CMF_CLM_CLAIM_PAYMENT_LINES CPL
 WHERE 1 = 1
  AND CPL.CLAIM_HEADER_ID IN
    (SELECT CLAIM_HEADER_ID
     FROM CMF_CLM_CLAIM_HEADERS     
     WHERE CLAIM_NUM = %s);
"""

print(s % claim_num)