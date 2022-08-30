from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import event as event
from .producers import muons as muons
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity


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
            q.is_ttbar,
            q.is_singletop,
            q.is_ewk_tau,
            q.is_dyjets,
            q.is_wjets,
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