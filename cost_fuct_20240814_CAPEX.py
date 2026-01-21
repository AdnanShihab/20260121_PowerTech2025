"""
Obj function

stage1 = 2025-2025
stage2 = 2026-2030
stage3 = 2031-2035
"""

# =========================================== Gas Gen Parameters ===========================================
# Considered already installed and invested

# =========================================== PV Parameters ===========================================
land_area_pv = 9290  # [m2 per 1 MW solar]
roof_top_area_pv = 6000  # [m2 per 1 MW solar]

cost_pv_installation_2025 = 797000     # EUR/MW --> including the land development cost
cost_pv_installation_2026 = cost_pv_installation_2025-(cost_pv_installation_2025*0.12)
cost_pv_installation_2027 = cost_pv_installation_2026-(cost_pv_installation_2026*0.12)
cost_pv_installation_2028 = cost_pv_installation_2027-(cost_pv_installation_2027*0.12)
cost_pv_installation_2029 = cost_pv_installation_2028-(cost_pv_installation_2028*0.12)
cost_pv_installation_2030 = cost_pv_installation_2029-(cost_pv_installation_2029*0.12)
cost_pv_installation_2031 = cost_pv_installation_2030-(cost_pv_installation_2030*0.12)
cost_pv_installation_2032 = cost_pv_installation_2031-(cost_pv_installation_2031*0.12)
cost_pv_installation_2033 = cost_pv_installation_2032-(cost_pv_installation_2032*0.12)
cost_pv_installation_2034 = cost_pv_installation_2033-(cost_pv_installation_2033*0.12)

cost_land_industry_2026 = 0.35      # [EUR/m2/year]
cost_land_industry_2027 = cost_land_industry_2026*1.78  # Source: Perplexity check the record pls

cost_pv_system_rooftop_business_installation_2025 = 1000000  # EUR/MW
cost_pv_system_rooftop_business_installation_2026 = cost_pv_system_rooftop_business_installation_2025 - \
                                           (cost_pv_system_rooftop_business_installation_2025*0.12)

cost_pv_system_rooftop_household_installation_2025 = 1650000  # EUR/MW;
cost_pv_system_rooftop_household_installation_2026 = cost_pv_system_rooftop_household_installation_2025 - \
                                           (cost_pv_system_rooftop_household_installation_2025*0.12)


# =========================================== WT Parameters ===========================================
cost_wt_capex_2025 = 950000
cost_wt_capex_2026 = 940000
cost_wt_capex_2027 = 930000
cost_wt_capex_2028 = 920000
cost_wt_capex_2029 = 910000
cost_wt_capex_2030 = 900000
cost_wt_capex_2031 = 897000
cost_wt_capex_2032 = 894000
cost_wt_capex_2033 = 890000
cost_wt_capex_2034 = 888000
cost_wt_capex_2035 = 885000
cost_wt_capex_2036 = 882000
cost_wt_capex_2037 = 879000
cost_wt_capex_2038 = 876000

# =========================================== CHP Parameters ===========================================
cost_chp_capex_2025 = 855000
cost_chp_capex_2026 = 850000
cost_chp_capex_2027 = 845000
cost_chp_capex_2028 = 840000
cost_chp_capex_2029 = 835000
cost_chp_capex_2030 = 830000
cost_chp_capex_2031 = 828000
cost_chp_capex_2032 = 827000
cost_chp_capex_2033 = 825000
cost_chp_capex_2034 = 824000
cost_chp_capex_2035 = 822500
cost_chp_capex_2036 = 821000
cost_chp_capex_2037 = 819500
cost_chp_capex_2038 = 818000


# =========================================== HP Parameters ===========================================
cost_hp_capex_2025 = 1250000
cost_hp_capex_2026 = 1250000
cost_hp_capex_2027 = 1250000
cost_hp_capex_2028 = 1250000
cost_hp_capex_2029 = 1250000
cost_hp_capex_2030 = 1250000
cost_hp_capex_2031 = 1125000    # changed
cost_hp_capex_2032 = 1125000
cost_hp_capex_2033 = 1125000
cost_hp_capex_2034 = 1125000
cost_hp_capex_2035 = 1125000
cost_hp_capex_2036 = 1012500    # changed
cost_hp_capex_2037 = 1012500
cost_hp_capex_2038 = 1012500


# =========================================== P2G Parameters ===========================================
cost_p2g_capex_2025 = 2320000
cost_p2g_capex_2026 = 1926000
cost_p2g_capex_2027 = 1532000
cost_p2g_capex_2028 = 1138000
cost_p2g_capex_2029 = 744000
cost_p2g_capex_2030 = 350000
cost_p2g_capex_2031 = 346550
cost_p2g_capex_2032 = 343100
cost_p2g_capex_2033 = 339650
cost_p2g_capex_2034 = 336200
cost_p2g_capex_2035 = 332750
cost_p2g_capex_2036 = 329300
cost_p2g_capex_2037 = 325850
cost_p2g_capex_2038 = 322400


# =========================================== BESS Parameters ===========================================
cost_bess_capex_2025 = 221629
cost_bess_capex_2026 = 217418
cost_bess_capex_2027 = 213287
cost_bess_capex_2028 = 209234
cost_bess_capex_2029 = 205258
cost_bess_capex_2030 = 201358
cost_bess_capex_2031 = 197532
cost_bess_capex_2032 = 193779
cost_bess_capex_2033 = 190097
cost_bess_capex_2034 = 186485
cost_bess_capex_2035 = 182942
cost_bess_capex_2036 = 179466
cost_bess_capex_2037 = 176056
cost_bess_capex_2038 = 172711


# =========================================== TH Storage Parameters ===========================================
cost_storage_th_capex_2025 = 155.28
cost_storage_th_capex_2026 = 155.28
cost_storage_th_capex_2027 = 155.28
cost_storage_th_capex_2028 = 155.28
cost_storage_th_capex_2029 = 155.28
cost_storage_th_capex_2030 = 155.28
cost_storage_th_capex_2031 = 155.28
cost_storage_th_capex_2032 = 155.28
cost_storage_th_capex_2033 = 155.28
cost_storage_th_capex_2034 = 155.28
cost_storage_th_capex_2035 = 155.28
cost_storage_th_capex_2036 = 155.28
cost_storage_th_capex_2037 = 155.28
cost_storage_th_capex_2038 = 155.28


# =========================================== H2 Storage Parameters ===========================================
cost_storage_h2_capex_2025 = 0      # need to find
cost_storage_h2_capex_2026 = 0      # need to find
cost_storage_h2_capex_2027 = 0
cost_storage_h2_capex_2028 = 0
cost_storage_h2_capex_2029 = 0
cost_storage_h2_capex_2030 = 0
cost_storage_h2_capex_2031 = 0
cost_storage_h2_capex_2032 = 0
cost_storage_h2_capex_2033 = 0
cost_storage_h2_capex_2034 = 0
cost_storage_h2_capex_2035 = 0
cost_storage_h2_capex_2036 = 0
cost_storage_h2_capex_2037 = 0
cost_storage_h2_capex_2038 = 0


class PRICE:
    def __init__(self, stage, year, x_pv_bus, x_pv_size, x_wt_bus, x_wt_mw,
                 x_chp_bus, x_chp_mw, x_hp_bus, x_hp_size, x_storage_th_size, x_p2g_size_mw,
                 x_storage_h2_mwh, x_bess_bus, x_bess_mw, **kwargs):
        self.stage = stage
        self.year = year
        # self.day = day
        # self.net = net
        # self.x = x
        self.x_pv_bus = x_pv_bus
        self.x_pv_size = x_pv_size
        self.x_wt_bus = x_wt_bus
        self.x_wt_mw = x_wt_mw
        self.x_chp_bus = x_chp_bus
        self.x_chp_mw = x_chp_mw
        self.x_hp_bus = x_hp_bus
        self.x_hp_size = x_hp_size
        self.x_storage_th_size = x_storage_th_size
        self.x_p2g_size_mw = x_p2g_size_mw
        self.x_storage_h2_mwh = x_storage_h2_mwh
        self.x_bess_bus = x_bess_bus
        self.x_bess_mw = x_bess_mw

        # self.demand_e_mwh = demand_e_mwh
        # self.sgen_mwh = sgen_mwh
        # self.bess_mwh = bess_mwh
        # self.gas_gen_mwh = gas_gen_mwh
        # self.ext_e_mwh = ext_e_mwh

    # ---------------------------- PV CAPEX calc 2025 ----------------------------
    def price_capex_pv_2025(self):

        total_price_investment_pv_2025 = 0

        for v_x_pv_bus, v_x_pv_size in zip(self.x_pv_bus, self.x_pv_size):
            # print(v_x_pv_bus)
            # print(v_x_pv_size)
            if v_x_pv_bus == 1:  # Che Ind area
                # print("PV in Industrial area - bus 1")
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 2:
                # print("PV in Industrial area - bus 2")
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print("price =", inv_cost_pv)
            elif v_x_pv_bus == 12:
                # print("PV in Industrial area - bus 12")
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 13:
                # print("PV in Industrial area - bus 13")
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 14:
                # print("PV in Industrial area - bus 13")
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 3:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 4:   # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
            elif v_x_pv_bus == 5:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 7:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 8:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 9:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 10:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 11:  # commercial area
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_business_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print(inv_cost_pv)
            elif v_x_pv_bus == 6:  # Household bus
                pv_size = v_x_pv_size
                # print("pv_size =", pv_size)
                inv_cost_pv = (pv_size * cost_pv_system_rooftop_household_installation_2025)
                total_price_investment_pv_2025 += inv_cost_pv
                # print("price =", inv_cost_pv)
            else:
                print("missing bus bars in the grid")

        return total_price_investment_pv_2025

    # ---------------------------- WT CAPEX calc 2025 ----------------------------
    def price_capex_wt_2025(self):
        total_price_capex_wt_2025 = 0

        inv_cost_wt = (self.x_wt_mw * cost_wt_capex_2025)
        total_price_capex_wt_2025 += inv_cost_wt

        return total_price_capex_wt_2025

    # ---------------------------- CHP CAPEX calc 2025 ----------------------------
    def price_capex_chp_2025(self):
        total_price_capex_chp_2025 = 0

        inv_cost_chp = (self.x_chp_mw * cost_chp_capex_2025)
        total_price_capex_chp_2025 += inv_cost_chp

        return total_price_capex_chp_2025

    # ---------------------------- HP CAPEX calc 2025 ----------------------------
    def price_capex_hp_2025(self):
        total_price_capex_hp_2025 = 0

        inv_cost_hp = (self.x_hp_size * cost_hp_capex_2025)
        total_price_capex_hp_2025 += inv_cost_hp

        return total_price_capex_hp_2025

    # ---------------------------- Th_Storage CAPEX calc 2025 ----------------------------
    def price_capex_storage_th_2025(self):
        total_price_capex_storage_th_2025 = 0

        inv_cost_storage_th = (self.x_storage_th_size * cost_storage_th_capex_2025)
        total_price_capex_storage_th_2025 += inv_cost_storage_th

        return total_price_capex_storage_th_2025

    # ---------------------------- P2G CAPEX calc 2025 ----------------------------
    def price_capex_p2g_2025(self):
        total_price_capex_p2g_2025 = 0

        inv_cost_p2g = (self.x_p2g_size_mw * cost_p2g_capex_2025)
        total_price_capex_p2g_2025 += inv_cost_p2g

        return total_price_capex_p2g_2025

    # ---------------------------- H2 Storage CAPEX calc 2025 ----------------------------
    def price_capex_h2_storage_2025(self):
        total_price_capex_h2_storage_2025 = 0

        inv_cost_h2_storage = (self.x_storage_h2_mwh * cost_storage_h2_capex_2025)
        total_price_capex_h2_storage_2025 += inv_cost_h2_storage

        return total_price_capex_h2_storage_2025

    # ---------------------------- BESS CAPEX calc 2025 ----------------------------
    def price_capex_bess_2025(self):
        total_price_capex_bess_2025 = 0

        inv_cost_bess = (self.x_bess_mw * cost_bess_capex_2025)
        # print("inv BESS =", inv_cost_bess)
        total_price_capex_bess_2025 += inv_cost_bess
        # print("total_price_capex_bess_2025 =", total_price_capex_bess_2025)
        return total_price_capex_bess_2025

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2026 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def price_capex_2026(self):

        capex_tot_2026 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2026

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2026

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2026

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2026

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2026

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2026

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2026

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2026

        capex_tot_2026 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2026

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2027 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR,
    def price_capex_2027(self):
        capex_tot_2027 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2027

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2027

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2027

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2027

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2027

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2027

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2027

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2027

        capex_tot_2027 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2027

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2028 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2028(self):
        capex_tot_2028 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2028

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2028

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2028

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2028

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2028

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2028

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2028

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2028

        capex_tot_2028 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2028

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2029 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2029(self):
        capex_tot_2029 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2029

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2029

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2029

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2029

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2029

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2029

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2029

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2029

        capex_tot_2029 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2029

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2030 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2030(self):
        capex_tot_2030 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2030

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2030

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2030

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2030

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2030

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2030

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2030

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2030

        capex_tot_2030 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2030

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2031 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2031(self):
        capex_tot_2031 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2031

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2031

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2031

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2031

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2031

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2031

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2031

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2031

        capex_tot_2031 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2031

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2032 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2032(self):
        capex_tot_2032 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2032

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2032

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2032

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2032

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2032

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2032

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2032

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2032

        capex_tot_2032 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2032

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2033 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2033(self):
        # >>>>>>>>>>>>> CHANGE >>>>>>>>>>>>>>>
        capex_tot_2033 = 0

        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2033

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2033

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2033

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2033

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2033

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2033

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2033

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2033

        capex_tot_2033 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2033

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2034 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Note: cost_pv_installation_YEAR, cost_wt_capex_YEAR, cost_chp_capex_YEAR, cost_hp_capex_YEAR
    def price_capex_2034(self):
        # >>>>>>>>>>>>> CHANGE >>>>>>>>>>>>>>>
        capex_tot_2034 = 0

        # >>>>>>>>>>>>> CHANGE for all the element price >>>>>>>>>>>>>>>
        # -------------------------- PV --------------------------
        pv_tot_mw = self.x_pv_size.sum()
        inv_cost_pv = pv_tot_mw * cost_pv_installation_2034

        # ---------------------------- WT ----------------------------
        inv_cost_wt = self.x_wt_mw * cost_wt_capex_2034

        # ---------------------------- CHP ----------------------------
        inv_cost_chp = self.x_chp_mw * cost_chp_capex_2034

        # ---------------------------- HP  ----------------------------
        inv_cost_hp = self.x_hp_size * cost_hp_capex_2034

        # ---------------------------- Th_Storage  ----------------------------
        inv_cost_storage_th = self.x_storage_th_size * cost_storage_th_capex_2034

        # ---------------------------- P2G ----------------------------
        inv_cost_p2g = self.x_p2g_size_mw * cost_p2g_capex_2034

        # ---------------------------- H2 Storage ----------------------------
        inv_cost_h2_storage = self.x_storage_h2_mwh * cost_storage_h2_capex_2034

        # ---------------------------- BESS ----------------------------
        inv_cost_bess = self.x_bess_mw * cost_bess_capex_2034

        capex_tot_2034 += inv_cost_pv + inv_cost_wt + inv_cost_chp + inv_cost_hp + inv_cost_storage_th + \
                          inv_cost_p2g + inv_cost_h2_storage + inv_cost_bess

        return capex_tot_2034