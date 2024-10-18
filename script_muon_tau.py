from ROOT import TCanvas, TFile, TTree, TH1F, TH2F

def main():
  
  ttbarFile = TFile.Open("mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root","READ")
  ttbarTree = ttbarFile.Get("AnalysisTree")
  
  entries=ttbarTree.GetEntries()
  print("from file %s read tree %s with entries %d" %(ttbarFile.GetName(),ttbarTree.GetName(),entries))
  
  outfile = TFile.Open("outfile_tree.root","RECREATE")
  histos = {}
  histos["muon_pt_tau"] = TH1F("muon_pt_tau","muon pt tau ; muon pt tau [GeV] ; entries", 100, 0 , 100)
  histos["muon_eta_tau"] = TH1F("muon_eta_tau","muon eta tau; muon eta tau; entries", 100, -3 , 3)
  histos["muon_phi_tau"] = TH1F("muon_phi_tau","muon phi tau; muon phi tau; entries", 20, -3.5 , 3.5)
  histos["muon_d0_tau"] = TH1F("muon_d0_tau","muon d0 tau; muon d0 tau; entries", 100, -2 , 2)
  histos["muon_z0_tau"] = TH1F("muon_z0_tau","muon z0 tau; muon z0 tau; entries", 100, -200 , 200)
  histos["muon_e_tau"] = TH1F("muon_e_tau","muon e tau; muon e tau [GeV] ; entries", 100, 0 , 500)
  #histos["truthmuon_index"] = TH1F("truthmuon_index", "truthmuon_index; truthmuon_index; entries", 31,-1, 30)
  #histos["truthmuon_origin"] = TH1F("truthmuon_origin", "truthmuon_origin; truthmuon_origin; entries", 31,-1, 30)
  #histos["muon_index"] = TH1F("muon_index", "muon_index; muon_index; entries", 31,-1, 30)
  #histos["muon_origin"] = TH1F("muon_origin", "muon_origin; muon_origin; entries", 31,-1, 40)
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

      if (e.muon_truthOrigin[imu]==9):
        
        histos["muon_pt_tau"].Fill(e.muon_pt[imu]/1000.)
        histos["muon_eta_tau"].Fill(e.muon_eta[imu])
        histos["muon_phi_tau"].Fill(e.muon_phi[imu])
        histos["muon_d0_tau"].Fill(e.muon_d0[imu])
        histos["muon_z0_tau"].Fill(e.muon_z0[imu])
        histos["muon_e_tau"].Fill(e.muon_e[imu]/1000.)
      #histos["muon_index"].Fill(e.muon_truthmuon_index[imu])
      #histos["muon_origin"].Fill(e.muon_truthOrigin[imu])
      #else:
       # continue
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
