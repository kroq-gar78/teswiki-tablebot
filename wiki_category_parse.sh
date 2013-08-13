#!/bin/sh

# parse the contents of a category from a manual copy-paste action
# this seems to work now!

file=$1

#head $file | # get the first few lines, only for testing
cat $file |
sed -r '/^[[:alpha:]](\ cont\.)?$/d' | # remove start of each letter (need to figure out how to remove "cont.")
sed -r 's/^\ +//g' | # strip the extra whitespace at the beginning of each line
sed -r '/^(\t)?$/d' # remove blank lines

