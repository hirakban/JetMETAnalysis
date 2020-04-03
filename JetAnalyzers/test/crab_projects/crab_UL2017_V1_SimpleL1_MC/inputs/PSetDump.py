import FWCore.ParameterSet.Config as cms

process = cms.Process("JRA")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISummer19UL17MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/MINIAODSIM/FlatPU0to70_106X_mc2017_realistic_v6-v3/40000/FFEE2656-43CF-4247-8A06-8B04E8FF00F5.root')
)
process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.ak10PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak10PFCHSJets")
)


process.ak10PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak10PFCHSJets")
)


process.ak10PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak10PFCHSJets")
)


process.ak10PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak10PFCHSJets")
)


process.ak10PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFCHSL2L3Corrector"),
    src = cms.InputTag("ak10PFCHSJets")
)


process.ak10PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFCHSL1FastjetCorrector", "ak10PFCHSL2RelativeCorrector", "ak10PFCHSL3AbsoluteCorrector", "ak10PFCHSResidualCorrector")
)


process.ak10PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFCHSL1OffsetCorrector", "ak10PFCHSL2RelativeCorrector", "ak10PFCHSL3AbsoluteCorrector", "ak10PFCHSResidualCorrector")
)


process.ak10PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak10PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFCHSL2RelativeCorrector", "ak10PFCHSL3AbsoluteCorrector")
)


process.ak10PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFCHSL2RelativeCorrector", "ak10PFCHSL3AbsoluteCorrector", "ak10PFCHSResidualCorrector")
)


process.ak10PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL1L2L3Corrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL2RelativeCorrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL2L3Corrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak10PFJets")
)


process.ak10PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFL1FastjetCorrector", "ak10PFL2RelativeCorrector", "ak10PFL3AbsoluteCorrector", "ak10PFResidualCorrector")
)


process.ak10PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFL1OffsetCorrector", "ak10PFL2RelativeCorrector", "ak10PFL3AbsoluteCorrector", "ak10PFResidualCorrector")
)


process.ak10PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak10PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFL2RelativeCorrector", "ak10PFL3AbsoluteCorrector")
)


process.ak10PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PFL2RelativeCorrector", "ak10PFL3AbsoluteCorrector", "ak10PFResidualCorrector")
)


process.ak10PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak10PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak10PUPPIJets")
)


process.ak10PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak10PUPPIJets")
)


process.ak10PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak10PUPPIL2L3Corrector"),
    src = cms.InputTag("ak10PUPPIJets")
)


process.ak10PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PUPPIL1FastjetCorrector", "ak10PUPPIL2RelativeCorrector", "ak10PUPPIL3AbsoluteCorrector")
)


process.ak10PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK10PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak10PUPPIL2RelativeCorrector", "ak10PUPPIL3AbsoluteCorrector")
)


process.ak10PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK10PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak10PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK10PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak1PFCHSJets")
)


process.ak1PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak1PFCHSJets")
)


process.ak1PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak1PFCHSJets")
)


process.ak1PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak1PFCHSJets")
)


process.ak1PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFCHSL2L3Corrector"),
    src = cms.InputTag("ak1PFCHSJets")
)


process.ak1PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFCHSL1FastjetCorrector", "ak1PFCHSL2RelativeCorrector", "ak1PFCHSL3AbsoluteCorrector", "ak1PFCHSResidualCorrector")
)


process.ak1PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFCHSL1OffsetCorrector", "ak1PFCHSL2RelativeCorrector", "ak1PFCHSL3AbsoluteCorrector", "ak1PFCHSResidualCorrector")
)


process.ak1PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak1PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFCHSL2RelativeCorrector", "ak1PFCHSL3AbsoluteCorrector")
)


process.ak1PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFCHSL2RelativeCorrector", "ak1PFCHSL3AbsoluteCorrector", "ak1PFCHSResidualCorrector")
)


process.ak1PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL1L2L3Corrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL2RelativeCorrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL2L3Corrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak1PFJets")
)


process.ak1PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFL1FastjetCorrector", "ak1PFL2RelativeCorrector", "ak1PFL3AbsoluteCorrector", "ak1PFResidualCorrector")
)


process.ak1PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFL1OffsetCorrector", "ak1PFL2RelativeCorrector", "ak1PFL3AbsoluteCorrector", "ak1PFResidualCorrector")
)


process.ak1PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak1PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFL2RelativeCorrector", "ak1PFL3AbsoluteCorrector")
)


process.ak1PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PFL2RelativeCorrector", "ak1PFL3AbsoluteCorrector", "ak1PFResidualCorrector")
)


process.ak1PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak1PUPPIJets")
)


process.ak1PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak1PUPPIJets")
)


process.ak1PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak1PUPPIL2L3Corrector"),
    src = cms.InputTag("ak1PUPPIJets")
)


process.ak1PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PUPPIL1FastjetCorrector", "ak1PUPPIL2RelativeCorrector", "ak1PUPPIL3AbsoluteCorrector")
)


process.ak1PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK1PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak1PUPPIL2RelativeCorrector", "ak1PUPPIL3AbsoluteCorrector")
)


process.ak1PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK1PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak1PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK1PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak2PFCHSJets")
)


process.ak2PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak2PFCHSJets")
)


process.ak2PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak2PFCHSJets")
)


process.ak2PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak2PFCHSJets")
)


process.ak2PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFCHSL2L3Corrector"),
    src = cms.InputTag("ak2PFCHSJets")
)


process.ak2PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFCHSL1FastjetCorrector", "ak2PFCHSL2RelativeCorrector", "ak2PFCHSL3AbsoluteCorrector", "ak2PFCHSResidualCorrector")
)


process.ak2PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFCHSL1OffsetCorrector", "ak2PFCHSL2RelativeCorrector", "ak2PFCHSL3AbsoluteCorrector", "ak2PFCHSResidualCorrector")
)


process.ak2PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak2PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFCHSL2RelativeCorrector", "ak2PFCHSL3AbsoluteCorrector")
)


process.ak2PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFCHSL2RelativeCorrector", "ak2PFCHSL3AbsoluteCorrector", "ak2PFCHSResidualCorrector")
)


process.ak2PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL1L2L3Corrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL2RelativeCorrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL2L3Corrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak2PFJets")
)


process.ak2PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFL1FastjetCorrector", "ak2PFL2RelativeCorrector", "ak2PFL3AbsoluteCorrector", "ak2PFResidualCorrector")
)


process.ak2PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFL1OffsetCorrector", "ak2PFL2RelativeCorrector", "ak2PFL3AbsoluteCorrector", "ak2PFResidualCorrector")
)


process.ak2PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak2PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFL2RelativeCorrector", "ak2PFL3AbsoluteCorrector")
)


process.ak2PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PFL2RelativeCorrector", "ak2PFL3AbsoluteCorrector", "ak2PFResidualCorrector")
)


process.ak2PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak2PUPPIJets")
)


process.ak2PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak2PUPPIJets")
)


process.ak2PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak2PUPPIL2L3Corrector"),
    src = cms.InputTag("ak2PUPPIJets")
)


process.ak2PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PUPPIL1FastjetCorrector", "ak2PUPPIL2RelativeCorrector", "ak2PUPPIL3AbsoluteCorrector")
)


process.ak2PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK2PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak2PUPPIL2RelativeCorrector", "ak2PUPPIL3AbsoluteCorrector")
)


process.ak2PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK2PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak2PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK2PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak3PFCHSJets")
)


process.ak3PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak3PFCHSJets")
)


process.ak3PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak3PFCHSJets")
)


process.ak3PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak3PFCHSJets")
)


process.ak3PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFCHSL2L3Corrector"),
    src = cms.InputTag("ak3PFCHSJets")
)


process.ak3PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFCHSL1FastjetCorrector", "ak3PFCHSL2RelativeCorrector", "ak3PFCHSL3AbsoluteCorrector", "ak3PFCHSResidualCorrector")
)


process.ak3PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFCHSL1OffsetCorrector", "ak3PFCHSL2RelativeCorrector", "ak3PFCHSL3AbsoluteCorrector", "ak3PFCHSResidualCorrector")
)


process.ak3PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak3PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFCHSL2RelativeCorrector", "ak3PFCHSL3AbsoluteCorrector")
)


process.ak3PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFCHSL2RelativeCorrector", "ak3PFCHSL3AbsoluteCorrector", "ak3PFCHSResidualCorrector")
)


process.ak3PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL1L2L3Corrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL2RelativeCorrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL2L3Corrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFL1FastjetCorrector", "ak3PFL2RelativeCorrector", "ak3PFL3AbsoluteCorrector", "ak3PFResidualCorrector")
)


process.ak3PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFL1OffsetCorrector", "ak3PFL2RelativeCorrector", "ak3PFL3AbsoluteCorrector", "ak3PFResidualCorrector")
)


process.ak3PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak3PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFL2RelativeCorrector", "ak3PFL3AbsoluteCorrector")
)


process.ak3PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PFL2RelativeCorrector", "ak3PFL3AbsoluteCorrector", "ak3PFResidualCorrector")
)


process.ak3PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak3PUPPIJets")
)


process.ak3PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak3PUPPIJets")
)


process.ak3PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak3PUPPIL2L3Corrector"),
    src = cms.InputTag("ak3PUPPIJets")
)


process.ak3PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PUPPIL1FastjetCorrector", "ak3PUPPIL2RelativeCorrector", "ak3PUPPIL3AbsoluteCorrector")
)


process.ak3PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK3PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak3PUPPIL2RelativeCorrector", "ak3PUPPIL3AbsoluteCorrector")
)


process.ak3PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK3PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak3PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK3PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4CaloJetsL1 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL1FastL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastL2L3Corrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL1FastL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL1L2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1L2L3Corrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL1L2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1L2L3L6Corrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL1L2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL2 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL2L3Corrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL2L3L6Corrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloJetsL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL2L3ResidualCorrector"),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak4JPTJetsL1 = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4L1JPTFastjetCorrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL1FastL2L3 = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL1FastL2L3Corrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL1FastL2L3Residual = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL1L2L3 = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL1L2L3Corrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL1L2L3Residual = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL1L2L3ResidualCorrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL2 = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL2RelativeCorrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL2L3 = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL2L3Corrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTJetsL2L3Residual = cms.EDProducer("CorrectedJPTJetProducer",
    correctors = cms.VInputTag("ak4JPTL2L3ResidualCorrector"),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt4")
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1FastjetCorrector")
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("pfCHS"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.ak4PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak4PFCHSJets")
)


process.ak4PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.ak4PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.ak4PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL2L3Corrector"),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1L2L3Corrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL1L2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1L2L3L6Corrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL2L3Corrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL2L3L6Corrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak4PUPPIJets")
)


process.ak4PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak4PUPPIJets")
)


process.ak4PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PUPPIL2L3Corrector"),
    src = cms.InputTag("ak4PUPPIJets")
)


process.ak4PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PUPPIL1FastjetCorrector", "ak4PUPPIL2RelativeCorrector", "ak4PUPPIL3AbsoluteCorrector")
)


process.ak4PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PUPPIL2RelativeCorrector", "ak4PUPPIL3AbsoluteCorrector")
)


process.ak4PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4TrackJetsL1 = cms.EDProducer("CorrectedTrackJetProducer",
    correctors = cms.VInputTag("ak4TrackL1FastjetCorrector"),
    src = cms.InputTag("ak4TrackJets")
)


process.ak4TrackJetsL1L2L3 = cms.EDProducer("CorrectedTrackJetProducer",
    correctors = cms.VInputTag("ak5TRKL1L2L3Corrector"),
    src = cms.InputTag("ak4TrackJets")
)


process.ak4TrackJetsL2 = cms.EDProducer("CorrectedTrackJetProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector"),
    src = cms.InputTag("ak4TrackJets")
)


process.ak4TrackJetsL2L3 = cms.EDProducer("CorrectedTrackJetProducer",
    correctors = cms.VInputTag("ak4TrackL2L3Corrector"),
    src = cms.InputTag("ak4TrackJets")
)


process.ak4TrackL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.ak4pfchsl1l2l3JetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfchsGenPtEta"),
    srcRec = cms.InputTag("ak4pfchsl1l2l3PtEta")
)


process.ak4pfchsl1l2l3JetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfchsl1l2l3PtEtaUncor"),
    srcRec = cms.InputTag("ak4pfchsl1l2l3PtEta")
)


process.ak4pfl1l2l3JetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfGenPtEta"),
    srcRec = cms.InputTag("ak4pfl1l2l3PtEta")
)


process.ak4pfl1l2l3JetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfl1l2l3PtEtaUncor"),
    srcRec = cms.InputTag("ak4pfl1l2l3PtEta")
)


process.ak5PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak5PFCHSJets")
)


process.ak5PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak5PFCHSJets")
)


process.ak5PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak5PFCHSJets")
)


process.ak5PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak5PFCHSJets")
)


process.ak5PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFCHSL2L3Corrector"),
    src = cms.InputTag("ak5PFCHSJets")
)


process.ak5PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFCHSL1FastjetCorrector", "ak5PFCHSL2RelativeCorrector", "ak5PFCHSL3AbsoluteCorrector", "ak5PFCHSResidualCorrector")
)


process.ak5PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFCHSL1OffsetCorrector", "ak5PFCHSL2RelativeCorrector", "ak5PFCHSL3AbsoluteCorrector", "ak5PFCHSResidualCorrector")
)


process.ak5PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak5PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFCHSL2RelativeCorrector", "ak5PFCHSL3AbsoluteCorrector")
)


process.ak5PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFCHSL2RelativeCorrector", "ak5PFCHSL3AbsoluteCorrector", "ak5PFCHSResidualCorrector")
)


process.ak5PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL1L2L3Corrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL2RelativeCorrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL2L3Corrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak5PFJets")
)


process.ak5PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFL1FastjetCorrector", "ak5PFL2RelativeCorrector", "ak5PFL3AbsoluteCorrector", "ak5PFResidualCorrector")
)


process.ak5PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFL1OffsetCorrector", "ak5PFL2RelativeCorrector", "ak5PFL3AbsoluteCorrector", "ak5PFResidualCorrector")
)


process.ak5PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak5PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFL2RelativeCorrector", "ak5PFL3AbsoluteCorrector")
)


process.ak5PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PFL2RelativeCorrector", "ak5PFL3AbsoluteCorrector", "ak5PFResidualCorrector")
)


process.ak5PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak5PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak4PUPPIJets")
)


process.ak5PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak5PUPPIJets")
)


process.ak5PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak5PUPPIL2L3Corrector"),
    src = cms.InputTag("ak5PUPPIJets")
)


process.ak5PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PUPPIL1FastjetCorrector", "ak5PUPPIL2RelativeCorrector", "ak5PUPPIL3AbsoluteCorrector")
)


process.ak5PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak5PUPPIL2RelativeCorrector", "ak5PUPPIL3AbsoluteCorrector")
)


process.ak5PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak5PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak6PFCHSJets")
)


process.ak6PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak6PFCHSJets")
)


process.ak6PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak6PFCHSJets")
)


process.ak6PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak6PFCHSJets")
)


process.ak6PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFCHSL2L3Corrector"),
    src = cms.InputTag("ak6PFCHSJets")
)


process.ak6PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFCHSL1FastjetCorrector", "ak6PFCHSL2RelativeCorrector", "ak6PFCHSL3AbsoluteCorrector", "ak6PFCHSResidualCorrector")
)


process.ak6PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFCHSL1OffsetCorrector", "ak6PFCHSL2RelativeCorrector", "ak6PFCHSL3AbsoluteCorrector", "ak6PFCHSResidualCorrector")
)


process.ak6PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak6PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFCHSL2RelativeCorrector", "ak6PFCHSL3AbsoluteCorrector")
)


process.ak6PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFCHSL2RelativeCorrector", "ak6PFCHSL3AbsoluteCorrector", "ak6PFCHSResidualCorrector")
)


process.ak6PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL1L2L3Corrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL2RelativeCorrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL2L3Corrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak6PFJets")
)


process.ak6PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFL1FastjetCorrector", "ak6PFL2RelativeCorrector", "ak6PFL3AbsoluteCorrector", "ak6PFResidualCorrector")
)


process.ak6PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFL1OffsetCorrector", "ak6PFL2RelativeCorrector", "ak6PFL3AbsoluteCorrector", "ak6PFResidualCorrector")
)


process.ak6PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak6PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFL2RelativeCorrector", "ak6PFL3AbsoluteCorrector")
)


process.ak6PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PFL2RelativeCorrector", "ak6PFL3AbsoluteCorrector", "ak6PFResidualCorrector")
)


process.ak6PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak6PUPPIJets")
)


process.ak6PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak6PUPPIJets")
)


process.ak6PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak6PUPPIL2L3Corrector"),
    src = cms.InputTag("ak6PUPPIJets")
)


process.ak6PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PUPPIL1FastjetCorrector", "ak6PUPPIL2RelativeCorrector", "ak6PUPPIL3AbsoluteCorrector")
)


process.ak6PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK6PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak6PUPPIL2RelativeCorrector", "ak6PUPPIL3AbsoluteCorrector")
)


process.ak6PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK6PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak6PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK6PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak7CaloJetsL1 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL1FastL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL1FastL2L3Corrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL1FastL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL1L2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL1L2L3Corrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL1L2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL1L2L3L6Corrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL1L2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL2 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL2RelativeCorrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL2L3Corrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL2L3L6Corrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloJetsL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak7CaloL2L3ResidualCorrector"),
    src = cms.InputTag("ak7CaloJets")
)


process.ak7CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector")
)


process.ak7CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1OffsetCorrector", "ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector", "ak7CaloL6SLBCorrector")
)


process.ak7CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1FastjetCorrector", "ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector", "ak7CaloResidualCorrector")
)


process.ak7CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1OffsetCorrector", "ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector")
)


process.ak7CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1OffsetCorrector", "ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector", "ak7CaloResidualCorrector")
)


process.ak7CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak7CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector")
)


process.ak7CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector", "ak7CaloL6SLBCorrector")
)


process.ak7CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL2RelativeCorrector", "ak7CaloL3AbsoluteCorrector", "ak7CaloResidualCorrector")
)


process.ak7CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1FastjetCorrector", "ak7L1JPTFastjetCorrector", "ak7JPTL2RelativeCorrector", "ak7JPTL3AbsoluteCorrector")
)


process.ak7JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1FastjetCorrector", "ak7L1JPTFastjetCorrector", "ak7JPTL2RelativeCorrector", "ak7JPTL3AbsoluteCorrector", "ak7JPTResidualCorrector")
)


process.ak7JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1OffsetCorrector", "ak7L1JPTOffsetCorrector", "ak7JPTL2RelativeCorrector", "ak7JPTL3AbsoluteCorrector")
)


process.ak7JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1OffsetCorrector", "ak7L1JPTOffsetCorrector", "ak7JPTL2RelativeCorrector", "ak7JPTL3AbsoluteCorrector", "ak7JPTResidualCorrector")
)


process.ak7JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7CaloL1OffsetCorrector", "ak7L1JPTOffsetCorrector", "ak7JPTL2RelativeCorrector", "ak7JPTL3AbsoluteCorrector")
)


process.ak7JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L2Relative')
)


process.ak7JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L3Absolute')
)


process.ak7JPTL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7JPTJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7JPTJetsSoftMuonTagInfos")
)


process.ak7JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7L1JPTFastjetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak7CaloL1FastjetCorrector")
)


process.ak7L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak7CaloL1OffsetCorrector")
)


process.ak7PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak7PFCHSJets")
)


process.ak7PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak7PFCHSJets")
)


process.ak7PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak7PFCHSJets")
)


process.ak7PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak7PFCHSJets")
)


process.ak7PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFCHSL2L3Corrector"),
    src = cms.InputTag("ak7PFCHSJets")
)


process.ak7PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak7PFCHSL2RelativeCorrector", "ak7PFCHSL3AbsoluteCorrector")
)


process.ak7PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFCHSL1FastjetCorrector", "ak7PFCHSL2RelativeCorrector", "ak7PFCHSL3AbsoluteCorrector", "ak7PFCHSResidualCorrector")
)


process.ak7PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFCHSL1OffsetCorrector", "ak7PFCHSL2RelativeCorrector", "ak7PFCHSL3AbsoluteCorrector", "ak7PFCHSResidualCorrector")
)


process.ak7PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak7PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFCHSL2RelativeCorrector", "ak7PFCHSL3AbsoluteCorrector")
)


process.ak7PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFCHSL2RelativeCorrector", "ak7PFCHSL3AbsoluteCorrector", "ak7PFCHSResidualCorrector")
)


process.ak7PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL1L2L3Corrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL1L2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL1L2L3L6Corrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL2RelativeCorrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL2L3Corrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL2L3L6Corrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak7PFJets")
)


process.ak7PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector")
)


process.ak7PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector", "ak7PFL6SLBCorrector")
)


process.ak7PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFL1FastjetCorrector", "ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector", "ak7PFResidualCorrector")
)


process.ak7PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFL1OffsetCorrector", "ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector")
)


process.ak7PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFL1OffsetCorrector", "ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector", "ak7PFResidualCorrector")
)


process.ak7PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak7PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector")
)


process.ak7PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector", "ak7PFL6SLBCorrector")
)


process.ak7PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PFL2RelativeCorrector", "ak7PFL3AbsoluteCorrector", "ak7PFResidualCorrector")
)


process.ak7PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak7PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak8PUPPIJets")
)


process.ak7PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak7PUPPIJets")
)


process.ak7PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak7PUPPIL2L3Corrector"),
    src = cms.InputTag("ak7PUPPIJets")
)


process.ak7PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PUPPIL1FastjetCorrector", "ak7PUPPIL2RelativeCorrector", "ak7PUPPIL3AbsoluteCorrector")
)


process.ak7PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK7PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak7PUPPIL2RelativeCorrector", "ak7PUPPIL3AbsoluteCorrector")
)


process.ak7PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak7PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK7PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak8PFCHSJets")
)


process.ak8PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak8PFCHSJets")
)


process.ak8PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak8PFCHSJets")
)


process.ak8PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak8PFCHSJets")
)


process.ak8PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFCHSL2L3Corrector"),
    src = cms.InputTag("ak8PFCHSJets")
)


process.ak8PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFCHSL1FastjetCorrector", "ak8PFL2RelativeCorrector", "ak8PFL3AbsoluteCorrector")
)


process.ak8PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFCHSL1FastjetCorrector", "ak8PFCHSL2RelativeCorrector", "ak8PFCHSL3AbsoluteCorrector", "ak8PFCHSResidualCorrector")
)


process.ak8PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFCHSL1OffsetCorrector", "ak8PFCHSL2RelativeCorrector", "ak8PFCHSL3AbsoluteCorrector", "ak8PFCHSResidualCorrector")
)


process.ak8PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak8PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFCHSL2RelativeCorrector", "ak8PFCHSL3AbsoluteCorrector")
)


process.ak8PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFCHSL2RelativeCorrector", "ak8PFCHSL3AbsoluteCorrector", "ak8PFCHSResidualCorrector")
)


process.ak8PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL1L2L3Corrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL2RelativeCorrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL2L3Corrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak8PFJets")
)


process.ak8PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFL1FastjetCorrector", "ak8PFL2RelativeCorrector", "ak8PFL3AbsoluteCorrector")
)


process.ak8PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFL1FastjetCorrector", "ak8PFL2RelativeCorrector", "ak8PFL3AbsoluteCorrector", "ak8PFResidualCorrector")
)


process.ak8PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFL1OffsetCorrector", "ak8PFL2RelativeCorrector", "ak8PFL3AbsoluteCorrector", "ak8PFResidualCorrector")
)


process.ak8PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak8PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFL2RelativeCorrector", "ak8PFL3AbsoluteCorrector")
)


process.ak8PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PFL2RelativeCorrector", "ak8PFL3AbsoluteCorrector", "ak8PFResidualCorrector")
)


process.ak8PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak8PUPPIJets")
)


process.ak8PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak8PUPPIJets")
)


process.ak8PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak8PUPPIL2L3Corrector"),
    src = cms.InputTag("ak8PUPPIJets")
)


process.ak8PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PUPPIL1FastjetCorrector", "ak8PUPPIL2RelativeCorrector", "ak8PUPPIL3AbsoluteCorrector")
)


process.ak8PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak8PUPPIL2RelativeCorrector", "ak8PUPPIL3AbsoluteCorrector")
)


process.ak8PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak8PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector"),
    src = cms.InputTag("ak9PFCHSJets")
)


process.ak9PFCHSJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFCHSL1FastL2L3Corrector"),
    src = cms.InputTag("ak9PFCHSJets")
)


process.ak9PFCHSJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFCHSL1L2L3Corrector"),
    src = cms.InputTag("ak9PFCHSJets")
)


process.ak9PFCHSJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFCHSL2RelativeCorrector"),
    src = cms.InputTag("ak9PFCHSJets")
)


process.ak9PFCHSJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFCHSL2L3Corrector"),
    src = cms.InputTag("ak9PFCHSJets")
)


process.ak9PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFCHSL1FastjetCorrector", "ak9PFCHSL2RelativeCorrector", "ak9PFCHSL3AbsoluteCorrector", "ak9PFCHSResidualCorrector")
)


process.ak9PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFCHSL1OffsetCorrector", "ak9PFCHSL2RelativeCorrector", "ak9PFCHSL3AbsoluteCorrector", "ak9PFCHSResidualCorrector")
)


process.ak9PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak9PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFCHSL2RelativeCorrector", "ak9PFCHSL3AbsoluteCorrector")
)


process.ak9PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFCHSL2RelativeCorrector", "ak9PFCHSL3AbsoluteCorrector", "ak9PFCHSResidualCorrector")
)


process.ak9PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL1FastL2L3Corrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL1L2L3Corrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL2RelativeCorrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL2L3Corrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PFL2L3ResidualCorrector"),
    src = cms.InputTag("ak9PFJets")
)


process.ak9PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFL1FastjetCorrector", "ak9PFL2RelativeCorrector", "ak9PFL3AbsoluteCorrector", "ak9PFResidualCorrector")
)


process.ak9PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFL1OffsetCorrector", "ak9PFL2RelativeCorrector", "ak9PFL3AbsoluteCorrector", "ak9PFResidualCorrector")
)


process.ak9PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak9PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFL2RelativeCorrector", "ak9PFL3AbsoluteCorrector")
)


process.ak9PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PFL2RelativeCorrector", "ak9PFL3AbsoluteCorrector", "ak9PFResidualCorrector")
)


process.ak9PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PUPPIJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PUPPIL1FastjetCorrector"),
    src = cms.InputTag("ak9PUPPIJets")
)


process.ak9PUPPIJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PUPPIL1FastL2L3Corrector"),
    src = cms.InputTag("ak9PUPPIJets")
)


process.ak9PUPPIJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak9PUPPIL2L3Corrector"),
    src = cms.InputTag("ak9PUPPIJets")
)


process.ak9PUPPIL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PUPPIL1FastjetCorrector", "ak9PUPPIL2RelativeCorrector", "ak9PUPPIL3AbsoluteCorrector")
)


process.ak9PUPPIL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK9PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PUPPIL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak9PUPPIL2RelativeCorrector", "ak9PUPPIL3AbsoluteCorrector")
)


process.ak9PUPPIL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK9PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak9PUPPIL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK9PFPuppi'),
    level = cms.string('L3Absolute')
)


process.genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    excludeResonances = cms.bool(False),
    ignoreParticleIDs = cms.vuint32(
        1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39, 12, 14, 16
    ),
    partonicFinalState = cms.bool(False),
    src = cms.InputTag("packedGenParticles"),
    tausAsJets = cms.bool(False)
)


process.ic5CaloJetsL1 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector"),
    src = cms.InputTag("ic5CaloJets")
)


process.ic5CaloJetsL1FastL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL1FastL2L3Corrector"),
    src = cms.InputTag("iterativeCone5CaloJets")
)


process.ic5CaloJetsL1FastL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("iterativeCone5CaloJets")
)


process.ic5CaloJetsL1L2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL1L2L3Corrector"),
    src = cms.InputTag("iterativeCone5CaloJets")
)


process.ic5CaloJetsL1L2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL1L2L3L6Corrector"),
    src = cms.InputTag("ic5CaloJets")
)


process.ic5CaloJetsL1L2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL1L2L3ResidualCorrector"),
    src = cms.InputTag("iterativeCone5CaloJets")
)


process.ic5CaloJetsL2 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL2RelativeCorrector"),
    src = cms.InputTag("ic5CaloJets")
)


process.ic5CaloJetsL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL2L3Corrector"),
    src = cms.InputTag("iterativeCone5CaloJets")
)


process.ic5CaloJetsL2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL2L3L6Corrector"),
    src = cms.InputTag("ic5CaloJets")
)


process.ic5CaloJetsL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ic5CaloL2L3ResidualCorrector"),
    src = cms.InputTag("iterativeCone5CaloJets")
)


process.ic5CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector")
)


process.ic5CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL1OffsetCorrector", "ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector", "ic5CaloL6SLBCorrector")
)


process.ic5CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL1FastjetCorrector", "ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector", "ic5CaloResidualCorrector")
)


process.ic5CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL1OffsetCorrector", "ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector")
)


process.ic5CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL1OffsetCorrector", "ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector", "ic5CaloResidualCorrector")
)


process.ic5CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ic5CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector")
)


process.ic5CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector", "ic5CaloL6SLBCorrector")
)


process.ic5CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5CaloL2RelativeCorrector", "ic5CaloL3AbsoluteCorrector", "ic5CaloResidualCorrector")
)


process.ic5CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("ic5PFJets")
)


process.ic5PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL1FastL2L3Corrector"),
    src = cms.InputTag("iterativeCone5PFJets")
)


process.ic5PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("iterativeCone5PFJets")
)


process.ic5PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL1L2L3Corrector"),
    src = cms.InputTag("iterativeCone5PFJets")
)


process.ic5PFJetsL1L2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL1L2L3L6Corrector"),
    src = cms.InputTag("ic5PFJets")
)


process.ic5PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("iterativeCone5PFJets")
)


process.ic5PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL2RelativeCorrector"),
    src = cms.InputTag("ic5PFJets")
)


process.ic5PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL2L3Corrector"),
    src = cms.InputTag("iterativeCone5PFJets")
)


process.ic5PFJetsL2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL2L3L6Corrector"),
    src = cms.InputTag("ic5PFJets")
)


process.ic5PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ic5PFL2L3ResidualCorrector"),
    src = cms.InputTag("iterativeCone5PFJets")
)


process.ic5PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector")
)


process.ic5PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector", "ic5PFL6SLBCorrector")
)


process.ic5PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5PFL1FastjetCorrector", "ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector", "ic5PFResidualCorrector")
)


process.ic5PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5PFL1OffsetCorrector", "ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector")
)


process.ic5PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5PFL1OffsetCorrector", "ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector", "ic5PFResidualCorrector")
)


process.ic5PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ic5PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector")
)


process.ic5PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector", "ic5PFL6SLBCorrector")
)


process.ic5PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ic5PFL2RelativeCorrector", "ic5PFL3AbsoluteCorrector", "ic5PFResidualCorrector")
)


process.ic5PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.kt4CaloJetsL1 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL1FastL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL1FastL2L3Corrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL1FastL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL1L2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL1L2L3Corrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL1L2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL1L2L3L6Corrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL1L2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL1L2L3ResidualCorrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL2 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL2RelativeCorrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL2L3Corrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL2L3L6Corrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloJetsL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt4CaloL2L3ResidualCorrector"),
    src = cms.InputTag("kt4CaloJets")
)


process.kt4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector")
)


process.kt4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL1OffsetCorrector", "kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector", "kt4CaloL6SLBCorrector")
)


process.kt4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL1FastjetCorrector", "kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector", "kt4CaloResidualCorrector")
)


process.kt4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL1OffsetCorrector", "kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector")
)


process.kt4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL1OffsetCorrector", "kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector", "kt4CaloResidualCorrector")
)


process.kt4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.kt4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector")
)


process.kt4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector", "kt4CaloL6SLBCorrector")
)


process.kt4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4CaloL2RelativeCorrector", "kt4CaloL3AbsoluteCorrector", "kt4CaloResidualCorrector")
)


process.kt4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL1FastL2L3Corrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL1L2L3Corrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL1L2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL1L2L3L6Corrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL2RelativeCorrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL2L3Corrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL2L3L6Corrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt4PFL2L3ResidualCorrector"),
    src = cms.InputTag("kt4PFJets")
)


process.kt4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector")
)


process.kt4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector", "kt4PFL6SLBCorrector")
)


process.kt4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4PFL1FastjetCorrector", "kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector", "kt4PFResidualCorrector")
)


process.kt4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4PFL1OffsetCorrector", "kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector")
)


process.kt4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4PFL1OffsetCorrector", "kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector", "kt4PFResidualCorrector")
)


process.kt4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.kt4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector")
)


process.kt4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector", "kt4PFL6SLBCorrector")
)


process.kt4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt4PFL2RelativeCorrector", "kt4PFL3AbsoluteCorrector", "kt4PFResidualCorrector")
)


process.kt4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloJetsL1 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL1FastL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL1FastL2L3Corrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL1FastL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL1L2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL1L2L3Corrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL1L2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL1L2L3L6Corrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL1L2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL1L2L3ResidualCorrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL2 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL2RelativeCorrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL2L3 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL2L3Corrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL2L3L6 = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL2L3L6Corrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloJetsL2L3Residual = cms.EDProducer("CorrectedCaloJetProducer",
    correctors = cms.VInputTag("kt6CaloL2L3ResidualCorrector"),
    src = cms.InputTag("kt6CaloJets")
)


process.kt6CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector")
)


process.kt6CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL1OffsetCorrector", "kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector", "kt6CaloL6SLBCorrector")
)


process.kt6CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL1FastjetCorrector", "kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector", "kt6CaloResidualCorrector")
)


process.kt6CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL1OffsetCorrector", "kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector")
)


process.kt6CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL1OffsetCorrector", "kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector", "kt6CaloResidualCorrector")
)


process.kt6CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.kt6CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector")
)


process.kt6CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector", "kt6CaloL6SLBCorrector")
)


process.kt6CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6CaloL2RelativeCorrector", "kt6CaloL3AbsoluteCorrector", "kt6CaloResidualCorrector")
)


process.kt6CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.6),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.kt6PFJetsL1 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL1FastL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL1FastL2L3Corrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL1FastL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL1FastL2L3ResidualCorrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL1L2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL1L2L3Corrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL1L2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL1L2L3L6Corrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL1L2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL1L2L3ResidualCorrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL2 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL2RelativeCorrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL2L3 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL2L3Corrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL2L3L6 = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL2L3L6Corrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsL2L3Residual = cms.EDProducer("CorrectedPFJetProducer",
    correctors = cms.VInputTag("kt6PFL2L3ResidualCorrector"),
    src = cms.InputTag("kt6PFJets")
)


process.kt6PFJetsRhos = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.kt6PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector")
)


process.kt6PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector", "kt6PFL6SLBCorrector")
)


process.kt6PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6PFL1FastjetCorrector", "kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector", "kt6PFResidualCorrector")
)


process.kt6PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6PFL1OffsetCorrector", "kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector")
)


process.kt6PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6PFL1OffsetCorrector", "kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector", "kt6PFResidualCorrector")
)


process.kt6PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.kt6PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector")
)


process.kt6PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector", "kt6PFL6SLBCorrector")
)


process.kt6PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("kt6PFL2RelativeCorrector", "kt6PFL3AbsoluteCorrector", "kt6PFResidualCorrector")
)


process.kt6PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6PFchsJetsRhos = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    src = cms.InputTag("pfCHS"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME"),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.ak4pfGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4GenJetsNoNu")
)


process.ak4pfchsGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4GenJetsNoNu")
)


process.ak4pfchsl1l2l3PtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4PFCHSJetsL1FastL2L3")
)


process.ak4pfchsl1l2l3PtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4PFCHSJets")
)


process.ak4pfl1l2l3PtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4PFJetsL1FastL2L3")
)


process.ak4pfl1l2l3PtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4PFJets")
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.particleFlow = cms.EDFilter("CandPtrSelector",
    cut = cms.string(''),
    src = cms.InputTag("packedPFCandidates")
)


process.pfCHS = cms.EDFilter("CandPtrSelector",
    cut = cms.string('fromPV'),
    src = cms.InputTag("packedPFCandidates")
)


process.ak4pfchsl1l2l3 = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.25),
    deltaRPartonMax = cms.double(0.25),
    doComposition = cms.bool(False),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string('ak4PFCHSL1FastL2L3'),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("packedGenParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak4pfchsl1l2l3JetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("pfCHS"),
    srcRef = cms.InputTag("ak4pfchsGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak4pfchsl1l2l3JetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFchsJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.ak4pfl1l2l3 = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.25),
    deltaRPartonMax = cms.double(0.25),
    doComposition = cms.bool(False),
    doFlavor = cms.bool(False),
    doHLT = cms.bool(False),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string('ak4PFL1FastL2L3'),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcGenParticles = cms.InputTag("packedGenParticles"),
    srcJetToUncorJetMap = cms.InputTag("ak4pfl1l2l3JetToUncorJet","rec2gen"),
    srcPFCandidates = cms.InputTag("packedPFCandidates"),
    srcRef = cms.InputTag("ak4pfGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak4pfl1l2l3JetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag(""),
    srcRhos = cms.InputTag("kt6PFJetsRhos","rhos"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(100)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(False),
    fileName = cms.string('JRA.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(True),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerHardcodeGeometryEP = cms.ESProducer("CaloTowerHardcodeGeometryEP")


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorHardcodeGeometryEP = cms.ESProducer("CastorHardcodeGeometryEP")


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(True)
)


process.EcalBarrelGeometryEP = cms.ESProducer("EcalBarrelGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryEP = cms.ESProducer("EcalEndcapGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryEP = cms.ESProducer("EcalPreshowerGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalHardcodeGeometryEP = cms.ESProducer("HcalHardcodeGeometryEP",
    UseOldLoader = cms.bool(False)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcHardcodeGeometryEP = cms.ESProducer("ZdcHardcodeGeometryEP")


process.ak10PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Fastjet', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Offset', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute'
    )
)


process.ak10PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Fastjet', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual'
    )
)


process.ak10PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Offset', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual'
    )
)


process.ak10PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative', 
        'ak10PFL3Absolute'
    )
)


process.ak10PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual'
    )
)


process.ak10PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2L3Residual')
)


process.ak10PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PUPPIL1Fastjet', 
        'ak10PUPPIL2Relative', 
        'ak10PUPPIL3Absolute'
    )
)


process.ak10PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PUPPIL2Relative', 
        'ak10PUPPIL3Absolute'
    )
)


process.ak10PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak10PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Fastjet', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Offset', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute'
    )
)


process.ak1PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Fastjet', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual'
    )
)


process.ak1PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Offset', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual'
    )
)


process.ak1PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative', 
        'ak1PFL3Absolute'
    )
)


process.ak1PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual'
    )
)


process.ak1PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PUPPIL1Fastjet', 
        'ak1PUPPIL2Relative', 
        'ak1PUPPIL3Absolute'
    )
)


process.ak1PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PUPPIL2Relative', 
        'ak1PUPPIL3Absolute'
    )
)


process.ak1PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak1PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Fastjet', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Offset', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute'
    )
)


process.ak2PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Fastjet', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual'
    )
)


process.ak2PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Offset', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual'
    )
)


process.ak2PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative', 
        'ak2PFL3Absolute'
    )
)


process.ak2PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual'
    )
)


process.ak2PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PUPPIL1Fastjet', 
        'ak2PUPPIL2Relative', 
        'ak2PUPPIL3Absolute'
    )
)


process.ak2PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PUPPIL2Relative', 
        'ak2PUPPIL3Absolute'
    )
)


process.ak2PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak2PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Fastjet', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Offset', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute'
    )
)


process.ak3PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Fastjet', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual'
    )
)


process.ak3PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Offset', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual'
    )
)


process.ak3PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative', 
        'ak3PFL3Absolute'
    )
)


process.ak3PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual'
    )
)


process.ak3PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PUPPIL1Fastjet', 
        'ak3PUPPIL2Relative', 
        'ak3PUPPIL3Absolute'
    )
)


process.ak3PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PUPPIL2Relative', 
        'ak3PUPPIL3Absolute'
    )
)


process.ak3PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak3PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual'
    )
)


process.ak4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual'
    )
)


process.ak4JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual'
    )
)


process.ak4JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual'
    )
)


process.ak4JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Fastjet')
)


process.ak4L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB'
    )
)


process.ak4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual'
    )
)


process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual'
    )
)


process.ak4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative', 
        'ak4PFL3Absolute'
    )
)


process.ak4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB'
    )
)


process.ak4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual'
    )
)


process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PUPPIL1Fastjet', 
        'ak4PUPPIL2Relative', 
        'ak4PUPPIL3Absolute'
    )
)


process.ak4PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PUPPIL2Relative', 
        'ak4PUPPIL3Absolute'
    )
)


process.ak4PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4TrackL2Relative', 
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4TrackL2Relative', 
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Fastjet', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Offset', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute'
    )
)


process.ak5PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual'
    )
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual'
    )
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative', 
        'ak5PFL3Absolute'
    )
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual'
    )
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak5PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PUPPIL1Fastjet', 
        'ak5PUPPIL2Relative', 
        'ak5PUPPIL3Absolute'
    )
)


process.ak5PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PUPPIL2Relative', 
        'ak5PUPPIL3Absolute'
    )
)


process.ak5PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak5PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Fastjet', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Offset', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute'
    )
)


process.ak6PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Fastjet', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual'
    )
)


process.ak6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Offset', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual'
    )
)


process.ak6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative', 
        'ak6PFL3Absolute'
    )
)


process.ak6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual'
    )
)


process.ak6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PUPPIL1Fastjet', 
        'ak6PUPPIL2Relative', 
        'ak6PUPPIL3Absolute'
    )
)


process.ak6PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PUPPIL2Relative', 
        'ak6PUPPIL3Absolute'
    )
)


process.ak6PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak6PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual'
    )
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual'
    )
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual'
    )
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute'
    )
)


process.ak7L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Fastjet')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Offset')
)


process.ak7PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Offset', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB'
    )
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual'
    )
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual'
    )
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative', 
        'ak7PFL3Absolute'
    )
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB'
    )
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual'
    )
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2L3Residual')
)


process.ak7PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PUPPIL1Fastjet', 
        'ak7PUPPIL2Relative', 
        'ak7PUPPIL3Absolute'
    )
)


process.ak7PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PUPPIL2Relative', 
        'ak7PUPPIL3Absolute'
    )
)


process.ak7PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak7PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Fastjet', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute'
    )
)


process.ak8PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Fastjet', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Offset', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute'
    )
)


process.ak8PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Fastjet', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute'
    )
)


process.ak8PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Fastjet', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual'
    )
)


process.ak8PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Offset', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual'
    )
)


process.ak8PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative', 
        'ak8PFL3Absolute'
    )
)


process.ak8PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual'
    )
)


process.ak8PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PUPPIL1Fastjet', 
        'ak8PUPPIL2Relative', 
        'ak8PUPPIL3Absolute'
    )
)


process.ak8PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PUPPIL2Relative', 
        'ak8PUPPIL3Absolute'
    )
)


process.ak8PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak8PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Fastjet', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Offset', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute'
    )
)


process.ak9PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Fastjet', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual'
    )
)


process.ak9PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Offset', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual'
    )
)


process.ak9PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative', 
        'ak9PFL3Absolute'
    )
)


process.ak9PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual'
    )
)


process.ak9PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PUPPIL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PUPPIL1Fastjet', 
        'ak9PUPPIL2Relative', 
        'ak9PUPPIL3Absolute'
    )
)


process.ak9PUPPIL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PUPPIL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PUPPIL2Relative', 
        'ak9PUPPIL3Absolute'
    )
)


process.ak9PUPPIL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak9PUPPIL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFPuppi'),
    level = cms.string('L3Absolute')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalParameters = cms.ESProducer("HcalParametersESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual'
    )
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB'
    )
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual'
    )
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual'
    )
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative', 
        'ic5PFL3Absolute'
    )
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB'
    )
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual'
    )
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(True),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(True)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(True)
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual'
    )
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB'
    )
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual'
    )
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual'
    )
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative', 
        'kt4PFL3Absolute'
    )
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB'
    )
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual'
    )
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual'
    )
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB'
    )
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual'
    )
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual'
    )
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative', 
        'kt6PFL3Absolute'
    )
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB'
    )
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual'
    )
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2L3Residual')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(True)
)


process.trackerNumberingGeometry = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True)
)


process.trackerParameters = cms.ESProducer("TrackerParametersESModule",
    appendToDataLabel = cms.string('')
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('106X_mc2017_realistic_v6'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring( (
        'Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/cmsTracker.xml', 
        'Geometry/CMSCommonData/data/caloBase.xml', 
        'Geometry/CMSCommonData/data/cmsCalo.xml', 
        'Geometry/CMSCommonData/data/muonBase.xml', 
        'Geometry/CMSCommonData/data/cmsMuon.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/CMSCommonData/data/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/muonMB.xml', 
        'Geometry/CMSCommonData/data/muonMagnet.xml', 
        'Geometry/TrackerCommonData/data/trackerParameters.xml', 
        'Geometry/TrackerCommonData/data/pixfwdMaterials.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x2.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x3.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x4.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanelBase.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanel.xml', 
        'Geometry/TrackerCommonData/data/pixfwdBlade.xml', 
        'Geometry/TrackerCommonData/data/pixfwdNipple.xml', 
        'Geometry/TrackerCommonData/data/pixfwdDisk.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCylinder.xml', 
        'Geometry/TrackerCommonData/data/pixfwd.xml', 
        'Geometry/TrackerCommonData/data/pixbarmaterial.xml', 
        'Geometry/TrackerCommonData/data/pixbarladder.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderfull.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderhalf.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer0.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer1.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer2.xml', 
        'Geometry/TrackerCommonData/data/pixbar.xml', 
        'Geometry/TrackerCommonData/data/tibtidcommonmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmodpar.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0a.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0b.xml', 
        'Geometry/TrackerCommonData/data/tibmodule2.xml', 
        'Geometry/TrackerCommonData/data/tibstringpar.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring0lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring0.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring1lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring1.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring2lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring2.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring3lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring3.xml', 
        'Geometry/TrackerCommonData/data/tiblayerpar.xml', 
        'Geometry/TrackerCommonData/data/tiblayer0.xml', 
        'Geometry/TrackerCommonData/data/tiblayer1.xml', 
        'Geometry/TrackerCommonData/data/tiblayer2.xml', 
        'Geometry/TrackerCommonData/data/tiblayer3.xml', 
        'Geometry/TrackerCommonData/data/tib.xml', 
        'Geometry/TrackerCommonData/data/tidmaterial.xml', 
        'Geometry/TrackerCommonData/data/tidmodpar.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule2.xml', 
        'Geometry/TrackerCommonData/data/tidringpar.xml', 
        'Geometry/TrackerCommonData/data/tidring0.xml', 
        'Geometry/TrackerCommonData/data/tidring0f.xml', 
        'Geometry/TrackerCommonData/data/tidring0b.xml', 
        'Geometry/TrackerCommonData/data/tidring1.xml', 
        'Geometry/TrackerCommonData/data/tidring1f.xml', 
        'Geometry/TrackerCommonData/data/tidring1b.xml', 
        'Geometry/TrackerCommonData/data/tidring2.xml', 
        'Geometry/TrackerCommonData/data/tid.xml', 
        'Geometry/TrackerCommonData/data/tidf.xml', 
        'Geometry/TrackerCommonData/data/tidb.xml', 
        'Geometry/TrackerCommonData/data/tibtidservices.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesf.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesb.xml', 
        'Geometry/TrackerCommonData/data/tobmaterial.xml', 
        'Geometry/TrackerCommonData/data/tobmodpar.xml', 
        'Geometry/TrackerCommonData/data/tobmodule0.xml', 
        'Geometry/TrackerCommonData/data/tobmodule2.xml', 
        'Geometry/TrackerCommonData/data/tobmodule4.xml', 
        'Geometry/TrackerCommonData/data/tobrodpar.xml', 
        'Geometry/TrackerCommonData/data/tobrod0c.xml', 
        'Geometry/TrackerCommonData/data/tobrod0l.xml', 
        'Geometry/TrackerCommonData/data/tobrod0h.xml', 
        'Geometry/TrackerCommonData/data/tobrod0.xml', 
        'Geometry/TrackerCommonData/data/tobrod1l.xml', 
        'Geometry/TrackerCommonData/data/tobrod1h.xml', 
        'Geometry/TrackerCommonData/data/tobrod1.xml', 
        'Geometry/TrackerCommonData/data/tobrod2c.xml', 
        'Geometry/TrackerCommonData/data/tobrod2l.xml', 
        'Geometry/TrackerCommonData/data/tobrod2h.xml', 
        'Geometry/TrackerCommonData/data/tobrod2.xml', 
        'Geometry/TrackerCommonData/data/tobrod3l.xml', 
        'Geometry/TrackerCommonData/data/tobrod3h.xml', 
        'Geometry/TrackerCommonData/data/tobrod3.xml', 
        'Geometry/TrackerCommonData/data/tobrod4c.xml', 
        'Geometry/TrackerCommonData/data/tobrod4l.xml', 
        'Geometry/TrackerCommonData/data/tobrod4h.xml', 
        'Geometry/TrackerCommonData/data/tobrod4.xml', 
        'Geometry/TrackerCommonData/data/tobrod5l.xml', 
        'Geometry/TrackerCommonData/data/tobrod5h.xml', 
        'Geometry/TrackerCommonData/data/tobrod5.xml', 
        'Geometry/TrackerCommonData/data/tob.xml', 
        'Geometry/TrackerCommonData/data/tecmaterial.xml', 
        'Geometry/TrackerCommonData/data/tecmodpar.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule2.xml', 
        'Geometry/TrackerCommonData/data/tecmodule3.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule5.xml', 
        'Geometry/TrackerCommonData/data/tecmodule6.xml', 
        'Geometry/TrackerCommonData/data/tecpetpar.xml', 
        'Geometry/TrackerCommonData/data/tecring0.xml', 
        'Geometry/TrackerCommonData/data/tecring1.xml', 
        'Geometry/TrackerCommonData/data/tecring2.xml', 
        'Geometry/TrackerCommonData/data/tecring3.xml', 
        'Geometry/TrackerCommonData/data/tecring4.xml', 
        'Geometry/TrackerCommonData/data/tecring5.xml', 
        'Geometry/TrackerCommonData/data/tecring6.xml', 
        'Geometry/TrackerCommonData/data/tecring0f.xml', 
        'Geometry/TrackerCommonData/data/tecring1f.xml', 
        'Geometry/TrackerCommonData/data/tecring2f.xml', 
        'Geometry/TrackerCommonData/data/tecring3f.xml', 
        'Geometry/TrackerCommonData/data/tecring4f.xml', 
        'Geometry/TrackerCommonData/data/tecring5f.xml', 
        'Geometry/TrackerCommonData/data/tecring6f.xml', 
        'Geometry/TrackerCommonData/data/tecring0b.xml', 
        'Geometry/TrackerCommonData/data/tecring1b.xml', 
        'Geometry/TrackerCommonData/data/tecring2b.xml', 
        'Geometry/TrackerCommonData/data/tecring3b.xml', 
        'Geometry/TrackerCommonData/data/tecring4b.xml', 
        'Geometry/TrackerCommonData/data/tecring5b.xml', 
        'Geometry/TrackerCommonData/data/tecring6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetalf.xml', 
        'Geometry/TrackerCommonData/data/tecpetalb.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8b.xml', 
        'Geometry/TrackerCommonData/data/tecwheel.xml', 
        'Geometry/TrackerCommonData/data/tecwheela.xml', 
        'Geometry/TrackerCommonData/data/tecwheelb.xml', 
        'Geometry/TrackerCommonData/data/tecwheelc.xml', 
        'Geometry/TrackerCommonData/data/tecwheeld.xml', 
        'Geometry/TrackerCommonData/data/tecwheel6.xml', 
        'Geometry/TrackerCommonData/data/tecservices.xml', 
        'Geometry/TrackerCommonData/data/tecbackplate.xml', 
        'Geometry/TrackerCommonData/data/tec.xml', 
        'Geometry/TrackerCommonData/data/trackermaterial.xml', 
        'Geometry/TrackerCommonData/data/tracker.xml', 
        'Geometry/TrackerCommonData/data/trackerpixbar.xml', 
        'Geometry/TrackerCommonData/data/trackerpixfwd.xml', 
        'Geometry/TrackerCommonData/data/trackertibtidservices.xml', 
        'Geometry/TrackerCommonData/data/trackertib.xml', 
        'Geometry/TrackerCommonData/data/trackertid.xml', 
        'Geometry/TrackerCommonData/data/trackertob.xml', 
        'Geometry/TrackerCommonData/data/trackertec.xml', 
        'Geometry/TrackerCommonData/data/trackerbulkhead.xml', 
        'Geometry/TrackerCommonData/data/trackerother.xml', 
        'Geometry/EcalCommonData/data/eregalgo.xml', 
        'Geometry/EcalCommonData/data/ebalgo.xml', 
        'Geometry/EcalCommonData/data/ebcon.xml', 
        'Geometry/EcalCommonData/data/ebrot.xml', 
        'Geometry/EcalCommonData/data/eecon.xml', 
        'Geometry/EcalCommonData/data/eefixed.xml', 
        'Geometry/EcalCommonData/data/eehier.xml', 
        'Geometry/EcalCommonData/data/eealgo.xml', 
        'Geometry/EcalCommonData/data/escon.xml', 
        'Geometry/EcalCommonData/data/esalgo.xml', 
        'Geometry/EcalCommonData/data/eeF.xml', 
        'Geometry/EcalCommonData/data/eeB.xml', 
        'Geometry/EcalCommonData/data/ectkcable.xml', 
        'Geometry/HcalCommonData/data/hcalrotations.xml', 
        'Geometry/HcalCommonData/data/hcalalgo.xml', 
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml', 
        'Geometry/HcalCommonData/data/hcalendcapalgo.xml', 
        'Geometry/HcalCommonData/data/hcalouteralgo.xml', 
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml', 
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml', 
        'Geometry/HcalCommonData/data/hcalSimNumbering.xml', 
        'Geometry/HcalCommonData/data/hcalRecNumbering.xml', 
        'Geometry/MuonCommonData/data/mbCommon.xml', 
        'Geometry/MuonCommonData/data/mb1.xml', 
        'Geometry/MuonCommonData/data/mb2.xml', 
        'Geometry/MuonCommonData/data/mb3.xml', 
        'Geometry/MuonCommonData/data/mb4.xml', 
        'Geometry/MuonCommonData/data/muonYoke.xml', 
        'Geometry/MuonCommonData/data/mf.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/bundle/forwardshield.xml', 
        'Geometry/ForwardCommonData/data/brmrotations.xml', 
        'Geometry/ForwardCommonData/data/brm.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/MuonCommonData/data/muonNumbering.xml', 
        'Geometry/TrackerCommonData/data/trackerStructureTopology.xml', 
        'Geometry/TrackerSimData/data/trackersens.xml', 
        'Geometry/TrackerRecoData/data/trackerRecoMaterial.xml', 
        'Geometry/EcalSimData/data/ecalsens.xml', 
        'Geometry/HcalCommonData/data/hcalsenspmf.xml', 
        'Geometry/HcalSimData/data/hf.xml', 
        'Geometry/HcalSimData/data/hfpmt.xml', 
        'Geometry/HcalSimData/data/hffibrebundle.xml', 
        'Geometry/HcalSimData/data/CaloUtil.xml', 
        'Geometry/MuonSimData/data/muonSens.xml', 
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml', 
        'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml', 
        'Geometry/ForwardCommonData/data/brmsens.xml', 
        'Geometry/HcalSimData/data/HcalProdCuts.xml', 
        'Geometry/EcalSimData/data/EcalProdCuts.xml', 
        'Geometry/EcalSimData/data/ESProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml', 
        'Geometry/MuonSimData/data/muonProdCuts.xml', 
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml', 
        'Geometry/CMSCommonData/data/FieldParameters.xml'
     ) ),
    rootNodeName = cms.string('cms:OCMS')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.jec = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('sqlite_file:UL2017_V1_SimpleL1_MC.db'),
    toGet = cms.VPSet(
        cms.PSet(
            label = cms.untracked.string('AK4PF'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_UL2017_V1_SimpleL1_MC_AK4PF')
        ), 
        cms.PSet(
            label = cms.untracked.string('AK4PFchs'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_UL2017_V1_SimpleL1_MC_AK4PFchs')
        )
    )
)


process.prefer("es_hardcode")

process.prefer("jec")

process.ak8PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak8PFCHSL1L2L3ResidualCorrector, process.ak8PFCHSL1OffsetCorrector, process.ak8PFCHSL2RelativeCorrector, process.ak8PFCHSL3AbsoluteCorrector, process.ak8PFCHSResidualCorrector)


process.ak2PFL2L3CorrectorTask = cms.Task(process.ak2PFL2L3Corrector, process.ak2PFL2RelativeCorrector, process.ak2PFL3AbsoluteCorrector)


process.ic5PFL2L3L6CorrectorTask = cms.Task(process.ic5PFL2L3L6Corrector, process.ic5PFL6SLBCorrector, process.kt4PFL2L3Corrector)


process.ak6PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak6PFL1L2L3ResidualCorrector, process.ak6PFL1OffsetCorrector, process.ak6PFL2RelativeCorrector, process.ak6PFL3AbsoluteCorrector, process.ak6PFResidualCorrector)


process.ak3PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak3PFCHSL2L3ResidualCorrector, process.ak3PFCHSL2RelativeCorrector, process.ak3PFCHSL3AbsoluteCorrector, process.ak3PFCHSResidualCorrector)


process.ak7CaloL2L3ResidualCorrectorTask = cms.Task(process.ak7CaloL2L3ResidualCorrector, process.ak7CaloL2RelativeCorrector, process.ak7CaloL3AbsoluteCorrector, process.ak7CaloResidualCorrector)


process.ak9PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak9PFCHSL1L2L3ResidualCorrector, process.ak9PFCHSL1OffsetCorrector, process.ak9PFCHSL2RelativeCorrector, process.ak9PFCHSL3AbsoluteCorrector, process.ak9PFCHSResidualCorrector)


process.ak6PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak6PFCHSL2L3ResidualCorrector, process.ak6PFCHSL2RelativeCorrector, process.ak6PFCHSL3AbsoluteCorrector, process.ak6PFCHSResidualCorrector)


process.ak6PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak6PFL1FastjetCorrector, process.ak6PFL1FastjetL2L3ResidualCorrector, process.ak6PFL2RelativeCorrector, process.ak6PFL3AbsoluteCorrector, process.ak6PFResidualCorrector)


process.kt4PFL2L3CorrectorTask = cms.Task(process.kt4PFL2L3Corrector, process.kt4PFL2RelativeCorrector, process.kt4PFL3AbsoluteCorrector)


process.ak9PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak9PFCHSL2L3ResidualCorrector, process.ak9PFCHSL2RelativeCorrector, process.ak9PFCHSL3AbsoluteCorrector, process.ak9PFCHSResidualCorrector)


process.ak4PFL1L2L3CorrectorTask = cms.Task(process.ak4PFL1L2L3Corrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak2PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak2PFL1L2L3ResidualCorrector, process.ak2PFL1OffsetCorrector, process.ak2PFL2RelativeCorrector, process.ak2PFL3AbsoluteCorrector, process.ak2PFResidualCorrector)


process.ak7PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak7PFL1L2L3ResidualCorrector, process.ak7PFL1OffsetCorrector, process.ak7PFL2RelativeCorrector, process.ak7PFL3AbsoluteCorrector, process.ak7PFResidualCorrector)


process.ak9PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak9PFL1FastjetCorrector, process.ak9PFL1FastjetL2L3ResidualCorrector, process.ak9PFL2RelativeCorrector, process.ak9PFL3AbsoluteCorrector, process.ak9PFResidualCorrector)


process.ak2PFCHSL2L3CorrectorTask = cms.Task(process.ak2PFCHSL2L3Corrector, process.ak2PFCHSL2RelativeCorrector, process.ak2PFCHSL3AbsoluteCorrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3ResidualCorrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastL2L3Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4TrackL2L3CorrectorTask = cms.Task(process.ak4TrackL2L3Corrector, process.ak4TrackL2RelativeCorrector, process.ak4TrackL3AbsoluteCorrector)


process.ak7CaloL1L2L3CorrectorTask = cms.Task(process.ak7CaloL1L2L3Corrector, process.ak7CaloL1OffsetCorrector, process.ak7CaloL2RelativeCorrector, process.ak7CaloL3AbsoluteCorrector)


process.kt6PFL1FastL2L3L6CorrectorTask = cms.Task(process.kt4PFL1FastL2L3Corrector, process.kt6PFL1FastL2L3L6Corrector, process.kt6PFL6SLBCorrector)


process.ak1PFCHSL2L3CorrectorTask = cms.Task(process.ak1PFCHSL2L3Corrector, process.ak1PFCHSL2RelativeCorrector, process.ak1PFCHSL3AbsoluteCorrector)


process.kt6CaloL2L3CorrectorTask = cms.Task(process.kt6CaloL2L3Corrector, process.kt6CaloL2RelativeCorrector, process.kt6CaloL3AbsoluteCorrector)


process.kt4CaloL2L3L6CorrectorTask = cms.Task(process.ak7CaloL2L3Corrector, process.kt4CaloL2L3L6Corrector, process.kt4CaloL6SLBCorrector)


process.ak3PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak3PFCHSL1L2L3ResidualCorrector, process.ak3PFCHSL1OffsetCorrector, process.ak3PFCHSL2RelativeCorrector, process.ak3PFCHSL3AbsoluteCorrector, process.ak3PFCHSResidualCorrector)


process.ak10PFL2L3ResidualCorrectorTask = cms.Task(process.ak10PFL2L3ResidualCorrector, process.ak10PFL2RelativeCorrector, process.ak10PFL3AbsoluteCorrector, process.ak10PFResidualCorrector)


process.kt4CaloL1L2L3ResidualCorrectorTask = cms.Task(process.kt4CaloL1L2L3ResidualCorrector, process.kt4CaloL1OffsetCorrector, process.kt4CaloL2RelativeCorrector, process.kt4CaloL3AbsoluteCorrector, process.kt4CaloResidualCorrector)


process.ak6PFCHSL2L3CorrectorTask = cms.Task(process.ak6PFCHSL2L3Corrector, process.ak6PFCHSL2RelativeCorrector, process.ak6PFCHSL3AbsoluteCorrector)


process.ic5PFL1FastL2L3L6CorrectorTask = cms.Task(process.ic5PFL1FastL2L3L6Corrector, process.ic5PFL6SLBCorrector, process.kt4PFL1FastL2L3Corrector)


process.ak9PFL2L3ResidualCorrectorTask = cms.Task(process.ak9PFL2L3ResidualCorrector, process.ak9PFL2RelativeCorrector, process.ak9PFL3AbsoluteCorrector, process.ak9PFResidualCorrector)


process.ic5CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ic5CaloL1FastL2L3Corrector, process.ic5CaloL2RelativeCorrector, process.ic5CaloL3AbsoluteCorrector)


process.ak4PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1L2L3ResidualCorrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak7PFL1L2L3CorrectorTask = cms.Task(process.ak7PFL1L2L3Corrector, process.ak7PFL1OffsetCorrector, process.ak7PFL2RelativeCorrector, process.ak7PFL3AbsoluteCorrector)


process.kt6CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.kt6CaloL1FastL2L3Corrector, process.kt6CaloL2RelativeCorrector, process.kt6CaloL3AbsoluteCorrector)


process.ak5PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak5PFCHSL1L2L3ResidualCorrector, process.ak5PFCHSL1OffsetCorrector, process.ak5PFCHSL2RelativeCorrector, process.ak5PFCHSL3AbsoluteCorrector, process.ak5PFCHSResidualCorrector)


process.ic5CaloL2L3CorrectorTask = cms.Task(process.ic5CaloL2L3Corrector, process.ic5CaloL2RelativeCorrector, process.ic5CaloL3AbsoluteCorrector)


process.ak7CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak7CaloL1FastL2L3ResidualCorrector, process.ak7CaloL1FastjetCorrector, process.ak7CaloL2RelativeCorrector, process.ak7CaloL3AbsoluteCorrector, process.ak7CaloResidualCorrector)


process.kt4CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.kt4CaloL1FastL2L3Corrector, process.kt4CaloL2RelativeCorrector, process.kt4CaloL3AbsoluteCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1L2L3ResidualCorrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFPuppiL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL2L3ResidualCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL2L3Corrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3ResidualCorrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak7PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastjetCorrector, process.ak7PFL1FastL2L3Corrector, process.ak7PFL2RelativeCorrector, process.ak7PFL3AbsoluteCorrector)


process.ak4CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3L6Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak2PFL2L3ResidualCorrectorTask = cms.Task(process.ak2PFL2L3ResidualCorrector, process.ak2PFL2RelativeCorrector, process.ak2PFL3AbsoluteCorrector, process.ak2PFResidualCorrector)


process.kt4PFL1L2L3ResidualCorrectorTask = cms.Task(process.kt4PFL1L2L3ResidualCorrector, process.kt4PFL1OffsetCorrector, process.kt4PFL2RelativeCorrector, process.kt4PFL3AbsoluteCorrector, process.kt4PFResidualCorrector)


process.ak9PFCHSL2L3CorrectorTask = cms.Task(process.ak9PFCHSL2L3Corrector, process.ak9PFCHSL2RelativeCorrector, process.ak9PFCHSL3AbsoluteCorrector)


process.kt6PFL1L2L3ResidualCorrectorTask = cms.Task(process.kt6PFL1L2L3ResidualCorrector, process.kt6PFL1OffsetCorrector, process.kt6PFL2RelativeCorrector, process.kt6PFL3AbsoluteCorrector, process.kt6PFResidualCorrector)


process.ak8PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak8PFCHSL1FastjetCorrector, process.ak8PFCHSL1FastjetL2L3ResidualCorrector, process.ak8PFCHSL2RelativeCorrector, process.ak8PFCHSL3AbsoluteCorrector, process.ak8PFCHSResidualCorrector)


process.kt4PFL1L2L3CorrectorTask = cms.Task(process.kt4PFL1L2L3Corrector, process.kt4PFL1OffsetCorrector, process.kt4PFL2RelativeCorrector, process.kt4PFL3AbsoluteCorrector)


process.ic5CaloL2L3ResidualCorrectorTask = cms.Task(process.ic5CaloL2L3ResidualCorrector, process.ic5CaloL2RelativeCorrector, process.ic5CaloL3AbsoluteCorrector, process.ic5CaloResidualCorrector)


process.ak4PFL2L3L6CorrectorTask = cms.Task(process.ak4PFL2L3L6Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak7L1JPTOffsetCorrectorTask = cms.Task(process.ak7CaloL1OffsetCorrector, process.ak7L1JPTOffsetCorrector)


process.kt4PFL2L3ResidualCorrectorTask = cms.Task(process.kt4PFL2L3ResidualCorrector, process.kt4PFL2RelativeCorrector, process.kt4PFL3AbsoluteCorrector, process.kt4PFResidualCorrector)


process.ak4PFPuppiL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3ResidualCorrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4L1JPTOffsetCorrectorTask = cms.Task(process.ak4CaloL1OffsetCorrector, process.ak4L1JPTOffsetCorrector)


process.kt6PFL2L3CorrectorTask = cms.Task(process.kt6PFL2L3Corrector, process.kt6PFL2RelativeCorrector, process.kt6PFL3AbsoluteCorrector)


process.ak3PFL2L3CorrectorTask = cms.Task(process.ak3PFL2L3Corrector, process.ak3PFL2RelativeCorrector, process.ak3PFL3AbsoluteCorrector)


process.kt6PFL2L3L6CorrectorTask = cms.Task(process.kt4PFL2L3Corrector, process.kt6PFL2L3L6Corrector, process.kt6PFL6SLBCorrector)


process.ic5PFL2L3CorrectorTask = cms.Task(process.ic5PFL2L3Corrector, process.ic5PFL2RelativeCorrector, process.ic5PFL3AbsoluteCorrector)


process.ak8PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak8PFL1L2L3ResidualCorrector, process.ak8PFL1OffsetCorrector, process.ak8PFL2RelativeCorrector, process.ak8PFL3AbsoluteCorrector, process.ak8PFResidualCorrector)


process.ak7PFL2L3CorrectorTask = cms.Task(process.ak7PFL2L3Corrector, process.ak7PFL2RelativeCorrector, process.ak7PFL3AbsoluteCorrector)


process.ak10PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak10PFL1L2L3ResidualCorrector, process.ak10PFL1OffsetCorrector, process.ak10PFL2RelativeCorrector, process.ak10PFL3AbsoluteCorrector, process.ak10PFResidualCorrector)


process.ak7PFCHSL2L3CorrectorTask = cms.Task(process.ak7PFCHSL2L3Corrector, process.ak7PFCHSL2RelativeCorrector, process.ak7PFCHSL3AbsoluteCorrector)


process.ak5PFL2L3CorrectorTask = cms.Task(process.ak5PFL2L3Corrector, process.ak5PFL2RelativeCorrector, process.ak5PFL3AbsoluteCorrector)


process.ak7PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak7PFL1FastjetCorrector, process.ak7PFL1FastjetL2L3ResidualCorrector, process.ak7PFL2RelativeCorrector, process.ak7PFL3AbsoluteCorrector, process.ak7PFResidualCorrector)


process.ak4L1JPTFastjetCorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ak4L1JPTFastjetCorrector)


process.ak7PFCHSL1FastL2L3CorrectorTask = cms.Task(process.ak4PFCHSL1FastjetCorrector, process.ak7PFCHSL1FastL2L3Corrector, process.ak7PFCHSL2RelativeCorrector, process.ak7PFCHSL3AbsoluteCorrector)


process.kt4CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak7CaloL1L2L3Corrector, process.kt4CaloL1FastL2L3L6Corrector, process.kt4CaloL6SLBCorrector)


process.ak4JPTL2L3CorrectorTask = cms.Task(process.ak4JPTL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ic5CaloL1L2L3ResidualCorrectorTask = cms.Task(process.ic5CaloL1L2L3ResidualCorrector, process.ic5CaloL1OffsetCorrector, process.ic5CaloL2RelativeCorrector, process.ic5CaloL3AbsoluteCorrector, process.ic5CaloResidualCorrector)


process.ak10PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak10PFCHSL1L2L3ResidualCorrector, process.ak10PFCHSL1OffsetCorrector, process.ak10PFCHSL2RelativeCorrector, process.ak10PFCHSL3AbsoluteCorrector, process.ak10PFCHSResidualCorrector)


process.ak10PFCHSL2L3CorrectorTask = cms.Task(process.ak10PFCHSL2L3Corrector, process.ak10PFCHSL2RelativeCorrector, process.ak10PFCHSL3AbsoluteCorrector)


process.ak8PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak8PFL1FastjetCorrector, process.ak8PFL1FastjetL2L3ResidualCorrector, process.ak8PFL2RelativeCorrector, process.ak8PFL3AbsoluteCorrector, process.ak8PFResidualCorrector)


process.ak5PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak5PFCHSL2L3ResidualCorrector, process.ak5PFCHSL2RelativeCorrector, process.ak5PFCHSL3AbsoluteCorrector, process.ak5PFCHSResidualCorrector)


process.ak2PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak2PFCHSL1L2L3ResidualCorrector, process.ak2PFCHSL1OffsetCorrector, process.ak2PFCHSL2RelativeCorrector, process.ak2PFCHSL3AbsoluteCorrector, process.ak2PFCHSResidualCorrector)


process.ak4TrackL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ak4TrackL1FastL2L3Corrector, process.ak4TrackL2RelativeCorrector, process.ak4TrackL3AbsoluteCorrector)


process.ak4PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1FastL2L3ResidualCorrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak3PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak3PFCHSL1FastjetCorrector, process.ak3PFCHSL1FastjetL2L3ResidualCorrector, process.ak3PFCHSL2RelativeCorrector, process.ak3PFCHSL3AbsoluteCorrector, process.ak3PFCHSResidualCorrector)


process.ak8PFCHSL2L3CorrectorTask = cms.Task(process.ak8PFCHSL2L3Corrector, process.ak8PFCHSL2RelativeCorrector, process.ak8PFCHSL3AbsoluteCorrector)


process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.ak1PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak1PFCHSL1L2L3ResidualCorrector, process.ak1PFCHSL1OffsetCorrector, process.ak1PFCHSL2RelativeCorrector, process.ak1PFCHSL3AbsoluteCorrector, process.ak1PFCHSResidualCorrector)


process.kt6CaloL2L3L6CorrectorTask = cms.Task(process.ak7CaloL2L3Corrector, process.kt6CaloL2L3L6Corrector, process.kt6CaloL6SLBCorrector)


process.kt4CaloL1L2L3CorrectorTask = cms.Task(process.kt4CaloL1L2L3Corrector, process.kt4CaloL1OffsetCorrector, process.kt4CaloL2RelativeCorrector, process.kt4CaloL3AbsoluteCorrector)


process.ic5PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastjetCorrector, process.ic5PFL1FastL2L3Corrector, process.ic5PFL2RelativeCorrector, process.ic5PFL3AbsoluteCorrector)


process.kt6PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastjetCorrector, process.kt6PFL1FastL2L3Corrector, process.kt6PFL2RelativeCorrector, process.kt6PFL3AbsoluteCorrector)


process.kt6PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.kt6PFL1FastL2L3ResidualCorrector, process.kt6PFL1FastjetCorrector, process.kt6PFL2RelativeCorrector, process.kt6PFL3AbsoluteCorrector, process.kt6PFResidualCorrector)


process.ak7PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak7PFCHSL1L2L3ResidualCorrector, process.ak7PFCHSL1OffsetCorrector, process.ak7PFCHSL2RelativeCorrector, process.ak7PFCHSL3AbsoluteCorrector, process.ak7PFCHSResidualCorrector)


process.kt4CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.kt4CaloL1FastL2L3ResidualCorrector, process.kt4CaloL1FastjetCorrector, process.kt4CaloL2RelativeCorrector, process.kt4CaloL3AbsoluteCorrector, process.kt4CaloResidualCorrector)


process.ic5PFL1L2L3CorrectorTask = cms.Task(process.ic5PFL1L2L3Corrector, process.ic5PFL1OffsetCorrector, process.ic5PFL2RelativeCorrector, process.ic5PFL3AbsoluteCorrector)


process.ak4PFL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL2L3ResidualCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak5PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak5PFCHSL1FastjetCorrector, process.ak5PFCHSL1FastjetL2L3ResidualCorrector, process.ak5PFCHSL2RelativeCorrector, process.ak5PFCHSL3AbsoluteCorrector, process.ak5PFCHSResidualCorrector)


process.kt4PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastjetCorrector, process.kt4PFL1FastL2L3Corrector, process.kt4PFL2RelativeCorrector, process.kt4PFL3AbsoluteCorrector)


process.ak3PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak3PFL1L2L3ResidualCorrector, process.ak3PFL1OffsetCorrector, process.ak3PFL2RelativeCorrector, process.ak3PFL3AbsoluteCorrector, process.ak3PFResidualCorrector)


process.ak4CaloL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL2L3ResidualCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak1PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak1PFL1L2L3ResidualCorrector, process.ak1PFL1OffsetCorrector, process.ak1PFL2RelativeCorrector, process.ak1PFL3AbsoluteCorrector, process.ak1PFResidualCorrector)


process.ak3PFL2L3ResidualCorrectorTask = cms.Task(process.ak3PFL2L3ResidualCorrector, process.ak3PFL2RelativeCorrector, process.ak3PFL3AbsoluteCorrector, process.ak3PFResidualCorrector)


process.ak9PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak9PFCHSL1FastjetCorrector, process.ak9PFCHSL1FastjetL2L3ResidualCorrector, process.ak9PFCHSL2RelativeCorrector, process.ak9PFCHSL3AbsoluteCorrector, process.ak9PFCHSResidualCorrector)


process.ak9PFL2L3CorrectorTask = cms.Task(process.ak9PFL2L3Corrector, process.ak9PFL2RelativeCorrector, process.ak9PFL3AbsoluteCorrector)


process.ak4JPTL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1FastL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.kt6CaloL1L2L3CorrectorTask = cms.Task(process.kt6CaloL1L2L3Corrector, process.kt6CaloL1OffsetCorrector, process.kt6CaloL2RelativeCorrector, process.kt6CaloL3AbsoluteCorrector)


process.ak1PFL2L3CorrectorTask = cms.Task(process.ak1PFL2L3Corrector, process.ak1PFL2RelativeCorrector, process.ak1PFL3AbsoluteCorrector)


process.kt4PFL1FastL2L3L6CorrectorTask = cms.Task(process.kt4PFL1FastL2L3Corrector, process.kt4PFL1FastL2L3L6Corrector, process.kt4PFL6SLBCorrector)


process.ak4CaloL1L2L3CorrectorTask = cms.Task(process.ak4CaloL1L2L3Corrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.kt6CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.kt6CaloL1FastL2L3ResidualCorrector, process.kt6CaloL1FastjetCorrector, process.kt6CaloL2RelativeCorrector, process.kt6CaloL3AbsoluteCorrector, process.kt6CaloResidualCorrector)


process.ak8PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak8PFCHSL2L3ResidualCorrector, process.ak8PFCHSL2RelativeCorrector, process.ak8PFCHSL3AbsoluteCorrector, process.ak8PFCHSResidualCorrector)


process.ic5CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak7CaloL1L2L3Corrector, process.ic5CaloL1FastL2L3L6Corrector, process.ic5CaloL6SLBCorrector)


process.ak7PFL2L3ResidualCorrectorTask = cms.Task(process.ak7PFL2L3ResidualCorrector, process.ak7PFL2RelativeCorrector, process.ak7PFL3AbsoluteCorrector, process.ak7PFResidualCorrector)


process.ak2PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak2PFCHSL1FastjetCorrector, process.ak2PFCHSL1FastjetL2L3ResidualCorrector, process.ak2PFCHSL2RelativeCorrector, process.ak2PFCHSL3AbsoluteCorrector, process.ak2PFCHSResidualCorrector)


process.ic5PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.ic5PFL1FastL2L3ResidualCorrector, process.ic5PFL1FastjetCorrector, process.ic5PFL2RelativeCorrector, process.ic5PFL3AbsoluteCorrector, process.ic5PFResidualCorrector)


process.ak5PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak5PFL1FastjetCorrector, process.ak5PFL1FastjetL2L3ResidualCorrector, process.ak5PFL2RelativeCorrector, process.ak5PFL3AbsoluteCorrector, process.ak5PFResidualCorrector)


process.kt4PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.kt4PFL1FastL2L3ResidualCorrector, process.kt4PFL1FastjetCorrector, process.kt4PFL2RelativeCorrector, process.kt4PFL3AbsoluteCorrector, process.kt4PFResidualCorrector)


process.ak7CaloL2L3CorrectorTask = cms.Task(process.ak7CaloL2L3Corrector, process.ak7CaloL2RelativeCorrector, process.ak7CaloL3AbsoluteCorrector)


process.ak4PFPuppiL1L2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3Corrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak7CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak7CaloL1FastL2L3L6Corrector, process.ak7CaloL1L2L3Corrector, process.ak7CaloL6SLBCorrector)


process.ak5PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak5PFL1L2L3ResidualCorrector, process.ak5PFL1OffsetCorrector, process.ak5PFL2RelativeCorrector, process.ak5PFL3AbsoluteCorrector, process.ak5PFResidualCorrector)


process.kt6CaloL1L2L3ResidualCorrectorTask = cms.Task(process.kt6CaloL1L2L3ResidualCorrector, process.kt6CaloL1OffsetCorrector, process.kt6CaloL2RelativeCorrector, process.kt6CaloL3AbsoluteCorrector, process.kt6CaloResidualCorrector)


process.ak3PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak3PFL1FastjetCorrector, process.ak3PFL1FastjetL2L3ResidualCorrector, process.ak3PFL2RelativeCorrector, process.ak3PFL3AbsoluteCorrector, process.ak3PFResidualCorrector)


process.ic5CaloL2L3L6CorrectorTask = cms.Task(process.ak7CaloL2L3Corrector, process.ic5CaloL2L3L6Corrector, process.ic5CaloL6SLBCorrector)


process.ak2PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak2PFL1FastjetCorrector, process.ak2PFL1FastjetL2L3ResidualCorrector, process.ak2PFL2RelativeCorrector, process.ak2PFL3AbsoluteCorrector, process.ak2PFResidualCorrector)


process.ak7PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak7PFCHSL1FastjetCorrector, process.ak7PFCHSL1FastjetL2L3ResidualCorrector, process.ak7PFCHSL2RelativeCorrector, process.ak7PFCHSL3AbsoluteCorrector, process.ak7PFCHSResidualCorrector)


process.kt6CaloL2L3ResidualCorrectorTask = cms.Task(process.kt6CaloL2L3ResidualCorrector, process.kt6CaloL2RelativeCorrector, process.kt6CaloL3AbsoluteCorrector, process.kt6CaloResidualCorrector)


process.ak4CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1FastL2L3ResidualCorrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4PFCHSL1FastL2L3CorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3Corrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4CaloL2L3CorrectorTask = cms.Task(process.ak4CaloL2L3Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.kt4CaloL2L3ResidualCorrectorTask = cms.Task(process.kt4CaloL2L3ResidualCorrector, process.kt4CaloL2RelativeCorrector, process.kt4CaloL3AbsoluteCorrector, process.kt4CaloResidualCorrector)


process.ak4JPTL1L2L3CorrectorTask = cms.Task(process.ak4JPTL1L2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4PFCHSL2L3CorrectorTask = cms.Task(process.ak4PFCHSL2L3Corrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak5PFCHSL2L3CorrectorTask = cms.Task(process.ak5PFCHSL2L3Corrector, process.ak5PFCHSL2RelativeCorrector, process.ak5PFCHSL3AbsoluteCorrector)


process.ak4PFL1FastL2L3L6CorrectorTask = cms.Task(process.ak4PFL1FastL2L3L6Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak1PFL2L3ResidualCorrectorTask = cms.Task(process.ak1PFL2L3ResidualCorrector, process.ak1PFL2RelativeCorrector, process.ak1PFL3AbsoluteCorrector, process.ak1PFResidualCorrector)


process.ak4JPTL1FastL2L3CorrectorTask = cms.Task(process.ak4JPTL1FastL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ic5CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.ic5CaloL1FastL2L3ResidualCorrector, process.ic5CaloL1FastjetCorrector, process.ic5CaloL2RelativeCorrector, process.ic5CaloL3AbsoluteCorrector, process.ic5CaloResidualCorrector)


process.kt6CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak7CaloL1L2L3Corrector, process.kt6CaloL1FastL2L3L6Corrector, process.kt6CaloL6SLBCorrector)


process.ak7CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ak7CaloL1FastL2L3Corrector, process.ak7CaloL2RelativeCorrector, process.ak7CaloL3AbsoluteCorrector)


process.ak10PFL2L3CorrectorTask = cms.Task(process.ak10PFL2L3Corrector, process.ak10PFL2RelativeCorrector, process.ak10PFL3AbsoluteCorrector)


process.ak1PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak1PFL1FastjetCorrector, process.ak1PFL1FastjetL2L3ResidualCorrector, process.ak1PFL2RelativeCorrector, process.ak1PFL3AbsoluteCorrector, process.ak1PFResidualCorrector)


process.ak8PFL2L3CorrectorTask = cms.Task(process.ak8PFL2L3Corrector, process.ak8PFL2RelativeCorrector, process.ak8PFL3AbsoluteCorrector)


process.ak1PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak1PFCHSL2L3ResidualCorrector, process.ak1PFCHSL2RelativeCorrector, process.ak1PFCHSL3AbsoluteCorrector, process.ak1PFCHSResidualCorrector)


process.ak4PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL2L3ResidualCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak7CaloL1L2L3ResidualCorrectorTask = cms.Task(process.ak7CaloL1L2L3ResidualCorrector, process.ak7CaloL1OffsetCorrector, process.ak7CaloL2RelativeCorrector, process.ak7CaloL3AbsoluteCorrector, process.ak7CaloResidualCorrector)


process.ak4CaloL1L2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1L2L3ResidualCorrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.kt4PFL2L3L6CorrectorTask = cms.Task(process.kt4PFL2L3Corrector, process.kt4PFL2L3L6Corrector, process.kt4PFL6SLBCorrector)


process.ak1PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak1PFCHSL1FastjetCorrector, process.ak1PFCHSL1FastjetL2L3ResidualCorrector, process.ak1PFCHSL2RelativeCorrector, process.ak1PFCHSL3AbsoluteCorrector, process.ak1PFCHSResidualCorrector)


process.ic5PFL1L2L3ResidualCorrectorTask = cms.Task(process.ic5PFL1L2L3ResidualCorrector, process.ic5PFL1OffsetCorrector, process.ic5PFL2RelativeCorrector, process.ic5PFL3AbsoluteCorrector, process.ic5PFResidualCorrector)


process.ak5PFL2L3ResidualCorrectorTask = cms.Task(process.ak5PFL2L3ResidualCorrector, process.ak5PFL2RelativeCorrector, process.ak5PFL3AbsoluteCorrector, process.ak5PFResidualCorrector)


process.ak4JPTL1L2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1L2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak8PFL2L3ResidualCorrectorTask = cms.Task(process.ak8PFL2L3ResidualCorrector, process.ak8PFL2RelativeCorrector, process.ak8PFL3AbsoluteCorrector, process.ak8PFResidualCorrector)


process.ak7JPTL2L3CorrectorTask = cms.Task(process.ak7JPTL2L3Corrector, process.ak7JPTL2RelativeCorrector, process.ak7JPTL3AbsoluteCorrector, process.ak7L1JPTOffsetCorrectorTask)


process.ak10PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak10PFCHSL2L3ResidualCorrector, process.ak10PFCHSL2RelativeCorrector, process.ak10PFCHSL3AbsoluteCorrector, process.ak10PFCHSResidualCorrector)


process.ak4CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak9PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak9PFL1L2L3ResidualCorrector, process.ak9PFL1OffsetCorrector, process.ak9PFL2RelativeCorrector, process.ak9PFL3AbsoluteCorrector, process.ak9PFResidualCorrector)


process.kt4CaloL2L3CorrectorTask = cms.Task(process.kt4CaloL2L3Corrector, process.kt4CaloL2RelativeCorrector, process.kt4CaloL3AbsoluteCorrector)


process.ak4CaloL2L3L6CorrectorTask = cms.Task(process.ak4CaloL2L3L6Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak6PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak6PFCHSL1FastjetCorrector, process.ak6PFCHSL1FastjetL2L3ResidualCorrector, process.ak6PFCHSL2RelativeCorrector, process.ak6PFCHSL3AbsoluteCorrector, process.ak6PFCHSResidualCorrector)


process.kt6PFL1L2L3CorrectorTask = cms.Task(process.kt6PFL1L2L3Corrector, process.kt6PFL1OffsetCorrector, process.kt6PFL2RelativeCorrector, process.kt6PFL3AbsoluteCorrector)


process.ak7CaloL2L3L6CorrectorTask = cms.Task(process.ak7CaloL2L3Corrector, process.ak7CaloL2L3L6Corrector, process.ak7CaloL6SLBCorrector)


process.ak4JPTL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak6PFL2L3ResidualCorrectorTask = cms.Task(process.ak6PFL2L3ResidualCorrector, process.ak6PFL2RelativeCorrector, process.ak6PFL3AbsoluteCorrector, process.ak6PFResidualCorrector)


process.ak4PFPuppiL1FastL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3Corrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.kt6PFL2L3ResidualCorrectorTask = cms.Task(process.kt6PFL2L3ResidualCorrector, process.kt6PFL2RelativeCorrector, process.kt6PFL3AbsoluteCorrector, process.kt6PFResidualCorrector)


process.ak7PFL2L3L6CorrectorTask = cms.Task(process.ak7PFL2L3Corrector, process.ak7PFL2L3L6Corrector, process.ak7PFL6SLBCorrector)


process.ic5PFL2L3ResidualCorrectorTask = cms.Task(process.ic5PFL2L3ResidualCorrector, process.ic5PFL2RelativeCorrector, process.ic5PFL3AbsoluteCorrector, process.ic5PFResidualCorrector)


process.ak6PFL2L3CorrectorTask = cms.Task(process.ak6PFL2L3Corrector, process.ak6PFL2RelativeCorrector, process.ak6PFL3AbsoluteCorrector)


process.ak10PFL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak10PFL1FastjetCorrector, process.ak10PFL1FastjetL2L3ResidualCorrector, process.ak10PFL2RelativeCorrector, process.ak10PFL3AbsoluteCorrector, process.ak10PFResidualCorrector)


process.ak3PFCHSL2L3CorrectorTask = cms.Task(process.ak3PFCHSL2L3Corrector, process.ak3PFCHSL2RelativeCorrector, process.ak3PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1L2L3CorrectorTask = cms.Task(process.ak4PFCHSL1L2L3Corrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak6PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak6PFCHSL1L2L3ResidualCorrector, process.ak6PFCHSL1OffsetCorrector, process.ak6PFCHSL2RelativeCorrector, process.ak6PFCHSL3AbsoluteCorrector, process.ak6PFCHSResidualCorrector)


process.ak7PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak7PFCHSL2L3ResidualCorrector, process.ak7PFCHSL2RelativeCorrector, process.ak7PFCHSL3AbsoluteCorrector, process.ak7PFCHSResidualCorrector)


process.ak2PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak2PFCHSL2L3ResidualCorrector, process.ak2PFCHSL2RelativeCorrector, process.ak2PFCHSL3AbsoluteCorrector, process.ak2PFCHSResidualCorrector)


process.ak10PFCHSL1FastjetL2L3ResidualCorrectorTask = cms.Task(process.ak10PFCHSL1FastjetCorrector, process.ak10PFCHSL1FastjetL2L3ResidualCorrector, process.ak10PFCHSL2RelativeCorrector, process.ak10PFCHSL3AbsoluteCorrector, process.ak10PFCHSResidualCorrector)


process.ak4PFL2L3CorrectorTask = cms.Task(process.ak4PFL2L3Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak7JPTL1L2L3ResidualCorrectorTask = cms.Task(process.ak7JPTL1L2L3ResidualCorrector, process.ak7JPTL2RelativeCorrector, process.ak7JPTL3AbsoluteCorrector, process.ak7JPTResidualCorrector, process.ak7L1JPTOffsetCorrectorTask)


process.ic5CaloL1L2L3CorrectorTask = cms.Task(process.ic5CaloL1L2L3Corrector, process.ic5CaloL1OffsetCorrector, process.ic5CaloL2RelativeCorrector, process.ic5CaloL3AbsoluteCorrector)


process.ak7PFL1FastL2L3L6CorrectorTask = cms.Task(process.ak7CaloL1L2L3Corrector, process.ak7PFL1FastL2L3L6Corrector, process.ak7PFL6SLBCorrector)


process.ak7L1JPTFastjetCorrectorTask = cms.Task(process.ak7CaloL1FastjetCorrector, process.ak7L1JPTFastjetCorrector)


process.jetCorrectorsTask = cms.Task(process.ak4CaloL1FastL2L3CorrectorTask, process.ak4CaloL1FastL2L3L6CorrectorTask, process.ak4CaloL1FastL2L3ResidualCorrectorTask, process.ak4CaloL1L2L3CorrectorTask, process.ak4CaloL1L2L3ResidualCorrectorTask, process.ak4CaloL2L3CorrectorTask, process.ak4CaloL2L3L6CorrectorTask, process.ak4CaloL2L3ResidualCorrectorTask, process.ak4JPTL1FastL2L3CorrectorTask, process.ak4JPTL1FastL2L3ResidualCorrectorTask, process.ak4JPTL1L2L3CorrectorTask, process.ak4JPTL1L2L3ResidualCorrectorTask, process.ak4JPTL2L3CorrectorTask, process.ak4JPTL2L3ResidualCorrectorTask, process.ak4L1JPTFastjetCorrectorTask, process.ak4L1JPTOffsetCorrectorTask, process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.ak4PFCHSL1L2L3CorrectorTask, process.ak4PFCHSL1L2L3ResidualCorrectorTask, process.ak4PFCHSL2L3CorrectorTask, process.ak4PFCHSL2L3ResidualCorrectorTask, process.ak4PFL1FastL2L3CorrectorTask, process.ak4PFL1FastL2L3L6CorrectorTask, process.ak4PFL1FastL2L3ResidualCorrectorTask, process.ak4PFL1L2L3CorrectorTask, process.ak4PFL1L2L3ResidualCorrectorTask, process.ak4PFL2L3CorrectorTask, process.ak4PFL2L3L6CorrectorTask, process.ak4PFL2L3ResidualCorrectorTask, process.ak4PFPuppiL1FastL2L3CorrectorTask, process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask, process.ak4PFPuppiL1L2L3CorrectorTask, process.ak4PFPuppiL1L2L3ResidualCorrectorTask, process.ak4PFPuppiL2L3CorrectorTask, process.ak4PFPuppiL2L3ResidualCorrectorTask, process.ak4TrackL2L3CorrectorTask)


process.ak7JPTL1FastL2L3CorrectorTask = cms.Task(process.ak7JPTL1FastL2L3Corrector, process.ak7JPTL2RelativeCorrector, process.ak7JPTL3AbsoluteCorrector, process.ak7L1JPTFastjetCorrectorTask)


process.ak7JPTL1L2L3CorrectorTask = cms.Task(process.ak7JPTL1L2L3Corrector, process.ak7JPTL2RelativeCorrector, process.ak7JPTL3AbsoluteCorrector, process.ak7L1JPTOffsetCorrectorTask)


process.ak7JPTL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak7JPTL1FastL2L3ResidualCorrector, process.ak7JPTL2RelativeCorrector, process.ak7JPTL3AbsoluteCorrector, process.ak7JPTResidualCorrector, process.ak7L1JPTFastjetCorrectorTask)


process.jetCorrectorsAllAlgosTask = cms.Task(process.ak10PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak10PFCHSL1L2L3ResidualCorrectorTask, process.ak10PFCHSL2L3CorrectorTask, process.ak10PFCHSL2L3ResidualCorrectorTask, process.ak10PFL1FastjetL2L3ResidualCorrectorTask, process.ak10PFL1L2L3ResidualCorrectorTask, process.ak10PFL2L3CorrectorTask, process.ak10PFL2L3ResidualCorrectorTask, process.ak1PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak1PFCHSL1L2L3ResidualCorrectorTask, process.ak1PFCHSL2L3CorrectorTask, process.ak1PFCHSL2L3ResidualCorrectorTask, process.ak1PFL1FastjetL2L3ResidualCorrectorTask, process.ak1PFL1L2L3ResidualCorrectorTask, process.ak1PFL2L3CorrectorTask, process.ak1PFL2L3ResidualCorrectorTask, process.ak2PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak2PFCHSL1L2L3ResidualCorrectorTask, process.ak2PFCHSL2L3CorrectorTask, process.ak2PFCHSL2L3ResidualCorrectorTask, process.ak2PFL1FastjetL2L3ResidualCorrectorTask, process.ak2PFL1L2L3ResidualCorrectorTask, process.ak2PFL2L3CorrectorTask, process.ak2PFL2L3ResidualCorrectorTask, process.ak3PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak3PFCHSL1L2L3ResidualCorrectorTask, process.ak3PFCHSL2L3CorrectorTask, process.ak3PFCHSL2L3ResidualCorrectorTask, process.ak3PFL1FastjetL2L3ResidualCorrectorTask, process.ak3PFL1L2L3ResidualCorrectorTask, process.ak3PFL2L3CorrectorTask, process.ak3PFL2L3ResidualCorrectorTask, process.ak4TrackL1FastL2L3CorrectorTask, process.ak5PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak5PFCHSL1L2L3ResidualCorrectorTask, process.ak5PFCHSL2L3CorrectorTask, process.ak5PFCHSL2L3ResidualCorrectorTask, process.ak5PFL1FastjetL2L3ResidualCorrectorTask, process.ak5PFL1L2L3ResidualCorrectorTask, process.ak5PFL2L3CorrectorTask, process.ak5PFL2L3ResidualCorrectorTask, process.ak6PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak6PFCHSL1L2L3ResidualCorrectorTask, process.ak6PFCHSL2L3CorrectorTask, process.ak6PFCHSL2L3ResidualCorrectorTask, process.ak6PFL1FastjetL2L3ResidualCorrectorTask, process.ak6PFL1L2L3ResidualCorrectorTask, process.ak6PFL2L3CorrectorTask, process.ak6PFL2L3ResidualCorrectorTask, process.ak7CaloL1FastL2L3CorrectorTask, process.ak7CaloL1FastL2L3L6CorrectorTask, process.ak7CaloL1FastL2L3ResidualCorrectorTask, process.ak7CaloL1L2L3CorrectorTask, process.ak7CaloL1L2L3ResidualCorrectorTask, process.ak7CaloL2L3CorrectorTask, process.ak7CaloL2L3L6CorrectorTask, process.ak7CaloL2L3ResidualCorrectorTask, process.ak7JPTL1FastL2L3ResidualCorrectorTask, process.ak7JPTL1L2L3CorrectorTask, process.ak7JPTL1L2L3ResidualCorrectorTask, process.ak7JPTL2L3CorrectorTask, process.ak7JPTL6SLBCorrector, process.ak7L1JPTFastjetCorrectorTask, process.ak7L1JPTOffsetCorrectorTask, process.ak7PFCHSL1FastL2L3CorrectorTask, process.ak7PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak7PFCHSL1L2L3ResidualCorrectorTask, process.ak7PFCHSL2L3CorrectorTask, process.ak7PFCHSL2L3ResidualCorrectorTask, process.ak7PFL1FastL2L3CorrectorTask, process.ak7PFL1FastL2L3L6CorrectorTask, process.ak7PFL1FastjetL2L3ResidualCorrectorTask, process.ak7PFL1L2L3CorrectorTask, process.ak7PFL1L2L3ResidualCorrectorTask, process.ak7PFL2L3CorrectorTask, process.ak7PFL2L3L6CorrectorTask, process.ak7PFL2L3ResidualCorrectorTask, process.ak8PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak8PFCHSL1L2L3ResidualCorrectorTask, process.ak8PFCHSL2L3CorrectorTask, process.ak8PFCHSL2L3ResidualCorrectorTask, process.ak8PFL1FastjetL2L3ResidualCorrectorTask, process.ak8PFL1L2L3ResidualCorrectorTask, process.ak8PFL2L3CorrectorTask, process.ak8PFL2L3ResidualCorrectorTask, process.ak9PFCHSL1FastjetL2L3ResidualCorrectorTask, process.ak9PFCHSL1L2L3ResidualCorrectorTask, process.ak9PFCHSL2L3CorrectorTask, process.ak9PFCHSL2L3ResidualCorrectorTask, process.ak9PFL1FastjetL2L3ResidualCorrectorTask, process.ak9PFL1L2L3ResidualCorrectorTask, process.ak9PFL2L3CorrectorTask, process.ak9PFL2L3ResidualCorrectorTask, process.ic5CaloL1FastL2L3CorrectorTask, process.ic5CaloL1FastL2L3L6CorrectorTask, process.ic5CaloL1FastL2L3ResidualCorrectorTask, process.ic5CaloL1L2L3CorrectorTask, process.ic5CaloL1L2L3ResidualCorrectorTask, process.ic5CaloL2L3CorrectorTask, process.ic5CaloL2L3L6CorrectorTask, process.ic5CaloL2L3ResidualCorrectorTask, process.ic5PFL1FastL2L3CorrectorTask, process.ic5PFL1FastL2L3L6CorrectorTask, process.ic5PFL1FastL2L3ResidualCorrectorTask, process.ic5PFL1L2L3CorrectorTask, process.ic5PFL1L2L3ResidualCorrectorTask, process.ic5PFL2L3CorrectorTask, process.ic5PFL2L3L6CorrectorTask, process.ic5PFL2L3ResidualCorrectorTask, process.jetCorrectorsTask, process.kt4CaloL1FastL2L3CorrectorTask, process.kt4CaloL1FastL2L3L6CorrectorTask, process.kt4CaloL1FastL2L3ResidualCorrectorTask, process.kt4CaloL1L2L3CorrectorTask, process.kt4CaloL1L2L3ResidualCorrectorTask, process.kt4CaloL2L3CorrectorTask, process.kt4CaloL2L3L6CorrectorTask, process.kt4CaloL2L3ResidualCorrectorTask, process.kt4PFL1FastL2L3CorrectorTask, process.kt4PFL1FastL2L3L6CorrectorTask, process.kt4PFL1FastL2L3ResidualCorrectorTask, process.kt4PFL1L2L3CorrectorTask, process.kt4PFL1L2L3ResidualCorrectorTask, process.kt4PFL2L3CorrectorTask, process.kt4PFL2L3L6CorrectorTask, process.kt4PFL2L3ResidualCorrectorTask, process.kt6CaloL1FastL2L3CorrectorTask, process.kt6CaloL1FastL2L3L6CorrectorTask, process.kt6CaloL1FastL2L3ResidualCorrectorTask, process.kt6CaloL1L2L3CorrectorTask, process.kt6CaloL1L2L3ResidualCorrectorTask, process.kt6CaloL2L3CorrectorTask, process.kt6CaloL2L3L6CorrectorTask, process.kt6CaloL2L3ResidualCorrectorTask, process.kt6PFL1FastL2L3CorrectorTask, process.kt6PFL1FastL2L3L6CorrectorTask, process.kt6PFL1FastL2L3ResidualCorrectorTask, process.kt6PFL1L2L3CorrectorTask, process.kt6PFL1L2L3ResidualCorrectorTask, process.kt6PFL2L3CorrectorTask, process.kt6PFL2L3L6CorrectorTask, process.kt6PFL2L3ResidualCorrectorTask)


process.kt4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.kt4CaloL1FastL2L3ResidualCorrectorTask)


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.ak1PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak1PFL1L2L3ResidualCorrectorTask)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorTask)


process.ic5PFL2L3ResidualCorrectorChain = cms.Sequence(process.ic5PFL2L3ResidualCorrectorTask)


process.ak2PFL2L3CorrectorChain = cms.Sequence(process.ak2PFL2L3CorrectorTask)


process.ak8PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak8PFCHSL1FastjetCorrector+process.ak8PFCHSL2RelativeCorrector+process.ak8PFCHSL3AbsoluteCorrector+process.ak8PFCHSL1FastL2L3Corrector)


process.ak8PFCHSL2L3CorrectorChain = cms.Sequence(process.ak8PFCHSL2L3CorrectorTask)


process.ak1PUPPIL2L3CorrectorChain = cms.Sequence(process.ak1PUPPIL2RelativeCorrector+process.ak1PUPPIL3AbsoluteCorrector+process.ak1PUPPIL2L3Corrector)


process.ak3PFL2L3CorrectorChain = cms.Sequence(process.ak3PFL2L3CorrectorTask)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3ResidualCorrectorTask)


process.ak3PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak3PFL2L3ResidualCorrectorTask)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1L2L3CorrectorTask)


process.ak9PFCHSL2L3CorrectorChain = cms.Sequence(process.ak9PFCHSL2L3CorrectorTask)


process.kt4CaloL2L3L6CorrectorChain = cms.Sequence(process.kt4CaloL2L3L6CorrectorTask)


process.ak5PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak5PFL1FastjetL2L3ResidualCorrectorTask)


process.ak2PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak2PFCHSL2L3ResidualCorrectorTask)


process.ak9PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak9PFL1FastjetL2L3ResidualCorrectorTask)


process.ic5CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ic5CaloL1FastL2L3CorrectorTask)


process.ak8PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak8PUPPIL1FastjetCorrector+process.ak8PUPPIL2RelativeCorrector+process.ak8PUPPIL3AbsoluteCorrector+process.ak8PUPPIL1FastL2L3Corrector)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3CorrectorTask)


process.kt6PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.kt6PFL1FastL2L3ResidualCorrectorTask)


process.ak10PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak10PFCHSL2L3ResidualCorrectorTask)


process.ak7PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak7PFL2L3ResidualCorrectorTask)


process.ak7CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak7CaloL2L3ResidualCorrectorTask)


process.ak9PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak9PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak10PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak10PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak2PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak2PUPPIL1FastjetCorrector+process.ak2PUPPIL2RelativeCorrector+process.ak2PUPPIL3AbsoluteCorrector+process.ak2PUPPIL1FastL2L3Corrector)


process.ak2PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak2PFL1FastjetL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3ResidualCorrectorTask)


process.ak2PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak2PFCHSL1L2L3ResidualCorrectorTask)


process.ak7PFL2L3L6CorrectorChain = cms.Sequence(process.ak7PFL2L3L6CorrectorTask)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3ResidualCorrectorTask)


process.ak6PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak6PUPPIL1FastjetCorrector+process.ak6PUPPIL2RelativeCorrector+process.ak6PUPPIL3AbsoluteCorrector+process.ak6PUPPIL1FastL2L3Corrector)


process.ak4L1JPTFastjetCorrectorChain = cms.Sequence(process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4JPTL1L2L3CorrectorTask)


process.ak7CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak7CaloL1L2L3ResidualCorrectorTask)


process.ak1PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak1PFCHSL2L3ResidualCorrectorTask)


process.kt6PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.kt6PFL1L2L3ResidualCorrectorTask)


process.ak3PUPPIL2L3CorrectorChain = cms.Sequence(process.ak3PUPPIL2RelativeCorrector+process.ak3PUPPIL3AbsoluteCorrector+process.ak3PUPPIL2L3Corrector)


process.ak3PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak3PFL1L2L3ResidualCorrectorTask)


process.ic5CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ic5CaloL2L3ResidualCorrectorTask)


process.ak10PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak10PUPPIL1FastjetCorrector+process.ak10PUPPIL2RelativeCorrector+process.ak10PUPPIL3AbsoluteCorrector+process.ak10PUPPIL1FastL2L3Corrector)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3CorrectorTask)


process.ak7JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak7JPTL1FastL2L3CorrectorTask)


process.kt6PFL1FastL2L3CorrectorChain = cms.Sequence(process.kt6PFL1FastL2L3CorrectorTask)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2L3CorrectorTask)


process.ic5PFL1FastL2L3CorrectorChain = cms.Sequence(process.ic5PFL1FastL2L3CorrectorTask)


process.ak5PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak5PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak4TrackL1FastL2L3CorrectorChain = cms.Sequence(process.ak4TrackL1FastL2L3CorrectorTask)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1L2L3ResidualCorrectorTask)


process.ak3PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak3PUPPIL1FastjetCorrector+process.ak3PUPPIL2RelativeCorrector+process.ak3PUPPIL3AbsoluteCorrector+process.ak3PUPPIL1FastL2L3Corrector)


process.kt4PFL2L3CorrectorChain = cms.Sequence(process.kt4PFL2L3CorrectorTask)


process.ak6PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak6PFL1FastjetL2L3ResidualCorrectorTask)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3L6CorrectorTask)


process.ak9PUPPIL2L3CorrectorChain = cms.Sequence(process.ak9PUPPIL2RelativeCorrector+process.ak9PUPPIL3AbsoluteCorrector+process.ak9PUPPIL2L3Corrector)


process.ic5PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ic5PFL1FastL2L3ResidualCorrectorTask)


process.ak9PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak9PFCHSL1L2L3ResidualCorrectorTask)


process.ak8PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak8PFL1L2L3ResidualCorrectorTask)


process.ak2PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak2PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak6PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak6PFCHSL2L3ResidualCorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3ResidualCorrectorTask)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2L3L6CorrectorTask)


process.ak7L1JPTOffsetCorrectorChain = cms.Sequence(process.ak7L1JPTOffsetCorrectorTask)


process.kt4PFL2L3ResidualCorrectorChain = cms.Sequence(process.kt4PFL2L3ResidualCorrectorTask)


process.ak6PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak6PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak7CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak7CaloL1FastL2L3CorrectorTask)


process.ak4pfl1l2l3Sequence = cms.Sequence(((process.particleFlow+process.kt6PFJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak4PFJets+process.kt6PFJets+process.ak4PFL1FastL2L3CorrectorChain+process.ak4PFJetsL1FastL2L3+process.ak4GenJetsNoNu+process.ak4pfGenPtEta+process.ak4pfl1l2l3PtEta+process.ak4pfl1l2l3PtEtaUncor))+process.ak4pfl1l2l3JetToRef)+process.ak4pfl1l2l3JetToUncorJet))+process.ak4pfl1l2l3))


process.kt4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.kt4PFL1FastL2L3ResidualCorrectorTask)


process.ic5CaloL2L3L6CorrectorChain = cms.Sequence(process.ic5CaloL2L3L6CorrectorTask)


process.ak7PFL2L3CorrectorChain = cms.Sequence(process.ak7PFL2L3CorrectorTask)


process.kt4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.kt4CaloL2L3ResidualCorrectorTask)


process.kt6CaloL2L3L6CorrectorChain = cms.Sequence(process.kt6CaloL2L3L6CorrectorTask)


process.ic5CaloL1L2L3CorrectorChain = cms.Sequence(process.ic5CaloL1L2L3CorrectorTask)


process.kt6CaloL2L3CorrectorChain = cms.Sequence(process.kt6CaloL2L3CorrectorTask)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3ResidualCorrectorTask)


process.ak5PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak5PFCHSL1L2L3ResidualCorrectorTask)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2L3L6CorrectorTask)


process.ak7PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak7PFCHSL1L2L3ResidualCorrectorTask)


process.kt6CaloL2L3ResidualCorrectorChain = cms.Sequence(process.kt6CaloL2L3ResidualCorrectorTask)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4JPTL2L3CorrectorTask)


process.ak5PFL2L3CorrectorChain = cms.Sequence(process.ak5PFL2L3CorrectorTask)


process.kt4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.kt4PFL1FastL2L3L6CorrectorTask)


process.ak8PUPPIL2L3CorrectorChain = cms.Sequence(process.ak8PUPPIL2RelativeCorrector+process.ak8PUPPIL3AbsoluteCorrector+process.ak8PUPPIL2L3Corrector)


process.ak8PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak8PFL1FastjetCorrector+process.ak8PFL2RelativeCorrector+process.ak8PFL3AbsoluteCorrector+process.ak8PFL1FastL2L3Corrector)


process.ic5PFL2L3CorrectorChain = cms.Sequence(process.ic5PFL2L3CorrectorTask)


process.kt4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.kt4CaloL1L2L3ResidualCorrectorTask)


process.ak6PFL2L3CorrectorChain = cms.Sequence(process.ak6PFL2L3CorrectorTask)


process.ak5PUPPIL2L3CorrectorChain = cms.Sequence(process.ak5PUPPIL2RelativeCorrector+process.ak5PUPPIL3AbsoluteCorrector+process.ak5PUPPIL2L3Corrector)


process.kt4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.kt4PFL1L2L3ResidualCorrectorTask)


process.kt4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.kt4CaloL1FastL2L3L6CorrectorTask)


process.ic5PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ic5PFL1FastL2L3L6CorrectorTask)


process.kt6CaloL1FastL2L3CorrectorChain = cms.Sequence(process.kt6CaloL1FastL2L3CorrectorTask)


process.ak8PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak8PFCHSL2L3ResidualCorrectorTask)


process.ak10PFL2L3CorrectorChain = cms.Sequence(process.ak10PFL2L3CorrectorTask)


process.ak7JPTL2L3CorrectorChain = cms.Sequence(process.ak7JPTL2L3CorrectorTask)


process.ak9PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak9PUPPIL1FastjetCorrector+process.ak9PUPPIL2RelativeCorrector+process.ak9PUPPIL3AbsoluteCorrector+process.ak9PUPPIL1FastL2L3Corrector)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3CorrectorTask)


process.ak8PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak8PFCHSL1L2L3ResidualCorrectorTask)


process.ak10PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak10PFL1L2L3ResidualCorrectorTask)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3ResidualCorrectorTask)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1L2L3ResidualCorrectorTask)


process.ak7CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak7CaloL1FastL2L3ResidualCorrectorTask)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3CorrectorTask)


process.ak2PFCHSL2L3CorrectorChain = cms.Sequence(process.ak2PFCHSL2L3CorrectorTask)


process.ak10PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak10PFL2L3ResidualCorrectorTask)


process.ak3PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak3PFCHSL2L3ResidualCorrectorTask)


process.kt6PFL2L3CorrectorChain = cms.Sequence(process.kt6PFL2L3CorrectorTask)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1L2L3CorrectorTask)


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3CorrectorTask)


process.ic5CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ic5CaloL1FastL2L3ResidualCorrectorTask)


process.ak9PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak9PFL1L2L3ResidualCorrectorTask)


process.ak7PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak7PFL1FastL2L3CorrectorTask)


process.ak5PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak5PFL1L2L3ResidualCorrectorTask)


process.kt4PFL2L3L6CorrectorChain = cms.Sequence(process.kt4PFL2L3L6CorrectorTask)


process.ak10PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak10PFL1FastjetL2L3ResidualCorrectorTask)


process.ak2PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak2PFL2L3ResidualCorrectorTask)


process.ak1PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak1PFCHSL1L2L3ResidualCorrectorTask)


process.kt6PFL2L3ResidualCorrectorChain = cms.Sequence(process.kt6PFL2L3ResidualCorrectorTask)


process.ak1PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak1PUPPIL1FastjetCorrector+process.ak1PUPPIL2RelativeCorrector+process.ak1PUPPIL3AbsoluteCorrector+process.ak1PUPPIL1FastL2L3Corrector)


process.ak7JPTL1L2L3CorrectorChain = cms.Sequence(process.ak7JPTL1L2L3CorrectorTask)


process.ak7PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak7PFL1FastjetL2L3ResidualCorrectorTask)


process.kt4PFL1FastL2L3CorrectorChain = cms.Sequence(process.kt4PFL1FastL2L3CorrectorTask)


process.ak6PFCHSL2L3CorrectorChain = cms.Sequence(process.ak6PFCHSL2L3CorrectorTask)


process.ak7PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak7PUPPIL1FastjetCorrector+process.ak7PUPPIL2RelativeCorrector+process.ak7PUPPIL3AbsoluteCorrector+process.ak7PUPPIL1FastL2L3Corrector)


process.ak3PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak3PFCHSL1L2L3ResidualCorrectorTask)


process.ak3PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak3PFL1FastjetL2L3ResidualCorrectorTask)


process.ak5PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak5PUPPIL1FastjetCorrector+process.ak5PUPPIL2RelativeCorrector+process.ak5PUPPIL3AbsoluteCorrector+process.ak5PUPPIL1FastL2L3Corrector)


process.kt6CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.kt6CaloL1L2L3ResidualCorrectorTask)


process.ak7PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak7PFCHSL1FastL2L3CorrectorTask)


process.ak5PFCHSL2L3CorrectorChain = cms.Sequence(process.ak5PFCHSL2L3CorrectorTask)


process.ak6PUPPIL2L3CorrectorChain = cms.Sequence(process.ak6PUPPIL2RelativeCorrector+process.ak6PUPPIL3AbsoluteCorrector+process.ak6PUPPIL2L3Corrector)


process.ak4PUPPIL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PUPPIL1FastjetCorrector+process.ak4PUPPIL2RelativeCorrector+process.ak4PUPPIL3AbsoluteCorrector+process.ak4PUPPIL1FastL2L3Corrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask)


process.ak8PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak8PFL2L3ResidualCorrectorTask)


process.ak7CaloL2L3CorrectorChain = cms.Sequence(process.ak7CaloL2L3CorrectorTask)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2L3ResidualCorrectorTask)


process.ak1PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak1PFL1FastjetL2L3ResidualCorrectorTask)


process.ic5CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ic5CaloL1FastL2L3L6CorrectorTask)


process.ak3PFCHSL2L3CorrectorChain = cms.Sequence(process.ak3PFCHSL2L3CorrectorTask)


process.ak1PFCHSL2L3CorrectorChain = cms.Sequence(process.ak1PFCHSL2L3CorrectorTask)


process.ak7CaloL1L2L3CorrectorChain = cms.Sequence(process.ak7CaloL1L2L3CorrectorTask)


process.ak7CaloL2L3L6CorrectorChain = cms.Sequence(process.ak7CaloL2L3L6CorrectorTask)


process.ak7JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak7JPTL1FastL2L3ResidualCorrectorTask)


process.ak8PFL2L3CorrectorChain = cms.Sequence(process.ak8PFL2L3CorrectorTask)


process.ak1PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak1PFL2L3ResidualCorrectorTask)


process.ic5CaloL2L3CorrectorChain = cms.Sequence(process.ic5CaloL2L3CorrectorTask)


process.ak2PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak2PFL1L2L3ResidualCorrectorTask)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3CorrectorTask)


process.kt4CaloL2L3CorrectorChain = cms.Sequence(process.kt4CaloL2L3CorrectorTask)


process.ak9PFL2L3CorrectorChain = cms.Sequence(process.ak9PFL2L3CorrectorTask)


process.ak10PFCHSL2L3CorrectorChain = cms.Sequence(process.ak10PFCHSL2L3CorrectorTask)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL2L3ResidualCorrectorTask)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2L3CorrectorTask)


process.kt6CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.kt6CaloL1FastL2L3L6CorrectorTask)


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3ResidualCorrectorTask)


process.kt4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.kt4CaloL1FastL2L3CorrectorTask)


process.ic5PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ic5PFL1L2L3ResidualCorrectorTask)


process.ak4pfchsl1l2l3Sequence = cms.Sequence(((process.pfCHS+process.kt6PFchsJetsRhos+(((process.genParticlesForJetsNoNu+(process.ak4PFCHSJets+process.kt6PFJets+process.ak4PFCHSL1FastL2L3CorrectorChain+process.ak4PFCHSJetsL1FastL2L3+process.ak4GenJetsNoNu+process.ak4pfchsGenPtEta+process.ak4pfchsl1l2l3PtEta+process.ak4pfchsl1l2l3PtEtaUncor))+process.ak4pfchsl1l2l3JetToRef)+process.ak4pfchsl1l2l3JetToUncorJet))+process.ak4pfchsl1l2l3))


process.ak3PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak3PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.kt6CaloL1L2L3CorrectorChain = cms.Sequence(process.kt6CaloL1L2L3CorrectorTask)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3CorrectorTask)


process.ak10PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak10PFCHSL1L2L3ResidualCorrectorTask)


process.ak1PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak1PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak1PFL2L3CorrectorChain = cms.Sequence(process.ak1PFL2L3CorrectorTask)


process.ak8PFL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak8PFL1FastjetL2L3ResidualCorrectorTask)


process.ak7JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak7JPTL1L2L3ResidualCorrectorTask)


process.ak4PUPPIL2L3CorrectorChain = cms.Sequence(process.ak4PUPPIL2RelativeCorrector+process.ak4PUPPIL3AbsoluteCorrector+process.ak4PUPPIL2L3Corrector)


process.kt6PFL1L2L3CorrectorChain = cms.Sequence(process.kt6PFL1L2L3CorrectorTask)


process.ak7PUPPIL2L3CorrectorChain = cms.Sequence(process.ak7PUPPIL2RelativeCorrector+process.ak7PUPPIL3AbsoluteCorrector+process.ak7PUPPIL2L3Corrector)


process.ic5PFL2L3L6CorrectorChain = cms.Sequence(process.ic5PFL2L3L6CorrectorTask)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2L3CorrectorTask)


process.ak5PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak5PFL2L3ResidualCorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1L2L3ResidualCorrectorTask)


process.ak7PFL1L2L3CorrectorChain = cms.Sequence(process.ak7PFL1L2L3CorrectorTask)


process.kt6PFL2L3L6CorrectorChain = cms.Sequence(process.kt6PFL2L3L6CorrectorTask)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3CorrectorTask)


process.ak7PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak7PFCHSL2L3ResidualCorrectorTask)


process.ak7PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak7PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak6PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak6PFL1L2L3ResidualCorrectorTask)


process.kt4CaloL1L2L3CorrectorChain = cms.Sequence(process.kt4CaloL1L2L3CorrectorTask)


process.ak7CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak7CaloL1FastL2L3L6CorrectorTask)


process.kt4PFL1L2L3CorrectorChain = cms.Sequence(process.kt4PFL1L2L3CorrectorTask)


process.ak7PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak7PFL1L2L3ResidualCorrectorTask)


process.ak5PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak5PFCHSL2L3ResidualCorrectorTask)


process.kt6PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.kt6PFL1FastL2L3L6CorrectorTask)


process.kt6CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.kt6CaloL1FastL2L3ResidualCorrectorTask)


process.ic5PFL1L2L3CorrectorChain = cms.Sequence(process.ic5PFL1L2L3CorrectorTask)


process.ak6PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak6PFL2L3ResidualCorrectorTask)


process.ak6PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak6PFCHSL1L2L3ResidualCorrectorTask)


process.ak7L1JPTFastjetCorrectorChain = cms.Sequence(process.ak7L1JPTFastjetCorrectorTask)


process.ak2PUPPIL2L3CorrectorChain = cms.Sequence(process.ak2PUPPIL2RelativeCorrector+process.ak2PUPPIL3AbsoluteCorrector+process.ak2PUPPIL2L3Corrector)


process.ak9PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak9PFL2L3ResidualCorrectorTask)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3L6CorrectorTask)


process.ak7PFCHSL2L3CorrectorChain = cms.Sequence(process.ak7PFCHSL2L3CorrectorTask)


process.ak7PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak7PFL1FastL2L3L6CorrectorTask)


process.ic5CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ic5CaloL1L2L3ResidualCorrectorTask)


process.ak8PFCHSL1FastjetL2L3ResidualCorrectorChain = cms.Sequence(process.ak8PFCHSL1FastjetL2L3ResidualCorrectorTask)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2L3ResidualCorrectorTask)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2L3CorrectorTask)


process.ak9PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak9PFCHSL2L3ResidualCorrectorTask)


process.ak10PUPPIL2L3CorrectorChain = cms.Sequence(process.ak10PUPPIL2RelativeCorrector+process.ak10PUPPIL3AbsoluteCorrector+process.ak10PUPPIL2L3Corrector)


process.ak4pfl1l2l3Path = cms.Path(process.ak4pfl1l2l3Sequence)


process.ak4pfchsl1l2l3Path = cms.Path(process.ak4pfchsl1l2l3Sequence)


