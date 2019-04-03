# Submit Dataset to Crab

Look at the [JEC twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC#Recommended_for_MC) to find most recent era (eg Autumn18) and corrections (eg Autumn18_V8_MC).
Use [DAS](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FQCD_Pt-15to7000*%2F*Autumn18*%2FAODSIM) to search for QCD file (eg search dataset=/QCD_Pt-15to7000*/*Autumn18*/AODSIM).

Goto to the `test` directory and get the .db corrections file

    cd test
    svn export https://github.com/cms-jet/JECDatabase/trunk/SQLiteFiles/Autumn18_V8_MC.db

Update the config file `test/run_JRA_cfg.py`- `era`, `globaltag`, and test one file in `inputFiles`. 
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



# Analyze Trees
