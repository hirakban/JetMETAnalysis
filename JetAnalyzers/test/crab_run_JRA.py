from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Autumn18_noext'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'run_JRA_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.inputFiles = ["Autumn18_V8_MC.db"]

config.section_("Data")
config.Data.inputDataset = '/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/RunIIAutumn18DR-FlatPU0to70RAW_102X_upgrade2018_realistic_v15-v1/AODSIM'
#'/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/RunIIAutumn18DR-FlatPU0to70RAW_102X_upgrade2018_realistic_v15_ext2-v1/AODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/charring/jerAutumn18'
config.Data.publication = False
#config.Data.ignoreLocality = True

config.section_("Site")
#config.Site.blacklist = ['T1_US_FNAL']
#config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = "T3_US_FNALLPC"

# source /cvmfs/cms.cern.ch/crab3/crab.csh
