
def customize_MuonIDIso(configuration):
    configuration.add_config_parameters(
        ["mm", "mmet"],
        {
            "muon_NumberOfValidMuonHits_cut_barrel_lo": 1,
            "muon_NumberOfValidMuonHits_cut_barrel_up": 1e9,
            "muon_NumberOfValidMuonHits_cut_endcap_lo": 1,
            "muon_NumberOfValidMuonHits_cut_endcap_up": 1e9,

            "muon_NStations_cut_barrel_lo": 2,
            "muon_NStations_cut_barrel_up": 1e9,
            "muon_NStations_cut_endcap_lo": 2,
            "muon_NStations_cut_endcap_up": 1e9,

            "muon_NumberOfValidPixelHits_cut_barrel_lo": 1,
            "muon_NumberOfValidPixelHits_cut_barrel_up": 1e9,
            "muon_NumberOfValidPixelHits_cut_endcap_lo": 1,
            "muon_NumberOfValidPixelHits_cut_endcap_up": 1e9,

            "muon_NTrackerLayers_cut_barrel_lo": 6,
            "muon_NTrackerLayers_cut_barrel_up": 1e9,
            "muon_NTrackerLayers_cut_endcap_lo": 6,
            "muon_NTrackerLayers_cut_endcap_up": 1e9,

            "muon_Dxy_cut_barrel_lo": -1.,
            "muon_Dxy_cut_barrel_up": 0.2,
            "muon_Dxy_cut_endcap_lo": -1.,
            "muon_Dxy_cut_endcap_up": 0.2,

            "muon_Dz_cut_barrel_lo": -1.,
            "muon_Dz_cut_barrel_up": 0.5,
            "muon_Dz_cut_endcap_lo": -1.,
            "muon_Dz_cut_endcap_up": 0.5,

            "muon_NormalizedChi2_cut_barrel_lo": -1.,
            "muon_NormalizedChi2_cut_barrel_up": 10.,
            "muon_NormalizedChi2_cut_endcap_lo": -1.,
            "muon_NormalizedChi2_cut_endcap_up": 10.,
        },
    )

    configuration.add_config_parameters(
        ["mm"],
        {
            "muon_iso_cut_barrel_lo": -1.,
            "muon_iso_cut_barrel_up": 0.15,
            "muon_iso_cut_endcap_lo": -1.,
            "muon_iso_cut_endcap_up": 0.15,
        },
    )

    configuration.add_config_parameters(
        ["mmet"],
        {
            "muon_iso_cut_barrel_lo": -1.,
            "muon_iso_cut_barrel_up": 1.e9,
            "muon_iso_cut_endcap_lo": -1.,
            "muon_iso_cut_endcap_up": 1.e9,
        },
    )

    return configuration

def customize_ElectronIDIso(configuration):
    configuration.add_config_parameters(
        ["ee", "emet"],
        {
            "ele_Sieie_cut_barrel_lo": -1.,
            "ele_Sieie_cut_barrel_up": 0.0106,
            "ele_Sieie_cut_endcap_lo": -1.,
            "ele_Sieie_cut_endcap_up": 0.0387,

            "ele_DEtaInSeed_cut_barrel_lo": -1.,
            "ele_DEtaInSeed_cut_barrel_up": 0.0032,
            "ele_DEtaInSeed_cut_endcap_lo": -1.,
            "ele_DEtaInSeed_cut_endcap_up": 0.00632,

            "ele_DeltaPhiSuperClusterTrackAtVtx_cut_barrel_lo": -1.,
            "ele_DeltaPhiSuperClusterTrackAtVtx_cut_barrel_up": 0.0547,
            "ele_DeltaPhiSuperClusterTrackAtVtx_cut_endcap_lo": -1.,
            "ele_DeltaPhiSuperClusterTrackAtVtx_cut_endcap_up": 0.0394,

            "ele_Hoe_cut_barrel_0": 0.046,
            "ele_Hoe_cut_barrel_1": 1.16,
            "ele_Hoe_cut_barrel_2": 0.0324,
            "ele_Hoe_cut_endcap_0": 0.0275,
            "ele_Hoe_cut_endcap_1": 2.52,
            "ele_Hoe_cut_endcap_2": 0.183,

            "ele_EInvMinusPInv_cut_barrel_lo": -1.,
            "ele_EInvMinusPInv_cut_barrel_up": 0.184,
            "ele_EInvMinusPInv_cut_endcap_lo": -1.,
            "ele_EInvMinusPInv_cut_endcap_up": 0.0721,

            "ele_LostHits_cut_barrel_lo": -1,
            "ele_LostHits_cut_barrel_up": 2,
            "ele_LostHits_cut_endcap_lo": -1,
            "ele_LostHits_cut_endcap_up": 2,
        },
    )

    configuration.add_config_parameters(
        ["ee"],
        {
            "ele_Iso_cut_barrel_0": 0.0478,
            "ele_Iso_cut_barrel_1": 0.506,
            "ele_Iso_cut_endcap_0": 0.0658,
            "ele_Iso_cut_endcap_1": 0.963,
        },
    )

    configuration.add_config_parameters(
        ["emet"],
        {
            "ele_Iso_cut_barrel_0": 1.e9,
            "ele_Iso_cut_barrel_1": 0.,
            "ele_Iso_cut_endcap_0": 1.e9,
            "ele_Iso_cut_endcap_1": 0.,
        },
    )

    return configuration
