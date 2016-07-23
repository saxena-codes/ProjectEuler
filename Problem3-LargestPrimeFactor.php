<?php
  $number = 600851475143;
  //Only need to check upto square root of the number
  $sqrtnum = (int)sqrt($number);
  //Starting from largest to 4 -> as 1,2,3 are prime
  for($i=9999; $i>4; $i--) {
    $status = true;
    if($i%2 == 0) {
      $status = false;
    } else {
      for($j=2; $j<$i; $j++) {
        if($i%$j == 0) {
          $status = false;
          break;
        }
      }
    }
    if($status) {
      //It is a prime number
      //Now check if it divides the real number
      if($number%$i == 0) {
        echo $i;
        break;
      }
    }
  }
?>
