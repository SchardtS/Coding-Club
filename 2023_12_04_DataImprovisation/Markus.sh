# A fun solution: opens an interactive 3D pie chart in Firefox
firefox $(cut -f2 countries.txt | tail -n+2 | sort | uniq -c | perl -F'\s+' -ane 'BEGIN{print "https://3dpie.peterbeshai.com/\?t=Country%20Colors&n=3&met=0.5&spn=0.5";$c=0;} print "&v$c=$F[1]&c$c=$F[2]&l$c=$F[2]"; $c++; END{print "\n";}')
