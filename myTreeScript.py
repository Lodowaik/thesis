from ROOT import TCanvas, TFile, TTree, TH1F, TH2F, TEfficiency 

def myWP(reducedChi2, qOverPsign, rho):
  #if ((e.muon_reducedChi2[imu]<=2) and (((qOverPsign)**2)<=6) and (-1<=(e.muon_momentumBalanceSig[imu])<=4) \
   #     and (((e.muon_scatteringCurvatureSig[imu])**2)<=5) and (((e.muon_scatteringNeighbourSig[imu])**2)<=6.5))
   if(reducedChi2<=1.5 and qOverPsign<=5 and -1<=rho<=4): return True
   return False

def main():
  
  ttbarFile = TFile.Open("../data/mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root","READ")
  ttbarTree = ttbarFile.Get("AnalysisTree")
  
  entries=ttbarTree.GetEntries()
  print("from file %s read tree %s with entries %d" %(ttbarFile.GetName(),ttbarTree.GetName(),entries))
  
  outfile = TFile.Open("out/outfile_tree.root","RECREATE")
  histos = {}
  #tutti i muoni
  histos["muon_pt"] = TH1F("muon_pt","muon pt ; muon pt [GeV] ; entries", 100, 0 , 150)
  histos["muon_eta"] = TH1F("muon_eta","muon eta ; muon eta ; entries", 100, -3 , 3)
  histos["muon_phi"] = TH1F("muon_phi","muon phi ; muon phi ; entries", 20, -3.5 , 3.5)
  histos["muon_d0"] = TH1F("muon_d0","muon d0 ; muon d0 ; entries", 100, -2 , 2)
  histos["muon_z0"] = TH1F("muon_z0","muon z0 ; muon z0 ; entries", 100, -200 , 200)
  histos["muon_e"] = TH1F("muon_e","muon e ; muon e ; entries", 100, 0 , 500)
  
  #muoni con origine W
  histos["muon_pt_W"] = TH1F("muon_pt_W","muon pt W ; muon pt W [GeV] ; entries", 100, 0 , 150)
  histos["muon_eta_W"] = TH1F("muon_eta_W","muon eta W; muon eta W; entries", 100, -3 , 3)
  histos["muon_phi_W"] = TH1F("muon_phi_W","muon phi W; muon phi W; entries", 20, -3.5 , 3.5)
  histos["muon_d0_W"] = TH1F("muon_d0_W","muon d0 W; muon d0 W; entries", 100, -2 , 2)
  histos["muon_z0_W"] = TH1F("muon_z0_W","muon z0 W; muon z0 W; entries", 100, -200 , 200)
  histos["muon_e_W"] = TH1F("muon_e_W","muon e W; muon e W [GeV] ; entries", 100, 0 , 500)
  
  #muoni con origine tau
  histos["muon_pt_tau"] = TH1F("muon_pt_tau","muon pt tau ; muon pt tau [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_tau"] = TH1F("muon_eta_tau","muon eta tau; muon eta tau; entries", 100, -3 , 3)
  histos["muon_phi_tau"] = TH1F("muon_phi_tau","muon phi tau; muon phi tau; entries", 20, -3.5 , 3.5)
  histos["muon_d0_tau"] = TH1F("muon_d0_tau","muon d0 tau; muon d0 tau; entries", 100, -2 , 2)
  histos["muon_z0_tau"] = TH1F("muon_z0_tau","muon z0 tau; muon z0 tau; entries", 100, -200 , 200)
  histos["muon_e_tau"] = TH1F("muon_e_tau","muon e tau; muon e tau [GeV] ; entries", 100, 0 , 500)
  
  #muoni con origine bc, aka il mio segnale
  histos["muon_pt_bc"] = TH1F("muon_pt_bc","muon pt bc ; muon pt bc [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_bc"] = TH1F("muon_eta_bc","muon eta bc; muon eta bc; entries", 100, -3 , 3)
  histos["muon_phi_bc"] = TH1F("muon_phi_bc","muon phi bc; muon phi bc; entries", 20, -3.5 , 3.5)
  histos["muon_d0_bc"] = TH1F("muon_d0_bc","muon d0 bc; muon d0 bc; entries", 100, -2 , 2)
  histos["muon_z0_bc"] = TH1F("muon_z0_bc","muon z0 bc; muon z0 bc; entries", 100, -200 , 200)
  histos["muon_e_bc"] = TH1F("muon_e_bc","muon e bc; muon e bc [GeV] ; entries", 100, 0 , 500)
  
  #muoni con origine s
  histos["muon_pt_s"] = TH1F("muon_pt_s","muon pt s ; muon pt s [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_s"] = TH1F("muon_eta_s","muon eta s; muon eta s; entries", 100, -3 , 3)
  histos["muon_phi_s"] = TH1F("muon_phi_s","muon phi s; muon phi s; entries", 20, -3.5 , 3.5)
  histos["muon_d0_s"] = TH1F("muon_d0_s","muon d0 s; muon d0 s; entries", 100, -2 , 2)
  histos["muon_z0_s"] = TH1F("muon_z0_s","muon z0 s; muon z0 s; entries", 100, -200 , 200)
  histos["muon_e_s"] = TH1F("muon_e_s","muon e s; muon e s [GeV] ; entries", 100, 0 , 500)
  
  #muoni con origine ghost
  histos["muon_pt_ghost"] = TH1F("muon_pt_ghost","muon pt ghost ; muon pt ghost [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_ghost"] = TH1F("muon_eta_ghost","muon eta ghost; muon eta ghost; entries", 100, -3 , 3)
  histos["muon_phi_ghost"] = TH1F("muon_phi_ghost","muon phi ghost; muon phi ghost; entries", 20, -3.5 , 3.5)
  histos["muon_d0_ghost"] = TH1F("muon_d0_ghost","muon d0 ghost; muon d0 ghost; entries", 100, -2 , 2)
  histos["muon_z0_ghost"] = TH1F("muon_z0_ghost","muon z0 ghost; muon z0 ghost; entries", 100, -200 , 200)
  histos["muon_e_ghost"] = TH1F("muon_e_ghost","muon e ghost; muon e ghost [GeV] ; entries", 100, 0 , 500)
  
  #muoni con origine s oppure ghost, aka il mio background
  histos["muon_pt_bgd"] = TH1F("muon_pt_bgd", "muon pt bgd ; muon pt bgd [GeV] ; entries", 100, 0, 100)
  histos["muon_eta_bgd"] = TH1F("muon_eta_bgd","muon eta bgd; muon eta bgd; entries", 100, -3 , 3)
  histos["muon_phi_bgd"] = TH1F("muon_phi_bgd","muon phi bgd; muon phi bgd; entries", 20, -3.5 , 3.5)
 
  
  
  
  
  #differenze reco-truth per i muoni con origine W
  histos["diff_muon_pt_W"] = TH1F("diff_muon_pt_W", "diff_muon_pt_W; diff_muon_pt_W [GeV]; entries", 100, -15, 15)
  histos["diff_muon_eta_W"] = TH1F("diff_muon_eta_W", "diff_muon_eta_W; diff_muon_eta_W; entries", 100, -0.2, 0.2)
  histos["diff_muon_phi_W"] = TH1F("diff_muon_phi_W", "diff_muon_phi_W; diff_muon_phi_W; entries", 100, -0.2, 0.2)
  
  #differenze reco-truth per i muoni con origine tau
  histos["diff_muon_pt_tau"] = TH1F("diff_muon_pt_tau", "diff_muon_pt_tau; diff_muon_pt_tau [GeV]; entries", 100, -15, 15)
  histos["diff_muon_eta_tau"] = TH1F("diff_muon_eta_tau", "diff_muon_eta_tau; diff_muon_eta_tau; entries", 100, -0.2, 0.2)
  histos["diff_muon_phi_tau"] = TH1F("diff_muon_phi_tau", "diff_muon_phi_tau; diff_muon_phi_tau; entries", 100, -0.2, 0.2)
  
  #differenze reco-truth per i muoni con origine bc
  histos["diff_muon_pt_bc"] = TH1F("diff_muon_pt_bc", "diff_muon_pt_bc; diff_muon_pt_bc [GeV]; entries", 100, -15, 15)
  histos["diff_muon_eta_bc"] = TH1F("diff_muon_eta_bc", "diff_muon_eta_bc; diff_muon_eta_bc; entries", 100, -0.2, 0.2)
  histos["diff_muon_phi_bc"] = TH1F("diff_muon_phi_bc", "diff_muon_phi_bc; diff_muon_phi_bc; entries", 100, -0.2, 0.2)
  
  #differenze reco-truth per i muoni con origine s
  histos["diff_muon_pt_s"] = TH1F("diff_muon_pt_s", "diff_muon_pt_s; diff_muon_pt_s [GeV]; entries", 100, -15, 15)
  histos["diff_muon_eta_s"] = TH1F("diff_muon_eta_s", "diff_muon_eta_s; diff_muon_eta_s; entries", 100, -0.2, 0.2)
  histos["diff_muon_phi_s"] = TH1F("diff_muon_phi_s", "diff_muon_phi_s; diff_muon_phi_s; entries", 100, -0.2, 0.2)
  
  
  
  #errore relativo per i muoni con origine W
  histos["err_muon_pt_W"] = TH1F("err_muon_pt_W", "err_muon_pt_W; err_muon_pt_W ; entries", 100, -0.4, 0.4)
  histos["err_muon_eta_W"] = TH1F("err_muon_eta_W", "err_muon_eta_W; err_muon_eta_W; entries", 100, -0.03, 0.03)
  histos["err_muon_phi_W"] = TH1F("err_muon_phi_W", "err_muon_phi_W; err_muon_phi_W; entries", 100, -0.02, 0.02)
  
  #errore relativo per i muoni con origine tau
  histos["err_muon_pt_tau"] = TH1F("err_muon_pt_tau", "err_muon_pt_tau; err_muon_pt_tau ; entries", 100, -0.4, 0.4)
  histos["err_muon_eta_tau"] = TH1F("err_muon_eta_tau", "err_muon_eta_tau; err_muon_eta_tau ; entries", 100, -0.03, 0.03)
  histos["err_muon_phi_tau"] = TH1F("err_muon_phi_tau", "err_muon_phi_tau; err_muon_phi_tau ; entries", 100, -0.02, 0.02)
  
  #errore relativo per i muoni con origine bc
  histos["err_muon_pt_bc"] = TH1F("err_muon_pt_bc", "err_muon_pt_bc; err_muon_pt_bc ; entries", 100, -0.4, 0.4)
  histos["err_muon_eta_bc"] = TH1F("err_muon_eta_bc", "err_muon_eta_bc; err_muon_eta_bc ; entries", 100, -0.03, 0.03)
  histos["err_muon_phi_bc"] = TH1F("err_muon_phi_bc", "err_muon_phi_bc; err_muon_phi_bc ; entries", 100, -0.02, 0.02)
  
  #errore relativo per i muoni con origine s
  histos["err_muon_pt_s"] = TH1F("err_muon_pt_s", "err_muon_pt_s; err_muon_pt_s ; entries", 100, -0.4, 0.4)
  histos["err_muon_eta_s"] = TH1F("err_muon_eta_s", "err_muon_eta_s; err_muon_eta_s ; entries", 100, -0.03, 0.03)
  histos["err_muon_phi_s"] = TH1F("err_muon_phi_s", "err_muon_phi_s; err_muon_phi_s ; entries", 100, -0.02, 0.02)
  
  #istogrammi delle differenze reco-truth e degli errori relativi dei muoni con origine s:
        #ha poco senso farli, giusto?
   
  num_tight_signal = 0
  num_tight_bgd = 0
  den_signal = 0
  den_bgd = 0
  num_tagli_signal = 0
  num_tagli_bgd = 0
  qOverPsign = 0
  
  effs={}
  effs["eff_Tight_sig_vs_pt"]= TEfficiency("eff_Tight_sig_vs_pt","eff Tight signal vs pt; p_{T} [GeV] ; #epsilon",10,0,40)
  effs["eff_tagli_sig_vs_pt"]= TEfficiency("eff_tagli_sig_vs_pt","eff tagli signal vs pt; p_{T} [GeV] ; #epsilon",10,0,40)
  effs["eff_Tight_bgd_vs_pt"]= TEfficiency("eff_Tight_bgd_vs_pt","eff Tight background vs pt; p_{T} [GeV] ; #epsilon",10,0,40)
  effs["eff_tagli_bgd_vs_pt"]= TEfficiency("eff_tagli_bgd_vs_pt","eff tagli background vs pt; p_{T} [GeV] ; #epsilon",10,0,40)
  
   
  #VETTORI CON NUMERO DI ENTRIES, MEDIA, (RMS, ) ERRORE SULLA MEDIA E DEVSTANDARD DI QUESTO ERRORE PER I MUONI CON ORIGINE W, TAU, BC, S
  #MEDIA, (RMS), ERRORE SULLA MEDIA E DEVSTANDARD DELL'ERRORE VANNO CALCOLATI PER PT, ETA E PHI QUINDI IN TUTTO DIOBALDACCHINP UN BORDELLO DI VETTORI 
  import numpy as np
  
  num_entries = np.zeros(4) 
  
  mean_pt = np.zeros(4) 
  mean_eta = np.zeros(4) 
  mean_phi = np.zeros(4) 
  
  rms_pt = np.zeros(4) 
  rms_eta = np.zeros(4) 
  rms_phi = np.zeros(4) 
  
  err_mean_pt = np.zeros(4) 
  err_mean_eta = np.zeros(4) 
  err_mean_phi = np.zeros(4) 
  
  err_stdev_pt = np.zeros(4)
  err_stdev_eta = np.zeros(4)
  err_stdev_phi = np.zeros(4)
  
   
  entry = 0
  
  for e in ttbarTree:
    
    entry+=1
    
    if((entry%10000)==0):
      print("reading entry %d out of %d" % (entry,entries))
    
    if(entry>1e5):
      break
    
    for imu in range(0,len(e.muon_pt)):
      qOverPsign = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
      if ((e.muon_pt[imu]<=4000) or (abs(e.muon_eta[imu])>=2.5) or (e.muon_author[imu]!=1)):
        continue
      #istogrammi di tutti i muoni
      histos["muon_pt"].Fill(e.muon_pt[imu]/1000.)
      histos["muon_eta"].Fill(e.muon_eta[imu])
      histos["muon_phi"].Fill(e.muon_phi[imu])
      histos["muon_d0"].Fill(e.muon_d0[imu])
      histos["muon_z0"].Fill(e.muon_z0[imu])
      histos["muon_e"].Fill(e.muon_e[imu]/1000.)
      
      #istogrammi dei muoni con origine W
      if (e.muon_truthOrigin[imu]==12):
        histos["muon_pt_W"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_W"].Fill(e.muon_eta[imu])
        histos["muon_phi_W"].Fill(e.muon_phi[imu])
        histos["muon_d0_W"].Fill(e.muon_d0[imu])
        histos["muon_z0_W"].Fill(e.muon_z0[imu])
        histos["muon_e_W"].Fill(e.muon_e[imu]/1000.)
     
        #istogrammi delle differenze reco-truth per i muoni con origine W
        k=(e.muon_truthmuon_index[imu])
        if (e.muon_truthmuon_index[imu]==-1):
          continue
        diff_pt=(e.muon_pt[imu])-(e.truthmuon_pt[k])
        histos["diff_muon_pt_W"].Fill(diff_pt/1000.)
        diff_eta=(e.muon_eta[imu])-(e.truthmuon_eta[k])
        histos["diff_muon_eta_W"].Fill(diff_eta)
        diff_phi=(e.muon_phi[imu])-(e.truthmuon_phi[k])
        histos["diff_muon_phi_W"].Fill(diff_phi)
        
        #istogrammi degli errori relativi per i muoni con origine W
        err_pt=((e.muon_pt[imu])-(e.truthmuon_pt[k]))/(e.truthmuon_pt[k])
        histos["err_muon_pt_W"].Fill(err_pt)
        err_eta=((e.muon_eta[imu])-(e.truthmuon_eta[k]))/(e.truthmuon_eta[k])
        histos["err_muon_eta_W"].Fill(err_eta)
        err_phi=((e.muon_phi[imu])-(e.truthmuon_phi[k]))/(e.truthmuon_phi[k])
        histos["err_muon_phi_W"].Fill(err_phi)
      
      
      
      #istogrammi dei muoni con origine tau
      if (e.muon_truthOrigin[imu]==9):
        histos["muon_pt_tau"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_tau"].Fill(e.muon_eta[imu])
        histos["muon_phi_tau"].Fill(e.muon_phi[imu])
        histos["muon_d0_tau"].Fill(e.muon_d0[imu])
        histos["muon_z0_tau"].Fill(e.muon_z0[imu])
        histos["muon_e_tau"].Fill(e.muon_e[imu]/1000.)
        
        #istogrammi delle differenze reco-truth per i muoni con origine tau
        k=(e.muon_truthmuon_index[imu])
        if (e.muon_truthmuon_index[imu]==-1):
          continue
        diff_pt=(e.muon_pt[imu])-(e.truthmuon_pt[k])
        histos["diff_muon_pt_tau"].Fill(diff_pt/1000.)
        diff_eta=(e.muon_eta[imu])-(e.truthmuon_eta[k])
        histos["diff_muon_eta_tau"].Fill(diff_eta)
        diff_phi=(e.muon_phi[imu])-(e.truthmuon_phi[k])
        histos["diff_muon_phi_tau"].Fill(diff_phi)
        
        #istogrammi degli errori relativi per i muoni con origine tau
        err_pt=((e.muon_pt[imu])-(e.truthmuon_pt[k]))/(e.truthmuon_pt[k])
        histos["err_muon_pt_tau"].Fill(err_pt)
        err_eta=((e.muon_eta[imu])-(e.truthmuon_eta[k]))/(e.truthmuon_eta[k])
        histos["err_muon_eta_tau"].Fill(err_eta)
        err_phi=((e.muon_phi[imu])-(e.truthmuon_phi[k]))/(e.truthmuon_phi[k])
        histos["err_muon_phi_tau"].Fill(err_phi)
      
      
      
      #istogrammi dei muoni con origine bc
      if (25<=e.muon_truthOrigin[imu]<=29) or (32<=e.muon_truthOrigin[imu]<=33):
        den_signal = den_signal + 1
          #calcolo di qOverPsignificance per tutti i muoni
  #muon_qOverP_sign = np.zeros_like(muon_id_qOverP) #perché np.zeros_like non funziona su sti alberelli perché
 
    
      #e.muon_qOverP_sign[imu] = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
        #qOverPsign = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
      #  if ((e.muon_Tight[imu])>=0.5):
        if ((e.muon_Tight[imu])=='\x01'):
          num_tight_signal = num_tight_signal+1
        effs["eff_Tight_sig_vs_pt"].Fill((e.muon_Tight[imu])=='\x01',(e.muon_pt[imu]/1000.))
        effs["eff_tagli_sig_vs_pt"].Fill(myWP(reducedChi2=e.muon_reducedChi2[imu], qOverPsign=qOverPsign, rho = e.muon_momentumBalanceSig[imu]),\
        (e.muon_pt[imu]/1000.))
        #if ((e.muon_reducedChi2[imu]<=2) and (((qOverPsign)**2)<=6) and (-1<=(e.muon_momentumBalanceSig[imu])<=4) \
        #and (((e.muon_scatteringCurvatureSig[imu])**2)<=5) and (((e.muon_scatteringNeighbourSig[imu])**2)<=6.5)):
        if(myWP(reducedChi2=e.muon_reducedChi2[imu], qOverPsign=qOverPsign, rho = e.muon_momentumBalanceSig[imu])):
          num_tagli_signal = num_tagli_signal + 1
        histos["muon_pt_bc"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_bc"].Fill(e.muon_eta[imu])
        histos["muon_phi_bc"].Fill(e.muon_phi[imu])
        histos["muon_d0_bc"].Fill(e.muon_d0[imu])
        histos["muon_z0_bc"].Fill(e.muon_z0[imu])
        histos["muon_e_bc"].Fill(e.muon_e[imu]/1000.)
        #(e.muon_nprecisionLayers[imu]>1) and 
        
        #istogrammi delle differenze reco-truth per i muoni con origine bc
        k=(e.muon_truthmuon_index[imu])
        if (e.muon_truthmuon_index[imu]==-1):
          continue
        diff_pt=(e.muon_pt[imu])-(e.truthmuon_pt[k])
        histos["diff_muon_pt_bc"].Fill(diff_pt/1000.)
        diff_eta=(e.muon_eta[imu])-(e.truthmuon_eta[k])
        histos["diff_muon_eta_bc"].Fill(diff_eta)
        diff_phi=(e.muon_phi[imu])-(e.truthmuon_phi[k])
        histos["diff_muon_phi_bc"].Fill(diff_phi)
        
        #istogrammi degli errori relativi per i muoni con origine bc
        err_pt=((e.muon_pt[imu])-(e.truthmuon_pt[k]))/(e.truthmuon_pt[k])
        histos["err_muon_pt_bc"].Fill(err_pt)
        err_eta=((e.muon_eta[imu])-(e.truthmuon_eta[k]))/(e.truthmuon_eta[k])
        histos["err_muon_eta_bc"].Fill(err_eta)
        err_phi=((e.muon_phi[imu])-(e.truthmuon_phi[k]))/(e.truthmuon_phi[k])
        histos["err_muon_phi_bc"].Fill(err_phi)
        
      
      
      #istogrammi dei muoni con origine s
      if ((23<=e.muon_truthOrigin[imu]<=24) or (30<=e.muon_truthOrigin[imu]<=31) or (34<=e.muon_truthOrigin[imu]<=35)):
        histos["muon_pt_s"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_s"].Fill(e.muon_eta[imu])
        histos["muon_phi_s"].Fill(e.muon_phi[imu])
        histos["muon_d0_s"].Fill(e.muon_d0[imu])
        histos["muon_z0_s"].Fill(e.muon_z0[imu])
        histos["muon_e_s"].Fill(e.muon_e[imu]/1000.)  
        
        #istogrammi delle differenze reco-truth per i muoni con origine s
        k=(e.muon_truthmuon_index[imu])
        if (e.muon_truthmuon_index[imu]==-1):
          continue
        diff_pt=(e.muon_pt[imu])-(e.truthmuon_pt[k])
        histos["diff_muon_pt_s"].Fill(diff_pt/1000.)
        diff_eta=(e.muon_eta[imu])-(e.truthmuon_eta[k])
        histos["diff_muon_eta_s"].Fill(diff_eta)
        diff_phi=(e.muon_phi[imu])-(e.truthmuon_phi[k])
        histos["diff_muon_phi_s"].Fill(diff_phi)
        
        #istogrammi degli errori relativi per i muoni con origine s
        err_pt=((e.muon_pt[imu])-(e.truthmuon_pt[k]))/(e.truthmuon_pt[k])
        histos["err_muon_pt_s"].Fill(err_pt)
        err_eta=((e.muon_eta[imu])-(e.truthmuon_eta[k]))/(e.truthmuon_eta[k])
        histos["err_muon_eta_s"].Fill(err_eta)
        err_phi=((e.muon_phi[imu])-(e.truthmuon_phi[k]))/(e.truthmuon_phi[k])
        histos["err_muon_phi_s"].Fill(err_phi)
        
      
    #for imu in range(0,len(e.muon_pt)):
      
      if ((e.muon_pt[imu]<=4000) or (abs(e.muon_eta[imu])>=2.5) or (e.muon_author[imu]!=1)):
        continue
      #istogrammi dei muoni con origine ghost
      if e.muon_truthOrigin[imu]==0:
        histos["muon_pt_ghost"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_ghost"].Fill(e.muon_eta[imu])
        histos["muon_phi_ghost"].Fill(e.muon_phi[imu])
        histos["muon_d0_ghost"].Fill(e.muon_d0[imu])
        histos["muon_z0_ghost"].Fill(e.muon_z0[imu])
        histos["muon_e_ghost"].Fill(e.muon_e[imu]/1000.)
      
      #istogrammi dei muoni di background (s e ghost)
      if ((e.muon_truthOrigin[imu]==0) or (23<=e.muon_truthOrigin[imu]<=24) or (30<=e.muon_truthOrigin[imu]<=31) or (34<=e.muon_truthOrigin[imu]<=35)):
        den_bgd = den_bgd + 1
        #print(f"aaa {repr(e.muon_Tight[imu])}")
          #calcolo di qOverPsignificance per tutti i muoni
  #muon_qOverP_sign = np.zeros_like(muon_id_qOverP) #perché np.zeros_like non funziona su sti alberelli perché

      #e.muon_qOverP_sign[imu] = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
        #qOverPsign = (e.muon_id_qOverP[imu]-e.muon_me_qOverP[imu])/((e.muon_me_qOverPsigma[imu]**2 + e.muon_id_qOverPsigma[imu]**2)**0.5)
        
        if ((e.muon_Tight[imu])=='\x01'):
          num_tight_bgd = num_tight_bgd + 1
        #if  ((e.muon_reducedChi2[imu]>2) or (((qOverPsign)**2)>6) or (((e.muon_momentumBalanceSig[imu])<-1) or ((e.muon_momentumBalanceSig[imu])>4)) \
        #or (((e.muon_scatteringCurvatureSig[imu])**2)>5) or (((e.muon_scatteringNeighbourSig[imu])**2)>6.5)):
        if(myWP(reducedChi2=e.muon_reducedChi2[imu], qOverPsign=qOverPsign, rho = e.muon_momentumBalanceSig[imu])):
          num_tagli_bgd = num_tagli_bgd + 1
        effs["eff_Tight_bgd_vs_pt"].Fill((e.muon_Tight[imu])=='\x01',(e.muon_pt[imu]/1000.))
        effs["eff_tagli_bgd_vs_pt"].Fill(myWP(reducedChi2=e.muon_reducedChi2[imu], qOverPsign=qOverPsign, rho = e.muon_momentumBalanceSig[imu]),\
        (e.muon_pt[imu]/1000.))
        histos["muon_pt_bgd"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_bgd"].Fill(e.muon_eta[imu])
        histos["muon_phi_bgd"].Fill(e.muon_phi[imu])
      #(e.muon_nprecisionLayers[imu]<=1) and 
        
        #istogrammi delle differenze reco-truth e degli errori relativi dei muoni con origine s:
        #ha poco senso farli, giusto?
  
  num_entries[0] = (histos["diff_muon_pt_W"].GetEntries())
  num_entries[1] = (histos["diff_muon_pt_tau"].GetEntries())
  num_entries[2] = (histos["diff_muon_pt_bc"].GetEntries())
  num_entries[3] = (histos["diff_muon_pt_s"].GetEntries())
  
  mean_pt[0] = (histos["muon_pt_W"].GetMean())
  mean_pt[1] = (histos["muon_pt_tau"].GetMean())
  mean_pt[2] = (histos["muon_pt_bc"].GetMean())
  mean_pt[3] = (histos["muon_pt_s"].GetMean())
  
  mean_eta[0] = (histos["muon_eta_W"].GetMean())
  mean_eta[1] = (histos["muon_eta_tau"].GetMean())
  mean_eta[2] = (histos["muon_eta_bc"].GetMean())
  mean_eta[3] = (histos["muon_eta_s"].GetMean())
  
  mean_phi[0] = (histos["muon_phi_W"].GetMean())
  mean_phi[1] = (histos["muon_phi_tau"].GetMean())
  mean_phi[2] = (histos["muon_phi_bc"].GetMean())
  mean_phi[3] = (histos["muon_phi_s"].GetMean())
  
  rms_pt[0] = (histos["muon_pt_W"].GetStdDev())
  rms_pt[1] = (histos["muon_pt_tau"].GetStdDev())
  rms_pt[2] = (histos["muon_pt_bc"].GetStdDev())
  rms_pt[3] = (histos["muon_pt_s"].GetStdDev())
 
  rms_eta[0] = (histos["muon_eta_W"].GetStdDev())
  rms_eta[1] = (histos["muon_eta_tau"].GetStdDev())
  rms_eta[2] = (histos["muon_eta_bc"].GetStdDev())
  rms_eta[3] = (histos["muon_eta_s"].GetStdDev())
   
  rms_phi[0] = (histos["muon_phi_W"].GetStdDev())
  rms_phi[1] = (histos["muon_phi_tau"].GetStdDev())
  rms_phi[2] = (histos["muon_phi_bc"].GetStdDev())
  rms_phi[3] = (histos["muon_phi_s"].GetStdDev())
  
  err_mean_pt[0] = (histos["err_muon_pt_W"].GetMean())
  err_mean_pt[1] = (histos["err_muon_pt_tau"].GetMean())
  err_mean_pt[2] = (histos["err_muon_pt_bc"].GetMean())
  err_mean_pt[3] = (histos["err_muon_pt_s"].GetMean())
  
  err_mean_eta[0] = (histos["err_muon_eta_W"].GetMean())
  err_mean_eta[1] = (histos["err_muon_eta_tau"].GetMean())
  err_mean_eta[2] = (histos["err_muon_eta_bc"].GetMean())
  err_mean_eta[3] = (histos["err_muon_eta_s"].GetMean())
  
  err_mean_phi[0] = (histos["err_muon_phi_W"].GetMean())
  err_mean_phi[1] = (histos["err_muon_phi_tau"].GetMean())
  err_mean_phi[2] = (histos["err_muon_phi_bc"].GetMean())
  err_mean_phi[3] = (histos["err_muon_phi_s"].GetMean())
  
  err_stdev_pt[0] = (histos["err_muon_pt_W"].GetStdDev())
  err_stdev_pt[1] = (histos["err_muon_pt_tau"].GetStdDev())
  err_stdev_pt[2] = (histos["err_muon_pt_bc"].GetStdDev())
  err_stdev_pt[3] = (histos["err_muon_pt_s"].GetStdDev())
  
  err_stdev_eta[0] = (histos["err_muon_eta_W"].GetStdDev())
  err_stdev_eta[1] = (histos["err_muon_eta_tau"].GetStdDev())
  err_stdev_eta[2] = (histos["err_muon_eta_bc"].GetStdDev())
  err_stdev_eta[3] = (histos["err_muon_eta_s"].GetStdDev())
  
  err_stdev_phi[0] = (histos["err_muon_phi_W"].GetStdDev())
  err_stdev_phi[1] = (histos["err_muon_phi_tau"].GetStdDev())
  err_stdev_phi[2] = (histos["err_muon_phi_bc"].GetStdDev())
  err_stdev_phi[3] = (histos["err_muon_phi_s"].GetStdDev())
  
  
    #end of loop on muons
    
  #end of loop on entries
  
 
  for key, value in histos.items():
    print("writing %s histogram to file %s" % (value.GetName(),outfile.GetName()))
    outfile.WriteTObject(value)
  
  for key, value in effs.items():
    print("writing %s effs to file %s" % (value.GetName(),outfile.GetName()))
    outfile.WriteTObject(value)
   
  
  print("closing input file %s" % ttbarFile.GetName())
  ttbarFile.Close()
  print("output written to file %s" % outfile.GetName())
  outfile.Close()
  
  print("numero di muoni con origine W, tau, bc, s: ",         num_entries)
  
  print("media di pt per i muoni con origine W, tau, bc, s: ", mean_pt)
  print("media di eta per i muoni ecc",                        mean_eta)
  print ("media di phi per i muoni ecc",                       mean_phi)
  
  print("deviazione standard di pt per i muoni ecc: ",         rms_pt)
  print("deviazione standard di eta per i muoni ecc: ",        rms_eta)
  print("deviazione standard di phi per i muoni ecc: ",        rms_phi)
  
  print("err relativo medio di pt per i muoni ecc: ",          err_mean_pt)
  print("err relativo medio di eta: ",                         err_mean_eta)
  print("err relativo medio di phi: ",                         err_mean_phi)
  
  print("dev standard dell'err relativo di pt per i muoni ecc: ",          err_stdev_pt)
  print("dev standard dell'err relativo di eta: ",                         err_stdev_eta)
  print("dev standard dell'err relativo di phi: ",                         err_stdev_phi)

  print("TIGHT efficienza per il segnale sui reco:", num_tight_signal/den_signal)
  print("TIGHT efficienza per il background sui reco:", num_tight_bgd/den_bgd)
  print("PROVA efficienza per il segnale sui reco:", num_tagli_signal/den_signal)
  print("PROVA efficienza per il background sui reco:", num_tagli_bgd/den_bgd)
  return

if __name__ == "__main__":
  main()
