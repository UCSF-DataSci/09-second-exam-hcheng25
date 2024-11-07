[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16987533)
# DS-217 Final Exam: Multiple Sclerosis Analysis

## Question 1: Data Preparation with Command-Line Tools
- Created the _prepare.sh_ script
- Started by generating dirty data using _generate_dirty_data.py_
- While testing, I realized there were errors if I tried to output to the same file that was the input, so I opted to avoid multiple steps by using pipes in the clean-up steps
- Clean-up steps were to use _grep_ and _sed_ to remove comment lines, then remove empty lines, then replace double commas with a single comma
- The output of the clean-up was put into a cut step using a pipe to extract only the necessary columns, and the final output of this step was outputted to _ms_data.csv_
- A list of labels for an insurance_type variable was created using _echo_
- The terminal will display the number of entries in _ms_data.csv_ using line count through _wc_
- The terminal will also display the first 8 lines of _ms_data.csv_ using _head_