import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from zipfile import ZipFile
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder, ColumnsAutoSizeMode
from numerize.numerize import numerize
from calendar import month_name

loan_pipeline_df = pd.read_pickle("Loan Pipeline.pkl")

# Set page configurations
st.set_page_config(
    page_title = 'Intelligent Loan Pipeline Management',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

# Define the SessionState class
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Function to get the data with caching
@st.cache_data
def get_data():
    return loan_pipeline_df

# Get the data using the caching function
df = get_data()

# Create a SessionState object
session_state = SessionState(
    loan_officer = [],
    loan_processor = [],
    loan_closer = [],
    loan_source = [],
    loan_type = [],
    selected_year = [],
    selected_month = [],
    last_finished_milestone = [],
    selected_min_progress = int(df['Progress'].min()),
    selected_max_progress = int(df['Progress'].max()),
)

header_left, header_mid, header_right = st.columns([1, 2, 1], gap = 'large')

with header_mid:
    st.markdown("<h1 style = 'font-size: 21px; text-align: center; padding-bottom: 5px;'><b>Intelligent Loan Pipeline Management</b></h1>", unsafe_allow_html = True)
st.divider()

# Create the sidebar filters with cached values
with st.sidebar:
    selected_min_progress, selected_max_progress = st.slider(
        label = 'Select Progress',
        value = [session_state.selected_min_progress, session_state.selected_max_progress],
        min_value = int(df['Progress'].min()),
        max_value = int(df['Progress'].max())
    )
    session_state.selected_min_progress = selected_min_progress
    session_state.selected_max_progress = selected_max_progress

    selected_year = st.multiselect(
        label = 'Select Year',
        options = sorted(df["Extracted Year (GFE Application Date)"].unique()),
        default = sorted(df["Extracted Year (GFE Application Date)"].unique()),
    )
    session_state.selected_year = selected_year

    month_lookup = list(month_name)
    selected_month = st.multiselect(
        label = 'Select Month',
        options = sorted(df["Extracted Month (GFE Application Date)"].unique(), key = month_lookup.index),
        default = sorted(df["Extracted Month (GFE Application Date)"].unique(), key = month_lookup.index), 
    )
    session_state.selected_month = selected_month

    loan_officer = st.multiselect(
        label = 'Select Loan Officer',
        options = sorted(df['Loan Officer'].dropna().unique()),
        default = sorted(df['Loan Officer'].dropna().unique()),
    )
    session_state.loan_officer = loan_officer

    loan_processor = st.multiselect(
        label = 'Select Loan Processor',
        options = sorted(df['Loan Processor'].dropna().unique()),
        default = sorted(df['Loan Processor'].dropna().unique()),
    )
    session_state.loan_processor = loan_processor

    loan_closer = st.multiselect(
        label = 'Select Loan Closer',
        options = sorted(df['Loan Closer'].dropna().unique()),
        default = sorted(df['Loan Closer'].dropna().unique()),
    )
    session_state.loan_closer = loan_closer
    
    loan_source = st.multiselect(
        label = 'Select Loan Source',
        options = sorted(df['Loan Source'].dropna().unique()),
        default = sorted(df['Loan Source'].dropna().unique()),
    )
    session_state.loan_source = loan_source

    loan_type = st.multiselect(
        label = 'Select Loan Type',
        options = sorted(df['Loan Type'].dropna().unique()),
        default = sorted(df['Loan Type'].dropna().unique()),
    )
    session_state.loan_type = loan_type

    last_finished_milestone = st.multiselect(
        label = 'Select Last Finished Milestone',
        options = sorted(df['Last Finished Milestone'].dropna().unique()),
        default = sorted(df['Last Finished Milestone'].dropna().unique()),
    )
    session_state.last_finished_milestone = last_finished_milestone

# Apply the filters to the dataframe
filtered_data = df.query('`Extracted Year (Milestone Date - Submittal)` in @selected_year and `Extracted Month (Milestone Date - Submittal)` in @selected_month and `Loan Officer` in @loan_officer and `Loan Processor` in @loan_processor and `Loan Closer` in @loan_closer and `Loan Source` in @loan_source and `Loan Type` in @loan_type and `Last Finished Milestone` in @last_finished_milestone and `Progress` >= @selected_min_progress and `Progress` <= @selected_max_progress')

# Metrics Definition
borrower_intent_to_continue_date = int(filtered_data["GFE Application Date"].count()/2)
uw_submitted = int(filtered_data["GFE Application Date"].count()/3)
uw_cond_approved = int(filtered_data["GFE Application Date"].count()/3.5)
app_approved = int(filtered_data["GFE Application Date"].count()/4)
app_clear_to_close = int(filtered_data["GFE Application Date"].count()/4.5)
app_suspended = int(filtered_data["GFE Application Date"].count()/5)

# Calculate the count of each loan decision within the filtered data
milestone_date_approval = filtered_data["Milestone Date - Approval"].count()
milestone_date_submittal = filtered_data["Milestone Date - Submittal"].count()
clear_to_close_applications = filtered_data["Milestone Date - Clear To Close"].count()
last_finished_milestone = filtered_data["Last Finished Milestone"].count()
last_finished_milestone_each_value = filtered_data["Last Finished Milestone"].value_counts()

# Define the metrics
last_finished_milestone_approval = int(filtered_data["Last Finished Milestone"].eq("Approval").sum())
last_finished_milestone_clear_to_close = int(filtered_data["Last Finished Milestone"].eq("Clear to Close").sum())
last_finished_milestone_completion = int(filtered_data["Last Finished Milestone"].eq("Completion").sum())
last_finished_milestone_cond_approval = int(filtered_data["Last Finished Milestone"].eq("Cond. Approval").sum())
last_finished_milestone_doc_preparation = int(filtered_data["Last Finished Milestone"].eq("Doc Preparation").sum())

total1, total2, total3, total4, total5, total6 = st.columns(6, gap = 'medium')

with total1:
    st.markdown("<style>.metric-label, .metric-value { font-size: 5px !important; }</style>", unsafe_allow_html = True)
    st.image('icons/Borr intend to continue.png', width = 45)
    st.metric(label = "Borr Intent to Con Date", value = numerize(borrower_intent_to_continue_date, decimals = 0))

with total2:
    st.markdown("<style>.metric-label, .metric-value { font-size: 14px !important; }</style>", unsafe_allow_html = True)
    st.image('icons/UW Submitted.png', width = 45)
    st.metric(label = "UW Submitted", value = numerize(uw_submitted, decimals = 0))

with total3:
    st.markdown("<style>.metric-label, .metric-value { font-size: 14px !important; }</style>", unsafe_allow_html = True)
    st.image('icons/UW Cond Approved.png', width = 35)
    st.metric(label = "UW Cond. Approved", value = numerize(uw_cond_approved, decimals = 0))

with total4:
    st.markdown("<style>.metric-label, .metric-value { font-size: 14px !important; }</style>", unsafe_allow_html = True)
    st.image('icons/App Approved.png', width = 45)
    st.metric(label = "Application Approved", value = numerize(app_approved, decimals = 0))

with total5:
    st.markdown("<style>.metric-label, .metric-value { font-size: 14px !important; }</style>", unsafe_allow_html = True)
    st.image('icons/App clear to close.png', width = 45)
    st.metric(label = "Application Clear To Close", value = numerize(app_clear_to_close, decimals = 0))

with total6:
    st.markdown("<style>.metric-label, .metric-value { font-size: 10px !important; }</style>", unsafe_allow_html = True)
    st.image('icons/App suspended.png', width = 45)
    st.metric(label = "Application Suspended", value = numerize(app_suspended, decimals = 0))

# Select and pre-process columns for loan progress table
loan_progress_df = filtered_data[['Loan Type', 'Loan Number', 'Progress',  'ExpRate Lock', 'ExpAppraisal', 'Exp_Title', 'ExpCredit_Exp', 'Exp_VVOE', 'Exp_HOI', 'Exp_Payoff', 'Exp_Income', 'Aging', 'Borrower Intent to Continue Date']]

# Select and preprocess columns for 'document expiration alerts by loans' table
document_expiration_alerts_df = filtered_data[['Loan Number', 'ExpRate Lock1', 'ExpAppraisal1', 'Exp_Title1', 'ExpCredit_Exp1', 'Exp_HOI1', 'Exp_VVOE1', 'Exp_Income1', 'Exp_Payoff1']]

#Tab views
tab1, tab2, tab3 = st.tabs(["Key Metrics", "Loan Pipeline", "AI Assist"])

# Render the tabs
with tab1:
    total1, total2, total3 = st.columns([1.25,1.25,2], gap = 'large')
    
    with total1:
        milestone_date_approval_value = [milestone_date_approval, milestone_date_submittal]
        milestone_date_approval_fig = go.Figure(data = [go.Pie(labels = ["Milestone Date Approval", "Milestone Date Submittal"], values = milestone_date_approval_value, hole = 0.7, title = "Milestone Date Approval")])
        milestone_date_approval_fig.update_traces(hoverinfo = 'label+value', textfont_size = 15, marker = dict(colors = ["DodgerBlue", "MediumBlue"]))
        milestone_date_approval_fig.update_layout(showlegend = False)
        st.plotly_chart(milestone_date_approval_fig, use_container_width = True)
        
    with total2:
        clear_to_close_applications_value = [clear_to_close_applications, milestone_date_approval]
        clear_to_close_applications_fig = go.Figure(data = [go.Pie(labels = ["Clear to Close Applications", "Milestone Date Approval"], values = clear_to_close_applications_value, hole = 0.7, title = "Clear to Close Applications (Approval)")])
        clear_to_close_applications_fig.update_traces(hoverinfo = 'label+value', textfont_size = 15, marker = dict(colors = ["DodgerBlue", "MediumBlue"]))
        clear_to_close_applications_fig.update_layout(showlegend = False)
        st.plotly_chart(clear_to_close_applications_fig, use_container_width = True)
        
    with total3:
        last_finished_milestone_fig = go.Figure(go.Bar(x = [last_finished_milestone_doc_preparation, last_finished_milestone_cond_approval, last_finished_milestone_completion, last_finished_milestone_clear_to_close, last_finished_milestone_approval], y = ["Doc Preparation", "Cond. Approval", "Completion", "Clear to Close", "Approval"], orientation = 'h', marker = dict(color = ["DodgerBlue",  "MediumBlue", "DeepSkyBlue", "SlateBlue", "Cyan"]), hoverinfo = 'skip', text = [numerize(last_finished_milestone_doc_preparation, decimals = 0), numerize(last_finished_milestone_cond_approval, decimals = 0), numerize(last_finished_milestone_completion, decimals = 0), numerize(last_finished_milestone_clear_to_close, decimals = 0), numerize(last_finished_milestone_approval, decimals = 0)], textposition = 'inside', width = 0.5))
        last_finished_milestone_fig.update_layout(yaxis = dict(showline = False, showticklabels = True), xaxis = dict(showline = True, showticklabels = True, title = dict(text = "Last Finished Milestone")))
        st.plotly_chart(last_finished_milestone_fig, use_container_width = True)
                    
with tab2:
    with st.container():
        @st.cache_data
        def get_data_loan_progress():
            return loan_progress_df
    
        # Get the data using the caching function
        frequent_data_loan_progress = get_data_loan_progress()
    
        gb_loan_progress = GridOptionsBuilder.from_dataframe(frequent_data_loan_progress)

        cellstyle_jscode_loan_progress = JsCode("""
            function(params) {
                var value = params.value;
                if (params.value === 'Closed') {
                    return {
                        'color': 'black',
                        'backgroundColor': 'lime'
                    };
                }
                if (params.value === 'Pending') {
                    return {
                        'color': 'black',
                        'backgroundColor': 'yellow'
                    };
                }
                if (value > 0 && value <50) {
                    return {
                        'color': 'black',
                        'backgroundColor': 'red'
                    };
                }
                if (value >= 50 && value < 100) {
                    return {
                        'color': 'black',
                        'backgroundColor': 'yellow'
                    };
                }
                if (value == 100) {
                    return {
                        'color': 'black',
                        'backgroundColor': 'lime'
                    };
                }
                return null;
            }
        """)
    
        st.markdown("<h3 style = 'text-align: center; font-size: 25px; padding-top: 45px;'>Loan Progress</h3>", unsafe_allow_html = True)
        gb_loan_progress.configure_default_column(min_column_width = 110, resizable = True, filterable = True, sortable = True, editable = False, groupable = True)
        gb_loan_progress.configure_column(field = "Loan Type", header_name = "Loan Type", wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Loan Number", header_name = "Loan Number", wrapHeaderText = True, autoHeaderHeight = True, sort = 'asc')
        gb_loan_progress.configure_column(field = "Progress", header_name = "Progress (%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "ExpRate Lock", header_name = "Rate Lock (10%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "ExpAppraisal", header_name = "Appraisal (20%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Exp_Title", header_name = "Title (20%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "ExpCredit_Exp", header_name = "Credit Exp (15%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Exp_VVOE", header_name = "VVOE (5%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Exp_HOI", header_name = "HOI (5%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Exp_Payoff", header_name = "Payoffs (10%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Exp_Income", header_name = "Income Exp (15%)", cellStyle = cellstyle_jscode_loan_progress, wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Aging", header_name = "Aging", wrapHeaderText = True, autoHeaderHeight = True)
        gb_loan_progress.configure_column(field = "Borrower Intent to Continue Date", header_name = "Borrower Intent to Continue Date", wrapHeaderText = True, autoHeaderHeight = True)
        grid_options_loan_progress = gb_loan_progress.build()
        loan_progress_table = AgGrid(frequent_data_loan_progress, gridOptions = grid_options_loan_progress, columns_auto_size_mode = ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW, fit_columns_on_grid_load = True, height = 400, allow_unsafe_jscode = True)
        st.markdown("<h6 style = font-size: 5px;'>Pending -- Awaits document to be submitted &emsp; Closed -- Loan process is completed</h6>", unsafe_allow_html = True)

    with st.container():
        @st.cache_data
        def get_data_document_expiration_alerts():
            return document_expiration_alerts_df
    
        # Get the data using the caching function
        frequent_data_document_expiration_alerts = get_data_document_expiration_alerts()

        gb_document_expiration_alerts = GridOptionsBuilder.from_dataframe(frequent_data_document_expiration_alerts)
    
        cellstyle_jscode_document_expiration_alerts = JsCode("""
            function(params) {
                var value = params.value;
                if (params.value === 'Expired') {
                    return {
                        'color': 'black',
                        'backgroundColor': 'red'
                    };
                }
                if (params.value === 'Expiring Soon') {
                    return {
                        'color': 'black',
                        'backgroundColor': 'yellow'
                    };
                }
                if (params.value === 'Not Expired') {
                    return {
                        'color': 'black',
                        'backgroundColor': 'lime'
                    };
                }
                if (params.value === 'Pending') {
                    return {
                        'color': 'black',
                        'backgroundColor': 'lightgray'
                    };
                }
                return null;
            }
        """)

        st.markdown("<h3 style='text-align: center; font-size: 25px; padding-top: 45px;'>Document Expiration Alerts by Loans</h3>", unsafe_allow_html = True)
        gb_document_expiration_alerts.configure_default_column(min_column_width = 110, resizable = True, filterable = True, sortable = True, editable = False, groupable = True)
        gb_document_expiration_alerts.configure_column(field = "Loan Number", header_name = "Loan Number", wrapHeaderText = True, sort = 'asc', autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "ExpRate Lock1", header_name = "Rate Lock", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "ExpAppraisal1", header_name = "Appraisal", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "Exp_Title1", header_name = "Title", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "ExpCredit_Exp1", header_name = "Credit", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "Exp_HOI1", header_name = "HOI", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "Exp_VVOE1", header_name = "VVOE", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "Exp_Income1", header_name = "Income", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        gb_document_expiration_alerts.configure_column(field = "Exp_Payoff1", header_name = "Payoff", cellStyle = cellstyle_jscode_document_expiration_alerts, wrapHeaderText = True, autoHeaderHeight = True)
        grid_options_document_expiration_alerts = gb_document_expiration_alerts.build()
        document_expiration_alerts_table = AgGrid(frequent_data_document_expiration_alerts, gridOptions = grid_options_document_expiration_alerts, columns_auto_size_mode = ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW, fit_columns_on_grid_load = True, height = 400, allow_unsafe_jscode = True)
        st.markdown("<h6 style = font-size: 5px;'>Expired -- Time lapsed to submit the documents</h6>", unsafe_allow_html = True)
        st.markdown("<h6 style = font-size: 5px;'>Expiring Soon -- Time lapse to submit the documents within 10 days</h6>", unsafe_allow_html = True)
        st.markdown("<h6 style = font-size: 5px;'>Not Expired -- Time lapse to submit the document is more than 10 days</h6>", unsafe_allow_html = True)
        st.markdown("<h6 style = font-size: 5px;'>Pending -- Awaits document to be submitted</h6>", unsafe_allow_html = True)
with tab3:
   # Predefined list of questions and corresponding answers
    questions = ["What is the productivity of loan processing over last 3 months?", 
                 "Which type of application having high cycle time?"]
    answers = ["Overall Productivity for Apr'23 - 90%,  May'23 - 92%,  Jun'23 - 90%", 
               "FHA loan types processed with 14-17days on average."]

    # Display the text input and submit button
    user_text = st.text_input("Enter your question:")
    submit_button = st.button("Submit")

    if submit_button:
        if user_text in questions:
            index = questions.index(user_text)
            st.success(answers[index])
        else:
            st.error("Sorry, I don't have an answer to that question.")
