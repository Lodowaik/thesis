//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Oct  8 10:40:56 2024 by ROOT version 6.32.02
// from TTree AnalysisTree/My analysis tree
// found on file: mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root
//////////////////////////////////////////////////////////

#ifndef AnalysisTree_h
#define AnalysisTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"
#include "vector"
#include "vector"
#include "vector"

class AnalysisTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Float_t         actualInteractionsPerCrossing;
   Float_t         averageInteractionsPerCrossing;
   ULong64_t       eventNumber;
   Float_t         eventWeight;
   UInt_t          lumiBlock;
   Float_t         mcEventWeight;
   vector<float>   *mcEventWeights;
   vector<float>   *muon_DFCommonJetDr;
   vector<char>    *muon_HighPt;
   vector<char>    *muon_IsoCloseByCorr_assocClustDecor;
   vector<float>   *muon_IsoCloseByCorr_assocClustEnergy;
   vector<float>   *muon_IsoCloseByCorr_assocClustEta;
   vector<float>   *muon_IsoCloseByCorr_assocClustPhi;
   vector<char>    *muon_IsoCloseByCorr_assocPflowDecor;
   vector<float>   *muon_IsoCloseByCorr_assocPflowEnergy;
   vector<float>   *muon_IsoCloseByCorr_assocPflowEta;
   vector<float>   *muon_IsoCloseByCorr_assocPflowPhi;
   vector<char>    *muon_Loose;
   vector<char>    *muon_LowPt;
   vector<char>    *muon_LowPtMVA;
   vector<char>    *muon_Medium;
   vector<int>     *muon_PixDead;
   vector<int>     *muon_PixHits;
   vector<int>     *muon_PixHoles;
   vector<int>     *muon_SCTDead;
   vector<int>     *muon_SCTHits;
   vector<int>     *muon_SCTHoles;
   vector<int>     *muon_TRTHits;
   vector<int>     *muon_TRTOutliers;
   vector<char>    *muon_Tight;
   vector<char>    *muon_VeryLoose;
   vector<unsigned short> *muon_allAuthors;
   vector<int>     *muon_author;
   vector<int>     *muon_caloMuonIDTag;
   vector<float>   *muon_caloMuonScore;
   vector<int>     *muon_combinedTrackOutBoundsPrecisionHits;
   vector<float>   *muon_d0;
   vector<float>   *muon_d0sigma;
   vector<float>   *muon_e;
   vector<float>   *muon_energyLoss;
   vector<float>   *muon_energyLossMeas;
   vector<float>   *muon_energyLossMeasSigma;
   vector<float>   *muon_energyLossParam;
   vector<float>   *muon_energyLossParamSigmaMinus;
   vector<float>   *muon_energyLossParamSigmaPlus;
   vector<float>   *muon_energyLossSigma;
   vector<int>     *muon_energyLossType;
   vector<float>   *muon_eta;
   vector<int>     *muon_extendedLargeHits;
   vector<int>     *muon_extendedLargeHoles;
   vector<int>     *muon_extendedSmallHits;
   vector<int>     *muon_extendedSmallHoles;
   vector<char>    *muon_hasTrkID;
   vector<char>    *muon_hasTrkME;
   vector<char>    *muon_hasTrkMS;
   vector<float>   *muon_id_d0;
   vector<float>   *muon_id_d0sigma;
   vector<float>   *muon_id_e;
   vector<float>   *muon_id_eta;
   vector<float>   *muon_id_phi;
   vector<float>   *muon_id_pt;
   vector<float>   *muon_id_q;
   vector<float>   *muon_id_qOverP;
   vector<float>   *muon_id_qOverPsigma;
   vector<float>   *muon_id_reducedChi2;
   vector<float>   *muon_id_z0;
   vector<float>   *muon_id_z0sigma;
   vector<int>     *muon_innerLargeHits;
   vector<int>     *muon_innerLargeHoles;
   vector<int>     *muon_innerSmallHits;
   vector<int>     *muon_innerSmallHoles;
   vector<char>    *muon_isBEE;
   vector<char>    *muon_isBIS78;
   vector<char>    *muon_isBMG;
   vector<char>    *muon_isBadMuon;
   vector<char>    *muon_isBadMuon_highPt;
   vector<int>     *muon_isSmallGoodSectors;
   vector<char>    *muon_iso_Loose;
   vector<char>    *muon_iso_PflowLoose;
   vector<char>    *muon_iso_PflowTight;
   vector<char>    *muon_iso_Tight;
   vector<float>   *muon_me_d0;
   vector<float>   *muon_me_d0sigma;
   vector<float>   *muon_me_e;
   vector<float>   *muon_me_eta;
   vector<float>   *muon_me_phi;
   vector<float>   *muon_me_pt;
   vector<float>   *muon_me_q;
   vector<float>   *muon_me_qOverP;
   vector<float>   *muon_me_qOverPsigma;
   vector<float>   *muon_me_reducedChi2;
   vector<float>   *muon_me_z0;
   vector<float>   *muon_me_z0sigma;
   vector<int>     *muon_middleLargeHits;
   vector<int>     *muon_middleLargeHoles;
   vector<int>     *muon_middleSmallHits;
   vector<int>     *muon_middleSmallHoles;
   vector<float>   *muon_momentumBalanceSig;
   vector<float>   *muon_ms_d0;
   vector<float>   *muon_ms_d0sigma;
   vector<float>   *muon_ms_e;
   vector<float>   *muon_ms_eta;
   vector<float>   *muon_ms_phi;
   vector<float>   *muon_ms_pt;
   vector<float>   *muon_ms_q;
   vector<float>   *muon_ms_qOverP;
   vector<float>   *muon_ms_qOverPsigma;
   vector<float>   *muon_ms_reducedChi2;
   vector<float>   *muon_ms_z0;
   vector<float>   *muon_ms_z0sigma;
   vector<int>     *muon_muonType;
   vector<int>     *muon_nGoodPrecLayers;
   vector<float>   *muon_neflowisol20;
   vector<int>     *muon_nprecisionHoleLayers;
   vector<int>     *muon_nprecisionLayers;
   vector<int>     *muon_nprecisionLayerswoNSW;
   vector<int>     *muon_outerLargeHits;
   vector<int>     *muon_outerLargeHoles;
   vector<int>     *muon_outerSmallHits;
   vector<int>     *muon_outerSmallHoles;
   vector<char>    *muon_passSelToolIDCuts;
   vector<float>   *muon_phi;
   vector<float>   *muon_pt;
   vector<float>   *muon_ptcone20;
   vector<float>   *muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt1000;
   vector<float>   *muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt500;
   vector<float>   *muon_ptcone30;
   vector<float>   *muon_ptcone40;
   vector<float>   *muon_ptvarcone20;
   vector<float>   *muon_ptvarcone30;
   vector<float>   *muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt1000;
   vector<float>   *muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt500;
   vector<float>   *muon_ptvarcone40;
   vector<float>   *muon_q;
   vector<float>   *muon_qOverP;
   vector<float>   *muon_qOverPsigma;
   vector<int>     *muon_quality;
   vector<float>   *muon_reducedChi2;
   vector<float>   *muon_scatteringCurvatureSig;
   vector<float>   *muon_scatteringNeighbourSig;
   vector<float>   *muon_segmentDeltaEta;
   vector<float>   *muon_topoetcone20;
   vector<float>   *muon_topoetcone30;
   vector<float>   *muon_topoetcone40;
   vector<int>     *muon_truthIFFType;
   vector<int>     *muon_truthOrigin;
   vector<int>     *muon_truthType;
   vector<int>     *muon_truthmuon_index;
   vector<float>   *muon_z0;
   vector<float>   *muon_z0sigma;
   vector<char>    *passSelToolPreselection;
   Float_t         pileupWeight;
   UInt_t          runNumber;
   vector<int>     *truthmuon_IFFType;
   vector<float>   *truthmuon_e;
   vector<float>   *truthmuon_eta;
   vector<int>     *truthmuon_muon_index;
   vector<int>     *truthmuon_origin;
   vector<int>     *truthmuon_pdgId;
   vector<float>   *truthmuon_phi;
   vector<float>   *truthmuon_pt;
   vector<float>   *truthmuon_q;
   vector<int>     *truthmuon_type;

   // List of branches
   TBranch        *b_actualInteractionsPerCrossing;   //!
   TBranch        *b_averageInteractionsPerCrossing;   //!
   TBranch        *b_eventNumber;   //!
   TBranch        *b_eventWeight;   //!
   TBranch        *b_lumiBlock;   //!
   TBranch        *b_mcEventWeight;   //!
   TBranch        *b_mcEventWeights;   //!
   TBranch        *b_muon_DFCommonJetDr;   //!
   TBranch        *b_muon_HighPt;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocClustDecor;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocClustEnergy;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocClustEta;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocClustPhi;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocPflowDecor;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocPflowEnergy;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocPflowEta;   //!
   TBranch        *b_muon_IsoCloseByCorr_assocPflowPhi;   //!
   TBranch        *b_muon_Loose;   //!
   TBranch        *b_muon_LowPt;   //!
   TBranch        *b_muon_LowPtMVA;   //!
   TBranch        *b_muon_Medium;   //!
   TBranch        *b_muon_PixDead;   //!
   TBranch        *b_muon_PixHits;   //!
   TBranch        *b_muon_PixHoles;   //!
   TBranch        *b_muon_SCTDead;   //!
   TBranch        *b_muon_SCTHits;   //!
   TBranch        *b_muon_SCTHoles;   //!
   TBranch        *b_muon_TRTHits;   //!
   TBranch        *b_muon_TRTOutliers;   //!
   TBranch        *b_muon_Tight;   //!
   TBranch        *b_muon_VeryLoose;   //!
   TBranch        *b_muon_allAuthors;   //!
   TBranch        *b_muon_author;   //!
   TBranch        *b_muon_caloMuonIDTag;   //!
   TBranch        *b_muon_caloMuonScore;   //!
   TBranch        *b_muon_combinedTrackOutBoundsPrecisionHits;   //!
   TBranch        *b_muon_d0;   //!
   TBranch        *b_muon_d0sigma;   //!
   TBranch        *b_muon_e;   //!
   TBranch        *b_muon_energyLoss;   //!
   TBranch        *b_muon_energyLossMeas;   //!
   TBranch        *b_muon_energyLossMeasSigma;   //!
   TBranch        *b_muon_energyLossParam;   //!
   TBranch        *b_muon_energyLossParamSigmaMinus;   //!
   TBranch        *b_muon_energyLossParamSigmaPlus;   //!
   TBranch        *b_muon_energyLossSigma;   //!
   TBranch        *b_muon_energyLossType;   //!
   TBranch        *b_muon_eta;   //!
   TBranch        *b_muon_extendedLargeHits;   //!
   TBranch        *b_muon_extendedLargeHoles;   //!
   TBranch        *b_muon_extendedSmallHits;   //!
   TBranch        *b_muon_extendedSmallHoles;   //!
   TBranch        *b_muon_hasTrkID;   //!
   TBranch        *b_muon_hasTrkME;   //!
   TBranch        *b_muon_hasTrkMS;   //!
   TBranch        *b_muon_id_d0;   //!
   TBranch        *b_muon_id_d0sigma;   //!
   TBranch        *b_muon_id_e;   //!
   TBranch        *b_muon_id_eta;   //!
   TBranch        *b_muon_id_phi;   //!
   TBranch        *b_muon_id_pt;   //!
   TBranch        *b_muon_id_q;   //!
   TBranch        *b_muon_id_qOverP;   //!
   TBranch        *b_muon_id_qOverPsigma;   //!
   TBranch        *b_muon_id_reducedChi2;   //!
   TBranch        *b_muon_id_z0;   //!
   TBranch        *b_muon_id_z0sigma;   //!
   TBranch        *b_muon_innerLargeHits;   //!
   TBranch        *b_muon_innerLargeHoles;   //!
   TBranch        *b_muon_innerSmallHits;   //!
   TBranch        *b_muon_innerSmallHoles;   //!
   TBranch        *b_muon_isBEE;   //!
   TBranch        *b_muon_isBIS78;   //!
   TBranch        *b_muon_isBMG;   //!
   TBranch        *b_muon_isBadMuon;   //!
   TBranch        *b_muon_isBadMuon_highPt;   //!
   TBranch        *b_muon_isSmallGoodSectors;   //!
   TBranch        *b_muon_iso_Loose;   //!
   TBranch        *b_muon_iso_PflowLoose;   //!
   TBranch        *b_muon_iso_PflowTight;   //!
   TBranch        *b_muon_iso_Tight;   //!
   TBranch        *b_muon_me_d0;   //!
   TBranch        *b_muon_me_d0sigma;   //!
   TBranch        *b_muon_me_e;   //!
   TBranch        *b_muon_me_eta;   //!
   TBranch        *b_muon_me_phi;   //!
   TBranch        *b_muon_me_pt;   //!
   TBranch        *b_muon_me_q;   //!
   TBranch        *b_muon_me_qOverP;   //!
   TBranch        *b_muon_me_qOverPsigma;   //!
   TBranch        *b_muon_me_reducedChi2;   //!
   TBranch        *b_muon_me_z0;   //!
   TBranch        *b_muon_me_z0sigma;   //!
   TBranch        *b_muon_middleLargeHits;   //!
   TBranch        *b_muon_middleLargeHoles;   //!
   TBranch        *b_muon_middleSmallHits;   //!
   TBranch        *b_muon_middleSmallHoles;   //!
   TBranch        *b_muon_momentumBalanceSig;   //!
   TBranch        *b_muon_ms_d0;   //!
   TBranch        *b_muon_ms_d0sigma;   //!
   TBranch        *b_muon_ms_e;   //!
   TBranch        *b_muon_ms_eta;   //!
   TBranch        *b_muon_ms_phi;   //!
   TBranch        *b_muon_ms_pt;   //!
   TBranch        *b_muon_ms_q;   //!
   TBranch        *b_muon_ms_qOverP;   //!
   TBranch        *b_muon_ms_qOverPsigma;   //!
   TBranch        *b_muon_ms_reducedChi2;   //!
   TBranch        *b_muon_ms_z0;   //!
   TBranch        *b_muon_ms_z0sigma;   //!
   TBranch        *b_muon_muonType;   //!
   TBranch        *b_muon_nGoodPrecLayers;   //!
   TBranch        *b_muon_neflowisol20;   //!
   TBranch        *b_muon_nprecisionHoleLayers;   //!
   TBranch        *b_muon_nprecisionLayers;   //!
   TBranch        *b_muon_nprecisionLayerswoNSW;   //!
   TBranch        *b_muon_outerLargeHits;   //!
   TBranch        *b_muon_outerLargeHoles;   //!
   TBranch        *b_muon_outerSmallHits;   //!
   TBranch        *b_muon_outerSmallHoles;   //!
   TBranch        *b_muon_passSelToolIDCuts;   //!
   TBranch        *b_muon_phi;   //!
   TBranch        *b_muon_pt;   //!
   TBranch        *b_muon_ptcone20;   //!
   TBranch        *b_muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt1000;   //!
   TBranch        *b_muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt500;   //!
   TBranch        *b_muon_ptcone30;   //!
   TBranch        *b_muon_ptcone40;   //!
   TBranch        *b_muon_ptvarcone20;   //!
   TBranch        *b_muon_ptvarcone30;   //!
   TBranch        *b_muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt1000;   //!
   TBranch        *b_muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt500;   //!
   TBranch        *b_muon_ptvarcone40;   //!
   TBranch        *b_muon_q;   //!
   TBranch        *b_muon_qOverP;   //!
   TBranch        *b_muon_qOverPsigma;   //!
   TBranch        *b_muon_quality;   //!
   TBranch        *b_muon_reducedChi2;   //!
   TBranch        *b_muon_scatteringCurvatureSig;   //!
   TBranch        *b_muon_scatteringNeighbourSig;   //!
   TBranch        *b_muon_segmentDeltaEta;   //!
   TBranch        *b_muon_topoetcone20;   //!
   TBranch        *b_muon_topoetcone30;   //!
   TBranch        *b_muon_topoetcone40;   //!
   TBranch        *b_muon_truthIFFType;   //!
   TBranch        *b_muon_truthOrigin;   //!
   TBranch        *b_muon_truthType;   //!
   TBranch        *b_muon_truthmuon_index;   //!
   TBranch        *b_muon_z0;   //!
   TBranch        *b_muon_z0sigma;   //!
   TBranch        *b_passSelToolPreselection;   //!
   TBranch        *b_pileupWeight;   //!
   TBranch        *b_runNumber;   //!
   TBranch        *b_truthmuon_IFFType;   //!
   TBranch        *b_truthmuon_e;   //!
   TBranch        *b_truthmuon_eta;   //!
   TBranch        *b_truthmuon_muon_index;   //!
   TBranch        *b_truthmuon_origin;   //!
   TBranch        *b_truthmuon_pdgId;   //!
   TBranch        *b_truthmuon_phi;   //!
   TBranch        *b_truthmuon_pt;   //!
   TBranch        *b_truthmuon_q;   //!
   TBranch        *b_truthmuon_type;   //!

   AnalysisTree(TTree *tree=0);
   virtual ~AnalysisTree();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual bool     Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef AnalysisTree_cxx
AnalysisTree::AnalysisTree(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_s3681_r13145_p5980.root");
      }
      f->GetObject("AnalysisTree",tree);

   }
   Init(tree);
}

AnalysisTree::~AnalysisTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t AnalysisTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t AnalysisTree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void AnalysisTree::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   mcEventWeights = 0;
   muon_DFCommonJetDr = 0;
   muon_HighPt = 0;
   muon_IsoCloseByCorr_assocClustDecor = 0;
   muon_IsoCloseByCorr_assocClustEnergy = 0;
   muon_IsoCloseByCorr_assocClustEta = 0;
   muon_IsoCloseByCorr_assocClustPhi = 0;
   muon_IsoCloseByCorr_assocPflowDecor = 0;
   muon_IsoCloseByCorr_assocPflowEnergy = 0;
   muon_IsoCloseByCorr_assocPflowEta = 0;
   muon_IsoCloseByCorr_assocPflowPhi = 0;
   muon_Loose = 0;
   muon_LowPt = 0;
   muon_LowPtMVA = 0;
   muon_Medium = 0;
   muon_PixDead = 0;
   muon_PixHits = 0;
   muon_PixHoles = 0;
   muon_SCTDead = 0;
   muon_SCTHits = 0;
   muon_SCTHoles = 0;
   muon_TRTHits = 0;
   muon_TRTOutliers = 0;
   muon_Tight = 0;
   muon_VeryLoose = 0;
   muon_allAuthors = 0;
   muon_author = 0;
   muon_caloMuonIDTag = 0;
   muon_caloMuonScore = 0;
   muon_combinedTrackOutBoundsPrecisionHits = 0;
   muon_d0 = 0;
   muon_d0sigma = 0;
   muon_e = 0;
   muon_energyLoss = 0;
   muon_energyLossMeas = 0;
   muon_energyLossMeasSigma = 0;
   muon_energyLossParam = 0;
   muon_energyLossParamSigmaMinus = 0;
   muon_energyLossParamSigmaPlus = 0;
   muon_energyLossSigma = 0;
   muon_energyLossType = 0;
   muon_eta = 0;
   muon_extendedLargeHits = 0;
   muon_extendedLargeHoles = 0;
   muon_extendedSmallHits = 0;
   muon_extendedSmallHoles = 0;
   muon_hasTrkID = 0;
   muon_hasTrkME = 0;
   muon_hasTrkMS = 0;
   muon_id_d0 = 0;
   muon_id_d0sigma = 0;
   muon_id_e = 0;
   muon_id_eta = 0;
   muon_id_phi = 0;
   muon_id_pt = 0;
   muon_id_q = 0;
   muon_id_qOverP = 0;
   muon_id_qOverPsigma = 0;
   muon_id_reducedChi2 = 0;
   muon_id_z0 = 0;
   muon_id_z0sigma = 0;
   muon_innerLargeHits = 0;
   muon_innerLargeHoles = 0;
   muon_innerSmallHits = 0;
   muon_innerSmallHoles = 0;
   muon_isBEE = 0;
   muon_isBIS78 = 0;
   muon_isBMG = 0;
   muon_isBadMuon = 0;
   muon_isBadMuon_highPt = 0;
   muon_isSmallGoodSectors = 0;
   muon_iso_Loose = 0;
   muon_iso_PflowLoose = 0;
   muon_iso_PflowTight = 0;
   muon_iso_Tight = 0;
   muon_me_d0 = 0;
   muon_me_d0sigma = 0;
   muon_me_e = 0;
   muon_me_eta = 0;
   muon_me_phi = 0;
   muon_me_pt = 0;
   muon_me_q = 0;
   muon_me_qOverP = 0;
   muon_me_qOverPsigma = 0;
   muon_me_reducedChi2 = 0;
   muon_me_z0 = 0;
   muon_me_z0sigma = 0;
   muon_middleLargeHits = 0;
   muon_middleLargeHoles = 0;
   muon_middleSmallHits = 0;
   muon_middleSmallHoles = 0;
   muon_momentumBalanceSig = 0;
   muon_ms_d0 = 0;
   muon_ms_d0sigma = 0;
   muon_ms_e = 0;
   muon_ms_eta = 0;
   muon_ms_phi = 0;
   muon_ms_pt = 0;
   muon_ms_q = 0;
   muon_ms_qOverP = 0;
   muon_ms_qOverPsigma = 0;
   muon_ms_reducedChi2 = 0;
   muon_ms_z0 = 0;
   muon_ms_z0sigma = 0;
   muon_muonType = 0;
   muon_nGoodPrecLayers = 0;
   muon_neflowisol20 = 0;
   muon_nprecisionHoleLayers = 0;
   muon_nprecisionLayers = 0;
   muon_nprecisionLayerswoNSW = 0;
   muon_outerLargeHits = 0;
   muon_outerLargeHoles = 0;
   muon_outerSmallHits = 0;
   muon_outerSmallHoles = 0;
   muon_passSelToolIDCuts = 0;
   muon_phi = 0;
   muon_pt = 0;
   muon_ptcone20 = 0;
   muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt1000 = 0;
   muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt500 = 0;
   muon_ptcone30 = 0;
   muon_ptcone40 = 0;
   muon_ptvarcone20 = 0;
   muon_ptvarcone30 = 0;
   muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt1000 = 0;
   muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt500 = 0;
   muon_ptvarcone40 = 0;
   muon_q = 0;
   muon_qOverP = 0;
   muon_qOverPsigma = 0;
   muon_quality = 0;
   muon_reducedChi2 = 0;
   muon_scatteringCurvatureSig = 0;
   muon_scatteringNeighbourSig = 0;
   muon_segmentDeltaEta = 0;
   muon_topoetcone20 = 0;
   muon_topoetcone30 = 0;
   muon_topoetcone40 = 0;
   muon_truthIFFType = 0;
   muon_truthOrigin = 0;
   muon_truthType = 0;
   muon_truthmuon_index = 0;
   muon_z0 = 0;
   muon_z0sigma = 0;
   passSelToolPreselection = 0;
   truthmuon_IFFType = 0;
   truthmuon_e = 0;
   truthmuon_eta = 0;
   truthmuon_muon_index = 0;
   truthmuon_origin = 0;
   truthmuon_pdgId = 0;
   truthmuon_phi = 0;
   truthmuon_pt = 0;
   truthmuon_q = 0;
   truthmuon_type = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("actualInteractionsPerCrossing", &actualInteractionsPerCrossing, &b_actualInteractionsPerCrossing);
   fChain->SetBranchAddress("averageInteractionsPerCrossing", &averageInteractionsPerCrossing, &b_averageInteractionsPerCrossing);
   fChain->SetBranchAddress("eventNumber", &eventNumber, &b_eventNumber);
   fChain->SetBranchAddress("eventWeight", &eventWeight, &b_eventWeight);
   fChain->SetBranchAddress("lumiBlock", &lumiBlock, &b_lumiBlock);
   fChain->SetBranchAddress("mcEventWeight", &mcEventWeight, &b_mcEventWeight);
   fChain->SetBranchAddress("mcEventWeights", &mcEventWeights, &b_mcEventWeights);
   fChain->SetBranchAddress("muon_DFCommonJetDr", &muon_DFCommonJetDr, &b_muon_DFCommonJetDr);
   fChain->SetBranchAddress("muon_HighPt", &muon_HighPt, &b_muon_HighPt);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocClustDecor", &muon_IsoCloseByCorr_assocClustDecor, &b_muon_IsoCloseByCorr_assocClustDecor);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocClustEnergy", &muon_IsoCloseByCorr_assocClustEnergy, &b_muon_IsoCloseByCorr_assocClustEnergy);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocClustEta", &muon_IsoCloseByCorr_assocClustEta, &b_muon_IsoCloseByCorr_assocClustEta);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocClustPhi", &muon_IsoCloseByCorr_assocClustPhi, &b_muon_IsoCloseByCorr_assocClustPhi);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocPflowDecor", &muon_IsoCloseByCorr_assocPflowDecor, &b_muon_IsoCloseByCorr_assocPflowDecor);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocPflowEnergy", &muon_IsoCloseByCorr_assocPflowEnergy, &b_muon_IsoCloseByCorr_assocPflowEnergy);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocPflowEta", &muon_IsoCloseByCorr_assocPflowEta, &b_muon_IsoCloseByCorr_assocPflowEta);
   fChain->SetBranchAddress("muon_IsoCloseByCorr_assocPflowPhi", &muon_IsoCloseByCorr_assocPflowPhi, &b_muon_IsoCloseByCorr_assocPflowPhi);
   fChain->SetBranchAddress("muon_Loose", &muon_Loose, &b_muon_Loose);
   fChain->SetBranchAddress("muon_LowPt", &muon_LowPt, &b_muon_LowPt);
   fChain->SetBranchAddress("muon_LowPtMVA", &muon_LowPtMVA, &b_muon_LowPtMVA);
   fChain->SetBranchAddress("muon_Medium", &muon_Medium, &b_muon_Medium);
   fChain->SetBranchAddress("muon_PixDead", &muon_PixDead, &b_muon_PixDead);
   fChain->SetBranchAddress("muon_PixHits", &muon_PixHits, &b_muon_PixHits);
   fChain->SetBranchAddress("muon_PixHoles", &muon_PixHoles, &b_muon_PixHoles);
   fChain->SetBranchAddress("muon_SCTDead", &muon_SCTDead, &b_muon_SCTDead);
   fChain->SetBranchAddress("muon_SCTHits", &muon_SCTHits, &b_muon_SCTHits);
   fChain->SetBranchAddress("muon_SCTHoles", &muon_SCTHoles, &b_muon_SCTHoles);
   fChain->SetBranchAddress("muon_TRTHits", &muon_TRTHits, &b_muon_TRTHits);
   fChain->SetBranchAddress("muon_TRTOutliers", &muon_TRTOutliers, &b_muon_TRTOutliers);
   fChain->SetBranchAddress("muon_Tight", &muon_Tight, &b_muon_Tight);
   fChain->SetBranchAddress("muon_VeryLoose", &muon_VeryLoose, &b_muon_VeryLoose);
   fChain->SetBranchAddress("muon_allAuthors", &muon_allAuthors, &b_muon_allAuthors);
   fChain->SetBranchAddress("muon_author", &muon_author, &b_muon_author);
   fChain->SetBranchAddress("muon_caloMuonIDTag", &muon_caloMuonIDTag, &b_muon_caloMuonIDTag);
   fChain->SetBranchAddress("muon_caloMuonScore", &muon_caloMuonScore, &b_muon_caloMuonScore);
   fChain->SetBranchAddress("muon_combinedTrackOutBoundsPrecisionHits", &muon_combinedTrackOutBoundsPrecisionHits, &b_muon_combinedTrackOutBoundsPrecisionHits);
   fChain->SetBranchAddress("muon_d0", &muon_d0, &b_muon_d0);
   fChain->SetBranchAddress("muon_d0sigma", &muon_d0sigma, &b_muon_d0sigma);
   fChain->SetBranchAddress("muon_e", &muon_e, &b_muon_e);
   fChain->SetBranchAddress("muon_energyLoss", &muon_energyLoss, &b_muon_energyLoss);
   fChain->SetBranchAddress("muon_energyLossMeas", &muon_energyLossMeas, &b_muon_energyLossMeas);
   fChain->SetBranchAddress("muon_energyLossMeasSigma", &muon_energyLossMeasSigma, &b_muon_energyLossMeasSigma);
   fChain->SetBranchAddress("muon_energyLossParam", &muon_energyLossParam, &b_muon_energyLossParam);
   fChain->SetBranchAddress("muon_energyLossParamSigmaMinus", &muon_energyLossParamSigmaMinus, &b_muon_energyLossParamSigmaMinus);
   fChain->SetBranchAddress("muon_energyLossParamSigmaPlus", &muon_energyLossParamSigmaPlus, &b_muon_energyLossParamSigmaPlus);
   fChain->SetBranchAddress("muon_energyLossSigma", &muon_energyLossSigma, &b_muon_energyLossSigma);
   fChain->SetBranchAddress("muon_energyLossType", &muon_energyLossType, &b_muon_energyLossType);
   fChain->SetBranchAddress("muon_eta", &muon_eta, &b_muon_eta);
   fChain->SetBranchAddress("muon_extendedLargeHits", &muon_extendedLargeHits, &b_muon_extendedLargeHits);
   fChain->SetBranchAddress("muon_extendedLargeHoles", &muon_extendedLargeHoles, &b_muon_extendedLargeHoles);
   fChain->SetBranchAddress("muon_extendedSmallHits", &muon_extendedSmallHits, &b_muon_extendedSmallHits);
   fChain->SetBranchAddress("muon_extendedSmallHoles", &muon_extendedSmallHoles, &b_muon_extendedSmallHoles);
   fChain->SetBranchAddress("muon_hasTrkID", &muon_hasTrkID, &b_muon_hasTrkID);
   fChain->SetBranchAddress("muon_hasTrkME", &muon_hasTrkME, &b_muon_hasTrkME);
   fChain->SetBranchAddress("muon_hasTrkMS", &muon_hasTrkMS, &b_muon_hasTrkMS);
   fChain->SetBranchAddress("muon_id_d0", &muon_id_d0, &b_muon_id_d0);
   fChain->SetBranchAddress("muon_id_d0sigma", &muon_id_d0sigma, &b_muon_id_d0sigma);
   fChain->SetBranchAddress("muon_id_e", &muon_id_e, &b_muon_id_e);
   fChain->SetBranchAddress("muon_id_eta", &muon_id_eta, &b_muon_id_eta);
   fChain->SetBranchAddress("muon_id_phi", &muon_id_phi, &b_muon_id_phi);
   fChain->SetBranchAddress("muon_id_pt", &muon_id_pt, &b_muon_id_pt);
   fChain->SetBranchAddress("muon_id_q", &muon_id_q, &b_muon_id_q);
   fChain->SetBranchAddress("muon_id_qOverP", &muon_id_qOverP, &b_muon_id_qOverP);
   fChain->SetBranchAddress("muon_id_qOverPsigma", &muon_id_qOverPsigma, &b_muon_id_qOverPsigma);
   fChain->SetBranchAddress("muon_id_reducedChi2", &muon_id_reducedChi2, &b_muon_id_reducedChi2);
   fChain->SetBranchAddress("muon_id_z0", &muon_id_z0, &b_muon_id_z0);
   fChain->SetBranchAddress("muon_id_z0sigma", &muon_id_z0sigma, &b_muon_id_z0sigma);
   fChain->SetBranchAddress("muon_innerLargeHits", &muon_innerLargeHits, &b_muon_innerLargeHits);
   fChain->SetBranchAddress("muon_innerLargeHoles", &muon_innerLargeHoles, &b_muon_innerLargeHoles);
   fChain->SetBranchAddress("muon_innerSmallHits", &muon_innerSmallHits, &b_muon_innerSmallHits);
   fChain->SetBranchAddress("muon_innerSmallHoles", &muon_innerSmallHoles, &b_muon_innerSmallHoles);
   fChain->SetBranchAddress("muon_isBEE", &muon_isBEE, &b_muon_isBEE);
   fChain->SetBranchAddress("muon_isBIS78", &muon_isBIS78, &b_muon_isBIS78);
   fChain->SetBranchAddress("muon_isBMG", &muon_isBMG, &b_muon_isBMG);
   fChain->SetBranchAddress("muon_isBadMuon", &muon_isBadMuon, &b_muon_isBadMuon);
   fChain->SetBranchAddress("muon_isBadMuon_highPt", &muon_isBadMuon_highPt, &b_muon_isBadMuon_highPt);
   fChain->SetBranchAddress("muon_isSmallGoodSectors", &muon_isSmallGoodSectors, &b_muon_isSmallGoodSectors);
   fChain->SetBranchAddress("muon_iso_Loose", &muon_iso_Loose, &b_muon_iso_Loose);
   fChain->SetBranchAddress("muon_iso_PflowLoose", &muon_iso_PflowLoose, &b_muon_iso_PflowLoose);
   fChain->SetBranchAddress("muon_iso_PflowTight", &muon_iso_PflowTight, &b_muon_iso_PflowTight);
   fChain->SetBranchAddress("muon_iso_Tight", &muon_iso_Tight, &b_muon_iso_Tight);
   fChain->SetBranchAddress("muon_me_d0", &muon_me_d0, &b_muon_me_d0);
   fChain->SetBranchAddress("muon_me_d0sigma", &muon_me_d0sigma, &b_muon_me_d0sigma);
   fChain->SetBranchAddress("muon_me_e", &muon_me_e, &b_muon_me_e);
   fChain->SetBranchAddress("muon_me_eta", &muon_me_eta, &b_muon_me_eta);
   fChain->SetBranchAddress("muon_me_phi", &muon_me_phi, &b_muon_me_phi);
   fChain->SetBranchAddress("muon_me_pt", &muon_me_pt, &b_muon_me_pt);
   fChain->SetBranchAddress("muon_me_q", &muon_me_q, &b_muon_me_q);
   fChain->SetBranchAddress("muon_me_qOverP", &muon_me_qOverP, &b_muon_me_qOverP);
   fChain->SetBranchAddress("muon_me_qOverPsigma", &muon_me_qOverPsigma, &b_muon_me_qOverPsigma);
   fChain->SetBranchAddress("muon_me_reducedChi2", &muon_me_reducedChi2, &b_muon_me_reducedChi2);
   fChain->SetBranchAddress("muon_me_z0", &muon_me_z0, &b_muon_me_z0);
   fChain->SetBranchAddress("muon_me_z0sigma", &muon_me_z0sigma, &b_muon_me_z0sigma);
   fChain->SetBranchAddress("muon_middleLargeHits", &muon_middleLargeHits, &b_muon_middleLargeHits);
   fChain->SetBranchAddress("muon_middleLargeHoles", &muon_middleLargeHoles, &b_muon_middleLargeHoles);
   fChain->SetBranchAddress("muon_middleSmallHits", &muon_middleSmallHits, &b_muon_middleSmallHits);
   fChain->SetBranchAddress("muon_middleSmallHoles", &muon_middleSmallHoles, &b_muon_middleSmallHoles);
   fChain->SetBranchAddress("muon_momentumBalanceSig", &muon_momentumBalanceSig, &b_muon_momentumBalanceSig);
   fChain->SetBranchAddress("muon_ms_d0", &muon_ms_d0, &b_muon_ms_d0);
   fChain->SetBranchAddress("muon_ms_d0sigma", &muon_ms_d0sigma, &b_muon_ms_d0sigma);
   fChain->SetBranchAddress("muon_ms_e", &muon_ms_e, &b_muon_ms_e);
   fChain->SetBranchAddress("muon_ms_eta", &muon_ms_eta, &b_muon_ms_eta);
   fChain->SetBranchAddress("muon_ms_phi", &muon_ms_phi, &b_muon_ms_phi);
   fChain->SetBranchAddress("muon_ms_pt", &muon_ms_pt, &b_muon_ms_pt);
   fChain->SetBranchAddress("muon_ms_q", &muon_ms_q, &b_muon_ms_q);
   fChain->SetBranchAddress("muon_ms_qOverP", &muon_ms_qOverP, &b_muon_ms_qOverP);
   fChain->SetBranchAddress("muon_ms_qOverPsigma", &muon_ms_qOverPsigma, &b_muon_ms_qOverPsigma);
   fChain->SetBranchAddress("muon_ms_reducedChi2", &muon_ms_reducedChi2, &b_muon_ms_reducedChi2);
   fChain->SetBranchAddress("muon_ms_z0", &muon_ms_z0, &b_muon_ms_z0);
   fChain->SetBranchAddress("muon_ms_z0sigma", &muon_ms_z0sigma, &b_muon_ms_z0sigma);
   fChain->SetBranchAddress("muon_muonType", &muon_muonType, &b_muon_muonType);
   fChain->SetBranchAddress("muon_nGoodPrecLayers", &muon_nGoodPrecLayers, &b_muon_nGoodPrecLayers);
   fChain->SetBranchAddress("muon_neflowisol20", &muon_neflowisol20, &b_muon_neflowisol20);
   fChain->SetBranchAddress("muon_nprecisionHoleLayers", &muon_nprecisionHoleLayers, &b_muon_nprecisionHoleLayers);
   fChain->SetBranchAddress("muon_nprecisionLayers", &muon_nprecisionLayers, &b_muon_nprecisionLayers);
   fChain->SetBranchAddress("muon_nprecisionLayerswoNSW", &muon_nprecisionLayerswoNSW, &b_muon_nprecisionLayerswoNSW);
   fChain->SetBranchAddress("muon_outerLargeHits", &muon_outerLargeHits, &b_muon_outerLargeHits);
   fChain->SetBranchAddress("muon_outerLargeHoles", &muon_outerLargeHoles, &b_muon_outerLargeHoles);
   fChain->SetBranchAddress("muon_outerSmallHits", &muon_outerSmallHits, &b_muon_outerSmallHits);
   fChain->SetBranchAddress("muon_outerSmallHoles", &muon_outerSmallHoles, &b_muon_outerSmallHoles);
   fChain->SetBranchAddress("muon_passSelToolIDCuts", &muon_passSelToolIDCuts, &b_muon_passSelToolIDCuts);
   fChain->SetBranchAddress("muon_phi", &muon_phi, &b_muon_phi);
   fChain->SetBranchAddress("muon_pt", &muon_pt, &b_muon_pt);
   fChain->SetBranchAddress("muon_ptcone20", &muon_ptcone20, &b_muon_ptcone20);
   fChain->SetBranchAddress("muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt1000", &muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt1000, &b_muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt1000);
   fChain->SetBranchAddress("muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt500", &muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt500, &b_muon_ptcone20_Nonprompt_All_MaxWeightTTVA_pt500);
   fChain->SetBranchAddress("muon_ptcone30", &muon_ptcone30, &b_muon_ptcone30);
   fChain->SetBranchAddress("muon_ptcone40", &muon_ptcone40, &b_muon_ptcone40);
   fChain->SetBranchAddress("muon_ptvarcone20", &muon_ptvarcone20, &b_muon_ptvarcone20);
   fChain->SetBranchAddress("muon_ptvarcone30", &muon_ptvarcone30, &b_muon_ptvarcone30);
   fChain->SetBranchAddress("muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt1000", &muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt1000, &b_muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt1000);
   fChain->SetBranchAddress("muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt500", &muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt500, &b_muon_ptvarcone30_Nonprompt_All_MaxWeightTTVA_pt500);
   fChain->SetBranchAddress("muon_ptvarcone40", &muon_ptvarcone40, &b_muon_ptvarcone40);
   fChain->SetBranchAddress("muon_q", &muon_q, &b_muon_q);
   fChain->SetBranchAddress("muon_qOverP", &muon_qOverP, &b_muon_qOverP);
   fChain->SetBranchAddress("muon_qOverPsigma", &muon_qOverPsigma, &b_muon_qOverPsigma);
   fChain->SetBranchAddress("muon_quality", &muon_quality, &b_muon_quality);
   fChain->SetBranchAddress("muon_reducedChi2", &muon_reducedChi2, &b_muon_reducedChi2);
   fChain->SetBranchAddress("muon_scatteringCurvatureSig", &muon_scatteringCurvatureSig, &b_muon_scatteringCurvatureSig);
   fChain->SetBranchAddress("muon_scatteringNeighbourSig", &muon_scatteringNeighbourSig, &b_muon_scatteringNeighbourSig);
   fChain->SetBranchAddress("muon_segmentDeltaEta", &muon_segmentDeltaEta, &b_muon_segmentDeltaEta);
   fChain->SetBranchAddress("muon_topoetcone20", &muon_topoetcone20, &b_muon_topoetcone20);
   fChain->SetBranchAddress("muon_topoetcone30", &muon_topoetcone30, &b_muon_topoetcone30);
   fChain->SetBranchAddress("muon_topoetcone40", &muon_topoetcone40, &b_muon_topoetcone40);
   fChain->SetBranchAddress("muon_truthIFFType", &muon_truthIFFType, &b_muon_truthIFFType);
   fChain->SetBranchAddress("muon_truthOrigin", &muon_truthOrigin, &b_muon_truthOrigin);
   fChain->SetBranchAddress("muon_truthType", &muon_truthType, &b_muon_truthType);
   fChain->SetBranchAddress("muon_truthmuon_index", &muon_truthmuon_index, &b_muon_truthmuon_index);
   fChain->SetBranchAddress("muon_z0", &muon_z0, &b_muon_z0);
   fChain->SetBranchAddress("muon_z0sigma", &muon_z0sigma, &b_muon_z0sigma);
   fChain->SetBranchAddress("passSelToolPreselection", &passSelToolPreselection, &b_passSelToolPreselection);
   fChain->SetBranchAddress("pileupWeight", &pileupWeight, &b_pileupWeight);
   fChain->SetBranchAddress("runNumber", &runNumber, &b_runNumber);
   fChain->SetBranchAddress("truthmuon_IFFType", &truthmuon_IFFType, &b_truthmuon_IFFType);
   fChain->SetBranchAddress("truthmuon_e", &truthmuon_e, &b_truthmuon_e);
   fChain->SetBranchAddress("truthmuon_eta", &truthmuon_eta, &b_truthmuon_eta);
   fChain->SetBranchAddress("truthmuon_muon_index", &truthmuon_muon_index, &b_truthmuon_muon_index);
   fChain->SetBranchAddress("truthmuon_origin", &truthmuon_origin, &b_truthmuon_origin);
   fChain->SetBranchAddress("truthmuon_pdgId", &truthmuon_pdgId, &b_truthmuon_pdgId);
   fChain->SetBranchAddress("truthmuon_phi", &truthmuon_phi, &b_truthmuon_phi);
   fChain->SetBranchAddress("truthmuon_pt", &truthmuon_pt, &b_truthmuon_pt);
   fChain->SetBranchAddress("truthmuon_q", &truthmuon_q, &b_truthmuon_q);
   fChain->SetBranchAddress("truthmuon_type", &truthmuon_type, &b_truthmuon_type);
   Notify();
}

bool AnalysisTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return true;
}

void AnalysisTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t AnalysisTree::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef AnalysisTree_cxx
