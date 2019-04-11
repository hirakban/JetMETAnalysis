#!/bin/bash

#Be careful not to use same variable names defined in this file!
. ./inspect_graph_methods.sh

args=("$@")

if [ $# -ne 1 ] ; then
  echo "Please provide a variable (Rel, Phi, or Eta)."
  exit
fi

v=${args[0]}

filersp="jra_f.root" #use jra.root to not draw fits
rads=(4 8)
algos=("pf" "pfchs" "puppi")

eta1s=(0   1.1 2.1 3.2)
eta2s=(0.5 1.3 2.3 4.7)

#pt1s=(15 20 27 30 45 90  750)
#pt2s=(17 23 30 35 57 120 1000)

pt1s=(27 30)
pt2s=(30 35)

mus=(0 10 20 30 40 50 60)

#Use these parameters for JERmu script#
pTs="30 50 100 200"
era1="Fall17_17Nov2017_V32_102X_MC"
alg1="pfchs"
era2="Autumn18_V8_MC"
alg2="pfchs"
##

mkdir $v
for rad in "${rads[@]}" ; do
  out=$v/"ak"$rad
  mkdir $out

  if [ $rad = 8 ] ; then
    #for JERmu script
    pTs="100 200 500 1000"
  fi

  for ((ieta=0;ieta<${#eta1s[@]};++ieta)) ; do
    if [ $v == "Rel" ] ; then
      eval "root -l -b -q 'JERmu.c (${eta1s[ieta]}, \"$pTs\", $rad, \"$era1\", \"$alg1\", \"$era2\", \"$alg2\")'"
    fi

    compareAlgs $rad $v ${eta1s[ieta]} ${eta2s[ieta]} ${mus[2]} ${mus[3]} $out
    compareAlgs $rad $v ${eta1s[ieta]} ${eta2s[ieta]} ${mus[5]} ${mus[6]} $out

    for a in "${algos[@]}" ; do
      out2=$out"/"$a
      mkdir $out2

      inspectAlg $rad $v $a ${eta1s[ieta]} ${eta2s[ieta]} $out2

      for ((i=0;i<${#pt1s[@]};++i)) ; do
        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\")'"

        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\", ${mus[2]}, ${mus[3]})'"
        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\", ${mus[5]}, ${mus[6]})'"

#        for mu in "${mus[@]}" ; do
#          mu1=$mu
#          mu2=$(( mu+10 ))
#          eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\", $mu1, $mu2)'"
#        done
      done
    done
  done
done
