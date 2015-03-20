# Downloads job metrics and configuration from the Job Tracker.
# Usage: $ download_job_info.sh JOB_ID JOB_TRACKER

JOB_ID=$1
JOB_TRACKER=$2
RESULTS_DIR=results

wget -O "${RESULTS_DIR}/metrics_${JOB_ID}.html" "${JOB_TRACKER}/jobdetails.jsp?jobid=${JOB_ID}"
wget -O "${RESULTS_DIR}/conf_${JOB_ID}.html" "${JOB_TRACKER}/jobconf.jsp?jobid=${JOB_ID}"
wget -O "${RESULTS_DIR}/map_tasks_${JOB_ID}.html" "${JOB_TRACKER}/jobtasks.jsp?jobid=${JOB_ID}&type=map&pagenum=1"
wget -O "${RESULTS_DIR}/reduce_tasks_${JOB_ID}.html" "${JOB_TRACKER}/jobtasks.jsp?jobid=${JOB_ID}&type=reduce&pagenum=1"
