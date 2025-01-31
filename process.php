<?php

$a = escapeshellarg($_POST['a']);
$b = escapeshellarg($_POST['b']);
$c = escapeshellarg($_POST['c']);

$command = escapeshellcmd("python3 calculate.py $a $b $c");
$output = shell_exec($command);

echo "<h2>Assignment 4 Results:</h2>";
echo "<div>$output</div>";

?>
