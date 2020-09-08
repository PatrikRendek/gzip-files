# gzip-files
<h1> Compress logs</h1>

<p>This project helps to compress files (logs) with gzip python library.</p>

<h3> Usage </h3>
<p>To run compress_files.py /var/log/ as cron job running every 30 days add this line to your crontab. </p>
<code>00 00 * * *  test $(( $(date +\%s)/24/60/60\%30 )) = 26 && 	&lt; PATH TO compress_files.py &gt; /var/log/  </code>

<p>Or install python-crontab and run add_cron_job.py</p>
<code>pip3 install python-crontab</code>
<code>add_cron_job.py compress_files.py /var/log</code>
