# create .csv
python3 generate_dirty_data.py

# remove comment lines, empty lines, replace double commas with single commas, extract important columns, output to csv
grep -v '^# ' ms_data_dirty.csv | grep -v '^$' | sed 's/,,/,/g' | cut -d ',' -f1,2,4,5,6 > ms_data.csv

# make insurance list
echo 'insurance_type
Basic
Premium
Platinum' > insurance.lst

# summary in terminal
wc -l ms_data.csv
head -n 8 ms_data.csv