# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:03:26 2017

@author: Administrator
"""
import os
import numpy as np
import pandas as pd
import openpyxl
ori_data = open("D:\\06.python\A171102.160116.R0001.VERT",'r',encoding='gb18030',errors='ignore') .read()

def get_bias(data):
    sp_b = data.find("Biasvolt[mV]=")
    ed_b = data.find("Current[A]")
    ed_c = data.find("Sec/line:")
    bias= data[sp_b+13:ed_b-1]
    curr = data[ed_b+13:ed_c-1]
    par = np.array([bias,curr])
    return par

def get_DATA(data):   # get the effective data from "DATA" cut the useless part of data(parameters)
    data_s = data.find("DATA")
    u_DATA = data[data_s+50:]
    return u_DATA


with open("1.txt", "w") as f:
        f.write(get_DATA(ori_data))

column_name1=["Volatge","列名2","Current","dI/dV","列名1"]

column_name2=["mV","列名2","nA","a.u.","列名2"]

column_name3=["列名3","列名3","列名3","列名3","列名3"]

text_file = r"D:\06.python\1.txt" # open()

data = np.loadtxt(text_file)
data1 = np.delete(data,0,axis=1)
pd_data = pd.DataFrame(data1)
pd_data.columns = column_name1

 #插入行（列名）
insert_row = pd.DataFrame(column_name3)
insert_row1 = insert_row.T
insert_row1.columns=column_name1

insert_row2=pd.DataFrame(column_name2)
insert_row3=insert_row2.T
insert_row3.columns=column_name1

df1=[insert_row1,pd_data]
new_pd_data=pd.concat(df1,axis=0)

df2=[insert_row3,new_pd_data]
new_pd_data1=pd.concat(df2,axis=0)

new_pd_data2=new_pd_data1.reset_index(drop = True)

#删除多于行
new_pd_data2=new_pd_data2.drop(new_pd_data.index[3:26]) # 调开头
new_pd_data3=new_pd_data2.reset_index(drop = True)

#读取列数据合并
line2=new_pd_data3.iloc[0:980,0:1]  # 调结尾
line4=new_pd_data3.iloc[0:980,2:3]
line5=new_pd_data3.iloc[0:980,3:4]
line24=pd.merge(line2,line4,left_index=True, right_index=True)
line25=pd.merge(line2,line5,left_index=True, right_index=True)


#把数据存入excel中的sheet表中
writer = pd.ExcelWriter('light.xlsx')
line24.to_excel(writer,'sheet1',index=False)
line25.to_excel(writer,'sheet2',index=False)
writer.save()

os.remove("1.txt")
