identify testimage?.png | perl -ane '$start=110;$sq=200;$inc=5;($w,$h)=split("x",$F[2]);$cmd="convert -pointsize 30 -fill white";for($x=$sq/2;$x<$w;$x+=$sq){for($y=20;$y<$h;$y+=$sq){$now=$start+$inc*($x-$sq/2)/$sq;$s=int($now/60);$m=$now%60;$cmd.=" -draw '\''text $x,$y \"$s:".(sprintf "%02d", $m)."h\"'\''"}}print "$cmd $F[0] ".$F[0]=~s/.png/_annotated.png/r."\n"' | bash