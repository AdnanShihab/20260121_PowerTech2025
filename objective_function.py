"""
Obj function

stage1 = 2023-2025
stage2 = 2026-2030
stage3 = 2031-2035
"""

# from cost_inv_202405 import investment_cost
# from inv_cost_bess import investment_cost_bess
# from inv_cost_func_chp import investment_cost_chp
# from OM_cost_func_20230916 import om_cost
# from inv_cost_func_hp import investment_cost_hp
# from inv_cost_p2g import investment_cost_p2g

# cost_investment_pv_test = []
# cost_investment_pv_2023 = []
# cost_investment_pv_2024 = []
# cost_investment_pv_2025 = []
# cost_investment_pv_2026 = []
# cost_investment_pv_2027 = []
# cost_investment_pv_2028 = []
# cost_investment_pv_2029 = []
# cost_investment_pv_2030 = []
# cost_investment_pv_2031 = []

# Fixed parameters
cost_pv_installation = 100000  # [EUR] per 1 MW PV farm installation Source: MANGO
# cost_pv_installation_2023 = 110000     # EUR/MW
# cost_pv_installation_2024 = 108000     # EUR/kW
# cost_pv_installation_2025 = 106000     # EUR/kW
# cost_pv_installation_2026 = 104000     # EUR/kW
cost_pv_installation_2023 = 110000     # EUR/MW Source Chat GPT
cost_pv_installation_2024 = 100000     # EUR/kW
cost_pv_installation_2025 = 95000     # EUR/kW
cost_pv_installation_2026 = 90000     # EUR/kW
cost_pv_installation_2027 = 102000     # EUR/kW
cost_pv_installation_2028 = 100000     # EUR/kW
cost_pv_installation_2029 = 97000     # EUR/kW
cost_pv_installation_2030 = 95000     # EUR/kW
cost_pv_installation_2031 = 94000     # EUR/kW

cost_wind_installation = 1000000  # [EUR] per 1 MW PV farm installation Source: MANGO
cost_wind_installation_2023 = 100000     # EUR/MW Source Chat GPT
cost_wind_installation_2024 = 100000
cost_wind_installation_2025 = 95000
cost_wind_installation_2026 = 90000

cost_land_industry_2023 = 44  # [EUR/m2] # Source: Onenote PSCC + Excel file on Dropbox/PSC2024
cost_land_industry_2024 = 44*1.05
cost_land_industry_2025 = (44*1.05)*1.05
cost_land_industry_2026 = ((44*1.05)*1.05)*1.05
cost_land_industry_2027 = ((44*1.05)*1.05)*1.05
cost_land_industry_2028 = (((44*1.05)*1.05)*1.05)*1.05
cost_land_industry_2029 = ((((44*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_industry_2030 = (((((44*1.05)*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_industry_2031 = ((((((44*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05

cost_land_business_2023 = 45
cost_land_business_2024 = 45*1.05
cost_land_business_2025 = (45*1.05)*1.05
cost_land_business_2026 = ((45*1.05)*1.05)*1.05
cost_land_business_2027 = (((45*1.05)*1.05)*1.05)*1.05
cost_land_business_2028 = ((((45*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_business_2029 = (((((45*1.05)*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_business_2030 = ((((((45*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_business_2031 = (((((((45*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05

cost_land_residential_2023 = 214
cost_land_residential_2024 = 214*1.05
cost_land_residential_2025 = (214*1.05)*1.05
cost_land_residential_2026 = ((214*1.05)*1.05)*1.05

cost_land_residential_business_2023 = 182
cost_land_residential_business_2024 = 182*1.05
cost_land_residential_business_2025 = (182*1.05)*1.05
cost_land_residential_business_2026 = ((182*1.05)*1.05)*1.05
cost_land_residential_business_2027 = (((182*1.05)*1.05)*1.05)*1.05
cost_land_residential_business_2028 = ((((182*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_residential_business_2029 = (((((182*1.05)*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_residential_business_2030 = ((((((182*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05
cost_land_residential_business_2031 = (((((((182*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05)*1.05

land_area_pv = 9000  # [m2 per 1 MW solar] --> source: OneNote/PowerTech/Calculations

# Capital recovery factor (CRF) --> source Chat GPT
# r = 0.0326/12  # interest rate per year[%] is divided for each month
# q_PV = 20*12  # investment period [years] is 20 years and payment per year is 12 times
# crf_PV = (r * (1 + r) ** q_PV) / ((1 + r) ** q_PV - 1)  # This means that for each dollar of investment,
# approximately crf_PV EUR need to be repaid each month to recover the investment over the 20-year period
# at the given interest rate 3%.

# Capital recovery factor (CRF)--> source Chat GPT
r = 0.0326  # interest rate per year[%]
q_PV = 20  # investment period [years] is 20 years
crf_PV = (r * (1 + r) ** q_PV) / ((1 + r) ** q_PV - 1)  # This means you would need to set aside this amount each year
# to recover the total investment over the 20-year project lifetime at an annual interest rate of 3%.
# print(crf_PV)

FIT = 0    # EUR/MWh


class obj_func:
    def __init__(self, stage, year, net, x, p_demand, sgen, coal, p_ext, **kwargs):
        # self.idx = idx
        self.stage = stage
        self.year = year
        self.net = net
        self.x = x
        self.p_demand = p_demand
        self.sgen = sgen
        self.coal = coal
        self.p_ext = p_ext

    # ************************************************ PV ******************************************************
    # Backup
    # def cost_pv_test(self):
    #
    #     # total_price = 0
    #     #
    #     # # for idx_bus in self.net.bus.index:
    #     # for idx_bus, load_bus in enumerate(range(5, 7)):
    #     #
    #     #     # print(idx_bus)
    #     #
    #     #     pv_bus = self.x[0:2][idx_bus]
    #     #     pv_size = self.x[2:4][idx_bus]
    #     #
    #     #     # bus_bar_pv = [int(val) for val in self.x if val.is_integer()]  # Extract bus bar numbers
    #     #     # pv_capacities = [val for val in self.x if not val.is_integer()]  # Extract PV generator capacities
    #     #
    #     #     # print(pv_bus)
    #     #     # print(bus_bar_pv[idx_bus])
    #     #
    #     #     # cost_invest_ = investment_cost(self.net, bus_bar=self.x[0:2][idx_bus], pv_size=self.x[2:4][idx_bus])
    #     #     # cost_inv_pv_out = cost_invest_.cost_inv_pv_test()
    #     #
    #     #     if pv_bus == 5:  # Ind area
    #     #         cost_inv_pv = ((pv_size * 110000) +
    #     #                        (pv_size * 44 * 9000) * 1)
    #     #         # print('cost_inv_pv Ind area =', cost_inv_pv)
    #     #
    #     #     elif pv_bus == 6:  # Business area
    #     #         cost_inv_pv = ((pv_size * 110000) +
    #     #                        (pv_size * 45 * 9000) * 1)
    #     #         # print('cost_inv_pv Business area =', cost_inv_pv)
    #     #
    #     #     else:  # bus = 7
    #     #         cost_inv_pv = ((pv_size * 110000) +
    #     #                        (pv_size * 214 * 9000) * 1)
    #     #         # print('cost_inv_pv Res area =', cost_inv_pv)
    #     #
    #     #     total_price += cost_inv_pv
    #     #
    #     # return total_price

    # def cost_pv_test_2023(self):
    #
    #     total_price = 0
    #
    #     # for idx_bus in self.net.bus.index:
    #     for idx_bus, load_bus in enumerate(range(5, 7)):
    #
    #         pv_bus = self.x[0:2][idx_bus]
    #         pv_size = self.x[2:4][idx_bus]
    #
    #         # bus_bar_pv = [int(val) for val in self.x if val.is_integer()]  # Extract bus bar numbers
    #         # pv_capacities = [val for val in self.x if not val.is_integer()]  # Extract PV generator capacities
    #         # cost_invest_ = investment_cost(self.net, bus_bar=self.x[0:2][idx_bus], pv_size=self.x[2:4][idx_bus])
    #         # cost_inv_pv_out = cost_invest_.cost_inv_pv_test()
    #         # print("pv_bus", pv_bus)
    #
    #         if pv_bus == 5:  # Ind area
    #             cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
    #                            (pv_size * cost_land_industry_2023 * land_area_pv)) * crf_PV)
    #             # print('cost_inv_pv Ind area =', cost_inv_pv)
    #
    #         elif pv_bus == 6:  # Business area
    #             cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
    #                            (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
    #             # print('cost_inv_pv Business area =', cost_inv_pv)
    #
    #         else:  # bus = 7
    #             cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
    #                            (pv_size * cost_land_residential_2023 * land_area_pv)) * crf_PV)
    #             # print('cost_inv_pv Res area =', cost_inv_pv)
    #
    #         total_price += cost_inv_pv
    #
    #     return total_price

    def cost_sgen_invest_2023(self):

        total_price = 0

        # for idx_bus in self.net.bus.index:
        # for idx_bus, load_bus in enumerate(range(5, 7)):
        #
        #     # pv_bus = self.x[0:2][idx_bus]
        #     # pv_size = self.x[2:4][idx_bus]
        #     #
        #     # # bus_bar_pv = [int(val) for val in self.x if val.is_integer()]  # Extract bus bar numbers
        #     # # pv_capacities = [val for val in self.x if not val.is_integer()]  # Extract PV generator capacities
        #     # # cost_invest_ = investment_cost(self.net, bus_bar=self.x[0:2][idx_bus], pv_size=self.x[2:4][idx_bus])
        #     # # cost_inv_pv_out = cost_invest_.cost_inv_pv_test()
        #     # # print("pv_bus", pv_bus)
        #     #
        #     # if pv_bus == 5:  # Ind area
        #     #     cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
        #     #                    (pv_size * cost_land_industry_2023 * land_area_pv)) * crf_PV)
        #     #     # print('cost_inv_pv Ind area =', cost_inv_pv)
        #     #
        #     # elif pv_bus == 6:  # Business area
        #     #     cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
        #     #                    (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
        #     #     # print('cost_inv_pv Business area =', cost_inv_pv)
        #     #
        #     # else:  # bus = 7
        #     #     cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
        #     #                    (pv_size * cost_land_residential_2023 * land_area_pv)) * crf_PV)
        #     #     # print('cost_inv_pv Res area =', cost_inv_pv)
        #     #
        #     # total_price += cost_inv_pv

        pv_size = self.x[1]
        wind_size = self.x[3]

        cost_inv_pv = pv_size * cost_pv_installation_2023
        cost_inv_wind = wind_size * cost_wind_installation_2023

        total_investment_cost = cost_inv_pv + cost_inv_wind
        # print("total_price 2023 inside func=", total_investment_cost)

        # op_cost =

        total_price += total_investment_cost

        return total_price

    def cost_sgen_opex_2023(self):  # calc per 24 hours
        cost_opex_2023_24h = 0
        for i in range(len(self.p_demand)):
            # print('hr =', i)

            if self.sgen[i] > self.p_demand[i]:
                # p_curt = self.sgen[i] - self.p_demand[i]
                p_curt = 0
            else:
                p_curt = 0
            # print("self.sgen=", self.sgen)
            costs_opex_2023 = (40*self.coal + 4*self.sgen + 1*p_curt + 45*self.p_ext) - FIT*self.sgen   # p_ext becomes -ve when selling
            # print('costs_opex_ =', costs_opex_2023.sum())
            cost_opex_2023_24h += costs_opex_2023.sum()
        # print('cost_opex_2023 =', cost_opex_2023)
        # print('cost_opex_2023_24h =', cost_opex_2023_24h)
        return cost_opex_2023_24h

    def cost_sgen_invest_2024(self):

        total_price = 0

        pv_size = self.x[1]
        wind_size = self.x[3]

        cost_inv_pv = pv_size * cost_pv_installation_2024
        cost_inv_wind = wind_size * cost_wind_installation_2024

        total_investment_cost = cost_inv_pv + cost_inv_wind
        # print("total_price 2023 inside func=", total_investment_cost)

        # op_cost =

        total_price += total_investment_cost

        return total_price

    def cost_sgen_opex_2024(self):  # calc per 24 hours
        cost_opex_2024_24h = 0
        for i in range(len(self.p_demand)):
            # print('hr =', i)

            if self.sgen[i] > self.p_demand[i]:
                p_curt = self.sgen[i] - self.p_demand[i]
            else:
                p_curt = 0

            costs_opex_2024 = (45*self.coal + 4.5*self.sgen + 1.5*p_curt + 60*self.p_ext) - FIT*self.sgen   # p_ext becomes -ve when selling
            # print('costs_opex_ =', costs_opex_2023.sum())
            cost_opex_2024_24h += costs_opex_2024.sum()
        # print('cost_opex_2023 =', cost_opex_2023)
        # print('cost_opex_2023_24h =', cost_opex_2023_24h)
        return cost_opex_2024_24h

    def cost_sgen_invest_2025(self):

        total_price = 0

        pv_size = self.x[1]
        wind_size = self.x[3]

        cost_inv_pv = pv_size * cost_pv_installation_2025
        cost_inv_wind = wind_size * cost_wind_installation_2025

        total_investment_cost = cost_inv_pv + cost_inv_wind
        # print("total_price 2023 inside func=", total_investment_cost)

        # op_cost =

        total_price += total_investment_cost

        return total_price

    def cost_sgen_opex_2025(self):  # calc per 24 hours
        cost_opex_2025_24h = 0
        for i in range(len(self.p_demand)):
            # print('hr =', i)

            if self.sgen[i] > self.p_demand[i]:
                p_curt = self.sgen[i] - self.p_demand[i]
            else:
                p_curt = 0

            costs_opex_2025 = (50*self.coal + 5.5*self.sgen + 2.5*p_curt + 80*self.p_ext) - FIT*self.sgen   # p_ext becomes -ve when selling
            # print('costs_opex_ =', costs_opex_2023.sum())
            cost_opex_2025_24h += costs_opex_2025.sum()
        # print('cost_opex_2023 =', cost_opex_2023)
        # print('cost_opex_2023_24h =', cost_opex_2023_24h)
        return cost_opex_2025_24h

    def cost_sgen_invest_2026(self):

        total_price = 0

        pv_size = self.x[1]
        wind_size = self.x[3]

        cost_inv_pv = pv_size * cost_pv_installation_2026
        cost_inv_wind = wind_size * cost_wind_installation_2026

        total_investment_cost = cost_inv_pv + cost_inv_wind
        # print("total_price 2023 inside func=", total_investment_cost)

        # op_cost =

        total_price += total_investment_cost

        return total_price

    def cost_sgen_opex_2026(self):  # calc per 24 hours
        cost_opex_2026_24h = 0
        for i in range(len(self.p_demand)):
            # print('hr =', i)

            if self.sgen[i] > self.p_demand[i]:
                p_curt = self.sgen[i] - self.p_demand[i]
            else:
                p_curt = 0

            costs_opex_2026 = (55*self.coal + 6.5*self.sgen + 4.5*p_curt + 100*self.p_ext) - FIT*self.sgen   # p_ext becomes -ve when selling
            # print('costs_opex_ =', costs_opex_2023.sum())
            cost_opex_2026_24h += costs_opex_2026.sum()
        # print('cost_opex_2026 =', cost_opex_2026)
        # print('cost_opex_2026_24h =', cost_opex_2026_24h)
        return cost_opex_2026_24h


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OLD %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     def cost_pv_mix_grid_2023(self):
#
#         total_price = 0
#
#         # for idx_bus in self.net.bus.index:
#         for idx_bus, load_bus in enumerate(range(45, 56)):
#
#             pv_bus = self.x[0:13][idx_bus]
#             pv_size = self.x[13:26][idx_bus]
#
#             # bus_bar_pv = [int(val) for val in self.x if val.is_integer()]  # Extract bus bar numbers
#             # pv_capacities = [val for val in self.x if not val.is_integer()]  # Extract PV generator capacities
#             # cost_invest_ = investment_cost(self.net, bus_bar=self.x[0:2][idx_bus], pv_size=self.x[2:4][idx_bus])
#             # cost_inv_pv_out = cost_invest_.cost_inv_pv_test()
#             # print("pv_bus", pv_bus)
#             # print("pv_size =", pv_size)
#
#             if pv_bus == 45:  # Ind area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_industry_2023 * land_area_pv)) * crf_PV)
#                 # print('cost_pv at 45 =', cost_inv_pv)
#
#             elif pv_bus == 46:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#                 # print('cost_pv at 46 =', cost_inv_pv)
#
#             elif pv_bus == 47:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 48:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 49:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 50:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 51:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 52:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 53:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 54:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 55:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             elif pv_bus == 56:  # Business area
#                 cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                                (pv_size * cost_land_business_2023 * land_area_pv)) * crf_PV)
#
#             else:  # bus = 7
#                 # cost_inv_pv = (((pv_size * cost_pv_installation_2023) +
#                 #                (pv_size * cost_land_residential_2023 * land_area_pv)) * crf_PV)
#                 cost_inv_pv = None
#                 # print('cost_inv_pv Res area =', cost_inv_pv)
#
#             total_price += cost_inv_pv
#
#         return total_price
#
#     def cost_pv_test_2024(self):
#
#         total_price = 0
#
#         # for idx_bus in self.net.bus.index:
#         for idx_bus, load_bus in enumerate(range(5, 7)):
#
#             # pv_bus = self.x[4:6][idx_bus]
#             # pv_size = self.x[6:8][idx_bus]
#             pv_bus = self.x[0:2][idx_bus]
#             pv_size = self.x[2:4][idx_bus]
#             # print("pv_bus", pv_bus)
#
#             if pv_bus == 5:  # Ind area
#                 cost_inv_pv_ = ((pv_size * cost_pv_installation_2024) +
#                                (pv_size * cost_land_industry_2024 * land_area_pv))  # * crf_PV
#
#                 # print(cost_inv_pv_)
#                 # print(crf_PV)
#                 cost_inv_pv = cost_inv_pv_ * crf_PV
#                 # print('cost_inv_pv Ind area =', cost_inv_pv)
#
#             elif pv_bus == 6:  # Business area
#                 cost_inv_pv = ((pv_size * cost_pv_installation_2024) +
#                                (pv_size * cost_land_business_2024 * land_area_pv) * crf_PV)
#                 # print('cost_inv_pv Business area 2024 =', cost_inv_pv)
#
#             else:  # bus = 7
#                 cost_inv_pv = ((pv_size * cost_pv_installation_2024) +
#                                (pv_size * cost_land_residential_2024 * land_area_pv) * crf_PV)
#                 # print('cost_inv_pv Res area =', cost_inv_pv)
#
#             total_price += cost_inv_pv
#
#         return total_price
#
#     def cost_inv_2023_pv(self):        # Y1 2023
#         # if self.stage == 1:
#         for idx_f2 in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[0:15][idx_f2], pv_size=self.x[15:30][idx_f2],
#                                           bess_size_mwh=self.x[271])
#             cost_investment_2023 = cost_invest.capital_cost_pv_2023()
#             # cost_investment_2024 = cost_invest.capital_cost_pv_2024()
#             cost_investment_pv_2023.append(cost_investment_2023)
#             # cost_investment_pv_2024.append(cost_investment_2024)
#
#             cost_investment_bess_2023 = cost_invest.capital_cost_bess_2023()
#
#         res_inv_pv_2023 = sum(cost_investment_pv_2023)
#         # res_inv_pv_2024 = sum(cost_investment_pv_2024)
#
#         # print(res_inv_pv_2023, res_inv_pv_2024)
#
#         res_inv_pv_y1 = res_inv_pv_2023
#         # print("y1 = ", res_inv_pv_y1)
#
#         return res_inv_pv_y1
#
#     def cost_inv_2024_pv(self):  # y2 2024
#         # if self.stage == 1:
#         for idx_f2 in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[30:45][idx_f2], pv_size=self.x[45:60][idx_f2],
#                                           bess_size_mwh=self.x[272])
#             # cost_investment_2023 = cost_invest.capital_cost_pv_2023()
#             cost_investment_2024 = cost_invest.capital_cost_pv_2024()
#             # cost_investment_pv_2023.append(cost_investment_2023)
#             cost_investment_pv_2024.append(cost_investment_2024)
#
#             cost_investment_bess_2024 = cost_invest.capital_cost_bess_2024()
#
#         # res_inv_pv_2023 = sum(cost_investment_pv_2023)
#         res_inv_pv_2024 = sum(cost_investment_pv_2024)
#
#         # print(res_inv_pv_2023, res_inv_pv_2024)
#
#         cost_inv_pv_y2 = res_inv_pv_2024
#         # print("y2 =", res_inv_pv_y2)
#
#         return cost_inv_pv_y2
#
#     def cost_inv_2025_pv(self):  # y3 = 2025
#         for idx_f2 in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[60:75][idx_f2], pv_size=self.x[75:90][idx_f2],
#                                           bess_size_mwh=self.x[273])
#             cost_investment_2025 = cost_invest.capital_cost_pv_2025()
#
#             cost_investment_pv_2025.append(cost_investment_2025)
#
#         res_inv_pv_2025 = sum(cost_investment_pv_2025)
#         cost_inv_pv_y3 = res_inv_pv_2025
#
#         return cost_inv_pv_y3
#
#     def cost_inv_2026_pv(self):  # y3 = 2025
#         for idx_f2 in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[90:105][idx_f2], pv_size=self.x[105:120][idx_f2],
#                                           bess_size_mwh=self.x[274])
#             cost_investment_2026 = cost_invest.capital_cost_pv_2026()
#
#             cost_investment_pv_2026.append(cost_investment_2026)
#
#         res_inv_pv_2026 = sum(cost_investment_pv_2026)
#         cost_inv_pv_y4 = res_inv_pv_2026
#
#         return cost_inv_pv_y4
#
#     def cost_inv_2027_pv(self):  # y3 = 2025
#         for idx_f2 in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[120:135][idx_f2], pv_size=self.x[135:150][idx_f2],
#                                           bess_size_mwh=self.x[275])
#             cost_investment_2027 = cost_invest.capital_cost_pv_2027()
#
#             cost_investment_pv_2027.append(cost_investment_2027)
#
#         res_inv_pv_2027 = sum(cost_investment_pv_2027)
#         cost_inv_pv_y5 = res_inv_pv_2027
#
#         return cost_inv_pv_y5
#
#     def cost_inv_2028_pv(self):  # y3 = 2025
#         for idx_f2 in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[150:165][idx_f2], pv_size=self.x[165:180][idx_f2],
#                                           bess_size_mwh=self.x[276])
#             cost_investment_2028 = cost_invest.capital_cost_pv_2027()
#
#             cost_investment_pv_2028.append(cost_investment_2028)
#
#         res_inv_pv_2028 = sum(cost_investment_pv_2028)
#         cost_inv_pv_y6 = res_inv_pv_2028
#
#         return cost_inv_pv_y6
#
#     def year3_om(self): # y3 = 2025
#         tot_pv = sum(self.x[75:90])
#         cost_om_y3 = om_cost(x=tot_pv)
#         cost_om_pv_y3 = cost_om_y3.pv_om_cost()
#
#         return cost_om_pv_y3
#
#     def year4_inv(self):  # y4 = 2026
#         for idx in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[90:105][idx], pv_size=self.x[105:120][idx])
#             cost_investment_2026 = cost_invest.capital_cost_pv_2026()
#
#             cost_investment_pv_2026.append(cost_investment_2026)
#
#         res_inv_pv_2026 = sum(cost_investment_pv_2026)
#         cost_inv_pv_y4 = res_inv_pv_2026
#
#         return cost_inv_pv_y4
#
#     def year4_om(self):     # y4 = 2026
#         tot_pv = sum(self.x[105:120])
#         cost_om_y4 = om_cost(x=tot_pv)
#         cost_om_pv_y4 = cost_om_y4.pv_om_cost()
#
#         return cost_om_pv_y4
#
#     def year5_inv(self):  # y5 = 2027
#         for idx in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[120:135][idx], pv_size=self.x[135:150][idx])
#             cost_investment_2027 = cost_invest.capital_cost_pv_2027()
#
#             cost_investment_pv_2027.append(cost_investment_2027)
#
#         res_inv_pv_2027 = sum(cost_investment_pv_2027)
#         cost_inv_pv_y5 = res_inv_pv_2027
#
#         return cost_inv_pv_y5
#
#     def year5_om(self):     # y5 = 2027
#         tot_pv = sum(self.x[135:150])
#         cost_om_y5 = om_cost(x=tot_pv)
#         cost_om_pv_y5 = cost_om_y5.pv_om_cost()
#
#         return cost_om_pv_y5
#
#     def year6_inv(self):  # y6 = 2028
#         for idx in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[150:165][idx], pv_size=self.x[165:180][idx])
#             cost_investment_2028 = cost_invest.capital_cost_pv_2028()
#
#             cost_investment_pv_2028.append(cost_investment_2028)
#
#         res_inv_pv_2028 = sum(cost_investment_pv_2028)
#         cost_inv_pv_y6 = res_inv_pv_2028
#
#         return cost_inv_pv_y6
#
#     def year6_om(self):     # y6 = 2028
#         tot_pv = sum(self.x[165:180])
#         cost_om_y6 = om_cost(x=tot_pv)
#         cost_om_pv_y6 = cost_om_y6.pv_om_cost()
#
#         return cost_om_pv_y6
#
#     def year7_inv(self):  # y7 = 2029
#         for idx in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[180:195][idx], pv_size=self.x[195:210][idx])
#             cost_investment_2029 = cost_invest.capital_cost_pv_2029()
#
#             cost_investment_pv_2029.append(cost_investment_2029)
#
#         res_inv_pv_2029 = sum(cost_investment_pv_2029)
#         cost_inv_pv_y7 = res_inv_pv_2029
#
#         return cost_inv_pv_y7
#
#     def year7_om(self):     # y7 = 2029
#         tot_pv = sum(self.x[195:210])
#         cost_om_y7 = om_cost(x=tot_pv)
#         cost_om_pv_y7 = cost_om_y7.pv_om_cost()
#
#         return cost_om_pv_y7
#
#     def year8_inv(self):  # y8 = 2030
#         for idx in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[210:225][idx], pv_size=self.x[225:240][idx])
#             cost_investment_2030 = cost_invest.capital_cost_pv_2030()
#
#             cost_investment_pv_2030.append(cost_investment_2030)
#
#         res_inv_pv_2030 = sum(cost_investment_pv_2030)
#         cost_inv_pv_y8 = res_inv_pv_2030
#
#         return cost_inv_pv_y8
#
#     def year8_om(self):     # y8 = 2030
#         tot_pv = sum(self.x[225:240])
#         cost_om_y8 = om_cost(x=tot_pv)
#         cost_om_pv_y8 = cost_om_y8.pv_om_cost()
#
#         return cost_om_pv_y8
#
#     def year9_inv(self):  # y9 = 2031
#         for idx in self.net.bus.index:
#             cost_invest = investment_cost(self.net, bus_bar=self.x[240:255][idx], pv_size=self.x[255:270][idx])
#             cost_investment_2031 = cost_invest.capital_cost_pv_2031()
#
#             cost_investment_pv_2031.append(cost_investment_2031)
#
#         res_inv_pv_2031 = sum(cost_investment_pv_2031)
#         cost_inv_pv_y9 = res_inv_pv_2031
#
#         return cost_inv_pv_y9
#
#     def year9_om(self):     # y9 = 2031
#         tot_pv = sum(self.x[255:270])
#         cost_om_y9 = om_cost(x=tot_pv)
#         cost_om_pv_y9 = cost_om_y9.pv_om_cost()
#
#         return cost_om_pv_y9
#
#     # ************************************** BESS *********************************************************
#     def cost_inv_2023_bess(self):
#         # for idx_f2 in self.net.bus.index:
#         cost_invest = investment_cost_bess(bess_size_mwh=self.x[271])
#             # cost_investment_2023 = cost_invest.capital_cost_pv_2023()
#             # cost_investment_2024 = cost_invest.capital_cost_pv_2024()
#             # cost_investment_pv_2023.append(cost_investment_2023)
#             # cost_investment_pv_2024.append(cost_investment_2024)
#
#         cost_investment_bess_2023 = cost_invest.capital_cost_bess_2023()
#
#         # res_inv_pv_2023 = sum(cost_investment_pv_2023)
#         # res_inv_pv_2024 = sum(cost_investment_pv_2024)
#
#         # print(res_inv_pv_2023, res_inv_pv_2024)
#
#         # res_inv_pv_y1 = res_inv_pv_2023
#         # print("y1 = ", res_inv_pv_y1)
#
#         return cost_investment_bess_2023
#
#     def cost_inv_2024_bess(self):
#         cost_invest = investment_cost_bess(bess_size_mwh=self.x[272])
#         cost_investment_bess_2024 = cost_invest.capital_cost_bess_2024()
#         return cost_investment_bess_2024
#
#     def cost_inv_2025_bess(self):
#         cost_invest = investment_cost_bess(bess_size_mwh=self.x[273])
#         cost_investment_bess_2025 = cost_invest.capital_cost_bess_2025()
#         return cost_investment_bess_2025
#
#     def cost_inv_2026_bess(self):
#         cost_invest = investment_cost_bess(bess_size_mwh=self.x[274])
#         cost_investment_bess_2026 = cost_invest.capital_cost_bess_2026()
#         return cost_investment_bess_2026
#
#     def cost_inv_2027_bess(self):
#         cost_invest = investment_cost_bess(bess_size_mwh=self.x[275])
#         cost_investment_bess_2027 = cost_invest.capital_cost_bess_2027()
#         return cost_investment_bess_2027
#
#     def cost_inv_2028_bess(self):
#         cost_invest = investment_cost_bess(bess_size_mwh=self.x[276])
#         cost_investment_bess_2026 = cost_invest.capital_cost_bess_2025()
#         return cost_investment_bess_2026
#
#     # --------------------------------------------------------------------------
#     def cost_om_2023_bess(self):     # Y1 2023
#         # pv_size_mw = sum(self.x[15:30])
#         # bess_size_mwh = self.x[271]
#         # print("bess_size_mwh", bess_size_mwh)
#         # # cost_om_y1 = om_cost(pv_size=pv_size_mw, bess_size_mwh=bess_size_mwh)
#         # cost_om_y1 = om_cost(x=bess_size_mwh)
#         # # cost_om_pv_y1 = cost_om_y1.pv_om_cost()
#         # cost_om_bess_2023 = cost_om_y1.bess_om_cost_2023()
#
#         bess_size_mwh = self.x[271]
#         cost_om_y1_bess = om_cost(x=bess_size_mwh)
#         cost_om_bess_2023 = cost_om_y1_bess.bess_om_cost_2023()
#
#         return cost_om_bess_2023
#
#     def cost_om_2024_bess(self):    # y2 2024
#         # tot_pv = sum(self.x[45:60])
#         # print(tot_pv)
#         # cost_om_y2 = om_cost(pv_size=tot_pv, bess_size_mwh=self.x[272])
#         cost_om_y2 = om_cost(x=self.x[272])
#         # cost_om_pv_y2 = cost_om_y2.pv_om_cost()
#
#         cost_om_bess_2024 = cost_om_y2.bess_om_cost_2024()
#
#         return cost_om_bess_2024
#
#     def cost_om_2025_bess(self):    # y3 2025
#         cost_om_y3 = om_cost(x=self.x[273])
#         cost_om_bess_2025 = cost_om_y3.bess_om_cost_2025()
#         return cost_om_bess_2025
#
#     def cost_om_2026_bess(self):    # y4 2026
#         cost_om_y4 = om_cost(x=self.x[274])
#         cost_om_bess_2026 = cost_om_y4.bess_om_cost_2026()
#         return cost_om_bess_2026
#
#     def cost_om_2027_bess(self):    # y5 2027
#         cost_om_y5 = om_cost(x=self.x[275])
#         cost_om_bess_2027 = cost_om_y5.bess_om_cost_2027()
#         return cost_om_bess_2027
#
#     def cost_om_2028_bess(self):    # y6 2028
#         cost_om_y6 = om_cost(x=self.x[276])
#         cost_om_bess_2028 = cost_om_y6.bess_om_cost_2028()
#         return cost_om_bess_2028
#
#     # *********************************************** CHP ***************************************************
#     def cost_inv_2023_chp(self):
#         cost_inv_chp = investment_cost_chp(chp_size_mwh=self.x[281])
#         cost_inv_chp_2023 = cost_inv_chp.capital_cost_chp_2023()
#         return cost_inv_chp_2023
#
#     def cost_inv_2024_chp(self):
#         cost_inv_chp = investment_cost_chp(chp_size_mwh=self.x[282])
#         cost_inv_chp_2024 = cost_inv_chp.capital_cost_chp_2024()
#         return cost_inv_chp_2024
#
#     def cost_inv_2025_chp(self):
#         cost_inv_chp = investment_cost_chp(chp_size_mwh=self.x[283])
#         cost_inv_chp_2025 = cost_inv_chp.capital_cost_chp_2025()
#         return cost_inv_chp_2025
#
#     def cost_inv_2026_chp(self):
#         cost_inv_chp = investment_cost_chp(chp_size_mwh=self.x[284])
#         cost_inv_chp_2026 = cost_inv_chp.capital_cost_chp_2026()
#         return cost_inv_chp_2026
#
#     def cost_inv_2027_chp(self):
#         cost_inv_chp = investment_cost_chp(chp_size_mwh=self.x[285])
#         cost_inv_chp_2027 = cost_inv_chp.capital_cost_chp_2027()
#         return cost_inv_chp_2027
#
#     def cost_inv_2028_chp(self):
#         cost_inv_chp = investment_cost_chp(chp_size_mwh=self.x[286])
#         cost_inv_chp_2028 = cost_inv_chp.capital_cost_chp_2028()
#         return cost_inv_chp_2028
#
#     # --------------------------------------------------------------------------
#     def cost_om_2023_chp(self):
#         cost_om_chp_2023 = om_cost(x=self.x[281])
#         cost_om_chp_2023 = cost_om_chp_2023.chp_om_cost_2023()
#         return cost_om_chp_2023
#
#     def cost_om_2024_chp(self):
#         cost_om_chp_2024 = om_cost(x=self.x[282])
#         cost_om_chp_2023 = cost_om_chp_2024.chp_om_cost_2024()
#         return cost_om_chp_2023
#
#     def cost_om_2025_chp(self):
#         cost_om_chp_2025 = om_cost(x=self.x[283])
#         cost_om_chp_2025 = cost_om_chp_2025.chp_om_cost_2025()
#         return cost_om_chp_2025
#
#     def cost_om_2026_chp(self):
#         cost_om_chp_2026 = om_cost(x=self.x[284])
#         cost_om_chp_2026 = cost_om_chp_2026.chp_om_cost_2026()
#         return cost_om_chp_2026
#
#     def cost_om_2027_chp(self):
#         cost_om_chp_2027 = om_cost(x=self.x[285])
#         cost_om_chp_2027 = cost_om_chp_2027.chp_om_cost_2027()
#         return cost_om_chp_2027
#
#     def cost_om_2028_chp(self):
#         cost_om_chp_2028 = om_cost(x=self.x[286])
#         cost_om_chp_2028 = cost_om_chp_2028.chp_om_cost_2028()
#         return cost_om_chp_2028
#
#     # *********************************************** HP ***************************************************
#     def cost_inv_2023_hp(self):
#         cost_inv_hp = investment_cost_hp(hp_size_mwh=self.x[291])
#         cost_inv_hp_2023 = cost_inv_hp.capital_cost_hp_2023()
#         return cost_inv_hp_2023
#
#     def cost_inv_2024_hp(self):
#         cost_inv_hp = investment_cost_hp(hp_size_mwh=self.x[292])
#         cost_inv_hp_2024 = cost_inv_hp.capital_cost_hp_2024()
#         return cost_inv_hp_2024
#
#     def cost_inv_2025_hp(self):
#         cost_inv_hp = investment_cost_hp(hp_size_mwh=self.x[293])
#         cost_inv_hp_2025 = cost_inv_hp.capital_cost_hp_2025()
#         return cost_inv_hp_2025
#
#     def cost_inv_2026_hp(self):
#         cost_inv_hp = investment_cost_hp(hp_size_mwh=self.x[294])
#         cost_inv_hp_2026 = cost_inv_hp.capital_cost_hp_2026()
#         return cost_inv_hp_2026
#
#     def cost_inv_2027_hp(self):
#         cost_inv_hp = investment_cost_hp(hp_size_mwh=self.x[295])
#         cost_inv_hp_2027 = cost_inv_hp.capital_cost_hp_2027()
#         return cost_inv_hp_2027
#
#     def cost_inv_2028_hp(self):
#         cost_inv_hp = investment_cost_hp(hp_size_mwh=self.x[296])
#         cost_inv_hp_2028 = cost_inv_hp.capital_cost_hp_2028()
#         return cost_inv_hp_2028
#
#     # -----------------------------------------------------------
#
#     def cost_om_2023_hp(self):
#         cost_om_hp = om_cost(x=self.x[291])
#         cost_om_hp_2023 = cost_om_hp.hp_om_cost_2023()
#         return cost_om_hp_2023
#
#     def cost_om_2024_hp(self):
#         cost_om_hp = om_cost(x=self.x[292])
#         cost_om_hp = cost_om_hp.hp_om_cost_2024()
#         return cost_om_hp
#
#     def cost_om_2025_hp(self):
#         cost_om_hp = om_cost(x=self.x[293])
#         cost_om_hp = cost_om_hp.hp_om_cost_2025()
#         return cost_om_hp
#
#     def cost_om_2026_hp(self):
#         cost_om_hp = om_cost(x=self.x[294])
#         cost_om_hp = cost_om_hp.hp_om_cost_2026()
#         return cost_om_hp
#
#     def cost_om_2027_hp(self):
#         cost_om_hp = om_cost(x=self.x[295])
#         cost_om_hp = cost_om_hp.hp_om_cost_2027()
#         return cost_om_hp
#
#     def cost_om_2028_hp(self):
#         cost_om_hp = om_cost(x=self.x[296])
#         cost_om_hp = cost_om_hp.hp_om_cost_2028()
#         return cost_om_hp
#
#     # *********************************************** P2G ***************************************************
#     def cost_inv_2023_p2g(self):
#         cost_inv_ = investment_cost_p2g(p2g_size_mw=self.x[300])
#         cost_inv_hp = cost_inv_.capital_cost_p2g_2023()
#         return cost_inv_hp
#
#     def cost_inv_2024_p2g(self):
#         cost_inv_ = investment_cost_p2g(p2g_size_mw=self.x[301])
#         cost_inv_hp = cost_inv_.capital_cost_p2g_2024()
#         return cost_inv_hp
#
#     def cost_inv_2025_p2g(self):
#         cost_inv_ = investment_cost_p2g(p2g_size_mw=self.x[302])
#         cost_inv_hp = cost_inv_.capital_cost_p2g_2025()
#         return cost_inv_hp
#
#     def cost_inv_2026_p2g(self):
#         cost_inv_ = investment_cost_p2g(p2g_size_mw=self.x[303])
#         cost_inv_hp = cost_inv_.capital_cost_p2g_2026()
#         return cost_inv_hp
#
#     def cost_inv_2027_p2g(self):
#         cost_inv_ = investment_cost_p2g(p2g_size_mw=self.x[304])
#         cost_inv_hp = cost_inv_.capital_cost_p2g_2027()
#         return cost_inv_hp
#
#     def cost_inv_2028_p2g(self):
#         cost_inv_ = investment_cost_p2g(p2g_size_mw=self.x[305])
#         cost_inv_hp = cost_inv_.capital_cost_p2g_2028()
#         return cost_inv_hp
#
#     # -----------------------------------------------------------
#
#     def cost_om_2023_p2g(self):
#         cost_om_ = om_cost(x=self.x[300])
#         cost_om = cost_om_.p2g_om_cost_2023()
#         return cost_om
#
#     def cost_om_2024_p2g(self):
#         cost_om_ = om_cost(x=self.x[301])
#         cost_om = cost_om_.p2g_om_cost_2024()
#         return cost_om
#
#     def cost_om_2025_p2g(self):
#         cost_om_ = om_cost(x=self.x[302])
#         cost_om = cost_om_.p2g_om_cost_2025()
#         return cost_om
#
#     def cost_om_2026_p2g(self):
#         cost_om_ = om_cost(x=self.x[303])
#         cost_om = cost_om_.p2g_om_cost_2026()
#         return cost_om
#
#     def cost_om_2027_p2g(self):
#         cost_om_ = om_cost(x=self.x[304])
#         cost_om = cost_om_.p2g_om_cost_2027()
#         return cost_om
#
#     def cost_om_2028_p2g(self):
#         cost_om_ = om_cost(x=self.x[305])
#         cost_om = cost_om_.p2g_om_cost_2028()
#         return cost_om
