from ROOT import TCanvas, TFile, TTree, TH1F, TH2F


HISTO1="muon_pt_W"
HISTO2="muon_pt_bc"

f = TFile.Open("outfile_tree.root","READ")
h1 = f.Get(HISTO1)
h2 = f.Get(HISTO2)

h2.SetLineColor(2)
h2.SetMarkerColor(2)

h1.Scale(1./h1.Integral())
h2.Scale(1./h2.Integral())

h1.SetTitle("Signal")
h2.SetTitle("Background")

c=TCanvas()
h1.Draw()
h2.Draw("same")
c.BuildLegend()

c.SaveAs("output/"+HISTO1+"_"+HISTO2+".pdf")

input("...")
