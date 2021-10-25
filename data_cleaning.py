import pandas as pd
import os
import plotly

sm_file = ('04_sm','05_sm','06_sm')

root = os.getcwd()

sm_colnames = ['powerallphases',
'powerl1','powerl2','powerl3',
'currentneutral','currentl1',
'currentl2','currentl3','voltagel1',
'voltagel2','voltagel3','phaseanglevoltagel2l1',
'phaseanglevoltagel3l1','phaseanglecurrentvoltagel1',
'phaseanglecurrentvoltagel2','phaseanglecurrentvoltagel3']
def clean(df):
    df_address = []
    for f in sorted(os.listdir(os.getcwd()+'/'+df)):
        path = os.getcwd()+'/'+df+'/'+f
        df_tmp = pd.read_csv(path,names = sm_colnames,header = None)
        df_tmp = df_tmp.groupby(df_tmp.index//3600).sum()
        df_tmp['Date'] = f.split('.')[0]
        df_tmp['Time'] = df_tmp.index 
        df_address.append(df_tmp)
    final_df = pd.concat(df_address,axis = 0, ignore_index=True)
    return final_df

sm_df_4 = clean(sm_file[0])
sm_df_4['Time'] = sm_df_4['Date'] +'-' + sm_df_4['Time'].astype('str')
sm_df_4 = sm_df_4.drop(columns = ['Date'])
for row in range(sm_df_4.shape[0]):
    sm_df_4['Time'][row] = datetime.strptime(sm_df_4['Time'][row],'%Y-%m-%d-%H')
sm_df_5 = clean(sm_file[1])
sm_df_5['Time'] = sm_df_5['Date'] +'-' + sm_df_5['Time'].astype('str')
sm_df_5 = sm_df_5.drop(columns = ['Date'])
for row in range(sm_df_5.shape[0]):
    sm_df_5['Time'][row] = datetime.strptime(sm_df_5['Time'][row],'%Y-%m-%d-%H')
sm_df_6 = clean(sm_file[2])
sm_df_6['Time'] = sm_df_6['Date'] +'-' + sm_df_6['Time'].astype('str')
sm_df_6 = sm_df_6.drop(columns = ['Date'])
for row in range(sm_df_6.shape[0]):
    sm_df_6['Time'][row] = datetime.strptime(sm_df_6['Time'][row],'%Y-%m-%d-%H')

#output for sm: using the powerallphases 
sm_df_4_output = sm_df_4[['powerallphases','Time']]
sm_df_4_output['House'] = '04'

sm_df_5_output = sm_df_5[['powerallphases','Time']]
sm_df_5_output['House'] = '05'

sm_df_6_output = sm_df_6[['powerallphases','Time']]
sm_df_6_output['House'] = '06'

sm_final_output = pd.concat([sm_df_4_output,sm_df_5_output,sm_df_6_output])

sm_final_output.to_csv('sm_final_output.csv',index = False)


plug_folder = ['04_plugs','05_plugs','06_plugs']
plug_second_folder = [[] for _ in range(3)]
for i in range(0,len(plug_folder)):
    for j in sorted(os.listdir(os.getcwd()+'/'+plug_folder[i])):
        if j !='.DS_Store':
            plug_second_folder[i].append(j)



def clean_plugs(household):
    if household == 4:
        app = ['Fridge','Kitchen appliances','Lamp','Stereo and laptop','Freezer','Tablet','Entertainment','Microwave']
        app_result = [[] for _ in range(len(app))]
        for f in range(len(plug_second_folder[0])):
            final_result = []
            for file in sorted(os.listdir(os.getcwd()+'/'+plug_folder[0]+'/'+plug_second_folder[0][f])):
                result = pd.read_csv(os.getcwd()+'/'+plug_folder[0]+'/'+plug_second_folder[0][f]+'/'+file,header=None)
                result = result.groupby(result.index//3600).sum()
                result.columns = [app[f]]
                result['Date'] = file.split('.')[0]
                result['Time'] = result.index 
                result['period'] = result['Date'] + '-' + result['Time'].astype('str')
                result = result.drop(columns = ['Date','Time'])
                final_result.append(result)
                
            app_result[f] = pd.concat(final_result,axis = 0, ignore_index=True)
            
        return app_result

    if household == 5:
        app = ['Tablet','Coffee machine','Fountain','Microwave','Fridge','Entertainment','PC','Kettle']
        app_result = [[] for _ in range(len(app))]
        for f in range(len(plug_second_folder[1])):
            final_result = []
            for file in sorted(os.listdir(os.getcwd()+'/'+plug_folder[1]+'/'+plug_second_folder[1][f])):
                result = pd.read_csv(os.getcwd()+'/'+plug_folder[1]+'/'+plug_second_folder[1][f]+'/'+file,header=None)
                result = result.groupby(result.index//3600).sum()
                result.columns = [app[f]]
                result['Date'] = file.split('.')[0]
                result['Time'] = result.index 
                result['period'] = result['Date'] + '-' + result['Time'].astype('str')
                result = result.drop(columns = ['Date','Time'])
                final_result.append(result)
                
            app_result[f] = pd.concat(final_result,axis = 0, ignore_index=True)
            
        return app_result

    if household == 6:
        app = ['Lamp','Laptop','Router','Coffee machine','Entertainment','Fridge','Kettle']
        app_result = [[] for _ in range(len(app))]
        for f in range(len(plug_second_folder[2])):
            final_result = []
            for file in sorted(os.listdir(os.getcwd()+'/'+plug_folder[2]+'/'+plug_second_folder[2][f])):
                result = pd.read_csv(os.getcwd()+'/'+plug_folder[2]+'/'+plug_second_folder[2][f]+'/'+file,header=None)
                result = result.groupby(result.index//3600).sum()
                result.columns = [app[f]]
                result['Date'] = file.split('.')[0]
                result['Time'] = result.index 
                result['period'] = result['Date'] + '-' + result['Time'].astype('str')
                result = result.drop(columns = ['Date','Time'])
                final_result.append(result)
                
            app_result[f] = pd.concat(final_result,axis = 0, ignore_index=True)
            
        return app_result

from datetime import datetime    
# 04 plugs 
df_list_04 = clean_plugs(4)
final_list = df_list_04[0]['period'].tolist() 
missing_list = [[] for _ in range(len(df_list_04))]
for app_index in range(len(df_list_04)):
    for period in final_list:
        if period not in df_list_04[app_index]['period'].values:
            missing_list[app_index].append(period)
for i in range(len(missing_list)):
    if len(missing_list[i]) != 0:
        new_dict = {'{}'.format(df_list_04[i].columns[0]):[0 for _ in range(len(missing_list[i]))],'period':missing_list[i]}
        new_df = pd.DataFrame(new_dict)
        df_list_04[i] = pd.concat([df_list_04[i],new_df],ignore_index=True)
for i in range(len(df_list_04)):
    df_list_04[i].loc[df_list_04[i][df_list_04[i].columns[0]]<0,'{}'.format(df_list_04[i].columns[0])] = 0
    

df_list_04[7] = df_list_04[7].iloc[1: , :]

final_plugs_04 = pd.concat(df_list_04,axis = 1)
final_plugs_04 = final_plugs_04.loc[:,~final_plugs_04.columns.duplicated()]
final_plugs_04.drop(final_plugs_04.tail(1).index,inplace=True)
for row in range(final_plugs_04.shape[0]):
    final_plugs_04['period'][row] = datetime.strptime(final_plugs_04['period'][row],'%Y-%m-%d-%H')

# 05plugs
df_list_05 = clean_plugs(5)
final_list = df_list_05[0]['period'].tolist() 
missing_list = [[] for _ in range(len(df_list_05))]
for app_index in range(len(df_list_05)):
    for period in final_list:
        if period not in df_list_05[app_index]['period'].values:
            missing_list[app_index].append(period)
for i in range(len(missing_list)):
    if len(missing_list[i]) != 0:
        new_dict = {'{}'.format(df_list_05[i].columns[0]):[0 for _ in range(len(missing_list[i]))],'period':missing_list[i]}
        new_df = pd.DataFrame(new_dict)
        df_list_05[i] = pd.concat([df_list_05[i],new_df],ignore_index=True)
for i in range(len(df_list_05)):
    df_list_05[i].loc[df_list_05[i][df_list_05[i].columns[0]]<0,'{}'.format(df_list_05[i].columns[0])] = 0
    

final_plugs_05 = pd.concat(df_list_05,axis = 1)
final_plugs_05 = final_plugs_05.loc[:,~final_plugs_05.columns.duplicated()]
for row in range(final_plugs_05.shape[0]):
    final_plugs_05['period'][row] = datetime.strptime(final_plugs_05['period'][row],'%Y-%m-%d-%H')
# 06 plugs

df_list_06 = clean_plugs(6)
final_list = df_list_06[0]['period'].tolist() 
missing_list = [[] for _ in range(len(df_list_06))]
for app_index in range(len(df_list_06)):
    for period in final_list:
        if period not in df_list_06[app_index]['period'].values:
            missing_list[app_index].append(period)
for i in range(len(missing_list)):
    if len(missing_list[i]) != 0:
        new_dict = {'{}'.format(df_list_06[i].columns[0]):[0 for _ in range(len(missing_list[i]))],'period':missing_list[i]}
        new_df = pd.DataFrame(new_dict)
        df_list_06[i] = pd.concat([df_list_06[i],new_df],ignore_index=True)
for i in range(len(df_list_06)):
    df_list_06[i].loc[df_list_06[i][df_list_06[i].columns[0]]<0,'{}'.format(df_list_06[i].columns[0])] = 0
    

final_plugs_06 = pd.concat(df_list_06,axis = 1)
final_plugs_06 = final_plugs_06.loc[:,~final_plugs_06.columns.duplicated()]
final_plugs_06.drop(final_plugs_06.tail(1).index,inplace=True)
final_plugs_06 = final_plugs_06[final_plugs_06['period'].notna()]

for row in range(final_plugs_06.shape[0]):
    final_plugs_06['period'][row] = datetime.strptime(final_plugs_06['period'][row],'%Y-%m-%d-%H')
# transform period into time stamp
from datetime import datetime 
date_time_example = '2012-06-27-1'
data_time_output = datetime.strptime(date_time_example,'%Y-%m-%d-%H')


# merge the common column together to create a output file
final_out_put_04_plugs = final_plugs_04[['Fridge','period','Entertainment']]
final_out_put_04_plugs['House'] = '04' 

final_out_put_05_plugs = final_plugs_05[['Fridge','period','Entertainment']]
final_out_put_05_plugs['House'] = '05' 

final_out_put_06_plugs = final_plugs_06[['Fridge','period','Entertainment']]
final_out_put_06_plugs['House'] = '06' 

#merge output
final_output_df = pd.concat([final_out_put_04_plugs,final_out_put_05_plugs,final_out_put_06_plugs])

final_output_df.to_csv('plugs_output.csv',index = False)