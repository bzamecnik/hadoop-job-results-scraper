# Hadoop job results scraper

Scrapes the job results from a Hadoop Job Tracker web pages.

- `download_job_info.sh` - Downloads job metrics and configuration from the
Job Tracker.
- `parse_job_report.py` - Parses a HTML page with job results from a job tracker
into a TSV file with can be easily processed further.

The reason is that I haven't found any other API to get this information.

Requirements: Python (+ beautiful soup, pandas), wget

Author: Bohumír Zámečník ([@bzamecnik](https://twitter.com/bzamecnik))
License: MIT
