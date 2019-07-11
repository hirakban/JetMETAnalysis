vector<float> etabins = {0, 0.5, 0.8, 1.1, 1.3, 1.7, 1.9, 2.1, 2.3, 2.5, 2.8, 3.0, 3.2, 4.7};
vector<float> mubins  = {0, 10, 20, 30, 40, 50, 60, 70};

void setStyle();
void getPars(map<int, map<int, map<int, float> > >& pars, string inFile);
int getEtaIndex(float eta);
double getRes(double p0, double p1, double p2, double p3, double pt);

void JERmu(float eta=0, string str_pTs="30 50 100 200", int r=4, string era1 = "Fall17_17Nov2017_V4_MC", string alg1="pfchs",
           string era2 = "Fall17_17Nov2017_V4_MC", string alg2="puppi") {
  setStyle();

  map<string, tuple<string, Color_t, Style_t> > alg_style = { {"pf", {"PF", kBlue+1, 10} }, {"pfchs", {"PF+CHS", kRed+1, 1} }, {"puppi", {"PF+PUPPI", kGreen+2, 7} } };

  map<int, map<int, map<int, float> > > pars1, pars2;
  getPars( pars1, era1 + "/" + era1 + "_PtResolution_ak" + to_string(r) + alg1 + "l1l2l3.txt" );
  getPars( pars2, era2 + "/" + era2 + "_PtResolution_ak" + to_string(r) + alg2 + "l1l2l3.txt" );
//  getPars( pars2, era2 + "/" + era2 + "_PtResolution_ak" + to_string(r) + alg2 + ".txt" );

  int iEta = getEtaIndex(eta);

//  if (eta==0 && r==4) str_pTs = "15 " + str_pTs;
  vector<float> pTs;

  int delim_pos;
  while ( (delim_pos = str_pTs.find(' ')) != -1 ) {
    string str = str_pTs.substr(0, delim_pos);
    str_pTs.erase(0, delim_pos + 1);
    while (str_pTs.at(0) == ' ') str_pTs.erase(0, 1);

    pTs.push_back( stof(str) );
  }
  pTs.push_back( stof(str_pTs) );

  TCanvas* c = new TCanvas("c", "c", 600, 600);
  TH1F* h = new TH1F("h", "h", mubins.size()-1, &mubins[0]);
  h->Draw();

//  h->GetXaxis()->SetTitle("#mu");
  h->GetXaxis()->SetTitle("Number of Pileup Interactions");
  h->GetXaxis()->SetNdivisions(7, 2, 0);
  h->GetYaxis()->SetTitle("JER");
  h->GetYaxis()->SetTitleOffset(1.3);
  h->GetYaxis()->SetRangeUser(0, 0.4);
  h->GetYaxis()->SetNdivisions(5, 5, 0);

  TLatex text;
  text.SetNDC();
  text.SetTextSize(0.04);
  text.DrawLatex(0.75, 0.87, "p_{T}^{Jet} [GeV]");

//  TLegend* leg = new TLegend(.35,.75,.65,.85);
  TLegend* leg = new TLegend(.44,.75,.69,.85);
  leg->SetTextSize(0.04);
  leg->SetBorderSize(0);
  leg->SetFillColor(0);
  leg->SetFillStyle(0);

  for (int iPt=0, nPt=pTs.size(); iPt<nPt; iPt++) {

    TGraph* g1 = new TGraph(), *g2 = new TGraph();
    for (int iMu=0, nMu=mubins.size()-1; iMu<nMu; iMu++) {
      double mu = 0.5*(mubins[iMu]+mubins[iMu+1]);

      g1->SetPoint( iMu, mu, getRes( pars1[iEta][iMu][0], pars1[iEta][iMu][1], pars1[iEta][iMu][2], pars1[iEta][iMu][3], pTs[iPt] ) );
      g2->SetPoint( iMu, mu, getRes( pars2[iEta][iMu][0], pars2[iEta][iMu][1], pars2[iEta][iMu][2], pars2[iEta][iMu][3], pTs[iPt] ) );
    }
    g1->SetMarkerStyle(iPt+24);
    g1->SetMarkerColor( get<1>( alg_style[alg1] ) );
    g1->SetLineColor( get<1>( alg_style[alg1] ) );
//    g1->SetLineStyle( get<2>( alg_style[alg1] ) );
    g1->Draw("plsame");

    g2->SetMarkerStyle(iPt+24);
    g2->SetMarkerColor( get<1>( alg_style[alg2] ) );
    g2->SetLineColor( get<1>( alg_style[alg2] ) );
    g2->SetLineStyle( 7 ); //g2->SetLineStyle( get<2>( alg_style[alg2] ) );
    g2->Draw("plsame");

    TMarker* t = new TMarker(0.79, .84-iPt*nPt*0.012, iPt+24);
    t->SetNDC();
    t->Draw();  text.DrawLatex(0.83, .825-iPt*nPt*0.012,  Form("%.0f", pTs[iPt]) );

    if (iPt==0) {
//      leg->AddEntry(g1, Form("%s %s", era1.substr(0, era1.find('_')).data(), get<0>( alg_style[alg1] ).data()), "L");
//      leg->AddEntry(g2, Form("%s %s", era2.substr(0, era2.find('_')).data(), get<0>( alg_style[alg2] ).data()), "L");

      leg->AddEntry(g1, Form("#bf{%s}", get<0>( alg_style[alg1] ).data()), "L");
      leg->AddEntry(g2, Form("#bf{%s}", get<0>( alg_style[alg2] ).data()), "L");
    }
  }

  text.DrawLatex(0.2, 0.87, "Anti-k_{T}");
  text.DrawLatex(0.2, 0.82, Form("R=0.%i", r));
  text.DrawLatex(0.2, 0.77, "Response");
  text.DrawLatex(0.2, 0.72, "Corrected");

  text.DrawLatex( 0.45, 0.87, Form("%2.1f#leq|#eta|<%2.1f", etabins[iEta], etabins[iEta+1]) );
  leg->Draw();

  text.SetTextSize(0.05);
  text.SetTextFont(61);
  text.DrawLatex(0.18, 0.96, "CMS");

  text.SetTextSize(0.035);
  text.SetTextFont(42);
  text.DrawLatex(0.87, 0.96, "13 TeV");

  text.SetTextSize(0.04);
  text.SetTextFont(52);
  text.DrawLatex(0.295, 0.96, "Simulation"); // Preliminary");

  c->Print( Form("Rel/ak%i/JERMu_eta%.1f.pdf", r, etabins[iEta]) );
}

void setStyle() {
  gStyle->SetPadTopMargin(0.05);
  gStyle->SetPadBottomMargin(0.13);
  gStyle->SetPadLeftMargin(0.16);
  gStyle->SetPadRightMargin(0.03);

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  gStyle->SetTitleFont(42);
  gStyle->SetTitleColor(1);
  gStyle->SetTitleTextColor(1);
  gStyle->SetTitleFillColor(10);
  gStyle->SetTitleFontSize(0.05);

  gStyle->SetTitleColor(1, "XYZ");
  gStyle->SetTitleFont(42, "XYZ");
  gStyle->SetTitleSize(0.06, "XYZ");
  gStyle->SetTitleXOffset(0.9);
  gStyle->SetTitleYOffset(0.9);

  gStyle->SetLabelColor(1, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");
  gStyle->SetLabelOffset(0.007, "XYZ");
  gStyle->SetLabelSize(0.05, "XYZ");

  gStyle->SetAxisColor(1, "XYZ");
  gStyle->SetTickLength(0.03, "XYZ");
  gStyle->SetNdivisions(510, "XYZ");
  gStyle->SetPadTickX(1);
  gStyle->SetPadTickY(1);
}

void getPars(map<int, map<int, map<int, float> > >& pars, string inFile) {

  ifstream file(inFile);
  if ( !file.is_open() ) cout << inFile + " not found!" << endl;

  string line;
  getline(file, line);  //read first line

  int j = -1, nbins = mubins.size()-1;
  for (int i=0; getline(file, line); i++) {

    string str;
    int delim_pos;

    while (line.at(0) == ' ') line.erase(0, 1);

    if (line.at(0) == '-') continue; //absolute eta binning, don't care about negative values
    int k = i % nbins;
    if (k==0) j++;

    for (int col_num=0; (delim_pos = line.find(' ')) != -1; col_num++) {

      str = line.substr(0, delim_pos);
      line.erase(0, delim_pos + 1);
      while (line.at(0) == ' ') line.erase(0, 1);

      if      (col_num == 7) pars[j][k][0] = stof(str);
      else if (col_num == 8) pars[j][k][1] = stof(str);
      else if (col_num == 9) pars[j][k][2] = stof(str);
    }
    pars[j][k][3] = stof(line);    //last column after loop
  }
  file.close();
}

int getEtaIndex(float eta) {

  int nEta = etabins.size();
  for (int i=0; i<nEta; i++) {
    if (etabins[i] <= eta && eta < etabins[i+1]) return i;
  }
  if (eta == etabins[nEta]) return nEta-1;
  else return -1;
}

double getRes(double p0, double p1, double p2, double p3, double pt) {
  return sqrt(p0*fabs(p0)/(pt*pt)+p1*p1*pow(pt,p3)+p2*p2);
}
