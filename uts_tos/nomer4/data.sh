#!/bin/bash
curl -s http://bankmandiri.co.id | grep 'date' | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g'

curl -s http://bankmandiri.co.id | grep "right" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sort
