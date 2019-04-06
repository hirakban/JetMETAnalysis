void setStyle();

void drawRsp( TString fname="jra.root", int r=4, TString var="Rel", float eta1=0, float eta2=0.5, int pt1=30, int pt2=35, TString alg="puppi", int mu1=0, int mu2=0 ) {
  TFile* file = TFile::Open(fname);
  if (!file) return;

  setStyle();
  TCanvas* c = new TCanvas("c", "c", 600, 600);
  TLatex text;
  text.SetNDC();
  text.SetTextSize(0.04);

  TString name;
  if (mu2!=0) {
    if (eta1==0) name = var + Form("Rsp_JetEta%ito%.1f_Mu%ito%i_RefPt%ito%i", int(eta1), eta2, mu1, mu2, pt1, pt2);
    else         name = var + Form("Rsp_JetEta%.1fto%.1f_Mu%ito%i_RefPt%ito%i", eta1, eta2, mu1, mu2, pt1, pt2);
  }
  else {
    if (eta1==0) name = var + Form("Rsp_JetEta%ito%.1f_RefPt%ito%i", int(eta1), eta2, pt1, pt2);
    else         name = var + Form("Rsp_JetEta%.1fto%.1f_RefPt%ito%i", eta1, eta2, pt1, pt2);
  }

  TH1F* h=0;
  if (var == "Rel") h = new TH1F("h", "h", 50, 0, 2);
  else              h = new TH1F("h", "h", 100, -0.5, 0.5);
  h->Draw();

  if (alg == "") {
    map<TString, pair<Color_t, Style_t> > algs = { {"pf", {kBlue+1, kOpenCircle} }, {"pfchs", {kRed+1, kOpenSquare} }, {"puppi", {kGreen+2, kOpenTriangleUp} } };

    TLegend* leg = new TLegend(.76,.76,1,.9);
    leg->SetTextSize(0.04);
    leg->SetBorderSize(0);
    leg->SetFillColor(0);
    leg->SetFillStyle(0);

    h->GetXaxis()->SetTitle( var=="Rel" ? "p_{T}^{Jet}/p_{T}^{ref}" : (var=="Eta" ? "#Delta#eta" : "#Delta#phi") );
    h->GetXaxis()->SetNdivisions(5,5,0);
    h->GetYaxis()->SetNdivisions(5,5,0);

    float ymax=0;
    for (auto& pair : algs) {
      TString palg = pair.first;

      TDirectoryFile* tdir = (TDirectoryFile*) file->Get( Form("ak%i%sl1l2l3", r, palg.Data()) );
      TH1F* halg = (TH1F*) tdir->Get(name);

      halg->Scale( 1 / halg->Integral() );
      if (halg->GetMaximum() > ymax) ymax = halg->GetMaximum();

      halg->SetMarkerSize(0.8);
      halg->SetMarkerStyle(pair.second.second);
      halg->SetMarkerColor(pair.second.first);
      halg->SetLineColor(pair.second.first);

      TString label = "PF";
      if (palg.Contains("pfchs"))      label = "PF+CHS";
      else if (palg.Contains("puppi")) label = "PUPPI";

      leg->AddEntry(halg, label.Data(), "pl");
      halg->Draw("samepe");
    }
    h->GetYaxis()->SetRangeUser(0, ymax*1.4);
    leg->Draw();

    text.DrawLatex(0.2, 0.87, "Anti-k_{T}");
    text.DrawLatex(0.2, 0.82, Form("R=0.%i", r));

    text.DrawLatex( 0.45, 0.87, Form("%2.1f#leq#eta<%2.1f", eta1, eta2) );
    text.DrawLatex( 0.45, 0.82, Form("%i#leq#mu<%i", mu1, mu2) );
    text.DrawLatex( pt1==1000 ? 0.4 : 0.45, 0.77, Form("%i#leqp_{T}^{Ref}(GeV)<%i", pt1, pt2) );
  }
  else {
    TDirectoryFile* tdir = (TDirectoryFile*) file->Get( Form("ak%i%sl1l2l3", r, alg.Data()) );

    TH1F* h1 = (TH1F*) tdir->Get(name);
    h1->Draw("samepe");

    h->GetXaxis()->SetTitle( h1->GetXaxis()->GetTitle() );
    h->GetYaxis()->SetRangeUser(0, h1->GetMaximum()*1.2 );
    h->GetXaxis()->SetNdivisions(5,5,0);
    h->GetXaxis()->SetRangeUser(0, 2);

    float ex=0.73, px=0.68;
    if (pt1==300) { ex=0.7; px=0.63; }
    else if (pt1==1000) { ex=0.69; px=0.6; }

    text.DrawLatex( ex, 0.87, Form("%2.1f#leq#eta<%2.1f", eta1, eta2) );
    if (mu2!=0) text.DrawLatex( ex+0.01, 0.82, Form("%i#leq#mu<%i", mu1, mu2) );
    if (pt2!=0) {

      text.DrawLatex( px, 0.77, Form("%i#leqp_{T}^{Ref}(GeV)<%i", pt1, pt2) );

      TString label = "PF";
      if (alg.Contains("pfchs"))      label = "PF+CHS";
      else if (alg.Contains("puppi")) label = "PUPPI";

      text.DrawLatex(0.2, 0.87, "Anti-k_{T}");
      text.DrawLatex(0.2, 0.82, Form("R=0.%i", r));
      text.DrawLatex(0.2, 0.77, label);
    }
  }
  text.SetTextSize(0.05);
  text.SetTextFont(61);
  text.DrawLatex(0.18, 0.96, "CMS");

  text.SetTextSize(0.035);
  text.SetTextFont(42);
  text.DrawLatex(0.85, 0.96, "(13 TeV)");

  c->Print( Form("%s/ak%i%s_%s.pdf", var.Data(), r, alg.Data(), name.Data()) );
}

void setStyle(){
  gStyle->SetPadTopMargin(0.05);
  gStyle->SetPadBottomMargin(0.13);
  gStyle->SetPadLeftMargin(0.16);
  gStyle->SetPadRightMargin(0.02);

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
  gStyle->SetTitleXOffset(1.0);
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
