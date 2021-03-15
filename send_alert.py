import sys
import os

os.system("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"%s\"}' https://hooks.slack.com/services/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"%(sys.argv[1]))