"""
Parses a HTML page with job results from a job tracker into a TSV file
with can be easily processed further.

The reason is that I haven't found any other API to get this information.

Usage: python parse_job_report.py metrics_job_1234.html
Produces: metrics_job_1234.tsv

Example output (excerpt):

	Map	Reduce	Total
FILE: Number of bytes read	1000	10000	11000
FILE: Number of bytes written	2000	20000	22000
[...]
CPU time spent (ms)	100	1000	1100
[...]
Wall time (ms)	0	0	3000
"""

from bs4 import BeautifulSoup
import os.path
import pandas as pd
import re
import sys

def job_report_to_tsv(input_file, output_file):
    soup = BeautifulSoup(open(input_file))
    
    rows = soup.find_all('table')[3].find_all('tr')
    column_names = split_row(rows[0])
    data_rows = [split_row(row) for row in rows[1:]]
    index = [row[0] for row in data_rows]
    data = [[to_number(n) for n in row[1:]] for row in data_rows]
    
    df = pd.DataFrame(data, index=index, columns=column_names[1:])
    
    df.loc['Wall time (ms)'] = (0, 0, 1000 * get_wall_time(soup))
    
    df.to_csv(output_file, sep='\t')

def split_row(row):
    return [td.string for td in row.find_all(re.compile('t[dh]'))[-4:]]

def to_number(n):
    return n.replace(',', '')

def parse_duration_to_seconds(duration):
    '''1hrs, 16mins, 23sec -> (((1 * 60) + 16) * 60) + 23 = 4583 seconds'''
    parts = [p.strip() for p in duration.split(',')]
    units = {'hrs': 3600, 'mins': 60, 'sec': 1}
    regex = re.compile('([0-9]+)([a-z]+)')
    value_unit_parts = (regex.match(p).groups() for p in parts)
    return sum(int(value) * units[unit] for (value, unit) in value_unit_parts)

def get_wall_time(soup):
    '''Extracts wall time of job duration (in seconds)'''
    # find: <b>Finished in:</b> '7mins, 19sec'
    # eg. '7mins, 19sec'
    duration = str(soup.find('b', text='Finished in:').next_sibling.string).strip()
    return parse_duration_to_seconds(duration)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = "%s.tsv" % os.path.splitext(input_file)[0]
    job_report_to_tsv(input_file, output_file)
