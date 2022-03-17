#!/bin/bash
cat << EOF | curl -u user:pwd --data-binary @- https://http://<pushgateway_host>:9091/metrics/job/test_job
  test_metric{account_name="A"} 1
  test_metric{account_name="B"} 1
  test_metric{account_name="C"} 1
  test_metric{account_name="D"} 1
EOF
