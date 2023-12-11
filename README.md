# Log Ingestor & Query Interface system
This system is designed to ingest log data from JSON files and provide an interface to filter, query, and save the log data.

## Overview
The system consists of an interactive interface built using Python and Jupyter Notebook. It leverages Pandas, IPyWidgets, and IPython's display features to facilitate log data ingestion, filtering, and saving operations.

## Features
### File Upload: Allows users to upload multiple JSON log files.
### Log Data Display: Displays the uploaded log data in a tabular format for preview.
### Filtering Logs: Provides filters based on log attributes such as level, message, resourceId, timestamp, traceId, spanId, commit, and parentResourceId.
### Filtered Data Display: Displays filtered log data based on specified filter criteria.
### Saving Changes: Enables the user to save the filtered log data to a CSV file named 'filtered_log_data.csv'.

## Language and software used:
![image](https://github.com/dyte-submissions/november-2023-hiring-nishutiwari7/assets/67005380/7645ce26-c29d-482c-9ba0-9ed66d1c59f7)
![image](https://github.com/dyte-submissions/november-2023-hiring-nishutiwari7/assets/67005380/85025882-9a8b-46b0-8e9f-9a1d275deb45)
![image](https://github.com/dyte-submissions/november-2023-hiring-nishutiwari7/assets/67005380/52d098d0-1037-49b6-ade5-be463206c38c)


## Getting Started
To use this tool, follow the steps below:

## Prerequisites
Jupyter Notebook: Ensure you have Jupyter Notebook installed to run this code. You can install it via Anaconda or through pip.
Installation
Clone the repository:


git clone https://github.com/your-username/log-data-filter.git
Open the Jupyter Notebook or JupyterLab environment:

[jupyter notebook](https://jupyter.org/)
Upload the provided python file (log_ingestor.ipy) to your Jupyter environment.
Run the code.

## Code Structure
The system is primarily based on Python, utilizing Pandas, IPyWidgets, and IPython display features to create an interactive log ingestor and query interface.

File: log_ingestor.ipy
Functions:
on_file_upload: Handles file upload and log data processing.
filter_and_display_logs: Filters and displays log data based on provided filters.
save_changes: Saves filtered log data to a CSV file.
## Code Execution:

### Upload Log Files:
Click on the "Upload Log Files" button and select one or multiple JSON log files to upload.
![Capture](https://github.com/dyte-submissions/november-2023-hiring-nishutiwari7/assets/67005380/45b4260b-1687-40e6-98f3-d9fc237b1037)


### Filter Log Data:
![Capture2](https://github.com/dyte-submissions/november-2023-hiring-nishutiwari7/assets/67005380/5f5c697f-1320-4c07-979b-4302285149ca)


Use the dropdowns and text input fields to specify filtering criteria based on 'level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', and 'metadata'.
Click the "Filter Data" button to display filtered log data.
### Save Filtered Data:

After applying filters, click the "Save Data" button to save the filtered data to a CSV file named filtered_data.csv.
## Notes
Ensure that log files uploaded are in valid JSON format for accurate processing.
The filtering functionality allows for partial matching within columns.
For timestamp filtering, provide the timestamp in the format 'YYYY-MM-DD'.
## License
This project is licensed under the MIT License - see the LICENSE.txt file for details.

## Acknowledgments
I acknowledge the invaluable contributions of the Python programming language, Jupyter Notebook environment, and GitHub Classroom in facilitating the development, implementation, and sharing of this codebase. These tools have significantly contributed to the creation and collaboration within this project."
