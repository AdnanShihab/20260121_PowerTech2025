
# -------------------------------------- PV Parameters --------------------------------------
pv_life_time = 25
land_area_pv = 16187    # OLD value = 9290  # [m2 per 1 MW solar]
# roof_top_area_pv = 6000  # [m2 per 1 MW solar]

cost_land_industry_2025 = 0.35      # [EUR/m2/year] --> used for Gas Gen, PV and BESS

price_rooftop_leasing_yearly = 3    # EUR/m2; EUR 15000 per 5000 m2 --> used for PV

cost_fom_pv_ground_2025 = 10000

cost_fom_pv_roof_2025 = 7000


# -------------------------------------- WT Parameters --------------------------------------
wt_life_time = 30       # life-time

cost_land_lease_2025 = 0.061     # EUR/m2/year

land_area_wt = 80937.2  # [square meters/1MW] --> 1 MW needs approx. 20 acres

cost_fom_wt_2025 = 38000        # EUR/m2/year


# -------------------------------------- CHP Parameters --------------------------------------
land_area_chp = 46.67       # m2/MW

cost_fom_chp_2025 = 855000 * 0.03   # 3% of the investment cost

cost_ch4_import_2025 = 77           # [EUR/MWh]

# -------------------------------------- HP Parameters --------------------------------------
land_area_hp = 7.48     # m2/MW

cost_fom_hp_2025 = 30000


# -------------------------------------- P2G Parameters --------------------------------------
land_area_p2g = 29.28   # m2/MW

cost_fom_p2g_2025 = 2320000 * 0.04      # 4% of the CAPEX

import_tariff = 1   #0%
tax = 0.6

cost_h2_import_2025 = (190)+(190*tax)
cost_h2_import_2026 = (180)+(180*tax)
cost_h2_import_2027 = (170)+(170*tax)
cost_h2_import_2028 = (160)+(160*tax)
cost_h2_import_2029 = (150)+(150*tax)
cost_h2_import_2030 = (140)+(140*tax)
cost_h2_import_2031 = (130*import_tariff)+(130*tax)
cost_h2_import_2032 = (125*import_tariff)+(125*tax)
cost_h2_import_2033 = (122*import_tariff)+(122*tax)
cost_h2_import_2034 = (120*import_tariff)+(120*tax)


# -------------------------------------- BESS Parameters --------------------------------------
bess_life_time = 15     # Hoppecke li-ion 3150 Ah battery pack

cost_land_business_2025 = 91        # [EUR/m2] To purchase land --> used for P2G, BESS
cost_land_residential_2025 = 206    # To purchase land --> used for BESS, CHP, heat pump and th storage

land_area_bess = 49.88  # [m2 per 1 MW Battery pack]

cost_fom_bess_2025 = 4598.5


# -------------------------------------- Th Storage Parameters --------------------------------------
land_area_th_storage = 20   # m2/MW

cost_fom_th_storage_2025 = 10000


# -------------------------------------- H2 Storage Parameters --------------------------------------
# Add H2 storage parameters



# -------------------------------------- Gas Gen Parameters --------------------------------------
land_area_gen = 46.67       # Same as CHP plant
cost_fom_gen_2025 = 19050


# -------------------------------------- Power Grid Parameters --------------------------------------
# Switzerland
e_price__import_eur_mwh_2025 = 166
e_price_import_eur_mwh_2026 = 169
e_price_import_eur_mwh_2027 = 171
e_price_import_eur_mwh_2028 = 173
e_price_import_eur_mwh_2029 = 175
e_price_import_eur_mwh_2030 = 177
e_price_import_eur_mwh_2031 = 179
e_price_import_eur_mwh_2032 = 181
e_price_import_eur_mwh_2033 = 183
e_price_import_eur_mwh_2034 = 184

# Germany [vbw  - Oberer Preispfad]
# e_price__import_eur_mwh_2025 = 254
# e_price_import_eur_mwh_2026 = 226
# e_price_import_eur_mwh_2027 = 202
# e_price_import_eur_mwh_2028 = 170
# e_price_import_eur_mwh_2029 = 141
# e_price_import_eur_mwh_2030 = 120
# e_price_import_eur_mwh_2031 = 120
# e_price_import_eur_mwh_2032 = 119
# e_price_import_eur_mwh_2033 = 117
# e_price_import_eur_mwh_2034 = 116

# Switzerland
e_price_export_eur_mwh_2025 = 55
e_price_export_eur_mwh_2026 = 56
e_price_export_eur_mwh_2027 = 57
e_price_export_eur_mwh_2028 = 58
e_price_export_eur_mwh_2029 = 58
e_price_export_eur_mwh_2030 = 59
e_price_export_eur_mwh_2031 = 60
e_price_export_eur_mwh_2032 = 60
e_price_export_eur_mwh_2033 = 61
e_price_export_eur_mwh_2034 = 61

# Germany [vbw - Unterer Preispfad]
# e_price_export_eur_mwh_2025 = 88
# e_price_export_eur_mwh_2026 = 82
# e_price_export_eur_mwh_2027 = 77
# e_price_export_eur_mwh_2028 = 66
# e_price_export_eur_mwh_2029 = 59
# e_price_export_eur_mwh_2030 = 54
# e_price_export_eur_mwh_2031 = 55
# e_price_export_eur_mwh_2032 = 55
# e_price_export_eur_mwh_2033 = 55
# e_price_export_eur_mwh_2034 = 55

e_price_curt_eur_mwh_2025 = 80
e_price_curt_eur_mwh_2026 = 80
e_price_curt_eur_mwh_2027 = 80
e_price_curt_eur_mwh_2028 = 80
e_price_curt_eur_mwh_2029 = 80
e_price_curt_eur_mwh_2030 = 80
e_price_curt_eur_mwh_2031 = 80
e_price_curt_eur_mwh_2032 = 80
e_price_curt_eur_mwh_2033 = 80
e_price_curt_eur_mwh_2034 = 80



class OPEX:
    def __init__(self, stage, year, net, x_pv_bus, x_pv_size, x_wt_bus, x_wt_mw,
                 demand_e_mwh_jan, sgen_mwh_jan, bess_mwh_jan, gas_gen_mwh_jan, ext_e_mwh_jan,
                 x_chp_bus, x_chp_mw, chp_ch4_import_jan, chp_ch4_import_jul,
                 x_hp_bus, x_hp_size, x_storage_th_size, x_p2g_size_mw,
                 x_storage_h2_mwh, h2_import_jan, h2_import_jul, x_bess_bus, x_bess_mw,
                 demand_e_mwh_jul, sgen_mwh_jul, bess_mwh_jul, gas_gen_mwh_jul, ext_e_mwh_jul,
                 x_gen_bus_12_mw, x_gen_bus_1_mw, **kwargs):

        self.stage = stage
        self.year = year
        # self.day = day
        self.net = net
        # self.x = x
        self.x_pv_bus = x_pv_bus
        self.x_pv_size = x_pv_size
        self.x_wt_bus = x_wt_bus
        self.x_wt_mw = x_wt_mw
        self.x_chp_bus = x_chp_bus
        self.x_chp_mw = x_chp_mw
        self.chp_ch4_import_jan = chp_ch4_import_jan
        self.chp_ch4_import_jul = chp_ch4_import_jul
        self.x_hp_bus = x_hp_bus
        self.x_hp_size = x_hp_size
        self.x_storage_th_size = x_storage_th_size
        self.x_p2g_size_mw = x_p2g_size_mw
        self.h2_import_jan = h2_import_jan
        self.h2_import_jul = h2_import_jul
        self.x_storage_h2_mwh = x_storage_h2_mwh
        self.x_bess_bus = x_bess_bus
        self.x_bess_mw = x_bess_mw
        self.demand_e_mwh_jan = demand_e_mwh_jan
        self.sgen_mwh_jan = sgen_mwh_jan
        self.bess_mwh_jan = bess_mwh_jan
        self.gas_gen_mwh_jan = gas_gen_mwh_jan
        self.ext_e_mwh_jan = ext_e_mwh_jan
        self.demand_e_mwh_jul = demand_e_mwh_jul
        self.sgen_mwh_jul = sgen_mwh_jul
        self.bess_mwh_jul = bess_mwh_jul
        self.gas_gen_mwh_jul = gas_gen_mwh_jul
        self.ext_e_mwh_jul = ext_e_mwh_jul
        self.x_gen_bus_12_mw = x_gen_bus_12_mw
        self.x_gen_bus_1_mw = x_gen_bus_1_mw

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2025 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def opex_fixed_loc_elem_2025(self):     # Yearly cost calculation
        cost_om_fixed_loc_element_2025 = 0

        # ---------------------------- WT OM ----------------------------
        cost_wt_2025 = (self.x_wt_mw * cost_land_lease_2025 * land_area_wt) + \
                (cost_fom_wt_2025 * self.x_wt_mw)   # considering the agricultural land used in WT installations
        # are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element_2025 += cost_wt_2025

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_2025 = (self.x_p2g_size_mw * cost_land_business_2025 * land_area_p2g) + \
                (cost_fom_p2g_2025 * self.x_p2g_size_mw)
        cost_om_fixed_loc_element_2025 += cost_p2g_2025

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import_2025 * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import_2025 * self.h2_import_jul

        cost_om_fixed_loc_element_2025 += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_2025 = (self.x_chp_mw * cost_land_residential_2025 * land_area_chp) + \
                        (cost_fom_chp_2025 * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_2025_jan = cost_ch4_import_2025 * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_2025_jul = cost_ch4_import_2025 * self.chp_ch4_import_jul

        cost_om_fixed_loc_element_2025 += cost_chp_om_2025 + cost_chp_ch4_import_2025_jan + cost_chp_ch4_import_2025_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_opex_hp_2025 = (self.x_hp_size * cost_land_residential_2025 * land_area_hp) + \
                           (cost_fom_hp_2025 * self.x_hp_size)
        cost_om_fixed_loc_element_2025 += cost_opex_hp_2025

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_2025 = (self.x_gen_bus_12_mw * cost_land_industry_2025 * land_area_gen) + \
                        (cost_fom_gen_2025 * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element_2025 += cost_gen_bus12_2025       # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_2025 = (self.x_gen_bus_1_mw * cost_land_industry_2025 * land_area_gen) + \
                              (cost_fom_gen_2025 * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element_2025 += cost_gen_bus1_2025        # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_fom_th_storage = (self.x_storage_th_size * cost_land_residential_2025 * land_area_th_storage) + \
                              (cost_fom_th_storage_2025 * self.x_storage_th_size)
        cost_om_fixed_loc_element_2025 += cost_fom_th_storage

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element_2025

    def opex_var_loc_elem_2025(self):  # Yearly cost calculation
        cost_om_var_loc_element_2025 = 0

        # ---------------------------- PV OPEX COST -------------------------------
        cost_maint_pv_2025 = 0

        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                # print("PV in Industrial area - bus 1")
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * cost_land_industry_2025 * land_area_pv) + \
                                (cost_fom_pv_ground_2025*pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)

            elif v_x_pv_bus == 2:
                # print("PV in Industrial area - bus 2")

                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * cost_land_industry_2025 * land_area_pv) + \
                                (cost_fom_pv_ground_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 12:
                # print("PV in Industrial area - bus 12")

                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * cost_land_industry_2025 * land_area_pv) + \
                                (cost_fom_pv_ground_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 13:
                # print("PV in Industrial area - bus 13")

                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * cost_land_industry_2025 * land_area_pv) + \
                                (cost_fom_pv_ground_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 14:
                # print("PV in Industrial area - bus 13")

                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * cost_land_industry_2025 * land_area_pv) + \
                                (cost_fom_pv_ground_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof_2025 * pv_size)
                cost_maint_pv_2025 += cost_maint_pv
                # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
            else:
                print("missing bus bars in the grid for PV")

        # ---------------------------- BESS OPEX COST -------------------------------
        cost_om_bess_2025 = 0

        if self.x_bess_bus == 1:        # Ind area
            cost_om_bess = (self.x_bess_mw * cost_land_industry_2025 * land_area_bess) + \
                            (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 2:      # Ind area
            cost_om_bess = (self.x_bess_mw * cost_land_industry_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 12:     # Ind area
            cost_om_bess = (self.x_bess_mw * cost_land_industry_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 13:     # Ind area
            cost_om_bess = (self.x_bess_mw * cost_land_industry_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 14:     # Ind area
            cost_om_bess = (self.x_bess_mw * cost_land_industry_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 3:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 4:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 5:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 7:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 8:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 9:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 10:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 11:     # Comm area
            cost_om_bess = (self.x_bess_mw * cost_land_business_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        elif self.x_bess_bus == 6:     # Residential area
            cost_om_bess = (self.x_bess_mw * cost_land_residential_2025 * land_area_bess) + \
                           (cost_fom_bess_2025 * self.x_bess_mw)
            cost_om_bess_2025 += cost_om_bess

        else:
            print("missing bus-bars in the grid for BESS")

        # print("cost_om_bess_2025 =", cost_om_bess_2025)
        # print("cost_maint_pv_2025 =", cost_maint_pv_2025)
        cost_om_var_loc_element_2025 += cost_maint_pv_2025 + cost_om_bess_2025
        # print("cost_om_var_loc_element_2025 =", cost_om_bess_2025)
        return cost_om_var_loc_element_2025   # calculated for yearly operation of PV

    def opex_e_net_2025(self):      # 24 hours cost calculation --> how to add July here?
        # ============================================ January =======================================================
        cost_opex_2025_jan = 0

        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_2025 = 0

        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh_2025 = self.ext_e_mwh_jan[i]
                cost_imp_e_2025 += imp_e_mwh_2025 * e_price__import_eur_mwh_2025
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_2025 += imp_e_mwh_2025 * e_price__import_eur_mwh_2025

        # ------------------ Curt cost ------------------
        cost_curt_e_2025 = 0

        for i in range(len(self.demand_e_mwh_jan)):
            # print(i)
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]
            # print(e_curt_mwh)
            # print(self.sgen_mwh[i])
            # print(self.demand_e_mwh[i])
            # print(self.bess_mwh[i])
            # print(self.net.trafo['sn_mva'].sum()*0.8)
            # print()

            if e_curt_mwh > 0:
                cost_curt_e_2025 += e_curt_mwh * e_price_curt_eur_mwh_2025
                # print(cost_curt_e_2025)
                # print()
            else:
                cost_curt_e_2025 += 0

        # ------------------ Export cost ------------------
        cost_exp_e_2025 = 0

        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh_2025 = self.ext_e_mwh_jan[i]
                cost_exp_e_2025 += exp_e_mwh_2025 * e_price_export_eur_mwh_2025 * -1  # Because export is -ve
            else:
                exp_e_mwh_2025 = 0
                cost_exp_e_2025 += exp_e_mwh_2025 * e_price_export_eur_mwh_2025 * -1  # Because export is -ve

        # print()
        # print("opex_enet_imp_e_2025_jan =", cost_imp_e_2025)
        # print("opex_enet_curt_e_2025_jan =", cost_curt_e_2025)
        # print("opex_enet_exp_e_2025_jan =", cost_exp_e_2025)

        cost_opex_2025_jan += cost_imp_e_2025 + cost_curt_e_2025 - cost_exp_e_2025
        # print("opex_enet_2025_jan =", cost_opex_2025_jan)
        # print()
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ============================================ July =======================================================
        opex_enet_2025_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_2025_jul = 0

        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_2025_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_2025_jul += imp_e_mwh_2025_jul * e_price__import_eur_mwh_2025
                # print("cost_imp_e_2025_jul =", cost_imp_e_2025_jul)
            else:
                imp_e_mwh_2025_jul = 0
                cost_imp_e_2025_jul += imp_e_mwh_2025_jul * e_price__import_eur_mwh_2025
        # print("cost_imp_e_2025_jul =", cost_imp_e_2025_jul)

        # -------------------- Curt cost ------------------
        cost_curt_e_2025_jul = 0

        for i in range(len(self.demand_e_mwh_jul)):
            # print(i)
            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]
            # print(e_curt_mwh_jul)
            # print(self.sgen_mwh[i])
            # print(self.demand_e_mwh[i])
            # print(self.bess_mwh[i])
            # print(self.net.trafo['sn_mva'].sum()*0.8)
            # print()

            if e_curt_mwh_jul > 0:
                cost_curt_e_2025_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
                # print(cost_curt_e_2025)
                # print()
            else:
                cost_curt_e_2025_jul += 0
        # print("cost_curt_e_2025_jul =", cost_curt_e_2025_jul)

        # ------------------ Export cost ------------------
        cost_exp_e_2025_jul = 0

        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_2025_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_2025_jul += exp_e_mwh_2025_jul * e_price_export_eur_mwh_2025 * -1  # Because export is -ve
            else:
                exp_e_mwh_2025_jul = 0
                cost_exp_e_2025_jul += exp_e_mwh_2025_jul * e_price_export_eur_mwh_2025 * -1  # Because export is -ve
            # print("cost_exp_loop =", cost_exp_e_2025_jul)
        # print("cost_exp_e_2025_jul =", cost_exp_e_2025_jul)

        # print()
        # print("opex_enet_imp_e_2025_jul =", cost_imp_e_2025_jul)
        # print("opex_enet_curt_e_2025_jul =", cost_curt_e_2025_jul)
        # print("opex_enet_exp_e_2025_jul =", cost_exp_e_2025_jul)

        opex_enet_2025_jul += cost_imp_e_2025_jul + cost_curt_e_2025_jul - cost_exp_e_2025_jul
        # print('opex_enet_2025_jul =', opex_enet_2025_jul)
        # print()

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_2025_annum = (cost_opex_2025_jan + opex_enet_2025_jul)/2*365

        return opex_enet_tot_2025_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2026 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2026(self):  # Yearly cost calculation
        cost_om_var_loc_element_2025 = 0

        # ---------------------------- PV OPEX COST 2026 -------------------------------
        # Note: Change cost of land, fom ground lease cost, rooftop lease is fixed, because no data found,
        cost_land_industry = cost_land_industry_2025 * 1.03     # Year 2026
        cost_fom_pv_ground = 9600           # Year 2026

        # ---------- PV on roof-top ----------
        cost_fom_pv_roof = 6800
        # price_rooftop_leasing_yearly is kept fixed, because no data found

        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground*pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:   # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:      # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:      # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:      # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # ---------------------------- BESS OPEX COST 2026 -------------------------------
        # Note: Changed values for the year:
        cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.03
        cost_land_residential = cost_land_residential_2025 * 1.03
        cost_fom_bess = 4511.1285

        cost_om_bess = 0

        if self.x_bess_bus == 1:        # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:      # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:     # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:     # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:     # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:     # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:     # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                           (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element_2025 += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element_2025   # calculated for yearly operation of PV

    def opex_fixed_loc_elem_2026(self):     # Yearly cost calculation

        # Note: Parameters to change:
        cost_land_lease_wt = cost_land_lease_2025 * 1.03    # for WT Agri land - Each year the leasing cost increases 3%
        cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.03         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.03   # For CHP

        cost_fom_wt = 37600
        cost_fom_p2g = 77040.0
        cost_fom_chp = 25500.0
        cost_fom_hp = 30000
        cost_fom_gen = 18960
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2026
        cost_ch4_import = 79

        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                                (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_       # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                              (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_        # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2026(self):      # 24 hours cost calculation --> how to add July here?
        # ============================================ January =======================================================
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2026
        e_price_export_eur_mwh = e_price_export_eur_mwh_2026
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2026

        opex_enet_jan = 0

        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0

        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0

        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0

        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ============================================ July =======================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0

        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0

        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0

        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul)/2*365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2027 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2027(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2027 -------------------------------
        # NOTE: change cost_land_industry_2025, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.06  # From Year 2025 to 2027
        cost_fom_pv_ground = 9200  # Year 2027

        # ---------- PV on roof-top ----------
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 6600

        # NOTE: No change is needed below -->
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2027 -----------------------------------------
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.06     # from 2025 to 2027
        cost_land_residential = cost_land_residential_2025 * 1.06   # from 2025 to 2027
        cost_fom_bess = 4425

        # NOTE: No change is needed below -->
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2027(self):     # Yearly cost calculation

        # Note: Parameters to change: --> Change from 2025 - 2027 (Each year 3% increase)
        cost_land_lease_wt = cost_land_lease_2025 * 1.06    # WT Agri land - Each year the leasing cost increases 3%
        cost_land_industry = cost_land_industry_2025 * 1.06         # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.06         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.06   # For CHP

        cost_fom_wt = 37200
        cost_fom_p2g = 61280.0
        cost_fom_chp = 25350.0
        cost_fom_hp = 30000
        cost_fom_gen = 18870
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2027
        cost_ch4_import = 81

        # NOTE: No change is needed below -->
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                                (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_       # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                              (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_        # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2027(self):      # 24 hours cost calculation
        # ============================================ January =======================================================
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2027
        e_price_export_eur_mwh = e_price_export_eur_mwh_2027
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2027  # Fixed for my research

        # NOTE: No change is needed below -->
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ============================================ July =======================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul)/2*365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2028 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2028(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2027 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.09  # From Year 2025 to 2028
        cost_fom_pv_ground = 8800  # Year 2028

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 6400

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2028 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.09     # from 2025 to 2028
        cost_land_residential = cost_land_residential_2025 * 1.09   # from 2025 to 2028
        cost_fom_bess = 4340

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2028(self):     # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2027 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.09    # WT Agri land
        cost_land_industry = cost_land_industry_2025 * 1.09         # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.09         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.09   # For CHP

        cost_fom_wt = 36800
        cost_fom_p2g = 45520
        cost_fom_chp = 25200
        cost_fom_hp = 30000
        cost_fom_gen = 18780
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2028
        cost_ch4_import = 83

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                                (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_       # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                              (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_        # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2028(self):      # 24 hours cost calculation
        # ========================================== January 2028 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2028
        e_price_export_eur_mwh = e_price_export_eur_mwh_2028
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2028  # Fixed for my research

        # ------- NOTE: No change is needed below: ------- >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2028 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul)/2*365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2029 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2029(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2029 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.12  # From Year 2025 to 2029
        cost_fom_pv_ground = 8400  # Year 2029

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 6200

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2029 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.12  # from 2025 to 2029
        cost_land_residential = cost_land_residential_2025 * 1.12  # from 2025 to 2029
        cost_fom_bess = 4257.54

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2029(self):     # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2029 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.12            # WT Agri. land
        cost_land_industry = cost_land_industry_2025 * 1.12         # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.12         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.12   # For CHP

        cost_fom_wt = 36600
        cost_fom_p2g = 29760
        cost_fom_chp = 25050
        cost_fom_hp = 30000
        cost_fom_gen = 18690
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2029
        cost_ch4_import = 84

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                                (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_       # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                              (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_        # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2029(self):      # 24 hours cost calculation
        # ========================================== January 2029 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2029
        e_price_export_eur_mwh = e_price_export_eur_mwh_2029
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2029  # Fixed for my research

        # ------- NOTE: No change is needed below: ------------ >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2029 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul)/2*365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2030 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2030(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2030 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.15  # From Year 2025 to 2029
        cost_fom_pv_ground = 8000  # Year 2030

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 6000

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2030 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.15  # from 2025 to 2029
        cost_land_residential = cost_land_residential_2025 * 1.15  # from 2025 to 2029
        cost_fom_bess = 4176.117

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2030(self):     # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2030 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.15            # WT Agri. land
        cost_land_industry = cost_land_industry_2025 * 1.15         # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.15         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.15   # For CHP

        cost_fom_wt = 36000
        cost_fom_p2g = 14000
        cost_fom_chp = 24900
        cost_fom_hp = 30000
        cost_fom_gen = 18600
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2030
        cost_ch4_import = 86

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                                (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_       # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                              (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_        # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2030(self):      # 24 hours cost calculation
        # ========================================== January 2030 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2030
        e_price_export_eur_mwh = e_price_export_eur_mwh_2030
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2030  # Fixed for my research

        # ------- NOTE: No change is needed below: ------------ >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2029 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                             self.net.trafo['sn_mva'].sum()*0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul)/2*365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2031 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2031(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2031 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.18  # From Year 2025 to 2031
        cost_fom_pv_ground = 7900  # Year 2031

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 5900

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2031 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.18  # from 2025 to 2031
        cost_land_residential = cost_land_residential_2025 * 1.18  # from 2025 to 2031
        cost_fom_bess = 4096.7708

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2031(self):  # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2031 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.18  # WT Agri. land
        cost_land_industry = cost_land_industry_2025 * 1.18  # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.18  # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.18  # For CHP

        cost_fom_wt = 35880
        cost_fom_p2g = 13862.0
        cost_fom_chp = 24840.0
        cost_fom_hp = 30000
        cost_fom_gen = 18570
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2031
        cost_ch4_import = 87

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (
                    cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                             (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_  # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                            (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_  # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2031(self):  # 24 hours cost calculation
        # ========================================== January 2030 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2031
        e_price_export_eur_mwh = e_price_export_eur_mwh_2031
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2031  # Fixed for my research

        # ------- NOTE: No change is needed below: ------------ >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                                 self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2029 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                                     self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul) / 2 * 365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2032 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2032(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2032 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.21  # From Year 2025 to 2032
        cost_fom_pv_ground = 7800  # Year 2032

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 5800

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2032 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.21  # from 2025 to 2032
        cost_land_residential = cost_land_residential_2025 * 1.21  # from 2025 to 2032
        cost_fom_bess = 4017.4246

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2032(self):  # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2032 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.21            # WT Agri. land
        cost_land_industry = cost_land_industry_2025 * 1.21         # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.21         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.21   # For CHP

        cost_fom_wt = 35760
        cost_fom_p2g = 13724
        cost_fom_chp = 24810.0
        cost_fom_hp = 30000
        cost_fom_gen = 18540
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2032
        cost_ch4_import = 89

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (
                cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                             (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_  # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                            (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_  # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2032(self):  # 24 hours cost calculation
        # ========================================== January 2032 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2032
        e_price_export_eur_mwh = e_price_export_eur_mwh_2032
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2032  # Fixed for my research

        # ------- NOTE: No change is needed below: ------------ >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                                 self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2032 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                                     self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul) / 2 * 365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2033 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2033(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2033 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025 - 3% each year, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.24  # From Year 2025 to 2032
        cost_fom_pv_ground = 7700  # Year 2033

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 5700

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2033 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.24  # from 2025 to 2034
        cost_land_residential = cost_land_residential_2025 * 1.24  # from 2025 to 2034
        cost_fom_bess = 3941.0935

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2033(self):  # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2033 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.24            # WT Agri. land
        cost_land_industry = cost_land_industry_2025 * 1.24         # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.24         # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.24   # For CHP

        cost_fom_wt = 35640
        cost_fom_p2g = 13586.0
        cost_fom_chp = 24750.0
        cost_fom_hp = 30000
        cost_fom_gen = 18510
        cost_fom_th_storage = 100000

        cost_h2_import = cost_h2_import_2033  # EUR/MWh # Only added in 2033:
        cost_ch4_import = 90

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (
                cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += 0

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                             (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_  # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                            (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_  # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2033(self):  # 24 hours cost calculation
        # ========================================== January 2033 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2033
        e_price_export_eur_mwh = e_price_export_eur_mwh_2033
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2033  # Fixed for my research

        # ------- NOTE: No change is needed below: ------------ >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                                 self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2033 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                                     self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul) / 2 * 365

        return opex_enet_tot_annum

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPEX 2034 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def opex_var_loc_elem_2034(self):  # Yearly cost calculation
        cost_om_var_loc_element = 0

        # ---------------------------- PV OPEX COST 2034 -------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: change cost_land_industry_2025 - 3% each year, cost_fom_pv_ground
        cost_land_industry = cost_land_industry_2025 * 1.27  # From Year 2025 to 2034
        cost_fom_pv_ground = 7600  # Year 2034

        # ---------- PV on roof-top ----------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # NOTE: Change cost_fom_pv_roof
        # NOTE: price_rooftop_leasing_yearly is kept fixed, because no data found
        cost_fom_pv_roof = 5600

        # NOTE: No change is needed below: -------------- >
        cost_om_pv = 0
        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):

            if v_x_pv_bus == 1:  # Che Ind area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 2:  # PV in Industrial area - bus 2
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 12:  # PV in Industrial area - bus 12
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 13:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 14:  # PV in Industrial area - bus 13
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * cost_land_industry * land_area_pv) + \
                                (cost_fom_pv_ground * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 4:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size

                cost_maint_pv = (pv_size * price_rooftop_leasing_yearly * land_area_pv) + \
                                (cost_fom_pv_roof * pv_size)
                cost_om_pv += cost_maint_pv

            else:
                print("missing bus bars in the grid for PV")

        # -------------------------------------- BESS OPEX COST 2034 -----------------------------------------
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Changed values for the year:
        # cost_land_industry = cost_land_industry_2025 * 1.03
        cost_land_business = cost_land_business_2025 * 1.27  # from 2025 to 2034
        cost_land_residential = cost_land_residential_2025 * 1.27  # from 2025 to 2034
        cost_fom_bess = 3866.2127

        # NOTE: No change is needed below: ---------- >
        cost_om_bess = 0
        if self.x_bess_bus == 1:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 2:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 12:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 13:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 14:  # Ind area
            cost_om_bess_ = (self.x_bess_mw * cost_land_industry * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 3:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 4:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 5:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 7:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 8:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 9:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 10:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 11:  # Comm area
            cost_om_bess_ = (self.x_bess_mw * cost_land_business * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        elif self.x_bess_bus == 6:  # Residential area
            cost_om_bess_ = (self.x_bess_mw * cost_land_residential * land_area_bess) + \
                            (cost_fom_bess * self.x_bess_mw)
            cost_om_bess += cost_om_bess_

        else:
            print("missing bus-bars in the grid for BESS")

        cost_om_var_loc_element += cost_om_pv + cost_om_bess

        return cost_om_var_loc_element  # calculated for yearly operation of PV + BESS

    def opex_fixed_loc_elem_2034(self):  # Yearly cost calculation

        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # <<<<< ----------Note: Parameters to change: --> Change from 2025 - 2034 (Each year 3% increase)--------->>>>>
        # ----------- Each year the leasing cost increases 3% ----------
        cost_land_lease_wt = cost_land_lease_2025 * 1.27  # WT Agri. land
        cost_land_industry = cost_land_industry_2025 * 1.27  # For Gas Gen
        cost_land_business = cost_land_business_2025 * 1.27  # For P2G
        cost_land_residential = cost_land_residential_2025 * 1.27  # For CHP

        cost_fom_wt = 35520
        cost_fom_p2g = 13448.0
        cost_fom_chp = 24720.0
        cost_fom_hp = 30000
        cost_fom_gen = 18480
        cost_fom_th_storage = 10000

        cost_h2_import = cost_h2_import_2034   # EUR/MWh
        cost_ch4_import = 91

        # ----- NOTE: No change is needed below: ------- >
        cost_om_fixed_loc_element = 0
        # ---------------------------- WT OM ----------------------------
        cost_wt_om_ = (self.x_wt_mw * cost_land_lease_wt * land_area_wt) + (cost_fom_wt * self.x_wt_mw)
        # considering the agricultural land used in WT installations are cheaper than the land lease cost for PV
        cost_om_fixed_loc_element += cost_wt_om_

        # ---------------------------- P2G OM ----------------------------
        cost_p2g_om_ = (self.x_p2g_size_mw * cost_land_business * land_area_p2g) + (
                cost_fom_p2g * self.x_p2g_size_mw)
        cost_om_fixed_loc_element += cost_p2g_om_

        # ---------------------------- H2 import OM ----------------------------
        # ************** H2 import cost Jan **************
        cost_h2_import_jan = cost_h2_import * self.h2_import_jan
        # ************** H2 import cost Jul **************
        cost_h2_import_jul = cost_h2_import * self.h2_import_jul

        cost_om_fixed_loc_element += (cost_h2_import_jan + cost_h2_import_jul) / 2 * 365

        # ---------------------------- CHP OM ----------------------------
        cost_chp_om_ = (self.x_chp_mw * cost_land_residential * land_area_chp) + (cost_fom_chp * self.x_chp_mw)
        # ************** CHP - Fuel cost Jan **************
        cost_chp_ch4_import_jan = cost_ch4_import * self.chp_ch4_import_jan
        # ************** CHP - Fuel cost Jul **************
        cost_chp_ch4_import_jul = cost_ch4_import * self.chp_ch4_import_jul

        cost_om_fixed_loc_element += cost_chp_om_ + cost_chp_ch4_import_jan + cost_chp_ch4_import_jul

        # ---------------------------- Heat Pump OM ----------------------------
        cost_hp_om_ = (self.x_hp_size * cost_land_residential * land_area_hp) + (cost_fom_hp * self.x_hp_size)
        cost_om_fixed_loc_element += cost_hp_om_

        # ---------------------------- Gas Gen OM bus = 12 ----------------------------
        cost_gen_bus12_om_ = (self.x_gen_bus_12_mw * cost_land_industry * land_area_gen) + \
                             (cost_fom_gen * self.x_gen_bus_12_mw)
        cost_om_fixed_loc_element += cost_gen_bus12_om_  # used the cost of Ind. location
        # ---------------------------- Gas Gen OM bus = 1 ----------------------------
        cost_gen_bus1_om_ = (self.x_gen_bus_1_mw * cost_land_industry * land_area_gen) + \
                            (cost_fom_gen * self.x_gen_bus_1_mw)
        cost_om_fixed_loc_element += cost_gen_bus1_om_  # used the cost of Ind. location

        # ---------------------------- Th Storage OM ----------------------------
        cost_th_storage_om_ = (self.x_storage_th_size * cost_land_residential * land_area_th_storage) + \
                              (cost_fom_th_storage * self.x_storage_th_size)
        cost_om_fixed_loc_element += cost_th_storage_om_

        # ---------------------------- H2 Storage OM ----------------------------
        # blue_h2_mwh_import cost
        # h2_storage cost

        return cost_om_fixed_loc_element

    def opex_e_net_2034(self):  # 24 hours cost calculation
        # ========================================== January 2033 =====================================================
        # <<<<<<<<< ---------------------- CHANGE ---------------------- >>>>>>>>>>>>>
        # Note: Parameters to change:
        e_price_import_eur_mwh = e_price_import_eur_mwh_2034
        e_price_export_eur_mwh = e_price_export_eur_mwh_2034
        e_price_curt_eur_mwh = e_price_curt_eur_mwh_2034  # Fixed for my research

        # ------- NOTE: No change is needed below: ------------ >
        opex_enet_jan = 0
        # ------------------ Import cost ------------------
        # Power import
        cost_imp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] > 0:
                imp_e_mwh = self.ext_e_mwh_jan[i]
                cost_imp_e_ += imp_e_mwh * e_price_import_eur_mwh
                # print("cost_imp_e_2025_jan =", cost_imp_e_2025)
            else:
                imp_e_mwh_2025 = 0
                cost_imp_e_ += imp_e_mwh_2025 * e_price_import_eur_mwh

        # ------------------ Curt cost ------------------
        cost_curt_e_ = 0
        for i in range(len(self.demand_e_mwh_jan)):
            e_curt_mwh = self.sgen_mwh_jan[i] - (self.demand_e_mwh_jan[i] + self.bess_mwh_jan[i] +
                                                 self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh > 0:
                cost_curt_e_ += e_curt_mwh * e_price_curt_eur_mwh
            else:
                cost_curt_e_ += 0

        # ------------------ Export cost ------------------
        cost_exp_e_ = 0
        for i in range(len(self.ext_e_mwh_jan)):
            if self.ext_e_mwh_jan[i] < 0:
                exp_e_mwh = self.ext_e_mwh_jan[i]
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh = 0
                cost_exp_e_ += exp_e_mwh * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jan += cost_imp_e_ + cost_curt_e_ - cost_exp_e_
        # cost_opex_2025_jan = cost_opex_2025_jan * ((1-(1+0.08)**-2)/0.08)  # annuity cost - not using anymore

        # ========================================== July 2033 =====================================================
        opex_enet_jul = 0

        # ------------------ Import cost ------------------
        cost_imp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] > 0:
                imp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh
            else:
                imp_e_mwh_jul = 0
                cost_imp_e_jul += imp_e_mwh_jul * e_price_import_eur_mwh

        # -------------------- Curt cost ------------------
        cost_curt_e_jul = 0
        for i in range(len(self.demand_e_mwh_jul)):

            e_curt_mwh_jul = self.sgen_mwh_jul[i] - (self.demand_e_mwh_jul[i] + self.bess_mwh_jul[i] +
                                                     self.net.trafo['sn_mva'].sum() * 0.8)  # [mva*pf = mw/h = mwh]

            if e_curt_mwh_jul > 0:
                cost_curt_e_jul += e_curt_mwh_jul * e_price_curt_eur_mwh_2025
            else:
                cost_curt_e_jul += 0

        # ------------------ Export cost ------------------
        cost_exp_e_jul = 0
        for i in range(len(self.ext_e_mwh_jul)):
            if self.ext_e_mwh_jul[i] < 0:
                exp_e_mwh_jul = self.ext_e_mwh_jul[i]
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve
            else:
                exp_e_mwh_jul = 0
                cost_exp_e_jul += exp_e_mwh_jul * e_price_export_eur_mwh * -1  # Because export is -ve

        opex_enet_jul += cost_imp_e_jul + cost_curt_e_jul - cost_exp_e_jul

        # Annualised values:
        # cost_imp_e_2025_anum = (cost_imp_e_2025/2)*365        # annualised
        # cost_exp_e_2025_anum = (cost_exp_e_2025/2)*365        # annualised
        # cost_curt_e_2025_anum = (cost_curt_e_2025/2)*365      # annualised

        opex_enet_tot_annum = (opex_enet_jan + opex_enet_jul) / 2 * 365

        return opex_enet_tot_annum