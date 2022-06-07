from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

# from .producers import electrons as electrons
from .producers import event as event
from .producers import genparticles as genparticles
# from .producers import jets as jets
# from .producers import met as met
from .producers import muons as muons
# from .producers import pairquantities as pairquantities
# from .producers import pairselection as pairselection
# from .producers import scalefactors as scalefactors
# from .producers import triggers as triggers
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
# from .triggersetup import add_earlyRun3TriggerSetup
# from .jet_variations import add_jetVariations
# from .jec_data import add_jetCorrectionData
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity
# from .variations import add_leptonSFShifts  # add_tauVariations


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

    configuration.add_config_parameters(
        "mm",
        {
            "min_muon_pt": -1.0,
        },
    )

    configuration.add_producers(
        "global",
        [
            event.SampleFlags,
            event.Lumi,
            event.EventGenWeight,
        ],
    )

    configuration.add_producers(
        "mm",
        [
            muons.GoodMuonPtCut
        ],
    )

    configuration.add_outputs(
        "mm",
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
            q.genweight,
        ],
    )

    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=[event.EventGenWeight],
            samples=["data"],
        ),
    )

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()