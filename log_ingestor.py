#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output
import json

# Define an empty DataFrame to store log data
log_data = pd.DataFrame()

# Function to handle file upload and log data processing
def on_file_upload(change):
    uploaded_files = change['new']
    if uploaded_files:
        try:
            global log_data
            log_data = pd.DataFrame()

            for file_name, file_info in uploaded_files.items():
                content = file_info['content']
                temp_df = pd.read_json(content)
                log_data = log_data.append(temp_df, ignore_index=True)

            # Displaying the uploaded log data
            with output_logs:
                output_logs.clear_output()
                display(log_data)
        except ValueError as e:
            with output_logs:
                output_logs.clear_output()
                print(f"ValueError: {e}")
    else:
        with output_logs:
            output_logs.clear_output()
            print("No files uploaded.")

# Create an instance of FileUpload widget
file_upload = widgets.FileUpload(accept='.json', multiple=True)
file_upload.observe(on_file_upload, names='value')


# Create UI components for log filters
level_dropdown = widgets.Dropdown(options=['', 'error', 'info', 'warning'], description='level:')
message_text = widgets.Text(description='message:')
resource_id_text = widgets.Text(description='resourceId:')
timestamp_text = widgets.Text(description='timestamp (YYYY-MM-DD/YYYY-MM-DD):')
trace_id_text = widgets.Text(description='traceId:')
span_id_text = widgets.Text(description='spanId:')
commit_text = widgets.Text(description='commit:')
parent_resource_id_text = widgets.Text(description='parentResourceId:')

# Function to filter and display logs based on provided filters
def filter_and_display_logs(b):
    global log_data
    if log_data.empty:
        print("No log data available. Please upload log data first.")
        return
    
    with output_logs:
        output_logs.clear_output()
        
        filter_values = {
            'level': level_dropdown.value,  # Change the key to lowercase
            'message': message_text.value,
            'resourceId': resource_id_text.value,
            'timestamp': timestamp_text.value,
            'traceId': trace_id_text.value,
            'spanId': span_id_text.value,
            'commit': commit_text.value,
            'parentResourceId': parent_resource_id_text.value
        }
        
        filtered_data = log_data.copy()  # Create a copy to preserve original data
        
        for key, value in filter_values.items():
            if value:
                # Convert both column and value to lowercase for case-insensitive search
                filtered_data = filtered_data[filtered_data[key].astype(str).str.lower().str.contains(value.lower())]
        
        if filtered_data.empty:
            print("No data to display based on the applied filters.")
        else:
            display(filtered_data)


# Create a button to trigger data filtering
filter_button = widgets.Button(description="Filter Data")
filter_button.on_click(filter_and_display_logs)

# Create an output widget to display filtered logs
output_logs = widgets.Output()

# Display widgets in a structured layout
upload_area = widgets.VBox([widgets.Label('Upload Log Files'), file_upload])
filters_area = widgets.VBox([widgets.Label('Filter Logs'), level_dropdown, message_text, resource_id_text,
                             timestamp_text, trace_id_text, span_id_text, commit_text, parent_resource_id_text,
                             filter_button])
display(widgets.HBox([upload_area, filters_area]))
display(output_logs)

# Function to save changes to a CSV file
def save_changes(b):
    global log_data
    if log_data.empty:
        print("No log data available to save.")
        return
    
    log_data.to_csv('filtered_log_data.csv', index=False)
    print("Filtered log data saved successfully.")
    
# Create a button for saving changes
save_button = widgets.Button(description="Save Changes")
save_button.on_click(save_changes)

# Display widgets for file upload, filtering, and saving changes
display(file_upload, save_button)


# In[ ]:




