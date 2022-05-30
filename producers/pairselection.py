from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, Filter

####################
# Set of producers used for contruction of MT good pairs and the coressponding lorentz vectors
####################

# MTPairSelection = Producer(
#     name="MTPairSelection",
#     call="ditau_pairselection::mutau::PairSelection({df}, {input_vec}, {output}, {pairselection_min_dR})",
#     input=[
#         q.Tau_pt_corrected,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         nanoAOD.Tau_mass,
#         nanoAOD.Tau_IDraw,
#         nanoAOD.Muon_pt,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#         nanoAOD.Muon_iso,
#         q.good_muons_mask,
#         q.good_taus_mask,
#     ],
#     output=[q.selectedLepton],
#     scopes=["mt"],
# )

# GoodMTPairFlag = Producer(
#     name="GoodMTPairFlag",
#     call="ditau_pairselection::flagGoodPairs({df}, {output}, {input})",
#     input=[q.selectedLepton],
#     output=[],
#     scopes=["mt"],
# )

# GoodMTPairFilter = Filter(
#     name="GoodMTPairFilter",
#     call='basefunctions::FilterFlagsAny({df}, "GoodMuTauPairs", {input})',
#     input=[],
#     scopes=["mt"],
#     subproducers=[GoodMTPairFlag],
# )

# LLPairSelection = Producer(
#     name="LLPairSelection",
#     call="ditau_pairselection::mumu::PairSelection({df}, {input_vec}, {output}, {pairselection_min_dR})",
#     input=[
#         nanoAOD.Muon_pt,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#         q.good_muons_mask,
#     ],
#     output=[q.selectedLepton],
#     scopes=["mm"],
# )

ZLLPairSelection = Producer(
    name="LLPairSelection",
    call="ditau_pairselection::mumu::ZBosonPairSelection({df}, {input_vec}, {output}, {pairselection_min_dR})",
    input= {
        "mm": [
            nanoAOD.Muon_pt,
            nanoAOD.Muon_eta,
            nanoAOD.Muon_phi,
            nanoAOD.Muon_mass,
            q.good_muons_mask,
        ],
        "ee": [
            nanoAOD.Electron_pt,
            nanoAOD.Electron_eta,
            nanoAOD.Electron_phi,
            nanoAOD.Electron_mass,
            q.good_electrons_mask,
        ],
    },
    output=[q.selectedLepton],
    scopes=["mm", "ee"],
)

GoodLLPairFlag = Producer(
    name="GoodLLPairFlag",
    call="ditau_pairselection::flagGoodPairs({df}, {output}, {input})",
    input=[q.selectedLepton],
    output=[],
    scopes=["mm", "ee"],
)

GoodLLPairFilter = Filter(
    name="GoodLLPairFilter",
    call='basefunctions::FilterFlagsAny({df}, "GoodLLPairFilter", {input})',
    input=[],
    scopes=["mm", "ee"],
    subproducers=[GoodLLPairFlag],
)

# ETPairSelection = Producer(
#     name="ETPairSelection",
#     call="ditau_pairselection::eltau::PairSelection({df}, {input_vec}, {output}, {pairselection_min_dR})",
#     input=[
#         q.Tau_pt_corrected,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         nanoAOD.Tau_mass,
#         nanoAOD.Tau_IDraw,
#         nanoAOD.Electron_pt,
#         nanoAOD.Electron_eta,
#         nanoAOD.Electron_phi,
#         nanoAOD.Electron_mass,
#         nanoAOD.Electron_iso,
#         q.good_electrons_mask,
#         q.good_taus_mask,
#     ],
#     output=[q.selectedLepton],
#     scopes=["et"],
# )

# GoodETPairFlag = Producer(
#     name="GoodETPairFlag",
#     call="ditau_pairselection::flagGoodPairs({df}, {output}, {input})",
#     input=[q.selectedLepton],
#     output=[],
#     scopes=["et"],
# )

# GoodETPairFilter = Filter(
#     name="GoodETPairFilter",
#     call='basefunctions::FilterFlagsAny({df}, "GoodElTauPairs", {input})',
#     input=[],
#     scopes=["et"],
#     subproducers=[GoodETPairFlag],
# )

####################
## TauTau Pair Selection
####################
# TTPairSelection = Producer(
#     name="TTPairSelection",
#     call="ditau_pairselection::tautau::PairSelection({df}, {input_vec}, {output}, {pairselection_min_dR})",
#     input=[
#         q.Tau_pt_corrected,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         nanoAOD.Tau_mass,
#         nanoAOD.Tau_IDraw,
#         q.good_taus_mask,
#     ],
#     output=[q.selectedLepton],
#     scopes=["tt"],
# )

# GoodTTPairFlag = Producer(
#     name="GoodTTPairFlag",
#     call="ditau_pairselection::flagGoodPairs({df}, {output}, {input})",
#     input=[q.selectedLepton],
#     output=[],
#     scopes=["tt"],
# )

# GoodTTPairFilter = Filter(
#     name="GoodTTPairFilter",
#     call='basefunctions::FilterFlagsAny({df}, "GoodTauTauPairs", {input})',
#     input=[],
#     scopes=["tt"],
#     subproducers=[GoodTTPairFlag],
# )
####################
## ElMu Pair Selection
####################

# EMPairSelection = Producer(
#     name="EMPairSelection",
#     call="ditau_pairselection::elmu::PairSelection({df}, {input_vec}, {output}, {pairselection_min_dR})",
#     input=[
#         nanoAOD.Electron_pt,
#         nanoAOD.Electron_eta,
#         nanoAOD.Electron_phi,
#         nanoAOD.Electron_mass,
#         nanoAOD.Electron_iso,
#         nanoAOD.Muon_pt,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#         nanoAOD.Muon_iso,
#         q.good_electrons_mask,
#         q.good_muons_mask,
#     ],
#     output=[q.selectedLepton],
#     scopes=["em"],
# )

# GoodEMPairFlag = Producer(
#     name="GoodEMPairFlag",
#     call="ditau_pairselection::flagGoodPairs({df}, {output}, {input})",
#     input=[q.selectedLepton],
#     output=[],
#     scopes=["em"],
# )

# GoodEMPairFilter = Filter(
#     name="GoodEMPairFilter",
#     call='basefunctions::FilterFlagsAny({df}, "GoodElMuPairs", {input})',
#     input=[],
#     scopes=["em"],
#     subproducers=[GoodEMPairFlag],
# )


LVMu1 = Producer(
    name="LVMu1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input = {
        "mm": [
            q.selectedLepton,
            nanoAOD.Muon_pt,
            nanoAOD.Muon_eta,
            nanoAOD.Muon_phi,
            nanoAOD.Muon_mass,
        ],
        "mmet": [
            q.selectedLepton,
            nanoAOD.Muon_pt,
            nanoAOD.Muon_eta,
            nanoAOD.Muon_phi,
            nanoAOD.Muon_mass,
        ],
    },
    output=[q.p4_1],
    scopes=["mm", "mmet"],
)
LVMu2 = Producer(
    name="LVMu2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.selectedLepton,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_2],
    scopes=["mm", "em"],
)
LVEl1 = Producer(
    name="LVEl1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input= {
        "ee": [
            q.selectedLepton,
            nanoAOD.Electron_pt,
            nanoAOD.Electron_eta,
            nanoAOD.Electron_phi,
            nanoAOD.Electron_mass,
        ],
        "emet": [
            q.selectedLepton,
            nanoAOD.Electron_pt,
            nanoAOD.Electron_eta,
            nanoAOD.Electron_phi,
            nanoAOD.Electron_mass,
        ],
    },
    output=[q.p4_1],
    scopes=["ee", "emet"],
)
LVEl2 = Producer(
    name="LVEl2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.selectedLepton,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_2],
    scopes=["ee"],
)
# LVTau1 = Producer(
#     name="LVTau1",
#     call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
#     input=[
#         q.selectedLepton,
#         q.Tau_pt_corrected,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         q.Tau_mass_corrected,
#     ],
#     output=[q.p4_1],
#     scopes=["tt"],
# )
# LVTau2 = Producer(
#     name="LVTau2",
#     call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
#     input=[
#         q.selectedLepton,
#         q.Tau_pt_corrected,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         q.Tau_mass_corrected,
#     ],
#     output=[q.p4_2],
#     scopes=["mt", "et", "tt"],
# )
## uncorrected versions of all particles, used for MET propagation
LVMu1Uncorrected = Producer(
    name="LVMu1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input = {
        "mm": [
            q.selectedLepton,
            nanoAOD.Muon_pt,
            nanoAOD.Muon_eta,
            nanoAOD.Muon_phi,
            nanoAOD.Muon_mass,
        ],
        "mmet": [
            q.selectedLepton,
            nanoAOD.Muon_pt,
            nanoAOD.Muon_eta,
            nanoAOD.Muon_phi,
            nanoAOD.Muon_mass,
        ],
    },
    output=[q.p4_1_uncorrected],
    scopes=["mm", "mmet"],
)
LVMu2Uncorrected = Producer(
    name="LVMu2Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.selectedLepton,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["mm", "em"],
)
LVEl1Uncorrected = Producer(
    name="LVEl1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input= {
        "ee": [
            q.selectedLepton,
            nanoAOD.Electron_pt,
            nanoAOD.Electron_eta,
            nanoAOD.Electron_phi,
            nanoAOD.Electron_mass,
        ],
        "emet": [
            q.selectedLepton,
            nanoAOD.Electron_pt,
            nanoAOD.Electron_eta,
            nanoAOD.Electron_phi,
            nanoAOD.Electron_mass,
        ],
    },
    output=[q.p4_1_uncorrected],
    scopes=["ee", "emet"],
)
LVEl2Uncorrected = Producer(
    name="LVEl2Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.selectedLepton,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["ee"],
)
# LVTau1Uncorrected = Producer(
#     name="LVTau1Uncorrected",
#     call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
#     input=[
#         q.selectedLepton,
#         nanoAOD.Tau_pt,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         nanoAOD.Tau_mass,
#     ],
#     output=[q.p4_1_uncorrected],
#     scopes=["tt"],
# )
# LVTau2Uncorrected = Producer(
#     name="LVTau2Uncorrected",
#     call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
#     input=[
#         q.selectedLepton,
#         nanoAOD.Tau_pt,
#         nanoAOD.Tau_eta,
#         nanoAOD.Tau_phi,
#         nanoAOD.Tau_mass,
#     ],
#     output=[q.p4_2_uncorrected],
#     scopes=["mt", "et", "tt"],
# )
