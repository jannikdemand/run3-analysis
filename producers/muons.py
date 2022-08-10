from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, Filter

Muon_abs_dxy = Producer(
    name="Muon_abs_dxy",
    call="basefunctions::abs<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_dxy],
    output=[q.Muon_abs_dxy],
    scopes=["global"],
)

Muon_abs_dz = Producer(
    name="Muon_abs_dz",
    call="basefunctions::abs<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_dz],
    output=[q.Muon_abs_dz],
    scopes=["global"],
)

MuonVars = ProducerGroup(
    name="MuonVars",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[
        Muon_abs_dxy,
        Muon_abs_dz,
    ],
)

####################
# Set of producers used for loosest selection of muons
####################

MuonPtCut = Producer(
    name="MuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["global"],
)
MuonEtaCut = Producer(
    name="MuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["global"],
)
MuonDxyCut = Producer(
    name="MuonDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_muon_dxy})",
    input=[nanoAOD.Muon_dxy],
    output=[],
    scopes=["global"],
)
MuonDzCut = Producer(
    name="MuonDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_muon_dz})",
    input=[nanoAOD.Muon_dz],
    output=[],
    scopes=["global"],
)
MuonIDCut = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{muon_id}")',
    input=[],
    output=[],
    scopes=["global"],
)
MuonIsoCut = Producer(
    name="MuonIsoCut",
    call="physicsobject::muon::CutIsolation({df}, {output}, {input}, {muon_iso_cut})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=["global"],
)
BaseMuons = ProducerGroup(
    name="BaseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_muons_mask],
    scopes=["global"],
    subproducers=[
        MuonPtCut,
        MuonEtaCut,
        MuonDxyCut,
        MuonDzCut,
        MuonIDCut,
        MuonIsoCut,
    ],
)

####################
# Set of producers used for more specific selection of muons in channels
####################

# with valid ID flags
GoodMuonPtCut = Producer(
    name="GoodMuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonEtaCut = Producer(
    name="GoodMuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonIsoCut = Producer(
    name="GoodMuonIsoCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_iso_cut_barrel_lo}, {muon_iso_cut_barrel_up}, {muon_iso_cut_endcap_lo}, {muon_iso_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, nanoAOD.Muon_iso],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuons = ProducerGroup(
    name="GoodMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.good_muons_mask],
    scopes=["mm", "mmet"],
    subproducers=[
        GoodMuonPtCut,
        GoodMuonEtaCut,
        GoodMuonIsoCut,
    ],
)

# w/o valid ID flags
GoodMuonIsGlobalCut = Producer(
    name="GoodMuonIsGlobalCut",
    call='physicsobject::muon::CutID({df}, {output}, "Muon_isGlobal")',
    input=[],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonIsPFCut = Producer(
    name="GoodMuonIsPFCut",
    call='physicsobject::muon::CutID({df}, {output}, "Muon_isPFcand")',
    input=[],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonNumberOfValidMuonHitsCut = Producer(
    name="GoodMuonNumberOfValidMuonHitsCut",
    call="physicsobject::CutIntVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_NumberOfValidMuonHits_cut_barrel_lo}, {muon_NumberOfValidMuonHits_cut_barrel_up}, {muon_NumberOfValidMuonHits_cut_endcap_lo}, {muon_NumberOfValidMuonHits_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, nanoAOD.Muon_numberOfValidMuonHits],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonNStationsCut = Producer(
    name="GoodMuonNStationsCut",
    call="physicsobject::CutIntVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_NStations_cut_barrel_lo}, {muon_NStations_cut_barrel_up}, {muon_NStations_cut_endcap_lo}, {muon_NStations_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, nanoAOD.Muon_nStations],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonNumberOfValidPixelHitsCut = Producer(
    name="GoodMuonNumberOfValidPixelHitsCut",
    call="physicsobject::CutIntVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_NumberOfValidPixelHits_cut_barrel_lo}, {muon_NumberOfValidPixelHits_cut_barrel_up}, {muon_NumberOfValidPixelHits_cut_endcap_lo}, {muon_NumberOfValidPixelHits_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, nanoAOD.Muon_numberOfValidPixelHits],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonNTrackerLayersCut = Producer(
    name="GoodMuonNTrackerLayersCut",
    call="physicsobject::CutIntVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_NTrackerLayers_cut_barrel_lo}, {muon_NTrackerLayers_cut_barrel_up}, {muon_NTrackerLayers_cut_endcap_lo}, {muon_NTrackerLayers_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, nanoAOD.Muon_nTrackerLayers],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonDxyCut = Producer(
    name="GoodMuonDxyCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_Dxy_cut_barrel_lo}, {muon_Dxy_cut_barrel_up}, {muon_Dxy_cut_endcap_lo}, {muon_Dxy_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, q.Muon_abs_dxy],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonDzCut = Producer(
    name="GoodMuonDzCut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_Dz_cut_barrel_lo}, {muon_Dz_cut_barrel_up}, {muon_Dz_cut_endcap_lo}, {muon_Dz_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, q.Muon_abs_dz],
    output=[],
    scopes=["mm", "mmet"],
)
GoodMuonNormalizedChi2Cut = Producer(
    name="GoodMuonNormalizedChi2Cut",
    call="physicsobject::CutVariableBarrelEndcap({df}, {output}, {input}, 1.2, {muon_NormalizedChi2_cut_barrel_lo}, {muon_NormalizedChi2_cut_barrel_up}, {muon_NormalizedChi2_cut_endcap_lo}, {muon_NormalizedChi2_cut_endcap_up})",
    input=[nanoAOD.Muon_eta, nanoAOD.Muon_normalizedChi2],
    output=[],
    scopes=["mm", "mmet"],
)

GoodMuonsCustom = ProducerGroup(
    name="GoodMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.good_muons_mask],
    scopes=["mm", "mmet"],
    subproducers=[
        GoodMuonPtCut,
        GoodMuonEtaCut,

        # Tight ID
        GoodMuonIsGlobalCut,
        GoodMuonIsPFCut,
        GoodMuonNumberOfValidMuonHitsCut,
        GoodMuonNStationsCut,
        GoodMuonNumberOfValidPixelHitsCut,
        GoodMuonNTrackerLayersCut,
        GoodMuonDxyCut,
        GoodMuonDzCut,
        GoodMuonNormalizedChi2Cut,

        GoodMuonIsoCut,
    ],
)

NumberOfGoodMuons = Producer(
    name="NumberOfGoodMuons",
    call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
    input=[q.good_muons_mask],
    output=[q.nmuons],
    scopes=["mm", "mmet"],
)

####################
# Set of producers used for more specific selection of muons in channels
####################





####################
# Set of producers used for additional muon veto
####################

OneGoodMuonFlag = Producer(
    name="OneGoodMuonFlag",
    call="physicsobject::CutNFlag({df}, {output}, {input}, {n_good_muons})",
    input={
        "mmet": [q.good_muons_mask],
    },
    output=[q.n_good_muons_flag],
    scopes=["mmet"],
)
OneGoodMuonFilter = Filter(
    name="OneGoodMuonFilter",
    call='basefunctions::FilterFlagsAny({df}, "OneGoodMuonFilter", {input})',
    input=[q.n_good_muons_flag],
    scopes=["mmet"],
    subproducers=[]
)
OneGoodMuon = Producer(
    name="OneGoodMuon",
    call="physicsobject::SelectedObjects({df}, {output}, {input})",
    input={
        "mmet": [q.good_muons_mask],
    },
    output=[q.selectedLepton],
    scopes=["mmet"],
)

MuonVetoPtCut = Producer(
    name="MuonVetoPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_veto_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["mmet"],
)
MuonVetoEtaCut = Producer(
    name="MuonVetoEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_veto_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["mmet"],
)
MuonVetoDxyCut = Producer(
    name="MuonVetoDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_muon_veto_dxy})",
    input=[nanoAOD.Muon_dxy],
    output=[],
    scopes=["mmet"],
)
MuonVetoDzCut = Producer(
    name="MuonVetoDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_muon_veto_dz})",
    input=[nanoAOD.Muon_dz],
    output=[],
    scopes=["mmet"],
)
MuonVetoIDCut = Producer(
    name="MuonVetoIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{muon_veto_id}")',
    input=[],
    output=[],
    scopes=["mmet"],
)
MuonVetoIsoCut = Producer(
    name="MuonVetoIsoCut",
    call="physicsobject::muon::CutIsolation({df}, {output}, {input}, {muon_veto_iso_cut})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=["mmet"],
)
LooseMuons = ProducerGroup(
    name="LooseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.loose_muons_mask],
    scopes=["mmet"],
    subproducers=[
        MuonVetoPtCut,
        MuonVetoEtaCut,
        MuonVetoDxyCut,
        MuonVetoDzCut,
        MuonVetoIDCut,
        MuonVetoIsoCut,
    ],
)
VetoMuons = Producer(
    name="VetoMuons",
    call="physicsobject::VetoCandInMask({df}, {output}, {input}, {muon_index_in_pair})",
    input=[q.loose_muons_mask, q.selectedLepton],
    output=[q.veto_muons_mask],
    scopes=["mmet"],
)
ExtraMuonsVeto = Producer(
    name="ExtraMuonsVeto",
    call="physicsobject::IsEmptyFlag({df}, {output}, {input})",
    input={
        "mmet": [q.veto_muons_mask],
    },
    output=[q.muon_veto_flag],
    scopes=["mmet"],
)
VetoMuonFilter = Filter(
    name="VetoMuonFilter",
    call='basefunctions::FilterFlagsAny({df}, "ExtraLooseMuonVeto", {input})',
    input=[q.muon_veto_flag],
    scopes=["mmet"],
    subproducers=[]
)

OneGoodMuonSelection = ProducerGroup(
    name="OneGoodMuonSelection",
    call=None,
    input=None,
    output=None,
    scopes=["mmet"],
    subproducers=[
        OneGoodMuonFlag,
        OneGoodMuonFilter,
        OneGoodMuon,

        LooseMuons,
        VetoMuons,
        ExtraMuonsVeto,
        # VetoMuonFilter,
    ]
)

TwoGoodMuonFlag = Producer(
    name="TwoGoodMuonFlag",
    call="physicsobject::CutNFlag({df}, {output}, {input}, {n_good_muons})",
    input={
        "mm": [q.good_muons_mask],
    },
    output=[q.n_good_muons_flag],
    scopes=["mm"],
)
TwoGoodMuonFilter = Filter(
    name="TwoGoodMuonFilter",
    call='basefunctions::FilterFlagsAny({df}, "TwoGoodMuonFilter", {input})',
    input=[q.n_good_muons_flag],
    scopes=["mm"],
    subproducers=[]
)
TwoGoodMuonSelection = ProducerGroup(
    name="TwoGoodMuonSelection",
    call=None,
    input=None,
    output=None,
    scopes=["mm"],
    subproducers=[
        TwoGoodMuonFlag,
        TwoGoodMuonFilter,
    ]
)

####################
# Set of producers used for di-muon veto
####################

# VetoMuons = Producer(
#     name="VetoMuons",
#     call="physicsobject::VetoCandInMask({df}, {output}, {input}, {muon_index_in_pair})",
#     input=[q.base_muons_mask, q.selectedLepton],
#     output=[q.veto_muons_mask],
#     scopes=["mm", "mmet"],
# )
# VetoSecondMuon = Producer(
#     name="VetoSecondMuon",
#     call="physicsobject::VetoCandInMask({df}, {output}, {input}, {second_muon_index_in_pair})",
#     input=[q.veto_muons_mask, q.selectedLepton],
#     output=[q.veto_muons_mask_2],
#     scopes=["mm"],
# )

# ExtraMuonsVeto = Producer(
#     name="ExtraMuonsVeto",
#     call="physicsobject::LeptonVetoFlag({df}, {output}, {input})",
#     input={
#         "mm": [q.veto_muons_mask_2],
#         "em": [q.veto_muons_mask],
#         "et": [q.base_muons_mask],
#         "mt": [q.veto_muons_mask],
#         "tt": [q.base_muons_mask],
#     },
#     output=[q.muon_veto_flag],
#     scopes=["em", "et", "mt", "tt", "mm"],
# )

# DiMuonVetoPtCut = Producer(
#     name="DiMuonVetoPtCut",
#     call="physicsobject::CutPt({df}, {input}, {output}, {min_dimuonveto_pt})",
#     input=[nanoAOD.Muon_pt],
#     output=[],
#     scopes=["global"],
# )
# DiMuonVetoIDCut = Producer(
#     name="DiMuonVetoIDCut",
#     call='physicsobject::muon::CutID({df}, {output}, "{dimuonveto_id}")',
#     input=[],
#     output=[],
#     scopes=["global"],
# )
# DiMuonVetoMuons = ProducerGroup(
#     name="DiMuonVetoMuons",
#     call="physicsobject::CombineMasks({df}, {output}, {input})",
#     input=MuonEtaCut.output + MuonDxyCut.output + MuonDzCut.output + MuonIsoCut.output,
#     output=[],
#     scopes=["global"],
#     subproducers=[
#         DiMuonVetoPtCut,
#         DiMuonVetoIDCut,
#     ],
# )
# DiMuonVeto = ProducerGroup(
#     name="DiMuonVeto",
#     call="physicsobject::CheckForDiLeptonPairs({df}, {output}, {input}, {dileptonveto_dR})",
#     input=[
#         nanoAOD.Muon_pt,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#         nanoAOD.Muon_charge,
#     ],
#     output=[q.dimuon_veto],
#     scopes=["global"],
#     subproducers=[DiMuonVetoMuons],
# )
