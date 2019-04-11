#methods to plot JER graphs using jet_inspect_graphs_x

compareAlgs() {

  R=$1
  prefix=$2
  eta1=$3
  eta2=$4
  mu1=$5
  mu2=$6
  opath=$7

  algs="ak"$R"pfl1l2l3 ak"$R"pfchsl1l2l3 ak"$R"puppil1l2l3"
  legend="PF PF+CHS PF+PUPPI"

  eta="0.41:0.87:62:0.045:"$eta1"#leq#eta<"$eta2
  mu="0.41:0.815:62:0.045:"$mu1"#leq#mu<"$mu2
  labels="0.2:0.87:62:0.045:Anti-k_{T} 0.2:0.815:62:0.045:R=0."$R" "$eta" "$mu

  var=$prefix"ResVsJetPt_JetEta"$eta1"to"$eta2"_Mu"$mu1"to"$mu2

  if [ "$prefix" = "Rel" ] ; then

    file="relrsp.root"
    title="JER"
    if [ $R -eq 8 ] ; then
      range=0.8
    else
      range=0.5
    fi
  elif [ "$prefix" = "Eta" ] ; then

    file="etarsp.root"
    title="#eta Resolution"
    if [ $R -eq 8 ] ; then
      range=0.2
    else
      range=0.1
    fi
  elif [ "$prefix" = "Phi" ] ; then

    file="phirsp.root"
    title="#phi Resolution"
    if [ $R -eq 8 ] ; then
      range=0.2
    else
      range=0.1
    fi
  fi

  jet_inspect_graphs_x -sizes "1 1 1" -opath $opath -inputs $file -algs $algs -logx true -batch true \
  -variables $var -leglabels $legend -legx 0.62 -legy 0.91 -drawrange false -xtitle "p_{T}^{Jet} [GeV]" -tdr true \
  -xmin 15 -xmax 4000 -ymin 0 -ymax $range -ytitle "$title" -tdrlabels $labels
}

inspectAlg() {

  R=$1
  prefix=$2
  alg=$3
  eta1=$4
  eta2=$5
  opath=$6

  legend="0#leq#mu<10 10#leq#mu<20 20#leq#mu<30 30#leq#mu<40 40#leq#mu<50 50#leq#mu<60 60#leq#mu<70"
  eta="0.41:0.87:62:0.045:"$eta1"#leq#eta<"$eta2

  var=$prefix"ResVsJetPt_JetEta"$eta1"to"$eta2":Mu"

  if [ "$alg" = "pf" ] ; then

    algs="ak"$R"pfl1l2l3"
    alglabel="0.47:0.815:62:0.045:PF"

  elif [ "$alg" = "pfchs" ] ; then

    algs="ak"$R"pfchsl1l2l3"
    alglabel="0.41:0.815:62:0.045:PF+CHS"

  elif [ "$alg" = "puppi" ] ; then

    algs="ak"$R"puppil1l2l3"
    alglabel="0.4:0.815:62:0.045:PF+PUPPI"
  fi
  labels="0.2:0.87:62:0.045:Anti-k_{T} 0.2:0.815:62:0.045:R=0."$R" "$eta" "$alglabel

  if [ "$prefix" = "Rel" ] ; then

    file="relrsp.root"
    title="JER"
    if [ $R -eq 8 ] ; then
      range=0.8
    else
      range=0.5
    fi
  elif [ "$prefix" = "Eta" ] ; then

    file="etarsp.root"
    title="#eta Resolution"
    if [ $R -eq 8 ] ; then
      range=0.2
    else
      range=0.1
    fi
  elif [ "$prefix" = "Phi" ] ; then

    file="phirsp.root"
    title="#phi Resolution"
    if [ $R -eq 8 ] ; then
      range=0.2
    else
      range=0.1
    fi
  fi

  jet_inspect_graphs_x -opath $opath -inputs $file -algs $algs -logx true -batch true \
  -variables $var -leglabels $legend -legx 0.67 -legy 0.91 -drawrange false -xtitle "p_{T}^{Jet} [GeV]" -tdr true \
  -xmin 15 -xmax 4000 -ymin 0 -ymax $range -ytitle "$title" -tdrlabels $labels
}
