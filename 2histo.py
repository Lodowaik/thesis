from ROOT import TCanvas, TFile, TTree, TH1F, TH2F, TEfficiency


HISTO1="muon_qp_signal"
HISTO2="muon_qp_bgd"

f = TFile.Open("output_variabili.root","READ")
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












