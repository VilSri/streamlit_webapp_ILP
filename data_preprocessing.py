import datetime
import pandas as pd
import numpy as np
from calendar import month_name

df = pd.read_csv('C:/Users/vipul.srivastava01/Desktop/Streamlit/Intelligent Loan Pipeline Managment DATA.csv', low_memory = False)
df1 = pd.read_csv('C:/Users/vipul.srivastava01/Desktop/Streamlit/Intelligent Loan Pipeline Managment DATA original.csv', low_memory = False)

# Extracting values from column
def extract_values(column_name):
    value_list = []
    for i in range(len(df1)):
        if column_name[i] not in value_list:
            value_list.append(column_name[i])
    return value_list

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
    column_new_values = []
    column_name_str = column_name.astype(str)
    for i in range(len(df)):
        if column_name_str[i] != "nan":
            column_new_values.append("Closed")
        else:
            column_new_values.append("Pending")
    return column_new_values

def random_sum_to_one(list_name):
    np.random.seed(24)
    random_number = np.random.rand(len(list_name))
    if sum(random_number) != 1:
        random_number = np.random.rand(len(list_name))
    else:
        return random_number

np.random.seed(30)
random_loan_number = np.random.randint(126792, 998743, 57999)
df["Loan Number"] = random_loan_number.astype(str)

extract_values_gfe_application_date = extract_values(df1["GFE Application Date"])
extract_values_borrower_intent_to_continue_date = extract_values(df1["Borrower Intent to Continue Date"])
extract_values_milestone_date_approval = extract_values(df1["Milestone Date - Approval"])
extract_values_milestone_date_submittal = extract_values(df1["Milestone Date - Submittal"])
extract_values_milestone_date_clear_to_close = extract_values(df1["Milestone Date - Clear To Close"])
extract_values_document_date_received_appraisal = extract_values(df1["Document Date Received - Appraisal"])
extract_values_document_date_received_homeowner_insurance = extract_values(df1["Document Date Received - Homeowner's Insurance Declarations Page"])
extract_values_document_data_received_title_report = extract_values(df1["Document Date Received - Title Report"])
      
np.random.seed(28)
df["GFE Application Date"] = np.random.choice(extract_values_gfe_application_date, len(df), p = random_sum_to_one(extract_values_gfe_application_date))
df["Borrower Intent to Continue Date"] = np.random.choice(extract_values_borrower_intent_to_continue_date, len(df), p = random_sum_to_one(extract_values_borrower_intent_to_continue_date))
df["Milestone Date - Approval"] = np.random.choice(extract_values_milestone_date_approval, len(df), p = random_sum_to_one(extract_values_milestone_date_approval))
df["Milestone Date - Submittal"] = np.random.choice(extract_values_milestone_date_submittal, len(df), p = random_sum_to_one(extract_values_milestone_date_submittal))
df["Milestone Date - Clear To Close"] = np.random.choice(extract_values_milestone_date_clear_to_close, len(df), p = random_sum_to_one(extract_values_milestone_date_clear_to_close))
df["Document Date Received - Appraisal"] = np.random.choice(extract_values_document_date_received_appraisal, len(df), p = random_sum_to_one(extract_values_document_date_received_appraisal))
df["Document Date Received - Homeowner's Insurance Declarations Page"] = np.random.choice(extract_values_document_date_received_homeowner_insurance, len(df), p = random_sum_to_one(extract_values_document_date_received_homeowner_insurance))
df["Document Date Received - Title Report"] = np.random.choice(extract_values_document_data_received_title_report, len(df), p = random_sum_to_one(extract_values_document_data_received_title_report))

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

# df["ExpRate Lock"] = update_column_values(df["ExpRate Lock"])
# df["ExpAppraisal"] = update_column_values(df["ExpAppraisal"])
# df["Exp_Title"] = update_column_values(df["Exp_Title"])                                                                                                                                                                                                                                                                           
# df["ExpCredit_Exp"] = update_column_values(df["ExpCredit_Exp"])
# df["Exp_VVOE"] = update_column_values(df["Exp_VVOE"])
# df["Exp_HOI"] = update_column_values(df["Exp_HOI"])
# df["Exp_Payoff"] = update_column_values(df["Exp_Payoff"])
# df["Exp_Income"] = update_column_values(df["Exp_Income"])

# Deleting the unwanted columns    
df.drop(["Age of Loan (Days)", "Est Closing Date", "Subject Property State", "Company - Users Organization Code", "Broker Lender State", "Subject Property Type", "VA Loan Summ Credit Score", "Loan Program", "Milestone Date - Cond. Approval", "Processing Suspended Date", "Document Date Ordered - Appraisal", "Lock Date", "Lock Expiration Date", "Document Date Ordered - Credit Report", "Credit Expiration date", "RateLock", "Milestone Date - Process Open", "Fannie Mae Loan Doc Type Code", "Payoff Alert Received Date", "Funds Sent Date", "TIL Intl Disclosure Provided Date", "Income documentation expiration date", "Verification Date Stamp", "HOI Expiration Date", "Exp_income1", "Payoff Alert Date", "Exp_payoff1", "HOI Expiration Date 2", "Credit Expiration Date 2", "Exp_credite1", "Exp_Title 2", "title Expiration Date 2", "Last Finished Milestone Count1", "Final VVOE Expiration Date", "Title Expiration Date", "RandBW"], axis = 1, inplace = True)

# Top 5 frequently occuring names in respective columns
loan_officer_list = ['Omar Ali  Kaddah', 'Dib Ali Kaddah', 'Brian Andrew Alcaraz', 'Amy Marie Moeller', 'Nicholas George Apostolakis']
loan_processor_list = ['Douglass Wayne Stout', 'Samantha Miller', 'Frank Anthony Cimperman Jr', 'Kimberly Marie Whitlock', 'Mallory Royster']
loan_closer_list = ['Brooke Dudas', 'Mark Sellman', 'Suzanne Holmes', 'Susan Kondratick', 'Tameia Cooper']
loan_source_list = ['Encompass - New File', 'Encompass - Loan Duplication', 'Blend', 'WebCenter', 'WebMax']
loan_type_list = ['Conventional', 'FHA', 'VA', 'FarmersHomeA', 'Other', 'HELOC']
last_finished_milestone_list = ['Approval', 'Clear to Close', 'Completion', 'Cond. Approval', 'Doc Preparation']
progress_list = [ 15, 25, 35, 45, 50, 30, 40, 20, 60, 65, 55, 75, 70, 80, 85, 90, 95]
# year_list = ['2018', '2019', '2020', '2021', '']
# month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', '']
update_column_list = ['Closed', 'Pending']
date_remaining_na_list = [0, 9, 11, -1]
date_remaining_list = [0, 9, 11]
error_type_list = ['Rate Lock Mismatch', 'Interest Rate Mismatch', 'Incorrect Customer Demographics', 'Incorrect Income Details', 'Title Errors', 'Rate Lock Expired']

# Updating columns with given list
np.random.seed(35)
df["Loan Officer"] = np.random.choice(loan_officer_list, len(df), p = [0.2, 0.3, 0.15, 0.25, 0.1])
df["Loan Processor"] = np.random.choice(loan_processor_list, len(df), p = [0.3, 0.15, 0.1, 0.25, 0.2])
df["Loan Closer"] = np.random.choice(loan_closer_list, len(df), p = [0.1, 0.25, 0.2, 0.15, 0.3])
df["Loan Source"] = np.random.choice(loan_source_list, len(df), p = [0.25, 0.2, 0.15, 0.10, 0.3])
df["Loan Type"] = np.random.choice(loan_type_list, len(df), p = [0.22, 0.17, 0.19, 0.16, 0.12, 0.14])
df["Last Finished Milestone"] = np.random.choice(last_finished_milestone_list, len(df), p = [0.25, 0.1, 0.05, 0.4, 0.2])
df["Progress"] = np.random.choice(progress_list, len(df), p = [0.03, 0.05, 0.04, 0.06, 0.05, 0.08, 0.04, 0.08, 0.09, 0.07, 0.03, 0.05, 0.07, 0.09, 0.07, 0.06, 0.04])

# df["Extracted Year (GFE Application Date)"] = np.random.choice(year_list, len(df), p = [0.3, 0.15, 0.2, 0.35])
# df["Extracted Month (GFE Application Date)"] = np.random.choice(month_list, len(df), p = [0.12, 0.04, 0.06, 0.02, 0.09, 0.14, 0.07, 0.05, 0.11, 0.12, 0.03, 0.15])
# df["Extracted Year (Borrower Intent to Continue Date)"] = np.random.choice(year_list, len(df), p = [0.35, 0.15, 0.2, 0.3])
# df["Extracted Month (Borrower Intent to Continue Date)"] = np.random.choice(month_list, len(df), p = [0.11, 0.1, 0.04, 0.14, 0.06, 0.13, 0.04, 0.09, 0.07, 0.05, 0.12, 0.05])
# df["Extracted Year (Milestone Date - Approval)"] = np.random.choice(year_list, len(df), p = [0.4, 0.15, 0.2, 0.25])
# df["Extracted Month (Milestone Date - Approval)"] = np.random.choice(month_list, len(df), p = [0.06, 0.07, 0.06, 0.05, 0.02, 0.09, 0.14, 0.11, 0.12, 0.1, 0.05, 0.13])
# df["Extracted Year (Milestone Date - Submittal)"] = np.random.choice(year_list, len(df), p = [0.3, 0.25, 0.1, 0.35])
# df["Extracted Month (Milestone Date - Submittal)"] = np.random.choice(month_list, len(df), p = [0.12, 0.04, 0.09, 0.06, 0.04, 0.14, 0.09, 0.05, 0.1, 0.11, 0.03, 0.13])
# df["Extracted Year (Milestone Date - Clear To Close)"] = np.random.choice(year_list, len(df), p = [0.15, 0.25, 0.2, 0.4])
# df["Extracted Month (Milestone Date - Clear To Close)"] = np.random.choice(month_list, len(df), p = [0.07, 0.1, 0.04, 0.09, 0.05, 0.06, 0.04, 0.14, 0.05, 0.11, 0.12, 0.13])

df["ExpRate Lock"] = np.random.choice(update_column_list, len(df), p = [0.35, 0.65])
df["ExpAppraisal"] = np.random.choice(update_column_list, len(df), p = [0.3, 0.7])
df["Exp_Title"] = np.random.choice(update_column_list, len(df), p = [0.45, 0.55])
df["ExpCredit_Exp"] = np.random.choice(update_column_list, len(df), p = [0.28, 0.72])
df["Exp_VVOE"] = np.random.choice(update_column_list, len(df), p = [0.43, 0.57])
df["Exp_HOI"] = np.random.choice(update_column_list, len(df), p = [0.4, 0.6])
df["Exp_Payoff"] = np.random.choice(update_column_list, len(df), p = [0.58, 0.42])
df["Exp_Income"] = np.random.choice(update_column_list, len(df), p = [0.32, 0.68])
df["ExpRate Lock1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.3, 0.28, 0.32, 0.1])
df["ExpAppraisal1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.2, 0.35, 0.3, 0.15])
df["Exp_Title1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.1, 0.3, 0.4, 0.2])
df["ExpCredit_Exp1"] = np.random.choice(date_remaining_list, len(df), p = [0.25, 0.4, 0.35])
df["Exp_VVOE1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.21, 0.3, 0.35, 0.14])
df["Exp_HOI1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.24, 0.32, 0.28, 0.16])
df["Exp_Payoff1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.15, 0.25, 0.41, 0.19])
df["Exp_Income1"] = np.random.choice(date_remaining_na_list, len(df), p = [0.18, 0.26, 0.39, 0.17])
df["Time Taken (minutes)"] = np.random.randint(10, 250, 57999)
df["Application Status"] = np.random.choice(['Error', 'No Error'], len(df), p = [0.2, 0.8])

df["Progress"] = df[["Progress"]].astype(int)
df["Loan Number"] = df[["Loan Number"]].astype("Int64")
df["Loan Number"] = df["Loan Number"].astype(str)
# df["Loan Officer"] = change_data_types(df["Loan Officer"])
# df["Loan Processor"] = change_data_types(df["Loan Processor"])
# df["Loan Closer"] = change_data_types(df["Loan Closer"])
# df["Loan Type"] = change_data_types(df["Loan Type"])
# df["ExpRate Lock1"] = df["ExpRate Lock1"].astype("Int64")
# df["ExpAppraisal1"] = df["ExpAppraisal1"].astype("Int64")
# df["Exp_Title1"] = df["Exp_Title1"].astype("Int64")
# df["ExpCredit_Exp1"] = df["ExpCredit_Exp1"].astype("Int64")
# df["Exp_VVOE1"] = df["Exp_VVOE1"].astype("Int64")
# df["Exp_HOI1"] = df["Exp_HOI1"].astype("Int64")
# df["Exp_Payoff1"] = df["Exp_Payoff1"].astype("Int64")
# df["Exp_Income1"] = df["Exp_Income1"].astype("Int64")

# df["Extracted Year (GFE Application Date)"] = pd.to_datetime(df["Extracted Year (GFE Application Date)"])
# df["Extracted Month (GFE Application Date)"] = pd.to_datetime(df["Extracted Month (GFE Application Date)"])
# df["Extracted Year (Borrower Intent to Continue Date)"] = pd.to_datetime(df["Extracted Year (Borrower Intent to Continue Date)"])
# df["Extracted Month (Borrower Intent to Continue Date)"] = pd.to_datetime(df["Extracted Month (Borrower Intent to Continue Date)"])
# df["Extracted Year (Milestone Date - Approval)"] = pd.to_datetime(df["Extracted Year (Milestone Date - Approval)"])
# df["Extracted Month (Milestone Date - Approval)"] = pd.to_datetime(df["Extracted Month (Milestone Date - Approval)"])
# df["Extracted Year (Milestone Date - Submittal)"] = pd.to_datetime(df["Extracted Year (Milestone Date - Submittal)"])
# df["Extracted Month (Milestone Date - Submittal)"] = pd.to_datetime(df["Extracted Month (Milestone Date - Submittal)"])
# df["Extracted Year (Milestone Date - Clear To Close)"] = pd.to_datetime(df["Extracted Year (Milestone Date - Clear To Close)"])
# df["Extracted Month (Milestone Date - Clear To Close)"] = pd.to_datetime(df["Extracted Month (Milestone Date - Clear To Close)"])

rate_lock_list = []
for i in range(len(df)):
    if ((df["ExpRate Lock1"][i]) == 0):
        rate_lock_list.append("Expired")
    elif (0 < df["ExpRate Lock1"][i] < 10):
        rate_lock_list.append("Expiring Soon")
    elif (10 <= df["ExpRate Lock1"][i]):
            rate_lock_list.append("Not Expired")
    else:
        rate_lock_list.append("Pending")
df["ExpRate Lock1"] = rate_lock_list

appraisal_list = []
for i in range(len(df)):
    if (df["ExpAppraisal1"][i] == 0):
        appraisal_list.append("Expired")
    elif (0 < df["ExpAppraisal1"][i] < 10):
        appraisal_list.append("Expiring Soon")
    elif (10 <= df["ExpAppraisal1"][i]):
        appraisal_list.append("Not Expired")
    else:
        appraisal_list.append("Pending") 
df["ExpAppraisal1"] = appraisal_list

title_list = []
for i in range(len(df)):
    if (df["Exp_Title1"][i] == 0):
        title_list.append("Expired")
    elif (0 < df["Exp_Title1"][i] < 10):
        title_list.append("Expiring Soon")
    elif (10 <= df["Exp_Title1"][i]):
        title_list.append("Not Expired")
    else:
        title_list.append("Pending")
df["Exp_Title1"] = title_list

credit_list = []
for i in range(len(df)):
    if (df["ExpCredit_Exp1"][i] == 0):
        credit_list.append("Expired")
    elif (0 < df["ExpCredit_Exp1"][i] < 10):
        credit_list.append("Expiring Soon")
    elif (10 <= df["ExpCredit_Exp1"][i]):
        credit_list.append("Not Expired")
    else:
        credit_list.append("Pending")
df["ExpCredit_Exp1"] = credit_list

vvoe_list = []
for i in range(len(df)):
    if (df["Exp_VVOE1"][i] == 0):
        vvoe_list.append("Expired")
    elif (0 < df["Exp_VVOE1"][i] < 10):
        vvoe_list.append("Expiring Soon")
    elif (10 <= df["Exp_VVOE1"][i]):
        vvoe_list.append("Not Expired")
    else:
        vvoe_list.append("Pending")
df["Exp_VVOE1"] = vvoe_list

hoi_list = []
for i in range(len(df)):
    if (df["Exp_HOI1"][i] == 0):
        hoi_list.append("Expired")
    elif (0 < df["Exp_HOI1"][i] < 10):
        hoi_list.append("Expiring Soon")
    elif (10 <= df["Exp_HOI1"][i]):
        hoi_list.append("Not Expired")
    else:
        hoi_list.append("Pending")
df["Exp_HOI1"] = hoi_list

income_list = []
for i in range(len(df)):
    if (df["Exp_Income1"][i] == 0):
        income_list.append("Expired")
    elif (0 < df["Exp_Income1"][i] < 10):
        income_list.append("Expiring Soon")
    elif (10 <= df["Exp_Income1"][i]):
        income_list.append("Not Expired")
    else:
        income_list.append("Pending")
df["Exp_Income1"] = income_list

payoff_list = []
for i in range(len(df)):
    if (df["Exp_Payoff1"][i] == 0):
        payoff_list.append("Expired")
    elif (0 < df["Exp_Payoff1"][i] < 10):
        payoff_list.append("Expiring Soon")
    elif (10 <= df["Exp_Payoff1"][i]):
        payoff_list.append("Not Expired")
    else:
        payoff_list.append("Pending")
df["Exp_Payoff1"] = payoff_list

# no_error_list = []
# for i in range(len(df)):
#     if df["Application Status"][i] == "No Error":
#         no_error_list.append("No Error")
#     else:
#         no_error_list.append("")
# df["Error Type"] = no_error_list

# average_time_list = []
# for j in loan_processor_list:
#         for k in loan_type_list:
#             select_rows_df = df[(df["Loan Processor"] == j) & (df["Loan Type"] == k)]
#             calculate_average_time_taken = int(select_rows_df["Time Taken (minutes)"].mean())
#             # select_rows_df["Average Time Taken"] = calculate_average_time_taken
#             average_time_list.append(calculate_average_time_taken)
#             # df["Average Time Taken"] = select_rows_df["Average Time Taken"]

# l = []
# for i in range(len(average_time_list)):
#     for j in loan_processor_list:
#         for k in loan_type_list:
#             # if df[(df["Loan Processor"] == j) and (df["Loan Type"] == k)].empty() == False: #and l <= len(average_time_list):
#                 select_rows_df = df[(df["Loan Processor"] == j) & (df["Loan Type"] == k)]
#                 select_rows_df["Average Time Taken"] = average_time_list[i]

#                 l.append(select_rows_df["Average Time Taken"])
# df["Average Time Taken"] = l
# print(l)
# print(len(l))
# # print(df["Average Time Taken"])
# print(average_time_list)
# print(len(average_time_list))

update_progress_column_list = [] 
for i in range(len(df)):
    if df["ExpRate Lock"][i] == "Closed" and df["ExpAppraisal"][i] == "Closed" and df["Exp_Title"][i] == "Closed" and df["ExpCredit_Exp"][i] == "Closed" and df["Exp_HOI"][i] == "Closed" and df["Exp_VVOE"][i] == "Closed" and df["Exp_Income"][i] == "Closed" and df["Exp_Payoff"][i] == "Closed":
        update_progress_column_list.append(100)
    else:
        update_progress_column_list.append(df["Progress"][i])
df["Progress"] = update_progress_column_list

generate_random_error_type_list = np.random.choice(error_type_list, df[df["Application Status"] == 'Error'].count().sum(), p = [0.14, 0.15, 0.16, 0.2, 0.18, 0.17])

update_error_type_list = []
for i in range(len(df)):
    if df["Application Status"][i] == 'Error':
        update_error_type_list.append(generate_random_error_type_list[i])
    else:
        update_error_type_list.append("No Error")
df["Error Type"] = update_error_type_list

all_documents_status_list = []
for i in range(len(df)):
    if df["ExpRate Lock"][i] == "Closed" and df["ExpAppraisal"][i] == "Closed" and df["Exp_Title"][i] == "Closed" and df["ExpCredit_Exp"][i] == "Closed" and df["Exp_HOI"][i] == "Closed" and df["Exp_VVOE"][i] == "Closed" and df["Exp_Income"][i] == "Closed" and df["Exp_Payoff"][i] == "Closed" and df["Progress"][i] == 100:
        all_documents_status_list.append("Not Expired")
    else:
        all_documents_status_list.append("Expired")
df["All Documents Expiration Status"] = all_documents_status_list

all_documents_received_list = []
for i in range(len(df)):
    if df["Document Date Received - Appraisal"][i] != "nan" and df["Document Date Received - Homeowner's Insurance Declarations Page"][i] != "nan" and df["Document Date Received - Title Report"][i] != "nan":
                all_documents_received_list.append('Yes')
    else:
        all_documents_received_list.append('No')
df["All Documents Received Status"] = all_documents_received_list

# Saving file
df.to_pickle("Loan Pipeline.pkl")
df.to_csv("Loan Pipeline.csv", index = False)