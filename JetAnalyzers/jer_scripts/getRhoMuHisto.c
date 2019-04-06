void getRhoMuHisto( TString file = "root://131.225.204.161:1094//store/group/lpcjme/JRA_outfiles_102X/JRA_QCD_Autumn18FlatPU_JECv8.root" ) {

  TFile* f = TFile::Open(file);
  if (!f) return;
  TTree* t = (TTree*) f->Get("ak4pfchsl1l2l3/t");

  TProfile* p = new TProfile("p_Rho_Mu", "p_Rho_Mu", 200, 0, 100);
  t->Draw("rho:tnpus[12]>>p_Rho_Mu");

  TFile* outFile = new TFile("p_Rho_Mu.root","RECREATE");
  outFile->cd();
  p->Write();

  delete outFile;
  outFile = 0;
}
