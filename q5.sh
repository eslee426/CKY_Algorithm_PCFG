#!/bin/bash
# q5.sh 
# implents necessary functions for q5

echo Start Time: 
date +"%r"

echo Creating tree in JSON format for parse_dev.dat using CKY Algorithm
python cky_algorithm.py cfg_rare.counts parse_dev.dat > output
echo Comparing output
python eval_parser.py parse_dev.key output

echo End Time:
date +"%r"