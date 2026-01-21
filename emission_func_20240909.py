
ef_chp = 0.204          # tCO2/MWh_electricity
ef_e_net_2025 = 0.331   # tCO2/MWh_electricity
ef_gas_gen = 0.204      # tCO2/MWh_electricity


class emission_calc:
    def __init__(self, stage, year,
                 e_chp_jan, e_net_import_jan, e_gas_gen_jan,
                 e_chp_jul, e_net_import_jul, e_gas_gen_jul, **kwargs):
        self.stage = stage
        self.year = year
        # self.day = day

        self.e_chp_jan = e_chp_jan      # electricity is produced by CHP in Jan
        self.e_net_import_jan = e_net_import_jan
        self.e_gas_gen_jan = e_gas_gen_jan

        self.e_chp_jul = e_chp_jul  # electricity is produced by CHP in Jan
        self.e_net_import_jul = e_net_import_jul
        self.e_gas_gen_jul = e_gas_gen_jul

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2025 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ---------------------------- CHP CO2 emissions calc 2025 ----------------------------
    def emission_chp_2025(self):
        # ------------------- Jan -------------------
        emission_chp_jan_2025 = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul_2025 = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_2025 = emission_chp_jan_2025 + emission_chp_jul_2025

        return emission_chp_tot_2025*365/2     # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2025 ----------------------------
    def emission_enet_2025(self):
        # ------------------- Jan -------------------
        emission_net_jan_2025 = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:       # Imported energy is +ve
                emission_net_jan = row * ef_e_net_2025
                emission_net_jan_2025 += emission_net_jan
        # print('emission_net_jan_2025 =', emission_net_jan_2025)

        # ------------------- Jul -------------------
        emission_net_jul_2025 = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:       # Imported energy is +ve
                emission_net_jul = row * ef_e_net_2025
                emission_net_jul_2025 += emission_net_jul
        # print('emission_net_jul_2025 =', emission_net_jul_2025)

        emission_net_tot_2025 = emission_net_jan_2025 + emission_net_jul_2025

        return emission_net_tot_2025*365/2       # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2025 ----------------------------
    def emission_gas_gen_2025(self):
        # ------------------- Jan -------------------
        # print(self.e_gas_gen_jan)
        emission_gen_jan_2025 = self.e_gas_gen_jan * ef_gas_gen
        # print(emission_gen_jan_2025)
        # ------------------- Jul -------------------
        emission_gen_jul_2025 = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_2025 = emission_gen_jan_2025 + emission_gen_jul_2025

        return emission_gas_gen_tot_2025.sum()*365/2     # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2026 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ---------------------------- CHP CO2 emissions calc 2025 ----------------------------
    def emission_chp_2026(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2025 ----------------------------
    def emission_enet_2026(self):
        # Note parameters to change:
        ef_e_net = 0.3124   # 2026

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2025 ----------------------------
    def emission_gas_gen_2026(self):
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_2025 = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_2025.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2027 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ---------------------------- CHP CO2 emissions calc 2027 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2027(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2025 ----------------------------
    def emission_enet_2027(self):
        # Note: parameters to change:
        ef_e_net = 0.2938  # 2027

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2025 ----------------------------
    def emission_gas_gen_2027(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2028 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2028 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2028(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2028 ----------------------------
    def emission_enet_2028(self):
        # Note: parameters to change:
        ef_e_net = 0.2752  # Emission factor of eGrid in 2028

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2028 ----------------------------
    def emission_gas_gen_2028(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2029 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2029 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2029(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2028 ----------------------------
    def emission_enet_2029(self):
        # Note: <<<<<<<<<< ------------------ parameters to change: ------------------>>>>>>>>>>
        ef_e_net = 0.2566   # Emission factor of eGrid in 2029

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2028 ----------------------------
    def emission_gas_gen_2029(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2030 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2029 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2030(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2028 ----------------------------
    def emission_enet_2030(self):
        # Note: <<<<<<<<<< ------------------ parameters to change: ------------------>>>>>>>>>>
        ef_e_net = 0.238  # Emission factor of eGrid in 2030

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2028 ----------------------------
    def emission_gas_gen_2030(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2031 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2031 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2031(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2031 ----------------------------
    def emission_enet_2031(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.2206  # Emission factor of eGrid in 2030

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2028 ----------------------------
    def emission_gas_gen_2031(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2032 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2032 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2032(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2032 ----------------------------
    def emission_enet_2032(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.2032  # Emission factor of eGrid in 2030

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2032 ----------------------------
    def emission_gas_gen_2032(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2033 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2033 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2033(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2033 ----------------------------
    def emission_enet_2033(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.1858  # Emission factor of eGrid in 2033

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2033 ----------------------------
    def emission_gas_gen_2033(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2034 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2034 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2034(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2033 ----------------------------
    def emission_enet_2034(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.1684  # Emission factor of eGrid in 2034 [t/MWh]

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2034 ----------------------------
    def emission_gas_gen_2034(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2035 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2035 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2035(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2033 ----------------------------
    def emission_enet_2035(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.151  # Emission factor of eGrid in 2035 [t/MWh]

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2035 ----------------------------
    def emission_gas_gen_2035(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2036 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2036 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2036(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2033 ----------------------------
    def emission_enet_2036(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.1482  # Emission factor of eGrid in 2036 [t/MWh]

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2036 ----------------------------
    def emission_gas_gen_2036(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2037 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2037 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2037(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2037 ----------------------------
    def emission_enet_2037(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.1454  # Emission factor of eGrid in 2037 [t/MWh]

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2037 ----------------------------
    def emission_gas_gen_2037(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2038 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Only change the Emission factor of eGrid in each year
    # ---------------------------- CHP CO2 emissions calc 2038 ----------------------------
    # NOTE: Change nothing
    def emission_chp_2038(self):
        # ------------------- Jan -------------------
        emission_chp_jan = self.e_chp_jan * ef_chp
        # print('emission_chp_jan_2025 =', emission_chp_jan_2025)

        # ------------------- Jul -------------------
        emission_chp_jul = self.e_chp_jul * ef_chp
        # print('emission_chp_jul_2025 =', emission_chp_jul_2025)

        emission_chp_tot_tonne = emission_chp_jan + emission_chp_jul

        return emission_chp_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- eNet CO2 emissions calc 2038 ----------------------------
    def emission_enet_2038(self):
        # Note: <<<<<<<<<< parameters to change: >>>>>>>>>>
        ef_e_net = 0.1426    # Emission factor of eGrid in 2038 [t/MWh]

        # ------------------- Jan -------------------
        emission_net_jan = 0
        for idx, row in enumerate(self.e_net_import_jan):
            if row > 0:  # Imported energy is +ve
                emission_net_jan_ = row * ef_e_net
                emission_net_jan += emission_net_jan_

        # ------------------- Jul -------------------
        emission_net_jul = 0
        for idx, row in enumerate(self.e_net_import_jul):
            if row > 0:  # Imported energy is +ve
                emission_net_jul_ = row * ef_e_net
                emission_net_jul += emission_net_jul_

        emission_net_tot_tonne = emission_net_jan + emission_net_jul

        return emission_net_tot_tonne * 365 / 2  # [tCO2] for the year

    # ---------------------------- Gas gas CO2 emissions calc 2038 ----------------------------
    def emission_gas_gen_2038(self):
        # NOTE: Change nothing
        # ------------------- Jan -------------------
        emission_gen_jan = self.e_gas_gen_jan * ef_gas_gen

        # ------------------- Jul -------------------
        emission_gen_jul = self.e_gas_gen_jul * ef_gas_gen

        emission_gas_gen_tot_tonne = emission_gen_jan + emission_gen_jul

        return emission_gas_gen_tot_tonne.sum() * 365 / 2  # [tCO2] for the year