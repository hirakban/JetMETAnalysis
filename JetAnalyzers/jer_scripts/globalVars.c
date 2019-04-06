void setStyle();

void globalVars( TString file = "root://131.225.204.161:1094//store/group/lpcjme/JRA_outfiles_102X/JRA_QCD_Autumn18FlatPU_JECv8.root" ) {

  setStyle();

  TFile* f = TFile::Open(file);
  if (!f) return;
  TTree* t = (TTree*) f->Get("ak4pfchsl1l2l3/t");

  map<TString, pair<TString, TString> > vars;
  vars["rho"] = {"rho", "#rho [GeV]"};
  vars["npv"] = {"npv", "N_{PV}"};
  vars["mu"]  = {"tnpus[12]", "#mu"};

  for (auto const& vpair : vars) {
    TString var = vpair.second.first;
    TString label = vpair.second.second;

    TCanvas* c = new TCanvas("c", "c", 600, 600);
    TH1F* h = new TH1F("h","h",200,0,100);
    t->Draw(var + ">>h", "", "hist");

    h->SetLineWidth(2);
    h->GetXaxis()->SetTitle(label);
    h->GetXaxis()->SetNdivisions(5, 5, 0);
    h->GetYaxis()->SetRangeUser(0, h->GetMaximum()*1.2);
    if (var == "npv") h->Rebin();

    TLatex text;
    text.SetNDC();

    text.SetTextSize(0.035);
    text.SetTextFont(42);
    text.DrawLatex(0.8, 0.96, "(13 TeV)");
    text.DrawLatex( 0.75, 0.8, Form("#bf{Mean %.1f}" , h->GetMean()) );

    c->Print(vpair.first + ".pdf");

    delete c;
    delete h;
  }
}

void setStyle() {
  gStyle->SetPadTopMargin(0.05);
  gStyle->SetPadBottomMargin(0.13);
  gStyle->SetPadLeftMargin(0.1);
  gStyle->SetPadRightMargin(0.05);

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  gStyle->SetTitleFont(42);
  gStyle->SetTitleColor(1);
  gStyle->SetTitleTextColor(1);
  gStyle->SetTitleFillColor(10);
  gStyle->SetTitleFontSize(0.05);

  gStyle->SetTitleColor(1, "XYZ");
  gStyle->SetTitleFont(42, "XYZ");
  gStyle->SetTitleSize(0.05, "XYZ");
  gStyle->SetTitleXOffset(1.1);
  gStyle->SetTitleYOffset(0.9);

  gStyle->SetLabelColor(1, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");
  gStyle->SetLabelOffset(0.007, "XYZ");
  gStyle->SetLabelSize(0.04, "XYZ");

  gStyle->SetAxisColor(1, "XYZ");
  gStyle->SetTickLength(0.03, "XYZ");
  gStyle->SetNdivisions(510, "XYZ");
  gStyle->SetPadTickX(1);
  gStyle->SetPadTickY(1);
}
