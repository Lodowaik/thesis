from ROOT import TCanvas, TFile, TTree, TH1F, TH2F

def main():
  
  ttbarFile = TFile.Open("mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root","READ")
  ttbarTree = ttbarFile.Get("AnalysisTree")
  
  entries=ttbarTree.GetEntries()
  print("from file %s read tree %s with entries %d" %(ttbarFile.GetName(),ttbarTree.GetName(),entries))
  
  outfile = TFile.Open("outfile_tree.root","RECREATE")
  histos = {}
  histos["muon_pt_s"] = TH1F("muon_pt_s","muon pt s ; muon pt s [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_s"] = TH1F("muon_eta_s","muon eta s; muon eta s; entries", 100, -3 , 3)
  histos["muon_phi_s"] = TH1F("muon_phi_s","muon phi s; muon phi s; entries", 20, -3.5 , 3.5)
  histos["muon_d0_s"] = TH1F("muon_d0_s","muon d0 s; muon d0 s; entries", 100, -2 , 2)
  histos["muon_z0_s"] = TH1F("muon_z0_s","muon z0 s; muon z0 s; entries", 100, -200 , 200)
  histos["muon_e_s"] = TH1F("muon_e_s","muon e s; muon e s [GeV] ; entries", 100, 0 , 500)
  #histos["truthmuon_index"] = TH1F("truthmuon_index", "truthmuon_index; truthmuon_index; entries", 31,-1, 30)
  #histos["truthmuon_origin"] = TH1F("truthmuon_origin", "truthmuon_origin; truthmuon_origin; entries", 31,-1, 30)
  #histos["muon_index"] = TH1F("muon_index", "muon_index; muon_index; entries", 31,-1, 30)
  #histos["muon_origin"] = TH1F("muon_origin", "muon_origin; muon_origin; entries", 31,-1, 40)
  
  histos["diff_muon_pt_s"] = TH1F("diff_muon_pt_s", "diff_muon_pt_s; diff_muon_pt_s [GeV]; entries", 100, -15, 15)
  histos["diff_muon_eta_s"] = TH1F("diff_muon_eta_s", "diff_muon_eta_s; diff_muon_eta_s; entries", 100, -1, 1)
  histos["diff_muon_phi_s"] = TH1F("diff_muon_phi_s", "diff_muon_phi_s; diff_muon_phi_s; entries", 100, -1, 1)
  #histos["diff_muon_d0_bc"] = TH1F("diff_muon_d0_bc", "diff_muon_d0_bc; diff_muon_d0_bc ; entries", 100, -0.5, 0.5)
  #histos["diff_muon_z0_bc"] = TH1F("diff_muon_z0_bc", "diff_muon_z0_bc; diff_muon_z0_bc ; entries", 100, -15, 15)
  #histos["diff_muon_e_bc"] = TH1F("diff_muon_e_bc", "diff_muon_e_bc; diff_muon_e_bc [GeV]; entries", 100, -50, 50)
  
  
  entry = 0
  
  for e in ttbarTree:
    
    entry+=1
    
    if((entry%10000)==0):
      print("reading entry %d out of %d" % (entry,entries))
    
    if(entry>1e5):
      break
    
    for imu in range(0,len(e.muon_pt)):
      if (e.muon_pt[imu]<=4000) or (abs(e.muon_eta[imu])>=2.5):
        continue
      #if (e.truthmuon_muon_index[imu])<0:
        #print(f"In entry {entry} found muon with pt={e.muon_pt[imu]}")
      if (23<=e.muon_truthOrigin[imu]<=24) or (30<=e.muon_truthOrigin[imu]<=31) or (34<=e.muon_truthOrigin[imu]<=35):
        
        histos["muon_pt_s"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_s"].Fill(e.muon_eta[imu])
        histos["muon_phi_s"].Fill(e.muon_phi[imu])
        histos["muon_d0_s"].Fill(e.muon_d0[imu])
        histos["muon_z0_s"].Fill(e.muon_z0[imu])
        histos["muon_e_s"].Fill(e.muon_e[imu]/1000.)
      #histos["muon_index"].Fill(e.muon_truthmuon_index[imu])
      #histos["muon_origin"].Fill(e.muon_truthOrigin[imu])
      #else:
       # continue
        k=(e.muon_truthmuon_index[imu])
        if (e.muon_truthmuon_index[imu]==-1):
          continue
        #e.muon_pt[k]=e.muon_pt[imu]
       # for k in range (0, min(len(e.muon_pt), len(e.truthmuon_pt))):
        diff_pt=(e.muon_pt[imu])-(e.truthmuon_pt[k])
        histos["diff_muon_pt_s"].Fill(diff_pt/1000.)
        diff_eta=(e.muon_eta[imu])-(e.truthmuon_eta[k])
        histos["diff_muon_eta_s"].Fill(diff_eta)
        diff_phi=(e.muon_phi[imu])-(e.truthmuon_phi[k])
        histos["diff_muon_phi_s"].Fill(diff_phi)
        #diff_d0=(e.muon_d0[imu])-(e.truthmuon_d0[k])
        #histos["diff_muon_d0_bc"].Fill(diff_d0)
        #diff_z0=(e.muon_z0[imu])-(e.truthmuon_z0[k])
        #histos["diff_muon_z0_bc"].Fill(diff_z0)
        
        #diff_e=(e.muon_e[imu])-(e.truthmuon_e[k])
        #histos["diff_muon_e_bc"].Fill(diff_e/1000.)
      #end of loop on muons
    
  #end of loop on entries
    #for index in range (0, len(e.truthmuon_muon_index)):
      #histos["truthmuon_index"].Fill(e.truthmuon_muon_index[index])
      #histos["truthmuon_origin"].Fill(e.truthmuon_origin[index])
      
  for key, value in histos.items():
    print("writing %s histogram to file %s" % (value.GetName(),outfile.GetName()))
    outfile.WriteTObject(value)
    value.SaveAs("muon_pt.pdf", "")
  
  print("closing input file %s" % ttbarFile.GetName())
  ttbarFile.Close()
  print("output written to file %s" % outfile.GetName())
  outfile.Close()
  
  return

if __name__ == "__main__":
  main()
