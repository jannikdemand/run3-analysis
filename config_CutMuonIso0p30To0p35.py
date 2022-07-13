from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import electrons as electrons
from .producers import event as event
from .producers import genparticles as genparticles
from .producers import jets as jets
from .producers import met as met
from .producers import muons as muons
from .producers import pairquantities as pairquantities
from .producers import pairselection as pairselection
from .producers import scalefactors as scalefactors
from .producers import triggers as triggers
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from .triggersetup import add_earlyRun3TriggerSetup
from .jet_variations import add_jetVariations
from .jec_data import add_jetCorrectionData
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity
from .variations import add_leptonSFShifts, add_PUweightsShifts  # add_leptonIsoCutVariations
from .iso_variations import apply_leptonIsoCutVariations

def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
):
    configuration = Configuration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
    )

    # first add default parameters necessary for all scopes
    configuration.add_config_parameters(
        "global",
        {
            # "RunLumiEventFilter_Quantities": ["event", "luminosityBlock"],
            # "RunLumiEventFilter_Quantity_Types": ["ULong64_t", "UInt_t"],
            # "RunLumiEventFilter_Selections": ["3", "318"],

            "PU_reweighting_file": EraModifier(
                {
                    "2016": "",
                    "2017": "data/jsonpog-integration/POG/LUM/2017_UL/puWeights.json.gz",
                    "2018": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz",
                }
            ),
            "PU_reweighting_era": EraModifier(
                {
                    "2016": "",
                    "2017": "Collisions17_UltraLegacy_goldenJSON",
                    "2018": "Collisions18_UltraLegacy_goldenJSON",
                }
            ),
            "PU_reweighting_variation": "nominal",

            "golden_json_file": EraModifier(
                {
                    "2016": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                }
            ),
            "PU_reweighting_hist": "pileup",
            "met_filters": EraModifier(
                {
                    "2018": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                }
            ),
        },
    )

    # muon base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_muon_pt": 20.0,
            "max_muon_eta": 2.4,
            "max_muon_dxy": 1e9,  # 0.045,
            "max_muon_dz": 1e0,  # 0.2,
            "muon_id": "Muon_tightId",  # "Muon_mediumId",

            "muon_iso_cut": 1e9,  # 0.3,
        },
    )

    # electron base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_ele_pt": 10.0,
            "max_ele_eta": 2.5,
            "max_ele_dxy": 1.e9,  # 0.045,
            "max_ele_dz": 1.e9,  # 0.2,
            "max_ele_iso": 1.e9,  # 0.3
            "ele_id": "Electron_cutBased",  # "Electron_mvaFall17V2noIso_WP90",
            "ele_id_wp": 3,  # Cut-based medium ID
        },
    )

    ###### scope Specifics ######

    # mm scope selection
    configuration.add_config_parameters(
        ["mm"],
        {
            "muon_index_in_pair": 0,
            "second_muon_index_in_pair": 1,
            "min_muon_pt": 25.0,
            "max_muon_eta": 2.4,
            "n_good_muons": 2,

            "RoccoR_file": '"data/RoccoR_files/RoccoR2018UL.txt"',
            "RoccoR_seed": 1,
            "RoccoR_error_set": 0,
            "RoccoR_error_member": 0,
        },
    )

    # mmet scope selection (muon veto selection):
    configuration.add_config_parameters(
        ["mmet"],
        {
            "muon_index_in_pair": 0,  # dummy index for the selected lepton
            "min_muon_pt": 25.0,
            "max_muon_eta": 2.4,

            "min_muon_veto_pt": 10.0,
            "max_muon_veto_eta": 2.4,
            "max_muon_veto_dxy": 1.e9,  # 0.045,
            "max_muon_veto_dz": 1.e9,  # 0.2,
            "muon_veto_id": "Muon_looseId",  # "Muon_mediumId",
            "muon_veto_iso_cut": 1.e9,
            "n_good_muons": 1,

            "RoccoR_file": '"data/RoccoR_files/RoccoR2018UL.txt"',
            "RoccoR_seed": 1,
            "RoccoR_error_set": 0,
            "RoccoR_error_member": 0,
        },
    )

    # ee scope selection:
    configuration.add_config_parameters(
        ["ee"],
        {
            "electron_index_in_pair": 0,
            "min_electron_pt": 25.0,
            "max_electron_eta": 2.5,
            "electron_iso_cut": 1e9,

            "n_good_electrons": 2,
        },
    )

    # emet scope selection:
    configuration.add_config_parameters(
        ["emet"],
        {
            "electron_index_in_pair": 0,
            "min_electron_pt": 25.0,
            "max_electron_eta": 2.5,
            "electron_iso_cut": 1e9,
            "second_electron_index_in_pair": 1,

            "min_electron_veto_pt": 10.0,
            "max_electron_veto_eta": 2.5,
            "max_electron_veto_dxy": 1.e9,  # 0.045,
            "max_electron_veto_dz": 1.e9,  # 0.2,
            "electron_veto_id": "Electron_cutBased",
            "electron_veto_id_wp": 1,
            "electron_veto_iso_cut": 1.e9,
            "n_good_electrons": 1
        },
    )

    # isolation cuts
    apply_leptonIsoCutVariations(configuration, 0.3, 0.35)

    # Muon scale factors configuration
    configuration.add_config_parameters(
        ["mm", "mmet"],
        {
            "muon_sf_file": EraModifier(
                {
                    # "2016": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_Z.json.gz",
                    # "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_Z.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z.json.gz",
                }
            ),
            "muon_id_sf_name": "NUM_TightID_DEN_TrackerMuons",
            "muon_iso_sf_name": "NUM_TightRelIso_DEN_TightIDandIPCut",
            "muon_sf_year_id": EraModifier(
                {
                    # "2016": "2016postVFP_UL",
                    # "2017": "2017_UL",
                    "2018": "2018_UL",
                }
            ),
            "muon_sf_varation": "sf",  # "sf" is nominal, "systup"/"systdown" are up/down variations
        },
    )
    # electron scale factors configuration
    configuration.add_config_parameters(
        ["ee", "emet"],
        {
            "ele_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz",
                    "2017": "data/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz",
                    "2018": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz",
                }
            ),
            "ele_id_sf_name": "UL-Electron-ID-SF",
            "ele_sf_year_id": EraModifier(
                {
                    "2016preVFP": "2016preVFP",
                    "2016postVFP": "2016postVFP",
                    "2017": "2017",
                    "2018": "2018",
                }
            ),
            "ele_sf_varation": "sf",  # "sf" is nominal, "sfup"/"sfdown" are up/down variations
        },
    )


    ## all scopes misc settings
    configuration.add_config_parameters(
        scopes,
        {
            # "deltaR_jet_veto": 0.5,
            "pairselection_min_dR": -1.,  # 0.5,
        },
    )

    configuration.add_producers(
        "global",
        [
            # event.RunLumiEventFilter,
            event.SampleFlags,
            event.Lumi,
            event.npartons,
            genparticles.DYFilters,
            event.Npu,
            event.NpvGood,
            event.MetFilter,
            event.PUweights,
            event.EventGenWeight,
            muons.BaseMuons,
            electrons.BaseElectrons,
            # jets.JetEnergyCorrection,
            # jets.GoodJets,
            # jets.GoodBJets,
            met.MetBasics,

            # event.DiLeptonVeto,
        ],
    )
    ## add prefiring
    if era != "2018":
        configuration.add_producers(
            "global",
            [
                event.PrefireWeight,
            ],
        )

    # common

    configuration.add_producers(
        "mm",
        [
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.TwoGoodMuonSelection,
            pairselection.ZLLPairSelection,
            pairselection.GoodLLPairFilter,
            pairselection.LVMu1,
            pairselection.LVMu2,
            pairselection.LVMu1Uncorrected,
            pairselection.LVMu2Uncorrected,
            pairquantities.DileptonQuantities,
            pairquantities.DileptonMETQuantities,
            pairquantities.FirstMuonProducers,
            pairquantities.SecondMuonProducers,

            scalefactors.MuonIDIso_SF,
            triggers.MMGenerateSingleMuonTriggerFlags1,
            triggers.MMGenerateSingleMuonTriggerFlags2,

            genparticles.MMGenDiTauPairQuantities,
            genparticles.gen_match_1,
            genparticles.gen_match_2,

            genparticles.gen_matchIdx_1,
            genparticles.gen_matchIdx_2,

            genparticles.UnrollGenMatchLV1,
            genparticles.UnrollGenMatchLV2,

            pairquantities.ApplyRoccoRMC,
        ],
    )

    configuration.add_producers(
        "mmet",
        [
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.OneGoodMuonSelection,
            pairselection.LVMu1,
            pairselection.LVMu1Uncorrected,
            pairquantities.LepMETQuantities,
            pairquantities.FirstMuonProducers,

            scalefactors.MuonIDIso_SF,
            triggers.MMGenerateSingleMuonTriggerFlags1,

            genparticles.gen_match_1,

            genparticles.gen_matchIdx_1,

            genparticles.UnrollGenMatchLV1,

            pairquantities.ApplyRoccoRMC,
        ],
    )

    configuration.add_producers(
        "ee",
        [
            electrons.GoodElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.TwoGoodElectronSelection,
            pairselection.ZLLPairSelection,
            pairselection.GoodLLPairFilter,
            pairselection.LVEl1,
            pairselection.LVEl2,
            pairselection.LVEl1Uncorrected,
            pairselection.LVEl2Uncorrected,
            pairquantities.DileptonQuantities,
            pairquantities.DileptonMETQuantities,
            pairquantities.FirstElectronProducers,
            pairquantities.SecondElectronProducers,

            scalefactors.EleID_SF,
            triggers.EEGenerateSingleElectronTriggerFlags1,
            triggers.EEGenerateSingleElectronTriggerFlags2,

            # genparticles.MMGenDiTauPairQuantities,
            genparticles.gen_match_1,
            genparticles.gen_match_2,

            genparticles.gen_matchIdx_1,
            genparticles.gen_matchIdx_2,

            genparticles.UnrollGenMatchLV1,
            genparticles.UnrollGenMatchLV2,
        ],
    )

    configuration.add_producers(
        "emet",
        [
            electrons.GoodElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.OneGoodElectronSelection,
            pairselection.LVEl1,
            pairselection.LVEl1Uncorrected,
            pairquantities.LepMETQuantities,
            pairquantities.FirstElectronProducers,

            scalefactors.EleID_SF,
            triggers.EEGenerateSingleElectronTriggerFlags1,

            genparticles.gen_match_1,

            genparticles.gen_matchIdx_1,

            genparticles.UnrollGenMatchLV1,
        ],
    )


    # modification rules
    configuration.add_modification_rule(
        ["mm", "mmet"],
        ReplaceProducer(
            producers=[pairquantities.ApplyRoccoRMC, pairquantities.ApplyRoccoRData],
            samples="data",
            update_output=False,
        ),
    )

    configuration.add_modification_rule(
        ["mm", "mmet"],
        RemoveProducer(producers=scalefactors.MuonIDIso_SF, samples="data"),
    )
    configuration.add_modification_rule(
        ["ee", "emet"],
        RemoveProducer(producers=scalefactors.EleID_SF, samples="data"),
    )
    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=[event.PUweights, event.EventGenWeight, event.npartons, genparticles.DYFilters, event.Npu,],
            samples=["data"],
        ),
    )

    configuration.add_modification_rule(
        "global",
        AppendProducer(producers=event.JSONFilter, samples=["data"]),
    )

    configuration.add_modification_rule(
        "mm",
        RemoveProducer(
            producers=[
                genparticles.MMGenDiTauPairQuantities,
                genparticles.gen_match_1,
                genparticles.gen_match_2,
                genparticles.gen_matchIdx_1,
                genparticles.gen_matchIdx_2,
                genparticles.UnrollGenMatchLV1,
                genparticles.UnrollGenMatchLV2,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "mmet",
        RemoveProducer(
            producers=[
                # genparticles.MMGenDiTauPairQuantities,
                genparticles.gen_match_1,
                genparticles.gen_matchIdx_1,
                genparticles.UnrollGenMatchLV1,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "ee",
        RemoveProducer(
            producers=[
                # genparticles.MMGenDiTauPairQuantities,
                genparticles.gen_match_1,
                genparticles.gen_match_2,
                genparticles.gen_matchIdx_1,
                genparticles.gen_matchIdx_2,
                genparticles.UnrollGenMatchLV1,
                genparticles.UnrollGenMatchLV2,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "emet",
        RemoveProducer(
            producers=[
                # genparticles.MMGenDiTauPairQuantities,
                genparticles.gen_match_1,
                genparticles.gen_matchIdx_1,
                genparticles.UnrollGenMatchLV1,
            ],
            samples=["data"],
        ),
    )


    # Output contents
    configuration.add_outputs(
        scopes,
        [
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_ggh_htautau,
            q.is_vbf_htautau,
            q.is_diboson,

            nanoAOD.run,
            q.lumi,
            nanoAOD.event,
            q.npvGood,
            q.npu,
            q.npartons,
            q.puweight,
            q.genweight,

            # q.njets,
            # q.jpt_1,
            # q.jpt_2,
            # q.jeta_1,
            # q.jeta_2,
            # q.jphi_1,
            # q.jphi_2,
            # q.jtag_value_1,
            # q.jtag_value_2,

            # q.nbtag,
            # q.bpt_1,
            # q.bpt_2,
            # q.beta_1,
            # q.beta_2,
            # q.bphi_1,
            # q.bphi_2,
            # q.btag_value_1,
            # q.btag_value_2,

            # q.met,
            # q.metphi,
            # q.pfmet,
            # q.pfmetphi,
            q.met_uncorrected,
            q.metphi_uncorrected,
            q.pfmet_uncorrected,
            q.pfmetphi_uncorrected,
            q.metSumEt,
            q.metcov00,
            q.metcov01,
            q.metcov10,
            q.metcov11,

            # q.pzetamissvis,
            # q.mTdileptonMET,
            # q.mt_1,
            # q.mt_2,
            # q.pt_tt,
            # q.pt_ttjj,
            # q.mt_tot,
            q.genbosonmass,
            q.genbosonpt,
            q.genbosoneta,
            q.genbosonphi,
            q.genbosonrapidity,

            q.is_dy_ee,
            q.is_dy_mm,
            q.is_dy_tt,
        ],
    )

    configuration.add_outputs(
        "mm",
        [
            q.nmuons,

            q.pt_1,
            q.eta_1,
            q.phi_1,
            q.mass_1,
            q.dxy_1,
            q.dz_1,
            q.q_1,
            q.iso_1,

            q.pt_2,
            q.eta_2,
            q.phi_2,
            q.mass_2,
            q.dxy_2,
            q.dz_2,
            q.q_2,
            q.iso_2,

            q.dxyErr_1,
            q.dzErr_1,
            q.ip3d_1,
            q.jetIdx_1,
            q.jetNDauCharged_1,
            q.jetPtRelv2_1,
            q.jetRelIso_1,
            q.miniPFRelIso_all_1,
            q.mvaTTH_1,
            q.sip3d_1,
            q.tightCharge_1,

            q.dxybs_1,
            q.miniPFRelIso_chg_1,
            q.mvaLowPt_chg_1,
            q.pfRelIso03_all_1,
            q.pfRelIso03_chg_1,
            q.pfRelIso04_all_1,
            q.ptErr_1,
            q.segmentComp_1,
            q.softMva_1,
            q.tkRelIso_1,

            q.fsrPhotonIdx_1,
            # q.genPartIdx_1,
            q.highPtId_1,
            q.miniIsoId_1,
            q.multiIsoId_1,
            q.mvaId_1,
            q.mvaLowPtId_1,
            q.nStations_1,
            q.nTrackerLayers_1,
            q.pfIsoId_1,
            q.puppiIsoId_1,
            q.tkIsoId_1,

            q.highPurity_1,
            q.inTimeMuon_1,
            q.isGlobal_1,
            q.isStandalone_1,
            q.isTracker_1,
            q.looseId_1,
            q.mediumId_1,
            q.mediumPromptId_1,
            q.softId_1,
            q.tightId_1,
            q.triggerIdLoose_1,

            q.softMvaId_1,
            q.isPFcand_1,

            q.dxyErr_2,
            q.dzErr_2,
            q.ip3d_2,
            q.jetIdx_2,
            q.jetNDauCharged_2,
            q.jetPtRelv2_2,
            q.jetRelIso_2,
            q.miniPFRelIso_all_2,
            q.mvaTTH_2,
            q.sip3d_2,
            q.tightCharge_2,

            q.dxybs_2,
            q.miniPFRelIso_chg_2,
            q.mvaLowPt_chg_2,
            q.pfRelIso03_all_2,
            q.pfRelIso03_chg_2,
            q.pfRelIso04_all_2,
            q.ptErr_2,
            q.segmentComp_2,
            q.softMva_2,
            q.tkRelIso_2,

            q.fsrPhotonIdx_2,
            # q.genPartIdx_2,
            q.highPtId_2,
            q.miniIsoId_2,
            q.multiIsoId_2,
            q.mvaId_2,
            q.mvaLowPtId_2,
            q.nStations_2,
            q.nTrackerLayers_2,
            q.pfIsoId_2,
            q.puppiIsoId_2,
            q.tkIsoId_2,

            q.highPurity_2,
            q.inTimeMuon_2,
            q.isGlobal_2,
            q.isStandalone_2,
            q.isTracker_2,
            q.looseId_2,
            q.mediumId_2,
            q.mediumPromptId_2,
            q.softId_2,
            q.tightId_2,
            q.triggerIdLoose_2,

            q.softMvaId_2,
            q.isPFcand_2,

            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_match_1,

            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_match_2,

            q.gen_matchIdx_1,
            q.genmatch_pt_1,
            q.genmatch_eta_1,
            q.genmatch_phi_1,
            q.genmatch_mass_1,

            q.gen_matchIdx_2,
            q.genmatch_pt_2,
            q.genmatch_eta_2,
            q.genmatch_phi_2,
            q.genmatch_mass_2,

            q.gen_m_vis,

            q.pt_rc_1,
            q.pt_rc_2,

            # q.mjj,
            q.m_vis,
            q.pt_vis,

            triggers.MMGenerateSingleMuonTriggerFlags1.output_group,
            triggers.MMGenerateSingleMuonTriggerFlags2.output_group,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_2,
        ],
    )

    configuration.add_outputs(
        "mmet",
        [
            q.nmuons,

            q.pt_1,
            q.eta_1,
            q.phi_1,
            q.mass_1,
            q.dxy_1,
            q.dz_1,
            q.q_1,
            q.iso_1,

            q.dxyErr_1,
            q.dzErr_1,
            q.ip3d_1,
            q.jetIdx_1,
            q.jetNDauCharged_1,
            q.jetPtRelv2_1,
            q.jetRelIso_1,
            q.miniPFRelIso_all_1,
            q.mvaTTH_1,
            q.sip3d_1,
            q.tightCharge_1,

            q.dxybs_1,
            q.miniPFRelIso_chg_1,
            q.mvaLowPt_chg_1,
            q.pfRelIso03_all_1,
            q.pfRelIso03_chg_1,
            q.pfRelIso04_all_1,
            q.ptErr_1,
            q.segmentComp_1,
            q.softMva_1,
            q.tkRelIso_1,

            q.fsrPhotonIdx_1,
            # q.genPartIdx_1,
            q.highPtId_1,
            q.miniIsoId_1,
            q.multiIsoId_1,
            q.mvaId_1,
            q.mvaLowPtId_1,
            q.nStations_1,
            q.nTrackerLayers_1,
            q.pfIsoId_1,
            q.puppiIsoId_1,
            q.tkIsoId_1,

            q.softMvaId_1,
            q.isPFcand_1,

            q.highPurity_1,
            q.inTimeMuon_1,
            q.isGlobal_1,
            q.isStandalone_1,
            q.isTracker_1,
            q.looseId_1,
            q.mediumId_1,
            q.mediumPromptId_1,
            q.softId_1,
            q.tightId_1,
            q.triggerIdLoose_1,

            q.gen_match_1,

            q.gen_matchIdx_1,
            q.genmatch_pt_1,
            q.genmatch_eta_1,
            q.genmatch_phi_1,
            q.genmatch_mass_1,

            q.pt_rc_1,

            q.mt_1,

            triggers.MMGenerateSingleMuonTriggerFlags1.output_group,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,

            q.muon_veto_flag,
        ],
    )

    configuration.add_outputs(
        "ee",
        [
            q.nelectrons,

            q.pt_1,
            q.eta_1,
            q.phi_1,
            q.mass_1,
            q.dxy_1,
            q.dz_1,
            q.q_1,
            q.iso_1,

            q.descaledown_1,
            q.descaleup_1,
            q.desigmadown_1,
            q.desigmaup_1,
            q.deltaetaSC_1,
            q.dr03EcalRecHitSumEt_1,
            q.dr03HcalDepth1TowerSumEt_1,
            q.dr03TkSumPt_1,
            q.dr03TkSumPtHEEP_1,
            q.eCorr_1,
            q.eInvMinusPInv_1,
            q.energyErr_1,
            q.hoe_1,
            q.ip3d_1,
            q.jetPtRelv2_1,
            q.jetRelIso_1,
            q.miniPFRelIso_all_1,
            q.mvaFall17V2Iso_1,
            q.mvaFall17V2noIso_1,
            q.dxyErr_1,
            q.dzErr_1,
            q.mvaTTH_1,
            q.pfRelIso03_all_1,
            q.pfRelIso03_chg_1,
            q.r9_1,
            q.scEtOverPt_1,
            q.sieie_1,
            q.sip3d_1,

            q.cutBased_1,
            q.jetIdx_1,
            q.photonIdx_1,
            q.tightCharge_1,
            q.vidNestedWPBitmap_1,
            q.vidNestedWPBitmapHEEP_1,

            q.jetNDauCharged_1,
            q.lostHits_1,
            q.seedGain_1,
            
            q.convVeto_1,
            q.cutBased_HEEP_1,
            q.isPFcand_1,
            q.mvaFall17V2Iso_WP80_1,
            q.mvaFall17V2Iso_WP90_1,
            q.mvaFall17V2Iso_WPL_1,
            q.mvaFall17V2noIso_WP80_1,
            q.mvaFall17V2noIso_WP90_1,
            q.mvaFall17V2noIso_WPL_1,

            q.descaledown_2,
            q.descaleup_2,
            q.desigmadown_2,
            q.desigmaup_2,
            q.deltaetaSC_2,
            q.dr03EcalRecHitSumEt_2,
            q.dr03HcalDepth1TowerSumEt_2,
            q.dr03TkSumPt_2,
            q.dr03TkSumPtHEEP_2,
            q.eCorr_2,
            q.eInvMinusPInv_2,
            q.energyErr_2,
            q.hoe_2,
            q.ip3d_2,
            q.jetPtRelv2_2,
            q.jetRelIso_2,
            q.miniPFRelIso_all_2,
            q.mvaFall17V2Iso_2,
            q.mvaFall17V2noIso_2,
            q.dxyErr_2,
            q.dzErr_2,
            q.mvaTTH_2,
            q.pfRelIso03_all_2,
            q.pfRelIso03_chg_2,
            q.r9_2,
            q.scEtOverPt_2,
            q.sieie_2,
            q.sip3d_2,

            q.cutBased_2,
            q.jetIdx_2,
            q.photonIdx_2,
            q.tightCharge_2,
            q.vidNestedWPBitmap_2,
            q.vidNestedWPBitmapHEEP_2,

            q.jetNDauCharged_2,
            q.lostHits_2,
            q.seedGain_2,

            q.convVeto_2,
            q.cutBased_HEEP_2,
            q.isPFcand_2,
            q.mvaFall17V2Iso_WP80_2,
            q.mvaFall17V2Iso_WP90_2,
            q.mvaFall17V2Iso_WPL_2,
            q.mvaFall17V2noIso_WP80_2,
            q.mvaFall17V2noIso_WP90_2,
            q.mvaFall17V2noIso_WPL_2,


            q.pt_2,
            q.eta_2,
            q.phi_2,
            q.mass_2,
            q.dxy_2,
            q.dz_2,
            q.q_2,
            q.iso_2,

            # q.gen_pt_1,
            # q.gen_eta_1,
            # q.gen_phi_1,
            # q.gen_mass_1,
            # q.gen_pdgid_1,
            q.gen_match_1,

            # q.gen_pt_2,
            # q.gen_eta_2,
            # q.gen_phi_2,
            # q.gen_mass_2,
            # q.gen_pdgid_2,
            q.gen_match_2,

            q.gen_matchIdx_1,
            q.genmatch_pt_1,
            q.genmatch_eta_1,
            q.genmatch_phi_1,
            q.genmatch_mass_1,

            q.gen_matchIdx_2,
            q.genmatch_pt_2,
            q.genmatch_eta_2,
            q.genmatch_phi_2,
            q.genmatch_mass_2,

            # q.gen_m_vis,

            # q.mjj,
            q.m_vis,
            q.pt_vis,

            triggers.EEGenerateSingleElectronTriggerFlags1.output_group,
            triggers.EEGenerateSingleElectronTriggerFlags2.output_group,
            q.id_wgt_ele_wpmedium_1,
            q.id_wgt_ele_wpmedium_2,
        ],
    )

    configuration.add_outputs(
        "emet",
        [
            q.nelectrons,

            q.pt_1,
            q.eta_1,
            q.phi_1,
            q.mass_1,
            q.dxy_1,
            q.dz_1,
            q.q_1,
            q.iso_1,

            q.descaledown_1,
            q.descaleup_1,
            q.desigmadown_1,
            q.desigmaup_1,
            q.deltaetaSC_1,
            q.dr03EcalRecHitSumEt_1,
            q.dr03HcalDepth1TowerSumEt_1,
            q.dr03TkSumPt_1,
            q.dr03TkSumPtHEEP_1,
            q.eCorr_1,
            q.eInvMinusPInv_1,
            q.energyErr_1,
            q.hoe_1,
            q.ip3d_1,
            q.jetPtRelv2_1,
            q.jetRelIso_1,
            q.miniPFRelIso_all_1,
            q.mvaFall17V2Iso_1,
            q.mvaFall17V2noIso_1,
            q.dxyErr_1,
            q.dzErr_1,
            q.mvaTTH_1,
            q.pfRelIso03_all_1,
            q.pfRelIso03_chg_1,
            q.r9_1,
            q.scEtOverPt_1,
            q.sieie_1,
            q.sip3d_1,

            q.cutBased_1,
            q.jetIdx_1,
            q.photonIdx_1,
            q.tightCharge_1,
            q.vidNestedWPBitmap_1,
            q.vidNestedWPBitmapHEEP_1,

            q.jetNDauCharged_1,
            q.lostHits_1,
            q.seedGain_1,

            q.convVeto_1,
            q.cutBased_HEEP_1,
            q.isPFcand_1,
            q.mvaFall17V2Iso_WP80_1,
            q.mvaFall17V2Iso_WP90_1,
            q.mvaFall17V2Iso_WPL_1,
            q.mvaFall17V2noIso_WP80_1,
            q.mvaFall17V2noIso_WP90_1,
            q.mvaFall17V2noIso_WPL_1,

            q.gen_match_1,

            q.gen_matchIdx_1,
            q.genmatch_pt_1,
            q.genmatch_eta_1,
            q.genmatch_phi_1,
            q.genmatch_mass_1,

            q.mt_1,

            triggers.EEGenerateSingleElectronTriggerFlags1.output_group,
            q.id_wgt_ele_wpmedium_1,

            q.electron_veto_flag,
        ],
    )

    #########################
    # PU weights systematics
    #########################
    add_PUweightsShifts(configuration)

    #########################
    # Lepton ID/Iso scale factor shifts, channel dependent
    #########################
    add_leptonSFShifts(configuration)
    # add_leptonIsoCutVariations(configuration)

    #########################
    # Import triggersetup   #
    #########################
    add_earlyRun3TriggerSetup(configuration)

    #########################
    # MET Shifts
    #########################
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnUp",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredUp",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredUp",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnDown",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredDown",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredDown",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    #########################
    # Prefiring Shifts
    #########################
    if era != "2018":
        configuration.add_shift(
            SystematicShiftByQuantity(
                name="prefiringDown",
                quantity_change={
                    nanoAOD.prefireWeight: "L1PreFiringWeight_Dn",
                },
                scopes=["global"],
            )
        )
        configuration.add_shift(
            SystematicShiftByQuantity(
                name="prefiringUp",
                quantity_change={
                    nanoAOD.prefireWeight: "L1PreFiringWeight_Up",
                },
                scopes=["global"],
            )
        )
    #########################
    # MET Recoil Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResponseUp",
            shift_config={
                ("mm", "mmet", "ee", "emet"): {
                    "apply_recoil_resolution_systematic": False,
                    "apply_recoil_response_systematic": True,
                    "recoil_systematic_shift_up": True,
                    "recoil_systematic_shift_down": False,
                },
            },
            producers={
                ("mm", "mmet", "ee", "emet"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResponseDown",
            shift_config={
                ("mm", "mmet", "ee", "emet"): {
                    "apply_recoil_resolution_systematic": False,
                    "apply_recoil_response_systematic": True,
                    "recoil_systematic_shift_up": False,
                    "recoil_systematic_shift_down": True,
                },
            },
            producers={
                ("mm", "mmet", "ee", "emet"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResolutionUp",
            shift_config={
                ("mm", "mmet", "ee", "emet"): {
                    "apply_recoil_resolution_systematic": True,
                    "apply_recoil_response_systematic": False,
                    "recoil_systematic_shift_up": True,
                    "recoil_systematic_shift_down": False,
                },
            },
            producers={
                ("mm", "mmet", "ee", "emet"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResolutionDown",
            shift_config={
                ("mm", "mmet", "ee", "emet"): {
                    "apply_recoil_resolution_systematic": True,
                    "apply_recoil_response_systematic": False,
                    "recoil_systematic_shift_up": False,
                    "recoil_systematic_shift_down": True,
                },
            },
            producers={
                ("mm", "mmet", "ee", "emet"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    #########################
    # Jet energy resolution and jet energy scale
    #########################
    # add_jetVariations(configuration, available_sample_types, era)

    #########################
    # Jet energy correction for data
    #########################
    # add_jetCorrectionData(configuration, era)

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()
