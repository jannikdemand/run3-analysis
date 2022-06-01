from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, Filter

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
        ElectronIDCut,
        ElectronIsoCut,
    ],
)

####################
# Set of producers used for more specific selection of electrons in channels
####################

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
        GoodElectronIsoCut,
    ],
)

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
    name="ElectronPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_electron_veto_pt})",
    input=[nanoAOD.Electron_pt],
    output=[],
    scopes=["emet"],
)
ElectronVetoEtaCut = Producer(
    name="ElectronEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_electron_veto_eta})",
    input=[nanoAOD.Electron_eta],
    output=[],
    scopes=["emet"],
)
ElectronVetoDxyCut = Producer(
    name="ElectronDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_electron_veto_dxy})",
    input=[nanoAOD.Electron_dxy],
    output=[],
    scopes=["emet"],
)
ElectronVetoDzCut = Producer(
    name="ElectronDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_electron_veto_dz})",
    input=[nanoAOD.Electron_dz],
    output=[],
    scopes=["emet"],
)
ElectronVetoIDCut = Producer(
    name="ElectronIDCut",
    call='physicsobject::electron::CutCBID({df}, {output}, "{electron_veto_id}", {electron_veto_id_wp})',
    input=[],
    output=[],
    scopes=["emet"],
)
ElectronVetoIsoCut = Producer(
    name="ElectronIsoCut",
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

        LooseElectrons,
        VetoElectrons,
        ExtraElectronsVeto,
        VetoElectronFilter,
    ]
)

####################
# Set of producers used for di-electron veto
####################

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
