import datetime
import pandas as pd
import numpy as np
from calendar import month_name

df = pd.read_csv('C:/Users/vipul.srivastava01/Desktop/Streamlit/Intelligent Loan Pipeline Managment DATA.csv', low_memory = False)

# Extracting year from string data format
def extract_year_from_string(column_name):
    get_year = []
    for i in range(len(df)):
        if type(column_name[i]) == str:
            date = datetime.datetime.strptime(column_name[i], '%A, %B %d, %Y')
            #if date.year not in get_year:
            year = date.strftime("%Y")
            get_year.append(year)
        else:
            get_year.append(column_name[i])
    return(get_year)

# Extracting month from string data format
def extract_month_from_string(column_name):
    get_month = []
    for i in range(len(df)):
        if type(column_name[i]) == str:
            date = datetime.datetime.strptime(column_name[i], '%A, %B %d, %Y')
            month = date.strftime("%B")
            get_month.append(month)
        else:
            get_month.append(column_name[i])
    return(get_month)        

# Extracting year from float data format
def extract_year_from_float(column_name):
    get_year = []
    for i in range(len(df)):
        column_name_str = str(column_name[i])
        if column_name_str != "nan":
            date = datetime.datetime.strptime(column_name_str, '%m/%d/%Y')
            #if date.year not in get_year:
            year = date.strftime("%Y")
            get_year.append(year)
        else:
            get_year.append(column_name_str)
    return(get_year)

# Extracting month from float data format
def extract_month_from_float(column_name):
    get_month = []
    for i in range(len(df)):
        column_name_str = str(column_name[i])
        if column_name_str != "nan":
            date = datetime.datetime.strptime(column_name_str, '%m/%d/%Y')
            month = date.strftime("%B")
            get_month.append(month)
        else:
            get_month.append(column_name_str)
    return(get_month)

# Extracting year from float data format but different date format
def extract_year_from_float_different_date_format(column_name):
    get_year = []
    for i in range(len(df)):
        column_name_str = str(column_name[i])
        if column_name_str != "nan":
            date = datetime.datetime.strptime(column_name_str, '%A, %B %d, %Y')
            #if date.year not in get_year:
            year = date.strftime("%Y")
            get_year.append(year)
        else:
            get_year.append(column_name_str)
    return(get_year)

# Extracting month from float data format but different date format
def extract_month_from_float_different_date_format(column_name):
    get_month = []
    for i in range(len(df)):
        column_name_str = str(column_name[i])
        if column_name_str != "nan":
            date = datetime.datetime.strptime(column_name_str, '%A, %B %d, %Y')
            month = date.strftime("%B")
            get_month.append(month)
        else:
            get_month.append(column_name_str)
    return(get_month)        

# Converting data types from float to string of a column with mixed data types
def change_data_types(column_name):
    data_type_list = []
    for i in range(len(df)):
        if type(column_name[i]) == float:
            data_type_list.append(str(column_name[i]))
        else:
            data_type_list.append(column_name[i])
    return(data_type_list)

# Updating column values
def update_column_values(column_name):
    column_new_value = []
    column_name_str = column_name.astype(str)
    for i in range(len(df)):
        if column_name_str[i] != "nan":
            column_new_value.append("Closed")
        else:
            column_new_value.append("Pending")
    return column_new_value

random_loan_number = np.random.randint(126792, 998743, 155211)
df["Loan Number"] = random_loan_number.astype(str)

df["ExpRate Lock1"] = df["ExpRate Lock"].astype("Int64")
df["ExpAppraisal1"] = df["ExpAppraisal"].astype("Int64")
df["Exp_Title1"] = df["Exp_Title"].astype("Int64")
df["ExpCredit_Exp1"] = df["ExpCredit_Exp"].astype("Int64")
df["Exp_VVOE1"] = df["Exp_VVOE"].astype("Int64")
df["Exp_HOI1"] = df["Exp_HOI"].astype("Int64")
df["Exp_Payoff1"] = df["Exp_Payoff"].astype("Int64")
df["Exp_Income1"] = df["Exp_Income"].astype("Int64")

df["Extracted Year (GFE Application Date)"] = extract_year_from_string(df["GFE Application Date"])
df["Extracted Month (GFE Application Date)"] = extract_month_from_string(df["GFE Application Date"])

df["Extracted Year (Borrower Intent to Continue Date)"] = extract_year_from_float(df["Borrower Intent to Continue Date"])
df["Extracted Month (Borrower Intent to Continue Date)"] = extract_month_from_float(df["Borrower Intent to Continue Date"])

df["Extracted Year (Milestone Date - Approval)"] = extract_year_from_float_different_date_format(df["Milestone Date - Approval"])
df["Extracted Month (Milestone Date - Approval)"] = extract_month_from_float_different_date_format(df["Milestone Date - Approval"])
df["Extracted Year (Milestone Date - Submittal)"] = extract_year_from_float_different_date_format(df["Milestone Date - Submittal"])
df["Extracted Month (Milestone Date - Submittal)"] = extract_month_from_float_different_date_format(df["Milestone Date - Submittal"])
df["Extracted Year (Milestone Date - Clear To Close)"] = extract_year_from_float_different_date_format(df["Milestone Date - Clear To Close"])
df["Extracted Month (Milestone Date - Clear To Close)"] = extract_month_from_float_different_date_format(df["Milestone Date - Clear To Close"])

df["Loan Officer"] = change_data_types(df["Loan Officer"])
df["Loan Processor"] = change_data_types(df["Loan Processor"])
df["Loan Closer"] = change_data_types(df["Loan Closer"])
df["Loan Type"] = change_data_types(df["Loan Type"])

df["ExpRate Lock"] = update_column_values(df["ExpRate Lock"])
df["ExpAppraisal"] = update_column_values(df["ExpAppraisal"])
df["Exp_Title"] = update_column_values(df["Exp_Title"])
df["ExpCredit_Exp"] = update_column_values(df["ExpCredit_Exp"])
df["Exp_VVOE"] = update_column_values(df["Exp_VVOE"])
df["Exp_HOI"] = update_column_values(df["Exp_HOI"])
df["Exp_Payoff"] = update_column_values(df["Exp_Payoff"])
df["Exp_Income"] = update_column_values(df["Exp_Income"])

df["Progress"] = df[["Progress"]].astype(int)
df["Loan Number"] = df[["Loan Number"]].astype("Int64")
df["Loan Number"] = df["Loan Number"].astype(str)

rate_lock_list = []
for i in range(len(df)):
    if pd.isnull(df["ExpRate Lock1"][i]) == False:
        if (-1961 <= (df["ExpRate Lock1"][i]) < -1541):
            rate_lock_list.append("Expired")
        elif (-1541 <= df["ExpRate Lock1"][i] < -1121):
            rate_lock_list.append("Expiring Soon")
        elif (-1121 <= df["ExpRate Lock1"][i]):
            rate_lock_list.append("Not Expired")
    else:
        rate_lock_list.append("Pending")
df["ExpRate Lock1"] = rate_lock_list


appraisal_list = []
for i in range(len(df)):
    if pd.isnull(df["ExpAppraisal1"][i]) == False:
        if (-1869 <= df["ExpAppraisal1"][i] < -1470):
            appraisal_list.append("Expired")
        elif (-1470 <= df["ExpAppraisal1"][i] < -1071):
            appraisal_list.append("Expiring Soon")
        elif (-1071 <= df["ExpAppraisal1"][i]):
            appraisal_list.append("Not Expired")
    else:
        appraisal_list.append("Pending") 
df["ExpAppraisal1"] = appraisal_list

title_list = []
for i in range(len(df)):
    if pd.isnull(df["Exp_Title1"][i]) == False:
        if (-2014 <= df["Exp_Title1"][i] < -1511):
            title_list.append("Expired")
        elif (-1511 <= df["Exp_Title1"][i] < -1008):
            title_list.append("Expiring Soon")
        elif (-1008 <= df["Exp_Title1"][i]):
            title_list.append("Not Expired")
    else:
        title_list.append("Pending")
df["Exp_Title1"] = title_list

credit_list = []
for i in range(len(df)):
    if pd.isnull(df["ExpCredit_Exp1"][i]) == False:
        if (-44971 <= df["ExpCredit_Exp1"][i] < -30128):
            credit_list.append("Expired")
        elif (-30128 <= df["ExpCredit_Exp1"][i] < -15285):
            credit_list.append("Expiring Soon")
        elif (-15285 <= df["ExpCredit_Exp1"][i]):
            credit_list.append("Not Expired")
    else:
        credit_list.append("Pending")
df["ExpCredit_Exp1"] = credit_list

vvoe_list = []
for i in range(len(df)):
    if pd.isnull(df["Exp_VVOE1"][i]) == False:
        if (-1089 <= df["Exp_VVOE1"][i] < -950):
            vvoe_list.append("Expired")
        elif (-950 <= df["Exp_VVOE1"][i] < -811):
            vvoe_list.append("Expiring Soon")
        elif (-811 <= df["Exp_VVOE1"][i]):
            vvoe_list.append("Not Expired")
    else:
        vvoe_list.append("Pending")
df["Exp_VVOE1"] = vvoe_list

hoi_list = []
for i in range(len(df)):
    if pd.isnull(df["Exp_HOI1"][i]) == False:
        if (-1924 <= df["Exp_HOI1"][i] < -1506):
            hoi_list.append("Expired")
        elif (-1506 <= df["Exp_HOI1"][i] < -1088):
            hoi_list.append("Expiring Soon")
        elif (-1088 <= df["Exp_HOI1"][i]):
            hoi_list.append("Not Expired")
    else:
        hoi_list.append("Pending")
df["Exp_HOI1"] = hoi_list

income_list = []
for i in range(len(df)):
    if pd.isnull(df["Exp_Income1"][i]) == False:
        if (-33984 <= df["Exp_Income1"][i] < -32326):
            income_list.append("Expired")
        elif (-32326 <= df["Exp_Income1"][i] < -30668):
            income_list.append("Expiring Soon")
        elif (-30668 <= df["Exp_Income1"][i]):
            income_list.append("Not Expired")
    else:
        income_list.append("Pending")
df["Exp_Income1"] = income_list

payoff_list = []
for i in range(len(df)):
    if pd.isnull(df["Exp_Payoff1"][i]) == False:
        if (-1868 <= df["Exp_Payoff1"][i] < -1509):
            payoff_list.append("Expired")
        elif (-1509 <= df["Exp_Payoff1"][i] < -1150):
            payoff_list.append("Expiring Soon")
        elif (-1150 <= df["Exp_Payoff1"][i]):
            payoff_list.append("Not Expired")
    else:
        payoff_list.append("Pending")
df["Exp_Payoff1"] = payoff_list

# Deleting the unwanted columns    
df.drop(["Age of Loan (Days)", "Est Closing Date", "Subject Property State", "Company - Users Organization Code", "Broker Lender State", "Subject Property Type", "VA Loan Summ Credit Score", "Loan Program", "Milestone Date - Cond. Approval", "Processing Suspended Date", "Document Date Ordered - Appraisal", "Document Date Received - Appraisal", "Lock Date", "Lock Expiration Date", "Document Date Ordered - Credit Report", "Credit Expiration date", "RateLock", "Milestone Date - Process Open", "Fannie Mae Loan Doc Type Code", "Payoff Alert Received Date", "Funds Sent Date", "TIL Intl Disclosure Provided Date", "Document Date Received - Homeowner's Insurance Declarations Page", "Document Date Received - Title Report", "Income documentation expiration date", "Verification Date Stamp", "HOI Expiration Date", "Exp_income1", "Payoff Alert Date", "Exp_payoff1", "HOI Expiration Date 2", "Credit Expiration Date 2", "Exp_credite1", "Exp_Title 2", "title Expiration Date 2", "Last Finished Milestone Count1", "Final VVOE Expiration Date", "Title Expiration Date", "RandBW"], axis = 1, inplace = True)

# Top 5 frequently occuring names in respective columns
loan_officer_list = ['Omar Ali  Kaddah', 'Dib Ali Kaddah', 'Brian Andrew Alcaraz', 'Amy Marie Moeller', 'Nicholas George Apostolakis']
loan_processor_list = ['Douglass Wayne Stout', 'Samantha Miller', 'Frank Anthony Cimperman Jr', 'Kimberly Marie Whitlock', 'Mallory Royster']
loan_closer_list = ['Brooke Dudas', 'Mark Sellman', 'Suzanne Holmes', 'Susan Kondratick', 'Tameia Cooper']
loan_source_list = ['Encompass - New File', 'Encompass - Loan Duplication', 'Blend']
loan_type_list = ['Conventional', 'FHA', 'VA']
last_finished_milestone = ['Started', 'Reconciled', 'Application']

# Updating columns with given list
df["Loan Officer"] = np.random.choice(loan_officer_list, len(df))
df["Loan Processor"] = np.random.choice(loan_processor_list, len(df))
df["Loan Closer"] = np.random.choice(loan_closer_list, len(df))
df["Loan Source"] = np.random.choice(loan_source_list, len(df))
df["Loan Type"] = np.random.choice(loan_type_list, len(df))
df["Last Finished Milestone"] = np.random.choice(last_finished_milestone, len(df))

# Saving file
df.to_pickle("Loan Pipeline.pkl")
df.to_csv("Loan Pipeline.csv", index = False)