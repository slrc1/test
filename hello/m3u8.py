"""<?php

function tv_init()
{
$ch = curl_init("dammikartmp.tulix.tv/slrc1/slrc1/playlist.m3u8");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_HEADER,0);
$d = curl_exec($ch);
curl_close($ch);
if(strlen($d) < 50)return "Error ".$d;
$d = explode("\n",$d);
foreach($d as $dd)
if($dd[0] != "#"){$d = "dammikartmp.tulix.tv/slrc1/slrc1/".$dd;break;}
return $d;
}

function tv_load($d)
{
$ch = curl_init($d);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_HEADER,0);
$d = curl_exec($ch);
curl_close($ch);
$d = explode("\n", $d);
$ddd = array();
foreach($d as $dd)
{if($dd[0] != "#" and $dd != "" )$ddd[] = $dd;}
return $ddd;
}

function tv_loadts($d)
{
$ch = curl_init($d);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_HEADER,0);
$d = curl_exec($ch);
curl_close($ch);
return $d;
}

$t = tv_init();
$ts = tv_load($t);
foreach($ts as $tf)
{
$f = fopen("slrc1/$tf","wb");
$d = tv_loadts("dammikartmp.tulix.tv/slrc1/slrc1/$tf");
fwrite($f,$d);
fclose($f);
}

header("Content-type: image/png");
echo("sssszaZg");

?>
"""

class tv():
    def __init__():
        t = tv_init();
        return

