from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, ExtendedVectorProducer

####################
# Set of general producers for DiTauPair Quantities
####################

pt_1 = Producer(
    name="pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.pt_1],
    scopes=["mm", "mmet", "ee", "emet"],
)
pt_2 = Producer(
    name="pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.pt_2],
    scopes=["mm", "mmet", "ee", "emet"],
)
eta_1 = Producer(
    name="eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.eta_1],
    scopes=["mm", "mmet", "ee", "emet"],
)
eta_2 = Producer(
    name="eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.eta_2],
    scopes=["mm", "mmet", "ee", "emet"],
)
phi_1 = Producer(
    name="phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.phi_1],
    scopes=["mm", "mmet", "ee", "emet"],
)
phi_2 = Producer(
    name="phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.phi_2],
    scopes=["mm", "mmet", "ee", "emet"],
)
mass_1 = Producer(
    name="mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.mass_1],
    scopes=["mm", "mmet", "ee", "emet"],
)
mass_2 = Producer(
    name="mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.mass_2],
    scopes=["mm", "mmet", "ee", "emet"],
)
m_vis = Producer(
    name="m_vis",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.p4_1, q.p4_2],
    output=[q.m_vis],
    scopes=["mm", "mmet", "ee", "emet"],
)
pt_vis = Producer(
    name="pt_vis",
    call="quantities::pt_vis({df}, {output}, {input_vec})",
    input=[q.p4_1, q.p4_2],
    output=[q.pt_vis],
    scopes=["mm", "mmet", "ee", "emet"],
)
####################
# Set of channel specific producers
####################
muon_dxy_1 = Producer(
    name="muon_dxy_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dxy],
    output=[q.dxy_1],
    scopes=["mm", "mmet"],
)
muon_dxy_2 = Producer(
    name="muon_dxy_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dxy],
    output=[q.dxy_2],
    scopes=["mm"],
)
electron_dxy_1 = Producer(
    name="electron_dxy_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dxy],
    output=[q.dxy_1],
    scopes=["ee", "emet"],
)
electron_dxy_2 = Producer(
    name="electron_dxy_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dxy],
    output=[q.dxy_2],
    scopes=["ee"],
)

######################
###JULIUS ELECTRONS###
######################

#####float_t##########
electron_dxyErr_1 = Producer(
    name="electron_dxyErr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dxyErr],
    output=[q.dxyErr_1],
    scopes=["ee", "emet"],
)
electron_dxyErr_2 = Producer(
    name="electron_dxyErr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dxyErr],
    output=[q.dxyErr_2],
    scopes=["ee"],
)
electron_dzErr_1 = Producer(
    name="electron_dzErr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dzErr],
    output=[q.dzErr_1],
    scopes=["ee", "emet"],
)
electron_dzErr_2 = Producer(
    name="electron_dzErr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dzErr],
    output=[q.dzErr_2],
    scopes=["ee"],
)
electron_descaledown_1 = Producer(
    name="electron_descaledown_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEscaleDown],
    output=[q.descaledown_1],
    scopes=["ee", "emet"],
)
electron_descaledown_2 = Producer(
    name="electron_descaledown_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEscaleDown],
    output=[q.descaledown_2],
    scopes=["ee"],
)
electron_descaleup_1 = Producer(
    name="electron_descaleup_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEscaleUp],
    output=[q.descaleup_1],
    scopes=["ee", "emet"],
)
electron_descaleup_2 = Producer(
    name="electron_descaleup_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEscaleUp],
    output=[q.descaleup_2],
    scopes=["ee"],
)
electron_desigmadown_1 = Producer(
    name="electron_desigmadown_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEsigmaDown],
    output=[q.desigmadown_1],
    scopes=["ee", "emet"],
)
electron_desigmadown_2 = Producer(
    name="electron_desigmadown_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEsigmaDown],
    output=[q.desigmadown_2],
    scopes=["ee"],
)
electron_desigmaup_1 = Producer(
    name="electron_desigmaup_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEsigmaUp],
    output=[q.desigmaup_1],
    scopes=["ee", "emet"],
)
electron_desigmaup_2 = Producer(
    name="electron_desigmaup_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dEsigmaUp],
    output=[q.desigmaup_2],
    scopes=["ee"],
)
electron_deltaetaSC_1 = Producer(
    name="electron_deltaetaSC_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_deltaEtaSC],
    output=[q.deltaetaSC_1],
    scopes=["ee", "emet"],
)
electron_deltaetaSC_2 = Producer(
    name="electron_deltaetaSC_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_deltaEtaSC],
    output=[q.deltaetaSC_2],
    scopes=["ee"],
)
electron_dr03EcalRecHitSumEt_1 = Producer(
    name="electron_dr03EcalRecHitSumEt_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03EcalRecHitSumEt],
    output=[q.dr03EcalRecHitSumEt_1],
    scopes=["ee", "emet"],
)
electron_dr03EcalRecHitSumEt_2 = Producer(
    name="electron_dr03EcalRecHitSumEt_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03EcalRecHitSumEt],
    output=[q.dr03EcalRecHitSumEt_2],
    scopes=["ee"],
)
electron_dr03HcalDepth1TowerSumEt_1 = Producer(
    name="electron_dr03HcalDepth1TowerSumEt_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03HcalDepth1TowerSumEt],
    output=[q.dr03HcalDepth1TowerSumEt_1],
    scopes=["ee", "emet"],
)
electron_dr03HcalDepth1TowerSumEt_2 = Producer(
    name="electron_dr03HcalDepth1TowerSumEt_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03HcalDepth1TowerSumEt],
    output=[q.dr03HcalDepth1TowerSumEt_2],
    scopes=["ee"],
)
electron_dr03TkSumPt_1 = Producer(
    name="electron_dr03TkSumPt_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03TkSumPt],
    output=[q.dr03TkSumPt_1],
    scopes=["ee", "emet"],
)
electron_dr03TkSumPt_2 = Producer(
    name="electron_dr03TkSumPt_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03TkSumPt],
    output=[q.dr03TkSumPt_2],
    scopes=["ee"],
)
electron_dr03TkSumPtHEEP_1 = Producer(
    name="electron_dr03TkSumPtHEEP_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03TkSumPtHEEP],
    output=[q.dr03TkSumPtHEEP_1],
    scopes=["ee", "emet"],
)
electron_dr03TkSumPtHEEP_2 = Producer(
    name="electron_dr03TkSumPtHEEP_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dr03TkSumPtHEEP],
    output=[q.dr03TkSumPtHEEP_2],
    scopes=["ee"],
)
electron_eCorr_1 = Producer(
    name="electron_eCorr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_eCorr],
    output=[q.eCorr_1],
    scopes=["ee", "emet"],
)
electron_eCorr_2 = Producer(
    name="electron_eCorr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_eCorr],
    output=[q.eCorr_2],
    scopes=["ee"],
)
electron_eInvMinusPInv_1 = Producer(
    name="electron_eInvMinusPInv_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_eInvMinusPInv],
    output=[q.eInvMinusPInv_1],
    scopes=["ee", "emet"],
)
electron_eInvMinusPInv_2 = Producer(
    name="electron_eInvMinusPInv_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_eInvMinusPInv],
    output=[q.eInvMinusPInv_2],
    scopes=["ee"],
)
electron_energyErr_1 = Producer(
    name="electron_energyErr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_energyErr],
    output=[q.energyErr_1],
    scopes=["ee", "emet"],
)
electron_energyErr_2 = Producer(
    name="electron_energyErr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_energyErr],
    output=[q.energyErr_2],
    scopes=["ee"],
)
electron_hoe_1 = Producer(
    name="electron_hoe_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_hoe],
    output=[q.hoe_1],
    scopes=["ee", "emet"],
)
electron_hoe_2 = Producer(
    name="electron_hoe_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_hoe],
    output=[q.hoe_2],
    scopes=["ee"],
)
electron_ip3d_1 = Producer(
    name="electron_ip3d_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_ip3d],
    output=[q.ip3d_1],
    scopes=["ee", "emet"],
)
electron_ip3d_2 = Producer(
    name="electron_ip3d_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_ip3d],
    output=[q.ip3d_2],
    scopes=["ee"],
)
electron_jetPtRelv2_1 = Producer(
    name="electron_jetPtRelv2_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetPtRelv2],
    output=[q.jetPtRelv2_1],
    scopes=["ee", "emet"],
)
electron_jetPtRelv2_2 = Producer(
    name="electron_jetPtRelv2_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetPtRelv2],
    output=[q.jetPtRelv2_2],
    scopes=["ee"],
)
electron_jetRelIso_1 = Producer(
    name="electron_jetRelIso_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetRelIso],
    output=[q.jetRelIso_1],
    scopes=["ee", "emet"],
)
electron_jetRelIso_2 = Producer(
    name="electron_jetRelIso_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetRelIso],
    output=[q.jetRelIso_2],
    scopes=["ee"],
)
electron_miniPFRelIso_all_1 = Producer(
    name="electron_miniPFRelIso_all_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_miniPFRelIso_all],
    output=[q.miniPFRelIso_all_1],
    scopes=["ee", "emet"],
)
electron_miniPFRelIso_all_2 = Producer(
    name="electron_miniPFRelIso_all_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_miniPFRelIso_all],
    output=[q.miniPFRelIso_all_2],
    scopes=["ee"],
)
electron_mvaFall17V2Iso_1 = Producer(
    name="electron_mvaFall17V2Iso_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso],
    output=[q.mvaFall17V2Iso_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2Iso_2 = Producer(
    name="electron_mvaFall17V2Iso_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso],
    output=[q.mvaFall17V2Iso_2],
    scopes=["ee"],
)
electron_mvaFall17V2noIso_1 = Producer(
    name="electron_mvaFall17V2noIso_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso],
    output=[q.mvaFall17V2noIso_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2noIso_2 = Producer(
    name="electron_mvaFall17V2noIso_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso],
    output=[q.mvaFall17V2noIso_2],
    scopes=["ee"],
)
electron_mvaTTH_1 = Producer(
    name="electron_mvaTTH_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaTTH],
    output=[q.mvaTTH_1],
    scopes=["ee", "emet"],
)
electron_mvaTTH_2 = Producer(
    name="electron_mvaTTH_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaTTH],
    output=[q.mvaTTH_2],
    scopes=["ee"],
)
electron_pfRelIso03_all_1 = Producer(
    name="electron_pfRelIso03_all_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_pfRelIso03_all],
    output=[q.pfRelIso03_all_1],
    scopes=["ee", "emet"],
)
electron_pfRelIso03_all_2 = Producer(
    name="electron_pfRelIso03_all_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_pfRelIso03_all],
    output=[q.pfRelIso03_all_2],
    scopes=["ee"],
)
electron_pfRelIso03_chg_1 = Producer(
    name="electron_pfRelIso03_chg_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_pfRelIso03_chg],
    output=[q.pfRelIso03_chg_1],
    scopes=["ee", "emet"],
)
electron_pfRelIso03_chg_2 = Producer(
    name="electron_pfRelIso03_chg_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_pfRelIso03_chg],
    output=[q.pfRelIso03_chg_2],
    scopes=["ee"],
)
electron_r9_1 = Producer(
    name="electron_r9_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_r9],
    output=[q.r9_1],
    scopes=["ee", "emet"],
)
electron_r9_2 = Producer(
    name="electron_r9_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_r9],
    output=[q.r9_2],
    scopes=["ee"],
)
electron_scEtOverPt_1 = Producer(
    name="electron_scEtOverPt_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_scEtOverPt],
    output=[q.scEtOverPt_1],
    scopes=["ee", "emet"],
)
electron_scEtOverPt_2 = Producer(
    name="electron_scEtOverPt_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_scEtOverPt],
    output=[q.scEtOverPt_2],
    scopes=["ee"],
)
electron_sieie_1 = Producer(
    name="electron_sieie_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_sieie],
    output=[q.sieie_1],
    scopes=["ee", "emet"],
)
electron_sieie_2 = Producer(
    name="electron_sieie_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_sieie],
    output=[q.sieie_2],
    scopes=["ee"],
)
electron_sip3d_1 = Producer(
    name="electron_sip3d_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_sip3d],
    output=[q.sip3d_1],
    scopes=["ee", "emet"],
)
electron_sip3d_2 = Producer(
    name="electron_sip3d_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_sip3d],
    output=[q.sip3d_2],
    scopes=["ee"],
)

#####int_t##########
electron_cutBased_1 = Producer(
    name="electron_cutBased_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_cutBased],
    output=[q.cutBased_1],
    scopes=["ee", "emet"],
)
electron_cutBased_2 = Producer(
    name="electron_cutBased_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_cutBased],
    output=[q.cutBased_2],
    scopes=["ee"],
)
electron_jetIdx_1 = Producer(
    name="electron_jetIdx_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetIdx],
    output=[q.jetIdx_1],
    scopes=["ee", "emet"],
)
electron_jetIdx_2 = Producer(
    name="electron_jetIdx_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetIdx],
    output=[q.jetIdx_2],
    scopes=["ee"],
)
electron_photonIdx_1 = Producer(
    name="electron_photonIdx_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_photonIdx],
    output=[q.photonIdx_1],
    scopes=["ee", "emet"],
)
electron_photonIdx_2 = Producer(
    name="electron_photonIdx_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_photonIdx],
    output=[q.photonIdx_2],
    scopes=["ee"],
)
electron_tightCharge_1 = Producer(
    name="electron_tightCharge_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_tightCharge],
    output=[q.tightCharge_1],
    scopes=["ee", "emet"],
)
electron_tightCharge_2 = Producer(
    name="electron_tightCharge_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_tightCharge],
    output=[q.tightCharge_2],
    scopes=["ee"],
)
electron_vidNestedWPBitmap_1 = Producer(
    name="electron_vidNestedWPBitmap_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_vidNestedWPBitmap],
    output=[q.vidNestedWPBitmap_1],
    scopes=["ee", "emet"],
)
electron_vidNestedWPBitmap_2 = Producer(
    name="electron_vidNestedWPBitmap_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_vidNestedWPBitmap],
    output=[q.vidNestedWPBitmap_2],
    scopes=["ee"],
)
electron_vidNestedWPBitmapHEEP_1 = Producer(
    name="electron_vidNestedWPBitmapHEEP_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_vidNestedWPBitmapHEEP],
    output=[q.vidNestedWPBitmapHEEP_1],
    scopes=["ee", "emet"],
)
electron_vidNestedWPBitmapHEEP_2 = Producer(
    name="electron_vidNestedWPBitmapHEEP_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_vidNestedWPBitmapHEEP],
    output=[q.vidNestedWPBitmapHEEP_2],
    scopes=["ee"],
)
electron_jetNDauCharged_1 = Producer(
    name="electron_jetNDauCharged_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetNDauCharged],
    output=[q.jetNDauCharged_1],
    scopes=["ee", "emet"],
)
electron_jetNDauCharged_2 = Producer(
    name="electron_jetNDauCharged_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_jetNDauCharged],
    output=[q.jetNDauCharged_2],
    scopes=["ee"],
)
electron_lostHits_1 = Producer(
    name="electron_lostHits_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_lostHits],
    output=[q.lostHits_1],
    scopes=["ee", "emet"],
)
electron_lostHits_2 = Producer(
    name="electron_lostHits_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_lostHits],
    output=[q.lostHits_2],
    scopes=["ee"],
)
electron_seedGain_1 = Producer(
    name="electron_seedGain_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_seedGain],
    output=[q.seedGain_1],
    scopes=["ee", "emet"],
)
electron_seedGain_2 = Producer(
    name="electron_seedGain_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_seedGain],
    output=[q.seedGain_2],
    scopes=["ee"],
)
#####bool_t##########
electron_convVeto_1 = Producer(
    name="electron_convVeto_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_convVeto],
    output=[q.convVeto_1],
    scopes=["ee", "emet"],
)
electron_convVeto_2 = Producer(
    name="electron_convVeto_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_convVeto],
    output=[q.convVeto_2],
    scopes=["ee"],
)
electron_cutBased_HEEP_1 = Producer(
    name="electron_cutBased_HEEP_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_cutBased_HEEP],
    output=[q.cutBased_HEEP_1],
    scopes=["ee", "emet"],
)
electron_cutBased_HEEP_2 = Producer(
    name="electron_cutBased_HEEP_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_cutBased_HEEP],
    output=[q.cutBased_HEEP_2],
    scopes=["ee"],
)
electron_isPFcand_1 = Producer(
    name="electron_isPFcand_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_isPFcand],
    output=[q.isPFcand_1],
    scopes=["ee", "emet"],
)
electron_isPFcand_2 = Producer(
    name="electron_isPFcand_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_isPFcand],
    output=[q.isPFcand_2],
    scopes=["ee"],
)
electron_mvaFall17V2Iso_WP80_1 = Producer(
    name="electron_mvaFall17V2Iso_WP80_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso_WP80],
    output=[q.mvaFall17V2Iso_WP80_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2Iso_WP80_2 = Producer(
    name="electron_mvaFall17V2Iso_WP80_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso_WP80],
    output=[q.mvaFall17V2Iso_WP80_2],
    scopes=["ee"],
)
electron_mvaFall17V2Iso_WP90_1 = Producer(
    name="electron_mvaFall17V2Iso_WP90_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso_WP90],
    output=[q.mvaFall17V2Iso_WP90_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2Iso_WP90_2 = Producer(
    name="electron_mvaFall17V2Iso_WP90_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso_WP90],
    output=[q.mvaFall17V2Iso_WP90_2],
    scopes=["ee"],
)
electron_mvaFall17V2Iso_WPL_1 = Producer(
    name="electron_mvaFall17V2Iso_WPL_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso_WPL],
    output=[q.mvaFall17V2Iso_WPL_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2Iso_WPL_2 = Producer(
    name="electron_mvaFall17V2Iso_WPL_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2Iso_WPL],
    output=[q.mvaFall17V2Iso_WPL_2],
    scopes=["ee"],
)
electron_mvaFall17V2noIso_WP80_1 = Producer(
    name="electron_mvaFall17V2noIso_WP80_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso_WP80],
    output=[q.mvaFall17V2noIso_WP80_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2noIso_WP80_2 = Producer(
    name="electron_mvaFall17V2noIso_WP80_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso_WP80],
    output=[q.mvaFall17V2noIso_WP80_2],
    scopes=["ee"],
)
electron_mvaFall17V2noIso_WP90_1 = Producer(
    name="electron_mvaFall17V2noIso_WP90_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso_WP90],
    output=[q.mvaFall17V2noIso_WP90_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2noIso_WP90_2 = Producer(
    name="electron_mvaFall17V2noIso_WP90_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso_WP90],
    output=[q.mvaFall17V2noIso_WP90_2],
    scopes=["ee"],
)
electron_mvaFall17V2noIso_WPL_1 = Producer(
    name="electron_mvaFall17V2noIso_WPL_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso_WPL],
    output=[q.mvaFall17V2noIso_WPL_1],
    scopes=["ee", "emet"],
)
electron_mvaFall17V2noIso_WPL_2 = Producer(
    name="electron_mvaFall17V2noIso_WPL_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_mvaFall17V2noIso_WPL],
    output=[q.mvaFall17V2noIso_WPL_2],
    scopes=["ee"],
)

###################
###END ELECTRONS###
###################

##################
###JULIUS MUONS###
##################

#FROM ELECTRON CHANNELS
muon_dxyErr_1 = Producer(
    name="muon_dxyErr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dxyErr],
    output=[q.dxyErr_1],
    scopes=["mm", "mmet"],
)
muon_dxyErr_2 = Producer(
    name="muon_dxyErr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dxyErr],
    output=[q.dxyErr_2],
    scopes=["mm"],
)
muon_dzErr_1 = Producer(
    name="muon_dzErr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dzErr],
    output=[q.dzErr_1],
    scopes=["mm", "mmet"],
)
muon_dzErr_2 = Producer(
    name="muon_dzErr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dzErr],
    output=[q.dzErr_2],
    scopes=["mm"],
)
muon_ip3d_1 = Producer(
    name="muon_ip3d_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_ip3d],
    output=[q.ip3d_1],
    scopes=["mm", "mmet"],
)
muon_ip3d_2 = Producer(
    name="muon_ip3d_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_ip3d],
    output=[q.ip3d_2],
    scopes=["mm"],
)
muon_jetIdx_1 = Producer(
    name="muon_jetIdx_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetIdx],
    output=[q.jetIdx_1],
    scopes=["mm", "mmet"],
)
muon_jetIdx_2 = Producer(
    name="muon_jetIdx_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetIdx],
    output=[q.jetIdx_2],
    scopes=["mm"],
)
muon_jetNDauCharged_1 = Producer(
    name="muon_jetNDauCharged_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetNDauCharged],
    output=[q.jetNDauCharged_1],
    scopes=["mm", "mmet"],
)
muon_jetNDauCharged_2 = Producer(
    name="muon_jetNDauCharged_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetNDauCharged],
    output=[q.jetNDauCharged_2],
    scopes=["mm"],
)
muon_jetPtRelv2_1 = Producer(
    name="muon_jetPtRelv2_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetPtRelv2],
    output=[q.jetPtRelv2_1],
    scopes=["mm", "mmet"],
)
muon_jetPtRelv2_2 = Producer(
    name="muon_jetPtRelv2_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetPtRelv2],
    output=[q.jetPtRelv2_2],
    scopes=["mm"],
)
muon_jetRelIso_1 = Producer(
    name="muon_jetRelIso_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetRelIso],
    output=[q.jetRelIso_1],
    scopes=["mm", "mmet"],
)
muon_jetRelIso_2 = Producer(
    name="muon_jetRelIso_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_jetRelIso],
    output=[q.jetRelIso_2],
    scopes=["mm"],
)
muon_miniPFRelIso_all_1 = Producer(
    name="muon_miniPFRelIso_all_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_miniPFRelIso_all],
    output=[q.miniPFRelIso_all_1],
    scopes=["mm", "mmet"],
)
muon_miniPFRelIso_all_2 = Producer(
    name="muon_miniPFRelIso_all_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_miniPFRelIso_all],
    output=[q.miniPFRelIso_all_2],
    scopes=["mm"],
)
muon_mvaTTH_1 = Producer(
    name="muon_mvaTTH_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaTTH],
    output=[q.mvaTTH_1],
    scopes=["mm", "mmet"],
)
muon_mvaTTH_2 = Producer(
    name="muon_mvaTTH_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaTTH],
    output=[q.mvaTTH_2],
    scopes=["mm"],
)
muon_sip3d_1 = Producer(
    name="muon_sip3d_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_sip3d],
    output=[q.sip3d_1],
    scopes=["mm", "mmet"],
)
muon_sip3d_2 = Producer(
    name="muon_sip3d_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_sip3d],
    output=[q.sip3d_2],
    scopes=["mm"],
)
muon_tightCharge_1 = Producer(
    name="muon_tightCharge_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tightCharge],
    output=[q.tightCharge_1],
    scopes=["mm", "mmet"],
)
muon_tightCharge_2 = Producer(
    name="muon_tightCharge_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tightCharge],
    output=[q.tightCharge_2],
    scopes=["mm"],
)

#### FLOATS #####
muon_dxybs_1 = Producer(
    name="muon_dxybs_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dxybs],
    output=[q.dxybs_1],
    scopes=["mm", "mmet"],
)
muon_dxybs_2 = Producer(
    name="muon_dxybs_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dxybs],
    output=[q.dxybs_2],
    scopes=["mm"],
)
muon_miniPFRelIso_chg_1 = Producer(
    name="muon_miniPFRelIso_chg_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_miniPFRelIso_chg],
    output=[q.miniPFRelIso_chg_1],
    scopes=["mm", "mmet"],
)
muon_miniPFRelIso_chg_2 = Producer(
    name="muon_miniPFRelIso_chg_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_miniPFRelIso_chg],
    output=[q.miniPFRelIso_chg_2],
    scopes=["mm"],
)
muon_mvaLowPt_chg_1 = Producer(
    name="muon_mvaLowPt_chg_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaLowPt],
    output=[q.mvaLowPt_chg_1],
    scopes=["mm", "mmet"],
)
muon_mvaLowPt_chg_2 = Producer(
    name="muon_mvaLowPt_chg_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaLowPt],
    output=[q.mvaLowPt_chg_2],
    scopes=["mm"],
)
muon_pfRelIso03_all_1 = Producer(
    name="muon_pfRelIso03_all_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfRelIso03_all],
    output=[q.pfRelIso03_all_1],
    scopes=["mm", "mmet"],
)
muon_pfRelIso03_all_2 = Producer(
    name="muon_pfRelIso03_all_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfRelIso03_all],
    output=[q.pfRelIso03_all_2],
    scopes=["mm"],
)
muon_pfRelIso03_chg_1 = Producer(
    name="muon_pfRelIso03_chg_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfRelIso03_chg],
    output=[q.pfRelIso03_chg_1],
    scopes=["mm", "mmet"],
)
muon_pfRelIso03_chg_2 = Producer(
    name="muon_pfRelIso03_chg_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfRelIso03_chg],
    output=[q.pfRelIso03_chg_2],
    scopes=["mm"],
)
muon_pfRelIso04_all_1 = Producer(
    name="muon_pfRelIso04_all_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfRelIso04_all],
    output=[q.pfRelIso04_all_1],
    scopes=["mm", "mmet"],
)
muon_pfRelIso04_all_2 = Producer(
    name="muon_pfRelIso04_all_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfRelIso04_all],
    output=[q.pfRelIso04_all_2],
    scopes=["mm"],
)
muon_ptErr_1 = Producer(
    name="muon_ptErr_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_ptErr],
    output=[q.ptErr_1],
    scopes=["mm", "mmet"],
)
muon_ptErr_2 = Producer(
    name="muon_ptErr_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_ptErr],
    output=[q.ptErr_2],
    scopes=["mm"],
)
muon_segmentComp_1 = Producer(
    name="muon_segmentComp_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_segmentComp],
    output=[q.segmentComp_1],
    scopes=["mm", "mmet"],
)
muon_segmentComp_2 = Producer(
    name="muon_segmentComp_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_segmentComp],
    output=[q.segmentComp_2],
    scopes=["mm"],
)
muon_softMva_1 = Producer(
    name="muon_softMva_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softMva],
    output=[q.softMva_1],
    scopes=["mm", "mmet"],
)
muon_softMva_2 = Producer(
    name="muon_softMva_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softMva],
    output=[q.softMva_2],
    scopes=["mm"],
)
muon_tkRelIso_1 = Producer(
    name="muon_tkRelIso_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tkRelIso],
    output=[q.tkRelIso_1],
    scopes=["mm", "mmet"],
)
muon_tkRelIso_2 = Producer(
    name="muon_tkRelIso_1",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tkRelIso],
    output=[q.tkRelIso_2],
    scopes=["mm"],
)

###### INT_T  ########
muon_fsrPhotonIdx_1 = Producer(
    name="muon_fsrPhotonIdx_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_fsrPhotonIdx],
    output=[q.fsrPhotonIdx_1],
    scopes=["mm", "mmet"],
)
muon_fsrPhotonIdx_2 = Producer(
    name="muon_fsrPhotonIdx_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_fsrPhotonIdx],
    output=[q.fsrPhotonIdx_2],
    scopes=["mm"],
)
# muon_genPartIdx_1 = Producer(
#     name="muon_genPartIdx_1",
#     call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
#     input=[q.selectedLepton, nanoAOD.Muon_genPartIdx],
#     output=[q.genPartIdx_1],
#     scopes=["mm", "mmet"],
# )
# muon_genPartIdx_2 = Producer(
#     name="muon_genPartIdx_2",
#     call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
#     input=[q.selectedLepton, nanoAOD.Muon_genPartIdx],
#     output=[q.genPartIdx_2],
#     scopes=["mm"],
# )
muon_highPtId_1 = Producer(
    name="muon_highPtId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_highPtId],
    output=[q.highPtId_1],
    scopes=["mm", "mmet"],
)
muon_highPtId_2 = Producer(
    name="muon_highPtId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_highPtId],
    output=[q.highPtId_2],
    scopes=["mm"],
)
muon_miniIsoId_1 = Producer(
    name="muon_miniIsoId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_miniIsoId],
    output=[q.miniIsoId_1],
    scopes=["mm", "mmet"],
)
muon_miniIsoId_2 = Producer(
    name="muon_miniIsoId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_miniIsoId],
    output=[q.miniIsoId_2],
    scopes=["mm"],
)
muon_multiIsoId_1 = Producer(
    name="muon_multiIsoId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_multiIsoId],
    output=[q.multiIsoId_1],
    scopes=["mm", "mmet"],
)
muon_multiIsoId_2 = Producer(
    name="muon_multiIsoId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_multiIsoId],
    output=[q.multiIsoId_2],
    scopes=["mm"],
)
muon_mvaId_1 = Producer(
    name="muon_mvaId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaId],
    output=[q.mvaId_1],
    scopes=["mm", "mmet"],
)
muon_mvaId_2 = Producer(
    name="muon_mvaId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaId],
    output=[q.mvaId_2],
    scopes=["mm"],
)
muon_mvaLowPtId_1 = Producer(
    name="muon_mvaLowPtId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaLowPtId],
    output=[q.mvaLowPtId_1],
    scopes=["mm", "mmet"],
)
muon_mvaLowPtId_2 = Producer(
    name="muon_mvaLowPtId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mvaLowPtId],
    output=[q.mvaLowPtId_2],
    scopes=["mm"],
)
muon_nStations_1 = Producer(
    name="muon_nStations_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_nStations],
    output=[q.nStations_1],
    scopes=["mm", "mmet"],
)
muon_nStations_2 = Producer(
    name="muon_nStations_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_nStations],
    output=[q.nStations_2],
    scopes=["mm"],
)
muon_nTrackerLayers_1 = Producer(
    name="muon_nTrackerLayers_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_nTrackerLayers],
    output=[q.nTrackerLayers_1],
    scopes=["mm", "mmet"],
)
muon_nTrackerLayers_2 = Producer(
    name="muon_nTrackerLayers_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_nTrackerLayers],
    output=[q.nTrackerLayers_2],
    scopes=["mm"],
)
muon_pfIsoId_1 = Producer(
    name="muon_pfIsoId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfIsoId],
    output=[q.pfIsoId_1],
    scopes=["mm", "mmet"],
)
muon_pfIsoId_2 = Producer(
    name="muon_pfIsoId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_pfIsoId],
    output=[q.pfIsoId_2],
    scopes=["mm"],
)
muon_puppiIsoId_1 = Producer(
    name="muon_puppiIsoId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_puppiIsoId],
    output=[q.puppiIsoId_1],
    scopes=["mm", "mmet"],
)
muon_puppiIsoId_2 = Producer(
    name="muon_puppiIsoId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_puppiIsoId],
    output=[q.puppiIsoId_2],
    scopes=["mm"],
)
muon_tkIsoId_1 = Producer(
    name="muon_tkIsoId_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tkIsoId],
    output=[q.tkIsoId_1],
    scopes=["mm", "mmet"],
)
muon_tkIsoId_2 = Producer(
    name="muon_tkIsoId_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tkIsoId],
    output=[q.tkIsoId_2],
    scopes=["mm"],
)

#### bool_t #####
muon_highPurity_1 = Producer(
    name="muon_highPurity_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_highPurity],
    output=[q.highPurity_1],
    scopes=["mm", "mmet"],
)
muon_highPurity_2 = Producer(
    name="muon_highPurity_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_highPurity],
    output=[q.highPurity_2],
    scopes=["mm"],
)
muon_inTimeMuon_1 = Producer(
    name="muon_inTimeMuon_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_inTimeMuon],
    output=[q.inTimeMuon_1],
    scopes=["mm", "mmet"],
)
muon_inTimeMuon_2 = Producer(
    name="muon_inTimeMuon_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_inTimeMuon],
    output=[q.inTimeMuon_2],
    scopes=["mm"],
)
muon_isGlobal_1 = Producer(
    name="muon_isGlobal_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isGlobal],
    output=[q.isGlobal_1],
    scopes=["mm", "mmet"],
)
muon_isGlobal_2 = Producer(
    name="muon_isGlobal_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isGlobal],
    output=[q.isGlobal_2],
    scopes=["mm"],
)
muon_isStandalone_1 = Producer(
    name="muon_isStandalone_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isStandalone],
    output=[q.isStandalone_1],
    scopes=["mm", "mmet"],
)
muon_isStandalone_2 = Producer(
    name="muon_isStandalone_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isStandalone],
    output=[q.isStandalone_2],
    scopes=["mm"],
)
muon_isTracker_1 = Producer(
    name="muon_isTracker_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isTracker],
    output=[q.isTracker_1],
    scopes=["mm", "mmet"],
)
muon_isTracker_2 = Producer(
    name="muon_isTracker_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isTracker],
    output=[q.isTracker_2],
    scopes=["mm"],
)
muon_looseId_1 = Producer(
    name="muon_looseId_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_looseId],
    output=[q.looseId_1],
    scopes=["mm", "mmet"],
)
muon_looseId_2 = Producer(
    name="muon_looseId_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_looseId],
    output=[q.looseId_2],
    scopes=["mm"],
)
muon_mediumId_1 = Producer(
    name="muon_mediumId_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mediumId],
    output=[q.mediumId_1],
    scopes=["mm", "mmet"],
)
muon_mediumId_2 = Producer(
    name="muon_mediumId_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mediumId],
    output=[q.mediumId_2],
    scopes=["mm"],
)
muon_mediumPromptId_1 = Producer(
    name="muon_mediumPromptId_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mediumPromptId],
    output=[q.mediumPromptId_1],
    scopes=["mm", "mmet"],
)
muon_mediumPromptId_2 = Producer(
    name="muon_mediumPromptId_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_mediumPromptId],
    output=[q.mediumPromptId_2],
    scopes=["mm"],
)
muon_softId_1 = Producer(
    name="muon_softId_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softId],
    output=[q.softId_1],
    scopes=["mm", "mmet"],
)
muon_softId_2 = Producer(
    name="muon_softId_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softId],
    output=[q.softId_2],
    scopes=["mm"],
)
muon_tightId_1 = Producer(
    name="muon_tightId_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_tightId],
    output=[q.tightId_1],
    scopes=["mm", "mmet"],
)
muon_tightId_2 = Producer(
    name="muon_tightId_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softId],
    output=[q.tightId_2],
    scopes=["mm"],
)
muon_triggerIdLoose_1 = Producer(
    name="muon_triggerIdLoose_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_triggerIdLoose],
    output=[q.triggerIdLoose_1],
    scopes=["mm", "mmet"],
)
muon_triggerIdLoose_2 = Producer(
    name="muon_triggerIdLoose_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_triggerIdLoose],
    output=[q.triggerIdLoose_2],
    scopes=["mm"],
)
muon_softMvaId_1 = Producer(
    name="muon_softMvaId_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softMvaId],
    output=[q.softMvaId_1],
    scopes=["mm", "mmet"],
)
muon_softMvaId_2 = Producer(
    name="muon_softMvaId_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_softMvaId],
    output=[q.softMvaId_2],
    scopes=["mm"],
)
muon_isPFcand_1 = Producer(
    name="muon_isPFcand_1",
    call="basefunctions::getvar<bool>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isPFcand],
    output=[q.isPFcand_1],
    scopes=["mm", "mmet"],
)
muon_isPFcand_2 = Producer(
    name="muon_isPFcand_2",
    call="basefunctions::getvar<bool>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_isPFcand],
    output=[q.isPFcand_2],
    scopes=["mm"],
)

###################
#####END MUONS#####
###################
muon_dz_1 = Producer(
    name="muon_dz_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dz],
    output=[q.dz_1],
    scopes=["mm", "mmet"],
)
muon_dz_2 = Producer(
    name="muon_dz_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_dz],
    output=[q.dz_2],
    scopes=["mm"],
)
electron_dz_1 = Producer(
    name="electron_dz_1",
    call="basefunctions::getvar<float>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dz],
    output=[q.dz_1],
    scopes=["ee", "emet"],
)
electron_dz_2 = Producer(
    name="electron_dz_2",
    call="basefunctions::getvar<float>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_dz],
    output=[q.dz_2],
    scopes=["ee"],
)
muon_q_1 = Producer(
    name="muon_q_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_charge],
    output=[q.q_1],
    scopes=["mm", "mmet"],
)
muon_q_2 = Producer(
    name="muon_q_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_charge],
    output=[q.q_2],
    scopes=["mm"],
)
electron_q_1 = Producer(
    name="electron_q_1",
    call="basefunctions::getvar<int>({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_charge],
    output=[q.q_1],
    scopes=["ee", "emet"],
)
electron_q_2 = Producer(
    name="electron_q_2",
    call="basefunctions::getvar<int>({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_charge],
    output=[q.q_2],
    scopes=["ee"],
)
muon_iso_1 = Producer(
    name="muon_iso_1",
    call="quantities::isolation({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_iso],
    output=[q.iso_1],
    scopes=["mm", "mmet"],
)
muon_iso_2 = Producer(
    name="muon_iso_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Muon_iso],
    output=[q.iso_2],
    scopes=["mm"],
)
electron_iso_1 = Producer(
    name="electron_iso_1",
    call="quantities::isolation({df}, {output}, 0, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_iso],
    output=[q.iso_1],
    scopes=["ee", "emet"],
)
electron_iso_2 = Producer(
    name="electron_iso_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.selectedLepton, nanoAOD.Electron_iso],
    output=[q.iso_2],
    scopes=["ee"],
)

FirstElectronProducers = ProducerGroup(
    name="FirstElectronProducers",
    call=None,
    input=None,
    output=None,
    scopes=["ee", "emet"],
    subproducers=[
        electron_dxyErr_1,
        electron_dzErr_1,
        electron_descaledown_1,
        electron_descaleup_1,
        electron_desigmadown_1,
        electron_desigmaup_1,
        electron_deltaetaSC_1,
        electron_dr03EcalRecHitSumEt_1,
        electron_dr03HcalDepth1TowerSumEt_1,
        electron_dr03TkSumPt_1,
        electron_dr03TkSumPtHEEP_1,
        electron_eCorr_1,
        electron_eInvMinusPInv_1,
        electron_energyErr_1,
        electron_hoe_1,
        electron_ip3d_1,
        electron_jetPtRelv2_1,
        electron_jetRelIso_1,
        electron_miniPFRelIso_all_1,
        electron_mvaFall17V2Iso_1,
        electron_mvaFall17V2noIso_1,
        electron_mvaTTH_1,
        electron_pfRelIso03_all_1,
        electron_pfRelIso03_chg_1,
        electron_r9_1,
        electron_scEtOverPt_1,
        electron_sieie_1,
        electron_sip3d_1,
        electron_cutBased_1,
        electron_jetIdx_1,
        electron_photonIdx_1,
        electron_tightCharge_1,
        electron_vidNestedWPBitmap_1,
        electron_vidNestedWPBitmapHEEP_1,
        electron_convVeto_1,
        electron_cutBased_HEEP_1,
        electron_isPFcand_1,
        electron_mvaFall17V2Iso_WP80_1,
        electron_mvaFall17V2Iso_WP90_1,
        electron_mvaFall17V2Iso_WPL_1,
        electron_mvaFall17V2noIso_WP80_1,
        electron_mvaFall17V2noIso_WP90_1,
        electron_mvaFall17V2noIso_WPL_1,
        electron_jetNDauCharged_1,
        electron_lostHits_1,
        electron_seedGain_1,
    ],
)
SecondElectronProducers = ProducerGroup(
    name="SecondElectronProducers",
    call=None,
    input=None,
    output=None,
    scopes=["ee"],
    subproducers=[
        electron_dxyErr_2,
        electron_dzErr_2,
        electron_descaledown_2,
        electron_descaleup_2,
        electron_desigmadown_2,
        electron_desigmaup_2,
        electron_deltaetaSC_2,
        electron_dr03EcalRecHitSumEt_2,
        electron_dr03HcalDepth1TowerSumEt_2,
        electron_dr03TkSumPt_2,
        electron_dr03TkSumPtHEEP_2,
        electron_eCorr_2,
        electron_eInvMinusPInv_2,
        electron_energyErr_2,
        electron_hoe_2,
        electron_ip3d_2,
        electron_jetPtRelv2_2,
        electron_jetRelIso_2,
        electron_miniPFRelIso_all_2,
        electron_mvaFall17V2Iso_2,
        electron_mvaFall17V2noIso_2,
        electron_mvaTTH_2,
        electron_pfRelIso03_all_2,
        electron_pfRelIso03_chg_2,
        electron_r9_2,
        electron_scEtOverPt_2,
        electron_sieie_2,
        electron_sip3d_2,
        electron_cutBased_2,
        electron_jetIdx_2,
        electron_photonIdx_2,
        electron_tightCharge_2,
        electron_vidNestedWPBitmap_2,
        electron_vidNestedWPBitmapHEEP_2,
        electron_convVeto_2,
        electron_cutBased_HEEP_2,
        electron_isPFcand_2,
        electron_mvaFall17V2Iso_WP80_2,
        electron_mvaFall17V2Iso_WP90_2,
        electron_mvaFall17V2Iso_WPL_2,
        electron_mvaFall17V2noIso_WP80_2,
        electron_mvaFall17V2noIso_WP90_2,
        electron_mvaFall17V2noIso_WPL_2,
        electron_jetNDauCharged_2,
        electron_lostHits_2,
        electron_seedGain_2,
    ],
)

FirstMuonProducers = ProducerGroup(
    name="FirstMuonProducers",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "mmet"],
    subproducers=[
        muon_dxyErr_1,
        muon_dzErr_1,
        muon_ip3d_1,
        muon_jetIdx_1,
        muon_jetNDauCharged_1,
        muon_jetPtRelv2_1,
        muon_jetRelIso_1,
        muon_miniPFRelIso_all_1,
        muon_mvaTTH_1,
        muon_sip3d_1,
        muon_tightCharge_1,
        muon_dxybs_1,
        muon_miniPFRelIso_chg_1,
        muon_mvaLowPt_chg_1,
        muon_pfRelIso03_all_1,
        muon_pfRelIso03_chg_1,
        muon_pfRelIso04_all_1,
        muon_ptErr_1,
        muon_segmentComp_1,
        muon_softMva_1,
        muon_tkRelIso_1,
        muon_fsrPhotonIdx_1,
        # muon_genPartIdx_1,
        muon_highPtId_1,
        muon_miniIsoId_1,
        muon_multiIsoId_1,
        muon_mvaId_1,
        muon_mvaLowPtId_1,
        muon_nStations_1,
        muon_nTrackerLayers_1,
        muon_pfIsoId_1,
        muon_puppiIsoId_1,
        muon_tkIsoId_1,
        muon_highPurity_1,
        muon_inTimeMuon_1,
        muon_isGlobal_1,
        muon_isStandalone_1,
        muon_isTracker_1,
        muon_looseId_1,
        muon_mediumId_1,
        muon_mediumPromptId_1,
        muon_softId_1,
        muon_tightId_1,
        muon_triggerIdLoose_1,
        muon_softMvaId_1,
        muon_isPFcand_1,
    ],
)
SecondMuonProducers = ProducerGroup(
    name="SecondMuonProducers",
    call=None,
    input=None,
    output=None,
    scopes=["mm"],
    subproducers=[
        muon_dxyErr_2,
        muon_dzErr_2,
        muon_ip3d_2,
        muon_jetIdx_2,
        muon_jetNDauCharged_2,
        muon_jetPtRelv2_2,
        muon_jetRelIso_2,
        muon_miniPFRelIso_all_2,
        muon_mvaTTH_2,
        muon_sip3d_2,
        muon_tightCharge_2,
        muon_dxybs_2,
        muon_miniPFRelIso_chg_2,
        muon_mvaLowPt_chg_2,
        muon_pfRelIso03_all_2,
        muon_pfRelIso03_chg_2,
        muon_pfRelIso04_all_2,
        muon_ptErr_2,
        muon_segmentComp_2,
        muon_softMva_2,
        muon_tkRelIso_2,
        muon_fsrPhotonIdx_2,
        # muon_genPartIdx_2,
        muon_highPtId_2,
        muon_miniIsoId_2,
        muon_multiIsoId_2,
        muon_mvaId_2,
        muon_mvaLowPtId_2,
        muon_nStations_2,
        muon_nTrackerLayers_2,
        muon_pfIsoId_2,
        muon_puppiIsoId_2,
        muon_tkIsoId_2,
        muon_highPurity_2,
        muon_inTimeMuon_2,
        muon_isGlobal_2,
        muon_isStandalone_2,
        muon_isTracker_2,
        muon_looseId_2,
        muon_mediumId_2,
        muon_mediumPromptId_2,
        muon_softId_2,
        muon_tightId_2,
        muon_triggerIdLoose_2,
        muon_softMvaId_2,
        muon_isPFcand_2,
    ],
)

UnrollMuLV1 = ProducerGroup(
    name="UnrollMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "mmet"],
    subproducers=[
        pt_1,
        eta_1,
        phi_1,
        mass_1,
        muon_dxy_1,
        muon_dz_1,
        muon_q_1,
        muon_iso_1,
    ],
)
UnrollMuLV2 = ProducerGroup(
    name="UnrollMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "em"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        muon_dxy_2,
        muon_dz_2,
        muon_q_2,
        muon_iso_2,
    ],
)
UnrollElLV1 = ProducerGroup(
    name="UnrollElLV1",
    call=None,
    input=None,
    output=None,
    scopes=["ee", "emet"],
    subproducers=[
        pt_1,
        eta_1,
        phi_1,
        mass_1,
        electron_dxy_1,
        electron_dz_1,
        electron_q_1,
        electron_iso_1,
    ],
)
UnrollElLV2 = ProducerGroup(
    name="UnrollElLV2",
    call=None,
    input=None,
    output=None,
    scopes=["ee"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        electron_dxy_2,
        electron_dz_2,
        electron_q_2,
        electron_iso_2,
    ],
)

# Rochester correction
ApplyRoccoRData_1 = Producer(
    name="ApplyRoccoRData_1",
    call="physicsobject::muon::applyRoccoRData({df}, {output}, {RoccoR_file}, 0, {input}, {RoccoR_error_set}, {RoccoR_error_member})",
    input=[
        q.selectedLepton,
        nanoAOD.Muon_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
    ],
    output=[q.pt_rc_1],
    scopes=["mm", "mmet"],
)

ApplyRoccoRData_2 = Producer(
    name="ApplyRoccoRData_2",
    call="physicsobject::muon::applyRoccoRData({df}, {output}, {RoccoR_file}, 1, {input}, {RoccoR_error_set}, {RoccoR_error_member})",
    input=[
        q.selectedLepton,
        nanoAOD.Muon_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
    ],
    output=[q.pt_rc_2],
    scopes=["mm"],
)

ApplyRoccoRData = ProducerGroup(
    name="ApplyRoccoRData",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "mmet"],
    subproducers= {
        "mm": [ApplyRoccoRData_1, ApplyRoccoRData_2],
        "mmet": [ApplyRoccoRData_1],
    }
)

MuonRoccoRRndm = Producer(
    name="MuonRndm",
    call="physicsobject::muon::GenerateRndmRVec({df}, {output}, {input}, {RoccoR_seed})",
    input=[
        q.selectedLepton,
    ],
    output=[q.rndms],
    scopes=["mm", "mmet"],
)

ApplyRoccoRMC_1 = Producer(
    name="ApplyRoccoRMC_1",
    call="physicsobject::muon::applyRoccoRMC({df}, {output}, {RoccoR_file}, 0, {input}, {RoccoR_error_set}, {RoccoR_error_member})",
    input=[
        q.selectedLepton,
        nanoAOD.Muon_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        q.genmatch_pt_1,
        nanoAOD.Muon_nTrackerLayers,
        q.rndms
    ],
    output=[q.pt_rc_1],
    scopes=["mm", "mmet"],
)

ApplyRoccoRMC_2 = Producer(
    name="ApplyRoccoRMC_2",
    call="physicsobject::muon::applyRoccoRMC({df}, {output}, {RoccoR_file}, 1, {input}, {RoccoR_error_set}, {RoccoR_error_member})",
    input=[
        q.selectedLepton,
        nanoAOD.Muon_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        q.genmatch_pt_2,
        nanoAOD.Muon_nTrackerLayers,
        q.rndms
    ],
    output=[q.pt_rc_2],
    scopes=["mm"],
)

ApplyRoccoRMC = ProducerGroup(
    name="ApplyRoccoRMC",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "mmet"],
    subproducers= {
        "mm": [MuonRoccoRRndm, ApplyRoccoRMC_1, ApplyRoccoRMC_2],
        "mmet": [MuonRoccoRRndm, ApplyRoccoRMC_1],
    }
)

#####################
# Producer Groups
#####################

DileptonQuantities = ProducerGroup(
    name="DileptonQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "ee"],
    subproducers= {
        "mm": [UnrollMuLV1, UnrollMuLV2, m_vis, pt_vis],
        "ee": [UnrollElLV1, UnrollElLV2, m_vis, pt_vis],
    }
)

## advanced event quantities (can be caluculated when ditau pair and met and all jets are determined)
## leptons: q.p4_1, q.p4_2
## met: met_p4_recoilcorrected
## jets: good_jet_collection (if only the leading two are needed: q.jet_p4_1, q.jet_p4_2
## bjets: gen_bjet_collection

Pzetamissvis = Producer(
    name="Pzetamissvis",
    call="quantities::pzetamissvis({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.met_p4_recoilcorrected],
    output=[q.pzetamissvis],
    scopes=["mm", "mmet", "ee", "emet"],
)
mTdileptonMET = Producer(
    name="mTdileptonMET",
    call="quantities::mTdileptonMET({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.met_p4_recoilcorrected],
    output=[q.mTdileptonMET],
    scopes=["mm", "mmet", "ee", "emet"],
)
mt_1 = Producer(
    name="mt_1",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_1, q.met_p4],
    output=[q.mt_1],
    scopes=["mm", "mmet", "ee", "emet"],
)
mt_2 = Producer(
    name="mt_2",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_2, q.met_p4],
    output=[q.mt_2],
    scopes=["mm", "mmet", "ee", "emet"],
)
pt_tt = Producer(
    name="pt_tt",
    call="quantities::pt_tt({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.met_p4_recoilcorrected],
    output=[q.pt_tt],
    scopes=["mm", "mmet", "ee", "emet"],
)
pt_ttjj = Producer(
    name="pt_ttjj",
    call="quantities::pt_ttjj({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.jet_p4_1, q.jet_p4_2, q.met_p4_recoilcorrected],
    output=[q.pt_ttjj],
    scopes=["mm", "mmet", "ee", "emet"],
)
mt_tot = Producer(
    name="mt_tot",
    call="quantities::mt_tot({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.met_p4_recoilcorrected],
    output=[q.mt_tot],
    scopes=["mm", "mmet", "ee", "emet"],
)
DileptonMETQuantities = ProducerGroup(
    name="DileptonMETQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mm", "mmet", "ee", "emet"],
    subproducers=[mt_1, mt_2],  # Pzetamissvis, mTdileptonMET, pt_tt, pt_ttjj, mt_tot
)

# Lepton + MET quantities
LepMETQuantities = ProducerGroup(
    name="LepMETQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mmet", "emet"],
    subproducers= {
        "mmet": [UnrollMuLV1, mt_1],
        "emet": [UnrollElLV1, mt_1],
    },
)
