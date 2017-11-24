#!/usr/bin/perl

for ($i = 1; $i <= 20; $i++) {
  $search_nodes[$i] = 0;
}

  $nomacrosfile = $ARGV[0];
  $datafile = $ARGV[1];
  $macrofile = $ARGV[2];
  $macrofilebest = $ARGV[3];

  # read the total number of training nodes (no macros)  
  open(INFO, $nomacrosfile);
  $line = <INFO>;
  chop $line;
  @tokens = split(/\t+/, $line);
  $line = <INFO>;
  chop $line;
  @tokens = split(/ +/, $line);
   $training_nodes += $tokens[0];
  close(INFO);
  
  
  open(INFO, $datafile);
  $line = <INFO>;
  chop $line;
  @tokens = split(/\t+/, $line);
  $data_volume = $tokens[0];
  
  $line = <INFO>;
  chop $line;
  @tokens = split(/ +/, $line);
  for ($i = 0; $i < $data_volume; $i++) {
    $search_nodes[$i] += $tokens[$i];
    print "$search_nodes[$i] ";
  }
  print "\n";
  close(INFO);

  $min = 10000000;
  $min_idx = -1;
  for ($i = 0; $i < $data_volume; $i++) {
    if ($search_nodes[$i] < $min) {
      $min = $search_nodes[$i];
      $min_idx = $i;
      print "new min: ($min, $min_idx)\n";
    }
  }
  #  assert ($min_idx >= 0);
  if ($min < $training_nodes) {
    $min_idx++;
    system "cp $macrofile.$min_idx $macrofilebest";
  }