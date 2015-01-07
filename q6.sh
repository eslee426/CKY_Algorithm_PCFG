#!/bin/bash
# q6.sh 
# implents necessary functions for q6

echo Start Time: 
date +"%r"

echo Creating cfg_vert.counts from parse_train_vert.dat
python count_cfg_freq.py  parse_train_vert.dat > cfg_vert.counts
echo Creating parse_train_vert_rare.dat by replacing rare words
python add_rare.py cfg_vert.counts parse_train_vert.dat > parse_train_vert_rare.dat
echo creating cfg_vert_rare.counts to count rare words
python count_cfg_freq.py parse_train_vert_rare.dat > cfg_vert_rare.counts
echo Creating tree in JSON format for parse_dev.dat using CKY Algorithm
python cky_algorithm.py cfg_vert_rare.counts parse_dev.dat > output_vm_original
echo evaluating progress
python eval_parser.py parse_dev.key output_vm
echo Creating tree in JSON format for parse_dev.dat using NEW CKY Algorithm
python cky_algorithm2.py cfg_vert_rare.counts parse_dev.dat > output_vm_updated
echo evaluating progress of new Algorithm
python eval_parser.py parse_dev.key output_vm_updated


echo End Time:
date +"%r"