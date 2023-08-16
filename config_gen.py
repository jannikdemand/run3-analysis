from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import event as event
from .producers import genparticles as genparticles
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

    # configuration.add_config_parameters(
    #     "mm",
    #     {
    #     },
    # )

    configuration.add_producers(
        "global",
        [
            event.SampleFlags,
            event.Lumi,
            event.EventGenWeight,
            event.LHEPdfWeight,
            event.LHEScaleWeight,
            genparticles.DYFilters,
            genparticles.WFilters,
        ],
    )

    configuration.add_producers(
        "mm",
        [
            genparticles.GenLeptonProducers,
        ],
    )

    configuration.add_outputs(
        scopes,
        [
            getattr(q, f"LHEPdfWeight{i}") for i in range(103)
        ] + [
            getattr(q, f"LHEScaleWeight{i}") for i in range(8)
        ]
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

            q.is_dy_ee,
            q.is_dy_mm,
            q.is_dy_tt,

            q.is_w_e,
            q.is_w_m,
            q.is_w_t,

            nanoAOD.run,
            q.lumi,
            nanoAOD.event,
            q.genweight,

            q.genlep_pt_1,
            q.genlep_eta_1,
            q.genlep_phi_1,
            q.genlep_mass_1,
            q.genlep_pdgId_1,
            q.genlep_p4_1,

            q.genlep_pt_2,
            q.genlep_eta_2,
            q.genlep_phi_2,
            q.genlep_mass_2,
            q.genlep_pdgId_2,
            q.genlep_p4_2,

            q.genlepPreFSR_pt_1,
            q.genlepPreFSR_eta_1,
            q.genlepPreFSR_phi_1,
            q.genlepPreFSR_mass_1,
            q.genlepPreFSR_pdgId_1,
            q.genlepPreFSR_p4_1,

            q.genlepPreFSR_pt_2,
            q.genlepPreFSR_eta_2,
            q.genlepPreFSR_phi_2,
            q.genlepPreFSR_mass_2,
            q.genlepPreFSR_pdgId_2,
            q.genlepPreFSR_p4_2,

            q.genDressed_idx_1,
            q.genDressed_idx_2,

            q.genDressed_pt_1,
            q.genDressed_eta_1,
            q.genDressed_phi_1,
            q.genDressed_mass_1,
            q.genDressed_pdgId_1,
            q.genDressed_p4_1,
            q.genDressed_dR_1,

            q.genDressed_pt_2,
            q.genDressed_eta_2,
            q.genDressed_phi_2,
            q.genDressed_mass_2,
            q.genDressed_pdgId_2,
            q.genDressed_p4_2,
            q.genDressed_dR_2,

            q.genlep_dilepton_mass,
            q.genlepPreFSR_dilepton_mass,
            q.genDressed_dilepton_mass,
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