#!/bin/bash

#Be careful not to use same variable names defined in this file!
. ./inspect_graph_methods.sh

args=("$@")

if [ $# -ne 1 ] ; then
  echo "Please provide a variable (Rel, Phi, or Eta)."
  exit
fi

v=${args[0]}

filersp="jra_f.root" #use jra.root to not draw fits, use jra_f.root to draw fits 
#rads=(4 8)
rads=(4)
#algos=("pf" "pfchs" "puppi")
algos=("pfchs")

# Make sure the histograms with specified eta values as strings in their name exist (in input root file jra_f.root).

#eta1s=(0   0.5 0.8 1.1 2.1 3.2)
#eta2s=(0.5 0.8 1.1 1.3 2.3 4.7)

eta1s=(0   0.5 0.8 1.1 1.3 1.7 1.9 2.1 2.3 2.5 2.8 3   3.2)     #input eta = 3 as integer. 
eta2s=(0.5 0.8 1.1 1.3 1.7 1.9 2.1 2.3 2.5 2.8 3   3.2 4.7)

#pt1s=(15 20 27 30 45 90  750)
#pt2s=(17 23 30 35 57 120 1000)

pt1s=(15 20 23 27 30 45)
pt2s=(17 23 27 30 35 57)

#pt1s=(150)
#pt2s=(200)


mus=(0 10 20 30 40 50 60 70)

#Use these parameters for JERmu script#
pTs="30 50 100 200"
era1="Summer19UL18_V2_MC"
alg1="pfchs"
era2="Summer19UL17_V5_MC"
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

#    versions=$out"/versions"
#    mkdir $versions

#    compareVersions $rad $v ${eta1s[ieta]} ${eta2s[ieta]} ${mus[2]} ${mus[3]} $versions
#    compareVersions $rad $v ${eta1s[ieta]} ${eta2s[ieta]} ${mus[5]} ${mus[6]} $versions


    for a in "${algos[@]}" ; do
      out2=$out"/"$a
      mkdir $out2

      inspectAlg $rad $v $a ${eta1s[ieta]} ${eta2s[ieta]} $out2

      for ((i=0;i<${#pt1s[@]};++i)) ; do
        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\")'"

        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\", ${mus[1]}, ${mus[2]})'"
        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\", ${mus[2]}, ${mus[3]})'"
        eval "root -l -b -q 'drawRsp.c(\"$filersp\", $rad, \"$v\", ${eta1s[ieta]}, ${eta2s[ieta]}, ${pt1s[i]}, ${pt2s[i]}, \"$a\", ${mus[4]}, ${mus[5]})'"

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
