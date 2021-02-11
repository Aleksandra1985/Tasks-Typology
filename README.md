# Tasks-Typology

Under tasks typology, we understand the actual task activity, i.e., what is needed to be done. Here we differentiate between tasks types and subtypes. 

This repository contains the following files: tasks typology vocabulary (types and subtypes), python files for identifying tasks types and tasks subtypes (as an input for python files serve tasks textual desciptions and tasks typology vocabulary), excel file with the motivating example and illustrative tasks typology vocabulary. 

Below, we describe the main stages of Step 4. Typology Aspect Extraction

# Step 4.1. Typology Aspect Extraction (Tasks Type)

Python code:
# STAGE 1. Tasks corpus reading
# STAGE 2. Find the words in the task text that match the tasks typology vocabulary keywords (types)
# STAGE 3. Defining task type for each task
# STAGE 4. Writing the results in the *.csv file

Excel *.csv file computing:
# STAGE 5. Calculation of the relative occurrence of tasks typology vocabulary keywords (types)
# STAGE 6. Task type identification

# Step 4.2. Typology Aspect Extraction (Tasks Subtype)

Python code:
# STAGE 1. Tasks typology vocabulary reading and stemming
# STAGE 2. Tasks type corpus reading, special preprocessing and English language filtering
# STAGE 3. Find and count the number of words in the task text that match the tasks typology vocabulary keywords (subtypes) 
# STAGE 4. Writing of the matched words and their number in the *.csv file

Excel *.csv file computing:
# STAGE 6. Calculation of the relative occurrence of tasks typology vocabulary keywords (subtypes)
# STAGE 7. Task subtype identification
