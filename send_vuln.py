import sys
import os

os.system("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"%s\"}' https://hooks.slack.com/services/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"%(sys.argv[1]))