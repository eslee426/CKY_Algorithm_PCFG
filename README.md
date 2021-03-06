Assignment URL: http://www.cs.columbia.edu/~cs4705/hw2/hw2_2014.pdf

#PART 1: HOW TO RUN CODE

Question 4:
Shell Script: q4.sh
Takes about 20 sec to run

Given code to produce counts from training data
python count_cfg_freq.py parse_train.dat > cfg.counts
--> generates count file 

 to replace words with rare and to produce new training data with rare
python add_rare.py cfg.counts parse_train.dat > parse_train_rare.dat
--> outputs new fount file with rare into parse_train_rare.dat

to produce counts for rare training data
python count_cfg_freq.py parse_train_rare.dat > cfg_rare.counts
--> generates new count file


Question 5:
Shell Script: q5.sh
Takes less than 2 minutes tor un

appllies cky_algorithm --> takes about 1.5 min to run
python cky_algorithm.py cfg_rare.counts parse_dev.dat > output
--> sents std output to output file

 compares output file to key
python eval_parser.py parse_dev.key output
--> Prints onto screen


Question 6: 
Shell Script: 16.sh
Takes about 4 minute to run


follows all steps above except with new vertical markovization examples
python count_cfg_freq.py  parse_train_vert.dat > cfg_vert.counts
python add_rare.cfg_vert.counts parse_train_vert.dat > parse_train_vert_rare.dat
python count_cfg_freq.py parse_train_vert_rare.dat > cfg_vert_rare.counts
python cky_algorithm.py cfg_vert_rare.counts parse_dev.dat > output_vm
python eval_parser.py parse_dev.key output_vm
python cky_algorithm2.py cfg_vert_rare.counts parse_dev.dat > output_vm_updated
python eval_parser.py parse_dev.key output_vm_updated



#Part 2: Performance of Algorithm

Question 4:
n/a

Question 5: 

      Type       Total   Precision      Recall     F1 Score
===============================================================
         .         370     1.000        1.000        1.000
       ADJ         164     0.827        0.555        0.664
      ADJP          29     0.333        0.241        0.280
  ADJP+ADJ          22     0.542        0.591        0.565
       ADP         204     0.955        0.946        0.951
       ADV          64     0.694        0.531        0.602
      ADVP          30     0.333        0.133        0.190
  ADVP+ADV          53     0.756        0.642        0.694
      CONJ          53     1.000        1.000        1.000
       DET         167     0.988        0.976        0.982
      NOUN         671     0.752        0.842        0.795
        NP         884     0.636        0.533        0.580
    NP+ADJ           2     0.286        1.000        0.444
    NP+DET          21     0.783        0.857        0.818
   NP+NOUN         131     0.641        0.573        0.605
    NP+NUM          13     0.214        0.231        0.222
   NP+PRON          50     0.980        0.980        0.980
     NP+QP          11     0.667        0.182        0.286
       NUM          93     0.984        0.645        0.779
        PP         208     0.593        0.630        0.611
      PRON          14     1.000        0.929        0.963
       PRT          45     0.957        0.978        0.967
   PRT+PRT           2     0.400        1.000        0.571
        QP          26     0.647        0.423        0.512
         S         587     0.625        0.780        0.694
      SBAR          25     0.091        0.040        0.056
      VERB         283     0.683        0.799        0.736
        VP         399     0.559        0.594        0.576
   VP+VERB          15     0.250        0.267        0.258

     total        4664     0.715        0.715        0.715


Question 6:

Ran algorithm with regular cky algorithm

      Type       Total   Precision      Recall     F1 Score
===============================================================
         .         370     1.000        1.000        1.000
       ADJ         164     0.689        0.622        0.654
      ADJP          29     0.324        0.414        0.364
  ADJP+ADJ          22     0.591        0.591        0.591
       ADP         204     0.960        0.951        0.956
       ADV          64     0.759        0.641        0.695
      ADVP          30     0.417        0.167        0.238
  ADVP+ADV          53     0.700        0.660        0.680
      CONJ          53     1.000        1.000        1.000
       DET         167     0.988        0.994        0.991
      NOUN         671     0.796        0.851        0.823
        NP         884     0.618        0.550        0.582
    NP+ADJ           2     0.333        0.500        0.400
    NP+DET          21     0.944        0.810        0.872
   NP+NOUN         131     0.610        0.656        0.632
    NP+NUM          13     0.375        0.231        0.286
   NP+PRON          50     0.980        0.980        0.980
     NP+QP          11     0.750        0.273        0.400
       NUM          93     0.970        0.688        0.805
        PP         208     0.623        0.635        0.629
      PRON          14     1.000        0.929        0.963
       PRT          45     1.000        0.933        0.966
   PRT+PRT           2     0.286        1.000        0.444
        QP          26     0.722        0.500        0.591
         S         587     0.704        0.814        0.755
      SBAR          25     0.667        0.400        0.500
      VERB         283     0.790        0.813        0.801
        VP         399     0.663        0.677        0.670
   VP+VERB          15     0.294        0.333        0.312

     total        4664     0.743        0.743        0.743

With updated algorithm:

      Type       Total   Precision      Recall     F1 Score
===============================================================
         .         370     1.000        1.000        1.000
       ADJ         164     0.689        0.622        0.654
      ADJP          29     0.324        0.414        0.364
  ADJP+ADJ          22     0.591        0.591        0.591
       ADP         204     0.960        0.951        0.956
       ADV          64     0.759        0.641        0.695
      ADVP          30     0.417        0.167        0.238
  ADVP+ADV          53     0.700        0.660        0.680
      CONJ          53     1.000        1.000        1.000
       DET         167     0.988        0.994        0.991
      NOUN         671     0.796        0.851        0.823
        NP         884     0.618        0.550        0.582
    NP+ADJ           2     0.333        0.500        0.400
    NP+DET          21     0.944        0.810        0.872
   NP+NOUN         131     0.610        0.656        0.632
    NP+NUM          13     0.375        0.231        0.286
   NP+PRON          50     0.980        0.980        0.980
     NP+QP          11     0.750        0.273        0.400
       NUM          93     0.970        0.688        0.805
        PP         208     0.623        0.635        0.629
      PRON          14     1.000        0.929        0.963
       PRT          45     1.000        0.933        0.966
   PRT+PRT           2     0.286        1.000        0.444
        QP          26     0.722        0.500        0.591
         S         587     0.704        0.814        0.755
      SBAR          25     0.667        0.400        0.500
      VERB         283     0.790        0.813        0.801
        VP         399     0.663        0.677        0.670
   VP+VERB          15     0.294        0.333        0.312

     total        4664     0.743        0.743        0.743

#Part 3: Observations and Comments

Question 4:
The new training file it produces: 
	1. cfg_rare.counts
		- which replaces all rare words with _RARE_ and recounts
	2. parse_train_rare.dat
		- reprints train data with _RARE_ words added
I iterated through each line in the original counts file, keeping track of the word count. I put all words that occured less than 5 times into a set. I then iterated through each line of the .dat file and as I outputed the line, replaced any occurences of an infrequent word with _RARE_

Question 5:
	1. Created default dicts to keep track of all info needed and to speed up process of algorithm
	2. computes maximum likilihood parameters wiht string representation of rule using compute_ml(puts calculations in a dic) and calc_ml(performs actual calculation)
	3. CKY algorithm: Overall has a precision, recall and F1 Score of 0.715, which is is pretty good. It especially did well on rules associating with ".", ADP, CONJ, NP+PRON, PRON, PRT. It did not do so well on rules associating with SBAR, VP+VERB, and ADJP. This makes sense because there is a lot of ambiguity following these rules. 
	4. My aglorithm initially ran pretty slow. I improved my algorithm efficiently to run in 1.5 minutes by adding more dictionaries rather than list (faster lookups). This increased my precision and time dramatically. 


Question 6:
	1. Performance increased from 0.715 to 0.743. The rule that improved the most is SBAR, which increased from aprecision of 0.091 to 0.667. Most of the rules seemed to have increased a slight amount. This is using the new data given. I tried to improve my algorithm even more, but the precision in general stayed the same.
	2. To edit my algoirhtm, i only went through a more specific set of rules, determined by the parent subscript. I did this by putting all parents and their subsequent rules into a dictionary. This however, gave me a same exact precision/data. I feel like i improved my code a lot during the original algorithm, which led to small to no improvements with updated algorithm. It still runs in a small run of time. This may be because I am still using the same set of rules given. As you can see below, they produced the same tree. 

KEY
[S,
 [NP, [NOUN, Deal], [NOUN, stocks]],
 [S,
  [VP,
   [VERB, led],
   [VP,
    [NP, [DET, the], [NOUN, market]],
    [VP,
     [ADVP+ADV, down],
     [SBAR,
      [ADP, as],
      [S,
       [NP+PRON, they],
       [VP,
        [VERB, absorbed],
        [NP, [DET, the], [NP, [ADJ, heaviest], [NOUN, losses]]]]]]]]],

VM OUTPUT with original CKY Algorithm
[S,
 [NP^<S>, [NOUN, Deal], [NOUN, stocks]],
 [S,
  [VP^<S>,
   [VERB, led],
   [VP,
    [NP^<VP>, [DET, the], [NOUN, market]],
    [VP,
     [PRT^<VP>+PRT, down],
     [SBAR^<VP>,
      [ADP, as],
      [S^<SBAR>,
       [NP^<S>+PRON, they],
       [VP^<S>,
        [VERB, absorbed],
        [NP^<VP>, [DET, the], [NP, [NOUN, heaviest], [NOUN, losses]]]]]]]]],
  [., .]]]

  VM Output with UPDATED CKY Algorithm
 [S,
 [NP^<S>, [NOUN, Deal], [NOUN, stocks]],
 [S,
  [VP^<S>,
   [VERB, led],
   [VP,
    [NP^<VP>, [DET, the], [NOUN, market]],
    [VP,
     [PRT^<VP>+PRT, down],
     [SBAR^<VP>,
      [ADP, as],
      [S^<SBAR>,
       [NP^<S>+PRON, they],
       [VP^<S>,
        [VERB, absorbed],
        [NP^<VP>, [DET, the], [NP, [NOUN, heaviest], [NOUN, losses]]]]]]]]],
  [., .]]]


REGULAR
  [S,
 [NP, [NOUN, Deal], [NOUN, stocks]],
 [S,
  [VP, [VERB, led], [NP, [DET, the], [NOUN, market]]],
  [S,
   [ADVP, [ADV, down], [ADV, as]],
   [S,
    [NP+PRON, they],
    [S,
     [VP,
      [VERB, absorbed],
      [NP, [DET, the], [NP, [NOUN, heaviest], [NOUN, losses]]]],
     [., .]]]]]]


     As you can see above, the regular sentence in itself did not predict SBAR at all - which is included  in the original sentence. The VM output allowed the sentence to produce the SBAR, leading toa more accurate sentence.
     Sentence: Deal stocks led the market down as they absorbed the heaviest losses
