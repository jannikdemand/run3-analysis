from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, Filter

Electron_etaSC = Producer(
    name="Electron_etaSC",
    call="basefunctions::add<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_eta, nanoAOD.Electron_deltaEtaSC],
    output=[q.Electron_etaSC],
    scopes=["global"],
)
Electron_energySC = Producer(
    name="Electron_energySC",
    call="physicsobject::electron::superClusterEnergy({df}, {input}, {output})",
    input=[nanoAOD.Electron_pt, nanoAOD.Electron_scEtOverPt, q.Electron_etaSC],
    output=[q.Electron_energySC],
    scopes=["global"],
)
Electron_abs_dEtaInSeed = Producer(
    name="Electron_abs_dEtaInSeed",
    call="basefunctions::abs<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_dEtaInSeed],
    output=[q.Electron_abs_dEtaInSeed],
    scopes=["global"],
)
Electron_abs_deltaPhiSuperClusterTrackAtVtx = Producer(
    name="Electron_abs_deltaPhiSuperClusterTrackAtVtx",
    call="basefunctions::abs<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_deltaPhiSuperClusterTrackAtVtx],
    output=[q.Electron_abs_deltaPhiSuperClusterTrackAtVtx],
    scopes=["global"],
)
Electron_abs_eInvMinusPInv = Producer(
    name="Electron_abs_eInvMinusPInv",
    call="basefunctions::abs<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_eInvMinusPInv],
    output=[q.Electron_abs_eInvMinusPInv],
    scopes=["global"],
)

ElectronVars = ProducerGroup(
    name="ElectronVars",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[
        Electron_etaSC,
        Electron_energySC,
        Electron_abs_dEtaInSeed,
        Electron_abs_deltaPhiSuperClusterTrackAtVtx,
        Electron_abs_eInvMinusPInv,
    ],
)

ElectronVarsLess = ProducerGroup(
    name="ElectronVarsLess",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[
        Electron_etaSC,
        Electron_energySC,
    ],
)

####################
# Set of producers used for loosest selection of electrons
####################

ElectronPtCut = Producer(
    name="ElectronPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_ele_pt})",
    input=[nanoAOD.Electron_pt],
    output=[],
    scopes=["global"],
)
ElectronEtaCut = Producer(
    name="ElectronEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_ele_eta})",
    input=[nanoAOD.Electron_eta],
    output=[],
    scopes=["global"],
)
ElectronDxyCut = Producer(
    name="ElectronDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_ele_dxy})",
    input=[nanoAOD.Electron_dxy],
    output=[],
    scopes=["global"],
)
ElectronDzCut = Producer(
    name="ElectronDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_ele_dz})",
    input=[nanoAOD.Electron_dz],
    output=[],
    scopes=["global"],
)
ElectronIDCut = Producer(
    name="ElectronIDCut",
    call='physicsobject::electron::CutCBID({df}, {output}, "{ele_id}", {ele_id_wp})',
    input=[],
    output=[],
    scopes=["global"],
)
# ElectronIDCut = Producer(
#     name="ElectronIDCut",
#     call='physicsobject::electron::CutID({df}, {output}, "{ele_id}")',
#     input=[],
#     output=[],
#     scopes=["global"],
# )
ElectronIsoCut = Producer(
    name="ElectronIsoCut",
    call="physicsobject::electron::CutIsolation({df}, {output}, {input}, {max_ele_iso})",
    input=[nanoAOD.Electron_iso],
    output=[],
    scopes=["global"],
)
BaseElectrons = ProducerGroup(
    name="BaseElectrons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_electrons_mask],
    scopes=["global"],
    subproducers=[
        ElectronPtCut,
        ElectronEtaCut,
        ElectronDxyCut,
        ElectronDzCut,
        # HERE tmp
        # ElectronIDCut,
        # ElectronIsoCut,
    ],
)

####################
# Set of producers used for more specific selection of electrons in channels
####################

# with valid ID flags
GoodElectronPtCut = Producer(
    name="GoodElectronPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_electron_pt})",
    input=[nanoAOD.Electron_pt],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronEtaCut = Producer(
    name="GoodElectronEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_electron_eta})",
    input=[nanoAOD.Electron_eta],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronIDCut = Producer(
    name="GoodElectronIDCut",
    call='physicsobject::electron::CutCBID({df}, {output}, "{ele_id}", {ele_id_wp})',
    input=[],
    output=[],
    scopes=["ee"],
)
GoodElectronIDCutNoIso = Producer(
    name="GoodElectronIDCutNoIso",
    call='physicsobject::electron::CutCBIDNoIso({df}, {output}, "{ele_id_noiso}", {ele_id_noiso_wp})',
    input=[],
    output=[],
    scopes=["emet"],
)
GoodElectronIsoCut = Producer(
    name="GoodElectronIsoCut",
    call="physicsobject::electron::CutIsolation({df}, {output}, {input}, {electron_iso_cut})",
    input=[nanoAOD.Electron_iso],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectrons = ProducerGroup(
    name="GoodElectrons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_electrons_mask],
    output=[q.good_electrons_mask],
    scopes=["ee", "emet"],
    subproducers=[
        GoodElectronPtCut,
        GoodElectronEtaCut,
        GoodElectronIDCut,
        # GoodElectronIsoCut,
    ],
)
GoodElectronsNoIso = ProducerGroup(
    name="GoodElectronsNoIso",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_electrons_mask],
    output=[q.good_electrons_mask],
    scopes=["emet"],
    subproducers=[
        GoodElectronPtCut,
        GoodElectronEtaCut,
        GoodElectronIDCutNoIso,
        # GoodElectronIsoCut,
    ],
)

# w/o valid ID flags
GoodElectronConvVetoCut = Producer(
    name="GoodElectronConvVetoCut",
    call='physicsobject::muon::CutID({df}, {output}, "Electron_convVeto")',
    input=[],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronSieieCut = Producer(
    name="GoodElectronSieieCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.479, {ele_Sieie_cut_barrel_lo}, {ele_Sieie_cut_barrel_up}, {ele_Sieie_cut_endcap_lo}, {ele_Sieie_cut_endcap_up})",
    input=[q.Electron_etaSC, nanoAOD.Electron_sieie],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronDEtaInSeedCut = Producer(
    name="GoodElectronDEtaInSeedCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.479, {ele_DEtaInSeed_cut_barrel_lo}, {ele_DEtaInSeed_cut_barrel_up}, {ele_DEtaInSeed_cut_endcap_lo}, {ele_DEtaInSeed_cut_endcap_up})",
    input=[q.Electron_etaSC, q.Electron_abs_dEtaInSeed],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronDeltaPhiSuperClusterTrackAtVtxCut = Producer(
    name="GoodElectronDeltaPhiSuperClusterTrackAtVtxCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.479, {ele_DeltaPhiSuperClusterTrackAtVtx_cut_barrel_lo}, {ele_DeltaPhiSuperClusterTrackAtVtx_cut_barrel_up}, {ele_DeltaPhiSuperClusterTrackAtVtx_cut_endcap_lo}, {ele_DeltaPhiSuperClusterTrackAtVtx_cut_endcap_up})",
    input=[q.Electron_etaSC, q.Electron_abs_deltaPhiSuperClusterTrackAtVtx],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronHoeCut = Producer(
    name="GoodElectronHoeCut",
    call="physicsobject::electron::CutHoeBarrelEndcap({df}, {output}, {input}, 1.479, {ele_Hoe_cut_barrel_0}, {ele_Hoe_cut_barrel_1}, {ele_Hoe_cut_barrel_2}, {ele_Hoe_cut_endcap_0}, {ele_Hoe_cut_endcap_1}, {ele_Hoe_cut_endcap_2})",
    input=[q.Electron_etaSC, q.Electron_energySC, nanoAOD.rho, nanoAOD.Electron_hoe],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronIsoCustomCut = Producer(
    name="GoodElectronIsoCustomCut",
    call="physicsobject::electron::CutIsolationBarrelEndcap({df}, {output}, {input}, 1.479, {ele_Iso_cut_barrel_0}, {ele_Iso_cut_barrel_1}, {ele_Iso_cut_endcap_0}, {ele_Iso_cut_endcap_1})",
    input=[q.Electron_etaSC, nanoAOD.Electron_pt, nanoAOD.Electron_pfRelIso03_all],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronEInvMinusPInvCut = Producer(
    name="GoodElectronEInvMinusPInvCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.479, {ele_EInvMinusPInv_cut_barrel_lo}, {ele_EInvMinusPInv_cut_barrel_up}, {ele_EInvMinusPInv_cut_endcap_lo}, {ele_EInvMinusPInv_cut_endcap_up})",
    input=[q.Electron_etaSC, q.Electron_abs_eInvMinusPInv],
    output=[],
    scopes=["ee", "emet"],
)
GoodElectronLostHitsCut = Producer(
    name="GoodElectronLostHitsCut",
    call="physicsobject::CutIntVariableBarrelEndcap({df}, {output}, {input}, 1.479, {ele_LostHits_cut_barrel_lo}, {ele_LostHits_cut_barrel_up}, {ele_LostHits_cut_endcap_lo}, {ele_LostHits_cut_endcap_up})",
    input=[q.Electron_etaSC, nanoAOD.Electron_lostHits],
    output=[],
    scopes=["ee", "emet"],
)

GoodElectronsCustom = ProducerGroup(
    name="GoodElectronsCustom",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_electrons_mask],
    output=[q.good_electrons_mask],
    scopes=["ee", "emet"],
    subproducers=[
        GoodElectronPtCut,
        GoodElectronEtaCut,

        # Medium ID
        GoodElectronConvVetoCut,
        GoodElectronSieieCut,
        GoodElectronDEtaInSeedCut,
        GoodElectronDeltaPhiSuperClusterTrackAtVtxCut,
        GoodElectronHoeCut,
        GoodElectronIsoCustomCut,
        GoodElectronEInvMinusPInvCut,
        GoodElectronLostHitsCut,
    ],
)

NumberOfGoodElectrons = Producer(
    name="NumberOfGoodElectrons",
    call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
    input=[q.good_electrons_mask],
    output=[q.nelectrons],
    scopes=["ee", "emet"],
)


####################
# Set of producers used for additional electron veto
####################

OneGoodElectronFlag = Producer(
    name="OneGoodElectronFlag",
    call="physicsobject::CutNFlag({df}, {output}, {input}, {n_good_electrons})",
    input={
        "emet": [q.good_electrons_mask],
    },
    output=[q.n_good_electrons_flag],
    scopes=["emet"],
)
OneGoodElectronFilter = Filter(
    name="OneGoodElectronFilter",
    call='basefunctions::FilterFlagsAny({df}, "OneGoodElectronFilter", {input})',
    input=[q.n_good_electrons_flag],
    scopes=["emet"],
    subproducers=[]
)
OneGoodElectron = Producer(
    name="OneGoodElectron",
    call="physicsobject::SelectedObjects({df}, {output}, {input})",
    input={
        "emet": [q.good_electrons_mask],
    },
    output=[q.selectedLepton],
    scopes=["emet"],
)

ElectronVetoPtCut = Producer(
    name="ElectronVetoPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_electron_veto_pt})",
    input=[nanoAOD.Electron_pt],
    output=[],
    scopes=["emet"],
)
ElectronVetoEtaCut = Producer(
    name="ElectronVetoEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_electron_veto_eta})",
    input=[nanoAOD.Electron_eta],
    output=[],
    scopes=["emet"],
)
ElectronVetoDxyCut = Producer(
    name="ElectronVetoDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_electron_veto_dxy})",
    input=[nanoAOD.Electron_dxy],
    output=[],
    scopes=["emet"],
)
ElectronVetoDzCut = Producer(
    name="ElectronVetoDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_electron_veto_dz})",
    input=[nanoAOD.Electron_dz],
    output=[],
    scopes=["emet"],
)
ElectronVetoIDCut = Producer(
    name="ElectronVetoIDCut",
    call='physicsobject::electron::CutCBID({df}, {output}, "{electron_veto_id}", {electron_veto_id_wp})',
    input=[],
    output=[],
    scopes=["emet"],
)
ElectronVetoIsoCut = Producer(
    name="ElectronVetoIsoCut",
    call="physicsobject::electron::CutIsolation({df}, {output}, {input}, {electron_veto_iso_cut})",
    input=[nanoAOD.Electron_iso],
    output=[],
    scopes=["emet"],
)
LooseElectrons = ProducerGroup(
    name="LooseElectrons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.loose_electrons_mask],
    scopes=["emet"],
    subproducers=[
        ElectronVetoPtCut,
        ElectronVetoEtaCut,
        ElectronVetoDxyCut,
        ElectronVetoDzCut,
        ElectronVetoIDCut,
        ElectronVetoIsoCut,
    ],
)
VetoElectrons = Producer(
    name="VetoElectrons",
    call="physicsobject::VetoCandInMask({df}, {output}, {input}, {electron_index_in_pair})",
    input=[q.loose_electrons_mask, q.selectedLepton],
    output=[q.veto_electrons_mask],
    scopes=["emet"],
)
ExtraElectronsVeto = Producer(
    name="ExtraElectronsVeto",
    call="physicsobject::IsEmptyFlag({df}, {output}, {input})",
    input={
        "emet": [q.veto_electrons_mask],
    },
    output=[q.electron_veto_flag],
    scopes=["emet"],
)
VetoElectronFilter = Filter(
    name="VetoElectronFilter",
    call='basefunctions::FilterFlagsAny({df}, "ExtraLooseElectronVeto", {input})',
    input=[q.electron_veto_flag],
    scopes=["emet"],
    subproducers=[]
)

OneGoodElectronSelection = ProducerGroup(
    name="OneGoodElectronSelection",
    call=None,
    input=None,
    output=None,
    scopes=["emet"],
    subproducers=[
        OneGoodElectronFlag,
        OneGoodElectronFilter,
        OneGoodElectron,

        # HERE tmp
        # LooseElectrons,
        # VetoElectrons,
        # ExtraElectronsVeto,

        # VetoElectronFilter,
    ]
)

TwoGoodElectronFlag = Producer(
    name="TwoGoodElectronFlag",
    call="physicsobject::CutNFlag({df}, {output}, {input}, {n_good_electrons})",
    input={
        "ee": [q.good_electrons_mask],
    },
    output=[q.n_good_electrons_flag],
    scopes=["ee"],
)
TwoGoodElectronFilter = Filter(
    name="TwoGoodElectronFilter",
    call='basefunctions::FilterFlagsAny({df}, "TwoGoodElectronFilter", {input})',
    input=[q.n_good_electrons_flag],
    scopes=["ee"],
    subproducers=[]
)
TwoGoodElectronSelection = ProducerGroup(
    name="TwoGoodElectronSelection",
    call=None,
    input=None,
    output=None,
    scopes=["ee"],
    subproducers=[
        TwoGoodElectronFlag,
        TwoGoodElectronFilter,
    ]
)

####################
# Set of producers used for di-electron veto
####################

# VetoElectrons = Producer(
#     name="VetoElectrons",
#     call="physicsobject::VetoCandInMask({df}, {output}, {input}, {electron_index_in_pair})",
#     input=[q.base_electrons_mask, q.selectedLepton],
#     output=[q.veto_electrons_mask],
#     scopes=["ee", "emet"],
# )
# VetoSecondElectron = Producer(
#     name="VetoSecondElectron",
#     call="physicsobject::VetoCandInMask({df}, {output}, {input}, {second_electron_index_in_pair})",
#     input=[q.veto_electrons_mask, q.selectedLepton],
#     output=[q.veto_electrons_mask_2],
#     scopes=["ee"],
# )
# ExtraElectronsVeto = Producer(
#     name="ExtraElectronsVeto",
#     call="physicsobject::LeptonVetoFlag({df}, {output}, {input})",
#     input={
#         "em": [q.veto_electrons_mask],
#         "et": [q.veto_electrons_mask],
#         "mt": [q.base_electrons_mask],
#         "tt": [q.base_electrons_mask],
#         "mm": [q.base_electrons_mask],
#         "ee": [q.veto_electrons_mask_2],
#     },
#     output=[q.electron_veto_flag],
#     scopes=["em", "et", "mt", "tt", "mm", "ee"],
# )

# DiElectronVetoPtCut = Producer(
#     name="DiElectronVetoPtCut",
#     call="physicsobject::CutPt({df}, {input}, {output}, {min_dielectronveto_pt})",
#     input=[nanoAOD.Electron_pt],
#     output=[],
#     scopes=["global"],
# )
# DiElectronVetoIDCut = Producer(
#     name="DiElectronVetoIDCut",
#     call='physicsobject::electron::CutCBID({df}, {output}, "{dielectronveto_id}", {dielectronveto_id_wp})',
#     input=[],
#     output=[],
#     scopes=["global"],
# )
# DiElectronVetoElectrons = ProducerGroup(
#     name="DiElectronVetoElectrons",
#     call="physicsobject::CombineMasks({df}, {output}, {input})",
#     input=ElectronEtaCut.output
#     + ElectronDxyCut.output
#     + ElectronDzCut.output
#     + ElectronIsoCut.output,
#     output=[],
#     scopes=["global"],
#     subproducers=[
#         DiElectronVetoPtCut,
#         DiElectronVetoIDCut,
#     ],
# )
# DiElectronVeto = ProducerGroup(
#     name="DiElectronVeto",
#     call="physicsobject::CheckForDiLeptonPairs({df}, {output}, {input}, {dileptonveto_dR})",
#     input=[
#         nanoAOD.Electron_pt,
#         nanoAOD.Electron_eta,
#         nanoAOD.Electron_phi,
#         nanoAOD.Electron_mass,
#         nanoAOD.Electron_charge,
#     ],
#     output=[q.dielectron_veto],
#     scopes=["global"],
#     subproducers=[DiElectronVetoElectrons],
# )
