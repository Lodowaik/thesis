from ROOT import TCanvas, TFile, TTree, TH1F, TH2F


def main():

  import numpy as np

  ttbarFile = TFile.Open("mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root","READ")
  ttbarTree = ttbarFile.Get("AnalysisTree")
  
  entries=ttbarTree.GetEntries()
  print("from file %s read tree %s with entries %d" %(ttbarFile.GetName(),ttbarTree.GetName(),entries))

  outfile = TFile.Open("output_variabili.root","RECREATE")
  histos = {}
  
  #pt, eta e phi dei muoni con origine bc (segnale)
  histos["muon_pt_signal"] = TH1F("muon_pt_signal","muon pt signal ; muon pt signal [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_signal"] = TH1F("muon_eta_signal","muon eta signal; muon eta signal; entries", 100, -3 , 3)
  histos["muon_phi_signal"] = TH1F("muon_phi_signal","muon phi signal; muon phi signal; entries", 20, -3.5 , 3.5)
  
  #muoni con origine s oppure ghost, aka il mio background
  histos["muon_pt_bgd"] = TH1F("muon_pt_bgd", "muon pt bgd ; muon pt bgd [GeV] ; entries", 100, 0, 100)
  histos["muon_eta_bgd"] = TH1F("muon_eta_bgd","muon eta bgd; muon eta bgd; entries", 100, -3 , 3)
  histos["muon_phi_bgd"] = TH1F("muon_phi_bgd","muon phi bgd; muon phi bgd; entries", 20, -3.5 , 3.5)
 
  
  #nprecision_Layers (numero di layers attaversati nel muon spectrometer)
  histos["muon_npl_signal"] = TH1F("muon_npl_signal","muon npl signal ; muon npl signal ; entries", 5, 0 , 5)
  histos["muon_npl_bgd"] = TH1F("muon_npl_bgd","muon npl bgd ; muon npl bgd ; entries", 5, 0 , 5)
  
  #reducedChi2 (Chi quadro diviso numero di gradi di libertà)
  histos["muon_chi2_signal"] = TH1F("muon_chi2_signal", "muon chi2 signal; muon chi2 signal; entries", 100, 0, 10)
  histos["muon_chi2_bgd"] = TH1F("muon_chi2_bgd", "muon chi2 bgd; muon chi2 bgd; entries", 100, 0, 10)
  
  #qOverPsignificance
  histos["muon_qp_signal"] = TH1F("muon_qp_signal", "muon qp signal; muon qp signal; entries", 100, 0, 25)
  histos["muon_qp_bgd"] = TH1F("muon_qp_bgd", "muon qp bgd; muon qp bgd; entries", 100, 0, 25)
  
  #momentum imbalance (rho')
  histos["muon_rho_signal"] = TH1F("muon_rho_signal", "muon rho signal; muon rho signal; entries", 100, -3, 10)
  histos["muon_rho_bgd"] = TH1F("muon_rho_bgd", "muon rho bgd; muon rho bgd; entries", 100, -3, 10)
  
  #scattering Curvature Significance
  histos["muon_scs_signal"] = TH1F("muon_scs_signal", "muon scs signal; muon scs signal; entries", 100, 0, 15)
  histos["muon_scs_bgd"] = TH1F("muon_scs_bgd", "muon scs bgd; muon scs bgd; entries", 100, 0, 15)
  
  #scattering Neighbour Significance
  histos["muon_sns_signal"] = TH1F("muon_sns_signal", "muon sns signal; muon sns signal; entries", 100, 0, 20)
  histos["muon_sns_bgd"] = TH1F("muon_sns_bgd", "muon sns bgd; muon sns bgd; entries", 100, 0, 20)
  
  
  
  #calcolo di qOverPsignificance per tutti i muoni
  #muon_qOverP_sign = np.zeros_like(muon_id_qOverP) #perché np.zeros_like non funziona su sti alberelli perché
  for e in ttbarTree:
    for imu in range (0, len(e.muon_id_qOverP)):
      #e.muon_qOverP_sign[imu] = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
      e.muon_id_qOverP[imu] = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
      
     #BACKGROUND = S + GHOST
     #SEGNALE = BC
     
    #for imu in range(0,len(e.muon_pt)):
      if ((e.muon_pt[imu]<=4000) or (abs(e.muon_eta[imu])>=2.5) or (e.muon_author[imu]!=1)):
        continue
      
      #istogrammi dei muoni con origine BC aka il SEGNALE
      if (25<=e.muon_truthOrigin[imu]<=29) or (32<=e.muon_truthOrigin[imu]<=33):
        histos["muon_pt_signal"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_signal"].Fill(e.muon_eta[imu])
        histos["muon_phi_signal"].Fill(e.muon_phi[imu])
        histos["muon_npl_signal"].Fill(e.muon_nprecisionLayers[imu])
        histos["muon_chi2_signal"].Fill(e.muon_reducedChi2[imu])
        #histos["muon_qp_signal"].Fill(e.muon_qOverP_sign[imu])
        histos["muon_qp_signal"].Fill((e.muon_id_qOverP[imu])**2)
        histos["muon_rho_signal"].Fill(e.muon_momentumBalanceSig[imu])
        histos["muon_scs_signal"].Fill((e.muon_scatteringCurvatureSig[imu])**2)
        histos["muon_sns_signal"].Fill((e.muon_scatteringNeighbourSig[imu])**2)
        
      #istogrammi dei muoni di BACKGROUND (s + ghost)  
      if ((e.muon_truthOrigin[imu]==0) or (23<=e.muon_truthOrigin[imu]<=24) or (30<=e.muon_truthOrigin[imu]<=31) or (34<=e.muon_truthOrigin[imu]<=35)):
        histos["muon_npl_bgd"].Fill(e.muon_nprecisionLayers[imu])
        histos["muon_chi2_bgd"].Fill(e.muon_reducedChi2[imu])
        histos["muon_qp_bgd"].Fill((e.muon_id_qOverP[imu])**2)
        histos["muon_rho_bgd"].Fill(e.muon_momentumBalanceSig[imu])
        histos["muon_scs_bgd"].Fill((e.muon_scatteringCurvatureSig[imu])**2)
        histos["muon_sns_bgd"].Fill((e.muon_scatteringNeighbourSig[imu])**2)
        histos["muon_pt_bgd"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_bgd"].Fill(e.muon_eta[imu])
        histos["muon_phi_bgd"].Fill(e.muon_phi[imu])
      
  for key, value in histos.items():
    print("writing %s histogram to file %s" % (value.GetName(),outfile.GetName()))
    outfile.WriteTObject(value)
   
  
  print("closing input file %s" % ttbarFile.GetName())
  ttbarFile.Close()
  print("output written to file %s" % outfile.GetName())
  outfile.Close()    
      
     
  return

if __name__ == "__main__":
  main()
  
  
  #ao pare che funziona
     

 
    
      










