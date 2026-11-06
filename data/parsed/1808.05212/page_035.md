**if** (!$on) { }
}
}
}
# finish
groff ();
exit 0;
sub h
{
($x0, $y0, $w) = @_;
d($x0, $y0, $x0 + $w, $y0, 1);
}
sub v
{
($x0, $y0, $h) = @_;
d($x0, $y0, $x0, $y0 + $h, 1);
}
sub vv
{
($x0, $y0, $h) = @_;
d($x0, $y0, $x0, $y0 + $h, 2); # increased thickness
}
sub c
{
($x0, $y0, $rad) = @_;
$x0 += $col; $y0 += $row;
$x0 *= $xscale; $y0 *= $yscale; $rad *= $mscale;
print "\< circle \_cx=%g \_cy=%g \_r=%g \_stroke=\"black\"/\>\n",
$x0, $y0, $rad;
}
sub t
{
$n = 7;
@fixed = ( "Fira \_Mono", "DejaVu \_Sans \_Mono", "Menlo", "Consolas",
"Liberation \_Mono", "Monaco", "Lucida \_Console", "monospace",
"Nimbus \_Mono", "georgia" );
($txt, $x0, $y0) = @_;
$y0 += 0.7; $x0 == 0.0; # font mbb offsets
$x0 *= $xscale; $y0 *= $yscale; $rad *= $mscale;
$font = $fixed [$n];
print
"\<text \_x=\"%g \" \_y=\"%g \" \_ fill =\"black \" \_font-family=\"$font\\">%s\</text \>\n",
$x0, $y0, $txt;
}

