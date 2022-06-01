from code_generation.modifiers import EraModifier, SampleModifier


def add_earlyRun3TriggerSetup(configuration):
    ## mm, mmet scope trigger setup
    configuration.add_config_parameters(
        ["mm", "mmet"],
        {
            "singlemoun_trigger_1": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_mu24_1",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": -1,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.2,
                        },
                        {
                            "flagname": "trg_single_mu27_1",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": -1,
                            "etacut": 2.5,
                            "filterbit":-1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.2,
                        },
                    ],
                }
            ),
            "singlemoun_trigger_2": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_mu24_2",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": -1,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.2,
                        },
                        {
                            "flagname": "trg_single_mu27_2",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": -1,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.2,
                        },
                    ],
                }
            ),
        },
    )

    ## ee, emet scope trigger setup
    configuration.add_config_parameters(
        ["ee", "emet"],
        {
            "singleelectron_trigger_1": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_ele27_1",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 27,
                            "etacut": 2.7,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele32_1",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 32,
                            "etacut": 2.7,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele35_1",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 35,
                            "etacut": 2.7,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
            "singleelectron_trigger_2": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_ele27_2",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 27,
                            "etacut": 2.7,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele32_2",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 32,
                            "etacut": 2.7,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele35_2",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 35,
                            "etacut": 2.7,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    return configuration
