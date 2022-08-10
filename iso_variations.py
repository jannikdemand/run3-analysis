
def apply_leptonIsoCutVariations(configuration, cut_lo = -1., cut_up = 0.15):
    configuration.add_config_parameters(
        ["mm"],
        {
            # "muon_iso_cut": 0.15,
            "muon_iso_cut_barrel_lo": cut_lo,
            "muon_iso_cut_barrel_up": cut_up,
            "muon_iso_cut_endcap_lo": cut_lo,
            "muon_iso_cut_endcap_up": cut_up,
        },
    )

    configuration.add_config_parameters(
        ["mmet"],
        {
            # "muon_iso_cut": 0.15,
            "muon_iso_cut_barrel_lo": -1.,
            "muon_iso_cut_barrel_up": 1.e9,
            "muon_iso_cut_endcap_lo": -1.,
            "muon_iso_cut_endcap_up": 1.e9,
        },
    )

    # muon_iso_variations = [
    #     (0.15, 0.20),
    #     (0.20, 0.25),
    #     (0.25, 0.30),
    #     (0.30, 0.35),
    #     (0.35, 0.40),
    #     (0.40, 0.45),
    #     (0.45, 0.50),
    #     (0.50, 0.55),
    #     (0.55, 0.60),
    #     (0.60, 1.0),
    # ]

    # for cut_lo, cut_up in muon_iso_variations:
    #     cut_name = "CutMuonIso{:.2f}To{:.2f}".format(cut_lo, cut_up).replace(".", "p")
    #     configuration.add_shift(
    #         SystematicShift(
    #             name=cut_name,
    #             scopes = ["mm", "mmet"],
    #             shift_config={
    #                 ("mm", "mmet"): {
    #                     "muon_iso_cut_barrel_lo": cut_lo,
    #                     "muon_iso_cut_barrel_up": cut_up,
    #                     "muon_iso_cut_endcap_lo": cut_lo,
    #                     "muon_iso_cut_endcap_up": cut_up,
    #                 },
    #             },
    #             producers={
    #                 "mm": [
    #                     muons.GoodMuonIsoCut,
    #                 ],
    #                 "mmet": [
    #                     muons.GoodMuonIsoCut,
    #                 ]
    #             },
    #         )
    #     )

    return configuration


