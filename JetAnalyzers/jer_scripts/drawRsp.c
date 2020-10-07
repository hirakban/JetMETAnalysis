void setStyle();

void drawRsp( std::string input="jra.root", int r=4, TString var="Rel", float eta1=0, float eta2=0.5, int pt1=30, int pt2=35, TString alg="puppi", int mu1=0, int mu2=0 ) {  //

  int delim_pos=0, ninput = 0;					// ninput calculates the number of input files
  int size = input.size();

  vector<TString> inname;					//input string for each filename
  vector<TFile*> tf;						//used to fetch directory location

  for (int i = 0; i<size; i++){					//takes care of multiple input file
    if(input.at(i) == ' '){
      ninput ++;
      inname.push_back(input.substr(delim_pos, i-delim_pos)); 
      //std::cout << "ninput = " << ninput  << std::endl;
      delim_pos = i+1;
    }
    else if (i == size-1){					// takes care of final file or in case of one input file
      ninput ++;
      inname.push_back(input.substr(delim_pos, i-delim_pos+1)); 
      delim_pos = i+1;
    } 
  }
  std::vector<TString>::const_iterator iter;			//iterators for fetching inname.

  setStyle();
  TCanvas* c = new TCanvas("c", "c", 600, 600);
  TLatex text;
  text.SetNDC();
  text.SetTextSize(0.04);

  TString name;
  if (mu2!=0) {
    if (eta1==0 || eta1==3.0) name = var + Form("Rsp_JetEta%ito%.1f_Mu%ito%i_RefPt%ito%i", int(eta1), eta2, mu1, mu2, pt1, pt2);
    else if (eta2==3.0) name = var + Form("Rsp_JetEta%.1fto%i_Mu%ito%i_RefPt%ito%i", eta1, int(eta2), mu1, mu2, pt1, pt2);
    else         name = var + Form("Rsp_JetEta%.1fto%.1f_Mu%ito%i_RefPt%ito%i", eta1, eta2, mu1, mu2, pt1, pt2);
  }
  else {
    if (eta1==0 || eta1==3.0) name = var + Form("Rsp_JetEta%ito%.1f_RefPt%ito%i", int(eta1), eta2, pt1, pt2);
    else if (eta2==3.0) name = var + Form("Rsp_JetEta%.1fto%i_RefPt%ito%i", eta1, int(eta2), pt1, pt2);
    else         name = var + Form("Rsp_JetEta%.1fto%.1f_RefPt%ito%i", eta1, eta2, pt1, pt2);
  }

  TH1F* h=0;
  if (var == "Rel") h = new TH1F("h", "h", 50, 0, 2);
  else              h = new TH1F("h", "h", 100, -0.5, 0.5);
  h->Draw();

  if (alg == "") {
    map<TString, pair<Color_t, Style_t> > algs = { {"pf", {kBlue+1, kOpenCircle} }, {"pfchs", {kRed+1, kOpenSquare} }, {"puppi", {kGreen+2, kOpenTriangleUp} } };

    TLegend* leg = new TLegend(.62,.76,1,.9);
    leg->SetTextSize(0.02);
    leg->SetBorderSize(0);
    leg->SetFillColor(0);
    leg->SetFillStyle(0);

    h->GetXaxis()->SetTitle( var=="Rel" ? "p_{T}^{Jet}/p_{T}^{ref}" : (var=="Eta" ? "#Delta#eta" : "#Delta#phi") );
    h->GetXaxis()->SetNdivisions(5,5,0);
    h->GetYaxis()->SetNdivisions(5,5,0);

    float ymax=0; int nfiles = 0;
    // iterating over input files
    for (iter = inname.begin(); iter != inname.end(); ++iter){
      tf.push_back(TFile::Open(*iter));						//opens the input file
      
      for (auto& pair : algs) {
        TString palg = pair.first;
	//gets directory
        TDirectoryFile* tdir1 = (TDirectoryFile*) tf.back()->Get( Form("ak%i%sl1l2l3", r, palg.Data()) );
        if (!tdir1) {
          std::cout << Form("ak%i%sl1l2l3", r, palg.Data()) << " not found in " << *iter <<", skipping..." << std::endl;
          continue; 							//skips for directory not found
        }
        TH1F* halg1 = (TH1F*) tdir1->Get(name);					//gets the histogram
        halg1->Scale( 1 / halg1->Integral() );

        if (halg1->GetMaximum() > ymax) ymax = halg1->GetMaximum();		//normalization

        halg1->SetMarkerSize(0.8);
        halg1->SetMarkerStyle(pair.second.second+nfiles*5);			//sets different marker style 
        halg1->SetMarkerColor(pair.second.first+nfiles*2);			//and color for different input files
        halg1->SetLineColor(pair.second.first+nfiles*2);

        TString label = "PF";
        if (palg.Contains("pfchs"))      label = "PF+CHS, "+*iter;
        else if (palg.Contains("puppi")) label = "PUPPI, "+*iter;

        leg->AddEntry(halg1, label.Data(), "pl");

        halg1->Draw("samepe");
      }
      nfiles++ ;
    }
    h->GetYaxis()->SetRangeUser(0, ymax*1.4);
    leg->Draw();

    text.DrawLatex(0.2, 0.87, "Anti-k_{T}");
    text.DrawLatex(0.2, 0.82, Form("R=0.%i", r));

    text.DrawLatex( 0.35, 0.87, Form("%2.1f#leq#eta<%2.1f", eta1, eta2) );
    text.DrawLatex( 0.35, 0.82, Form("%i#leq#mu<%i", mu1, mu2) );
    text.DrawLatex( pt1==1000 ? 0.4 : 0.35, 0.77, Form("%i#leqp_{T}^{Ref}(GeV)<%i", pt1, pt2) );
  }
  else {
    float ymax = 0; int marker=0; 
    for (iter = inname.begin(); iter != inname.end(); ++iter){
      tf.push_back(TFile::Open(*iter));						//opens the input file
  
      TDirectoryFile* tdir1 = (TDirectoryFile*) tf.back()->Get( Form("ak%i%sl1l2l3", r, alg.Data()) );	//gets directory
        if (!tdir1) {
          std::cout << Form("ak%i%sl1l2l3", r, alg.Data()) << " not found in " << *iter <<", skipping..." << std::endl;
          continue; 							//skips for directory not found
        }
      TH1F* h1 = (TH1F*) tdir1->Get(name);				//gets the histogram
      if (ninput>1) h1->Scale( 1 / h1->Integral() );			//for more than 1 input file, apply normalization
      if (h1->GetMaximum() > ymax) ymax = h1->GetMaximum();

      h1->Draw("samepe");

      h1->SetMarkerSize(0.6);
      h1->SetMarkerStyle(20 + marker);
      h1->SetMarkerColor(2 + marker);
      h1->SetLineColor(2 + marker);
      marker +=1 ;

      h->GetXaxis()->SetTitle( h1->GetXaxis()->GetTitle() );
      h->GetYaxis()->SetRangeUser(0, ymax*1.4 );
      h->GetXaxis()->SetNdivisions(5,5,0);
    }
    if (var=="Eta" || var=="Phi") h->GetXaxis()->SetRangeUser(-0.5, 0.5);
    else                          h->GetXaxis()->SetRangeUser(0, 2);

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
      text.DrawLatex(0.2, 0.72, "Red = UL17");          //if we are using two eras, use these two lines to denote color. 
      text.DrawLatex(0.2, 0.67, "Green = UL18");	//
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
