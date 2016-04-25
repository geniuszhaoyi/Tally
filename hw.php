<?php
echo "Hello World<br>";
$con = mysql_connect("localhost","zjwdb_521742","aregERSG435");
if (!$con)
  {
  echo 'Could not connect: ' . mysql_error();
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("zjwdb_521742", $con);

$result = mysql_query("SELECT * FROM TollyBook");

while($row = mysql_fetch_array($result))
  {
  echo $row['tb_Name'] . " " . $row['tb_Desc'];
  echo "<br />";
  }

mysql_close($con);
?>
