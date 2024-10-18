from ROOT import TCanvas, TFile, TTree, TH1F, TH2F, TEfficiency


HISTO1="eff_Tight_bgd_vs_pt"
HISTO2="eff_tagli_bgd_vs_pt"

f = TFile.Open("outfile_tree.root","READ")
h1 = f.Get(HISTO1)
h2 = f.Get(HISTO2)

h2.SetLineColor(2)
h2.SetMarkerColor(2)

#h1.Scale(1./h1.Integral())
#h2.Scale(1./h2.Integral())

h1.SetTitle("Tight")
h2.SetTitle("Tagli")

c=TCanvas()
h1.Draw()
h2.Draw("same")
c.BuildLegend()

c.SaveAs("output/"+HISTO1+"_"+HISTO2+".pdf")

input("...")
