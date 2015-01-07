#!/bin/bash
# q4.sh 
# implents necessary functions for q4
echo Start Time: 
date +"%r"

echo Creating cfg.counts
python count_cfg_freq.py parse_train.dat > cfg.counts
echo Adding rare to parse_tree.dat to produce parse_tree_rare.dat
python add_rare.py cfg.counts parse_train.dat > parse_train_rare.dat
echo Creating cfg_rare.counts for parse_tree_rare.dat
python count_cfg_freq.py parse_train_rare.dat > cfg_rare.counts

echo End Time:
date +"%r"