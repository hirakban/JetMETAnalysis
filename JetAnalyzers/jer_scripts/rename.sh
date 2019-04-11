#!/bin/bash

args=("$@")

if [ $# -ne 1 ] ; then
  echo "Please provide a directory."
  exit
fi

dir=${args[0]}
files=$(ls $dir)
newdir="new"$dir

mkdir $newdir
for f in $files ; do
  newf="${f/ak/AK}"
  newf="${newf/l1l2l3/}"
  newf="${newf/pf/PF}"
  newf="${newf/puppi/PFPuppi}"

  cp $dir/$f $newdir/$newf
done
