# Submit Dataset to Crab

Look at the [JEC twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC#Recommended_for_MC) to find most recent era (eg Autumn18) and corrections (eg Autumn18_V8_MC).
Use [DAS](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FQCD_Pt-15to7000*%2F*Autumn18*%2FAODSIM) to search for QCD file (eg search dataset=/QCD_Pt-15to7000*/\*Autumn18\*/AODSIM).
Also refer to MCTruth derivation slides on [indico](https://indico.cern.ch) for correct QCD dataset.

Goto to the `test` directory and get the .db corrections file

    cd test
    svn export https://github.com/cms-jet/JECDatabase/trunk/SQLiteFiles/Autumn18_V8_MC.db

Update the config file `test/run_JRA_cfg.py`: `era`, `globaltag`, and test one file in `inputFiles`. 
If you wish to study jet composition variables, like neutral particle multiplicity or neutral hadron fraction, set `doComposition` to `True` in `python/Defaults_cff.py`.
Run locally to make sure things are ok.

    voms-proxy-init -voms cms -rfc
    cmsRun run_JRA_cfg.py

Open `JRA.root` and examine trees. For example, look at an event or look at a specific quantity.

    root -l JRA.root
    ak4pfl1l2l3->cd()
    t->Show(1)
    t->Draw("jtpt")    

Once satisfied, update the crab script `test/crab_run_JRA.py` with the correct `inputFiles` and `inputDataset`.
You also need to change `outLFNDirBase` to your EOS and `requestName` to something descriptive.

    source /cvmfs/cms.cern.ch/crab3/crab.csh
    voms-proxy-init -voms cms -rfc
    crab submit crab_run_JRA.py

Check [task monitoring](http://dashb-cms-job.cern.ch/dashboard/templates/task-analysis/) after ~10 minutes to make sure job was submitted.

# hadd

Take care when `hadd`ing files from EOS. Use your temporary `scratch` space if necessary.

    hadd /uscmst1b_scratch/lpc1/3DayLifetime/your_path/JER.root `xrdfsls -u /store/user/path_to_your_files/0000/ | grep .root`

Once completed, copy the file to your EOS or the `lpcjme` group (may need to request permission) using a descriptive name.

    xrdcp /uscmst1b_scratch/lpc1/3DayLifetime/your_path/JER.root root://cmseos.fnal.gov//store/group/lpcjme/JRA_outfiles_102X/JRA_QCD_Autumn18FlatPU_JECv8.root

# Analyze Tree

Edit the `jet_response_analyzer_x` config file `config/JER_jra.config`. Change `input`. Set `doIDrelrsp` to `true` if you want to study jet composition plots (tree must have variables).
Run the analyzer

    cd jer_scripts/
    jet_response_analyzer_x ../config/JER_jra.config > & log.txt &

Run the fitter and feel free to edit any parameters

    jet_response_fitter_x ../config/JER_jrf.config

Get the rho versus mu profile from the tree file

    root -l -b -q 'getRhoMuHisto.c ( "tree_file_name_EOS.root" )'

# Create Text Files

Run the resolution script three times- each time setting one of `dorelrsp`, `doetarsp`, or `dophirsp` to true.
This will produce three root files, one for each variable.

    jet_response_and_resolution_x ../config/JER_jrr.config

If a fit fails, open the root file to look at the problematic graph. For example, if you see `EtaResVsJetPt_JetEta0.8to1.1_Mu50to60 DID NOT FIT!!!`

    root -l etarsp.root
    ((TGraphErrors*)_file0->Get("ak8pfl1l2l3/EtaResVsJetPt_JetEta0.8to1.1_Mu50to60"))->Draw()

Adjusting the fit range usually solves the issue. Edit `bin/jet_response_and_resolution_x.cc` to target the specific problematic graph.
Search `//Example` for an example in the file.

Use the `plot.sh` script to produce many, many plots from `jet_inspect_graphs_x`, `drawRsp.c`, and `JERmu.c`.
Feel free to edit the parameters, and use comments or `continue` to skip things you don't want to plot.
`jet_inspect_graphs_x` parameters are in `inspect_graph_methods.sh`.
The `pt`, `eta`, and `mu` variables must match the config file `config/JER_jra.config`.

    ./plot.sh Rel
    ./plot.sh Eta
    ./plot.sh Phi

If plots look ok, create the `.db` files from the text files using [DBUploadTools](https://github.com/cms-jet/DBUploadTools/tree/master/JEC).
Put all the text files in a single directory. Rename the files, and move to `DBUploadTools` directory.

    ./rename.sh JER_text_files/
    mv newJER_text_files/ ../../../DBUploadTools/data
    cd ../../../DBUploadTools/
    cmsRun JR/createDBFromTxtFiles.py era=Autumn18_V8_MC path=DBUploadTools/data/

If `.db` file successfully created, check the contents with

    conddb --db Autumn18_V8_MC.db listTags
