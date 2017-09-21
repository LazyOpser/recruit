#coding:utf-8
#不加会报错，SyntaxError: Non-ASCII character '\xe5' in file
import cx_Oracle
import os
import sys
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

db=cx_Oracle.connect('uwopr/uw265kopr@10.1.108.42:1521/tmpit')
#db=cx_Oracle.connect('iqryopr','iqrqd96ohpr','10.1.108.42:1521/coresit')


if __name__=="__main__":
    #创建数据库连接，使用游标cursor


    cr3=db.cursor()
    #policyno3=raw_input("请输入需要修改业务来源的保单号：")
    #businesschannel=raw_input("请输入业务来源：")
    '''sql3="update nbz_policy_main t set t.businesschannel = '%s'" %businesschannel
    sql3 += "where t.policyno ='%s' " %policyno3  '''
    #sql4="update nbz_policy_main t set t.businesschannel = '%s' where t.policyno ='1020206072005000043'" %businesschannel
    sql5="select t.insuredname from nbz_policy_main t where t.policyno ='1020206072005000043'"#%policyno3
    #args3=(policyno3,businesschannel)
    #cr3.execute(policyno3,args3)
    #cr3.execute(sql4)
    cr3.execute(sql5)

    result =cr3.fetchall()
    result2=unicode(result)
    result3=str(result).decode('utf8').encode('gb2312')
    '''print type(result)
    a=repr(result)
    print type(a)
    print eval(a)'''
    print "被保险人是：%s"%result
    print result2
    print result3
    cr3.close()
    db.commit()
    db.close()




