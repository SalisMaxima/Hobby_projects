#!/usr/bin/env bash

if ! test -f /app/include/header.txt
then
  >&2 echo "ERROR: /app/include/header.txt is missing!"
  exit 1
fi
cat /app/include/header.txt
if ! test -f /app/include/date.txt
then
  if ! &>/dev/null which curl
  then
    >&2 echo "ERROR: curl not installed. Please install it!"
    exit 1
  fi
  >&2 echo "INFO: Fetching date from the Internet. Hang on!"
  date_str=$(curl -i -sS google.com | grep -E '^Date:' | sed 's/^Date: //')
  date=$(date -d "$date_str")
else
  date=$(cat /app/include/date.txt)
fi
printf "\n\n🕰️  The date is: %s\n\n" "$date"
printf "⚙️  Here's what's running in your container:\n\n"
ps -ef
test "$#" -gt 0 && printf "\n\nWe also got some arguments: %s\n\n" "$@"
printf "\n\n⚙️  %s arguments were provided to this application.\n\n" "$#"
