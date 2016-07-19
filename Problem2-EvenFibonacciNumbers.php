<?php
  $sum = 0;
  $fibonacciSeries = array("1","2");
  for($i=1; ; $i++) {
    $temp = $fibonacciSeries[$i] + $fibonacciSeries[$i-1];
    array_push($fibonacciSeries, $temp);
    if($temp.length > 4000000) break;
  }
  for($i=0; $i<count($fibonacciSeries); $i++) {
    if($fibonacciSeries[$i]%2 == 0) {
      $sum += $fibonacciSeries[$i];
    }
  }
  echo "Sum: " . $sum;
?>
