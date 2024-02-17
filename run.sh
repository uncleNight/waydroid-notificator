#!/bin/bash
/usr/bin/gunicorn --chdir /opt/waydroid-notificator -w 4 'app:app' -b $(ip -4 -brief addr show dev waydroid0|awk '{print $3}'|sed -E 's%/.+%%g')
