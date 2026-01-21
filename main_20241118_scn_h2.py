# 2024.07
import time
start_time = time.time()  # Start the simulation

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

import pandas as pd
import numpy as np

# ........................ PandaPower and Pymoo ........................

import pandapower.networks as pn
# from pymoo.core.mixed import MixedVariableGA
# from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Binary

# ........................ Functions ........................
from e_net_mv_20240725 import power_system
# from investment_cost_function_20240711 import PRICE
from cost_fuct_20240814_CAPEX import PRICE
from cost_func_om_2025_20240816 import OPEX
# from power_flow_calc import power_flow_calc
# from sgen import create_sgen
from chp_model_20240716 import CHP
from hp_model_20240718 import hp_model
from tes_dhnet_lp_storage_20240723 import TES
from p2g_model import P2G
from h2_storage_20240724 import HyES
from emission_func_20240909 import emission_calc
# from repair_capacity import repair_function

# from bess_20240725 import BESS
# import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# ........................ Power grid ........................
net = pn.create_cigre_network_mv(with_der=False)
net.load.drop(index=net.load.index, inplace=True)
net.sgen.drop(index=net.sgen.index, inplace=True)
net.gen.drop(index=net.gen.index, inplace=True)
net.xward.drop(net.xward.index, inplace=True)
net.shunt.drop(index=net.shunt.index, inplace=True)
# print(net.gen)

# ........................ Gas grid (OLD) ........................
# Gas grid and heat demand:
# index_hr = pd.date_range("2016-01-01 00:00", "2016-01-01 23:00", freq="H")
# gas_grid = pd.Series([300]*len(index_hr), index_hr)   # [MWh]
# g_demand_mwh_2023 = 37.72

# ........................ Fixed Parameters ........................
discount_rate = 0.08

g2025_re_share_max_limit = 0 #0.0
g2026_re_share_max_limit = 0 #0.1
g2027_re_share_max_limit = 0 #0.2
g2028_re_share_max_limit = 0 #0.3
g2029_re_share_max_limit = 0 #0.3
g2030_re_share_max_limit = 0 #0.5
g2031_re_share_max_limit = 0 #0.5
g2032_re_share_max_limit = 0 #0.6
g2033_re_share_max_limit = 0 #0.7
g2034_re_share_max_limit = 0 #0.7
g2035_re_share_max_limit = 0 #0.7
g2036_re_share_max_limit = 0 #0.8
g2037_re_share_max_limit = 0 #0.8
g2038_re_share_max_limit = 0 #1.0

min_v_drop = 0.5
max_v_drop = 1.5


# ........................ Optimization Function ........................


class MyProblem(ElementwiseProblem):

    def __init__(self, year, stage, carried_capacity, carried_capacity_pv, carried_cap_pv_array_mw, **kwargs):
        variables = dict()

        self.year = year
        self.stage = stage
        self.carried_capacity = carried_capacity
        self.carried_capacity_pv = carried_capacity_pv
        self.carried_cap_pv_array_mw = carried_cap_pv_array_mw

        # *********************************** PV stage 1 ******************************************
        # bus-bars for the PV generators in industrial area
        for k in range(0, 2):
            variables[f"x{k:01}"] = Integer(bounds=(1, 2))
        for k in range(2, 5):
            variables[f"x{k:01}"] = Integer(bounds=(12, 14))

        # bus-bars for the PV generators in commercial/small industry area
        for k in range(5, 8):
            variables[f"x{k:01}"] = Integer(bounds=(3, 5))
        for k in range(8, 13):
            variables[f"x{k:01}"] = Integer(bounds=(7, 11))

        # bus-bars for the PV generators in residential area
        for k in range(13, 14):
            variables[f"x{k:01}"] = Integer(bounds=(6, 6))

        # size of PV generators for all bus-bars
        for k in range(14, 28):
            variables[f"x{k:01}"] = Real(bounds=(0, 1))  # [MW]

        # *********************** WT ****************************
        # bus-bars for the Wind generators
        for k in range(28, 29):
            variables[f"x{k:01}"] = Integer(bounds=(0, 0))

        # size of WT generators at bus 0
        for k in range(29, 30):
            variables[f"x{k:01}"] = Real(bounds=(0, 100))  # [MW]

        # *********************** CHP ****************************
        # CHP bus-bar
        for k in range(30, 31):
            variables[f"x{k:01}"] = Integer(bounds=(6, 6))  # CHP locations is fixed at bus = 6

        # Size of the CHP
        if year == 2025:
            for k in range(31, 32):
                variables[f"x{k:01}"] = Real(bounds=(0.2, 0.2))  # [MW]
        else:
            for k in range(31, 32):
                variables[f"x{k:01}"] = Real(bounds=(0, 0.25))  # [MW]

        # *********************** HP ****************************
        # HP bus-bar
        for k in range(32, 33):
            variables[f"x{k:01}"] = Integer(bounds=(6, 6))

        # Size of the HP
        if year == 2025:
            for k in range(33, 34):
                variables[f"x{k:01}"] = Real(bounds=(0, 0))  # [MW]
        else:
            for k in range(33, 34):
                variables[f"x{k:01}"] = Real(bounds=(0, 1))  # [MW]

        # *********************** TES ****************************
        # Thermal energy storage (TES)
        for k in range(34, 35):
            variables[f"x{k:01}"] = Real(bounds=(0, 0))  # [MW]

        # *********************** P2G ****************************
        for k in range(35, 36):
            variables[f"x{k:01}"] = Real(bounds=(0, 1))  # [MW]

        # *********************** H2 Storage **********************
        for k in range(36, 37):
            variables[f"x{k:01}"] = Real(bounds=(0, 0))  # [MW]

        # ********************** BESS *****************************
        # Bus 1, 2 & 12 --> big industry
        for k in range(37, 38):
            variables[f"x{k:01}"] = Integer(bounds=(1, 14))

        # Charge/Discharge power rating per hr at bus 1, 2 & 12
        for k in range(38, 39):
            variables[f"x{k:01}"] = Real(bounds=(0, 2))  # [MW]

        # ********************** Gas Gen *****************************
        # Bus-bar = 12
        for k in range(39, 40):
            variables[f"x{k:01}"] = Integer(bounds=(12, 12))

        # Size Gas Gen
        if year == 2025:
            for k in range(40, 41):
                variables[f"x{k:01}"] = Real(bounds=(15, 15))  # [MW]
        else:
            for k in range(40, 41):
                variables[f"x{k:01}"] = Real(bounds=(0, 15))  # [MW]

        # Bus-bar = 1
        for k in range(41, 42):
            variables[f"x{k:01}"] = Integer(bounds=(1, 1))

        # Size Gas Gen
        if year == 2025:
            for k in range(42, 43):
                variables[f"x{k:01}"] = Real(bounds=(0.5, 0.5))  # [MW]
        else:
            for k in range(42, 43):
                variables[f"x{k:01}"] = Real(bounds=(0, 0.5))  # [MW]

        super().__init__(vars=variables, n_obj=2, n_ieq_constr=60, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):

        x = np.array([x[f"x{k:01}"] for k in range(0, 43)])

        obj_value = 0  # for the final F1 at the end
        obj_value_emission_tCO2 = 0  # for F2

        g1_jan, g1_jul, g2025_heat_balance_jan, g2025_heat_balance_jul, g2025_pv_bound, g2025_re_share, \
            g2_jan, g2_jul, g2026_heat_balance_jan, g2026_heat_balance_jul, g2026_pv_bound, g2026_re_share, \
            g3_jan, g3_jul, g2027_heat_balance_jan, g2027_heat_balance_jul, g2027_pv_bound, g2027_re_share, \
            g4_jan, g4_jul, g2028_heat_balance_jan, g2028_heat_balance_jul, g2028_pv_bound, g2028_re_share, \
            g5_jan, g5_jul, g2029_heat_balance_jan, g2029_heat_balance_jul, g2029_pv_bound, g2029_re_share, \
            g6_jan, g6_jul, g2030_heat_balance_jan, g2030_heat_balance_jul, g2030_pv_bound, g2030_re_share, \
            g7_jan, g7_jul, g2031_heat_balance_jan, g2031_heat_balance_jul, g2031_pv_bound, g2031_re_share, \
            g8_jan, g8_jul, g2032_heat_balance_jan, g2032_heat_balance_jul, g2032_pv_bound, g2032_re_share, \
            g9_jan, g9_jul, g2033_heat_balance_jan, g2033_heat_balance_jul, g2033_pv_bound, g2033_re_share, \
            g10_jan, g10_jul, g2034_heat_balance_jan, g2034_heat_balance_jul, g2034_pv_bound, g2034_re_share = \
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        penalty = 0  # also added as G

        # ----------------------------- Define x values -----------------------------
        x_pv_bus = x[0:14]
        x_pv_size = x[14:28]
        x_wt_bus = x[28:29]
        x_wt_mw = x[29]
        x_chp_bus = x[30]
        x_chp_mw = x[31]
        x_hp_bus = x[32]
        x_hp_size = x[33]  # mw

        x_storage_th_size = x[34]  # [mwh]
        x_p2g_size_mw = x[35]
        x_storage_h2_mwh = x[36]
        x_bess_bus = x[37]
        x_bess_mw = x[38]

        x_gen_bus_12 = x[39]
        x_gen_bus_12_mw = x[40]
        x_gen_bus_1 = x[41]
        x_gen_bus_1_mw = x[42]
        # print('x_chp_mw =', x_chp_mw)

        # ------------------------------ Capacities for CAPEX calculation ------------------------------
        capex_x_pv_mw = x_pv_size
        capex_x_wt_mw = x_wt_mw  # Keeping the present year x values to calculate CAPEX
        capex_x_chp_mw = x_chp_mw
        capex_x_hp_mw = x_hp_size
        capex_x_storage_th_mw = x_storage_th_size
        capex_x_p2g_mw = x_p2g_size_mw
        capex_x_storage_h2_mwh = x_storage_h2_mwh
        capex_x_bess_mw = x_bess_mw
        # capex_x_gen_bus_12 = x_gen_bus_12       # I am not calculating the CAPEX of gas gen
        # capex_x_gen_bus_1 = x_gen_bus_1
        # print('capex_x_pv_mw =', sum(capex_x_pv_mw))
        # print('capex_x_wt_mw =', capex_x_wt_mw)

        # ----------------------------------------- Inter-Year interconnection -----------------------------------------
        # NOTE: in this method if the carried capacity is higher (>) than the present x_values, we add carried cap with
        # the present x_values to calculate e-net and OPEX. However, CAPEX is always calculated with the present
        # x_values.
        # If carried capacity is lower (<) than the present x_values, we use the present x_values to calculate e-net
        # and OPEX and CAPEX.
        # -------------------------- PV --------------------------
        new_pv_mw_array = np.array([])
        # carried_cap_pv_mw = self.carried_capacity_pv['PV1']
        carried_cap_pv_mw = self.carried_cap_pv_array_mw
        # print('carried_cap_pv_array_mw (_evaluate) =', sum(self.carried_cap_pv_array_mw))

        if self.year != years[0]:
            df_carried_capacity_pv = pd.DataFrame(carried_cap_pv_mw, columns=['pv_mw'])
            for i, ((idx_new_pv, row_new_pv), (idx_carried_pv, row_carried_pv)) in \
                    enumerate(zip(pd.DataFrame(x_pv_size).iterrows(), df_carried_capacity_pv.iterrows())):
                new_pv_mw = row_new_pv.values[0] + row_carried_pv.values[0]  # new PV cap for the power flow and OPEX
                new_pv_mw_array = np.append(new_pv_mw_array, new_pv_mw)
                x_pv_size = new_pv_mw_array
        else:
            for i, (idx, row) in enumerate((pd.DataFrame(x_pv_size).iterrows())):
                new_pv_mw = row.values[0]
                new_pv_mw_array = np.append(new_pv_mw_array, new_pv_mw)
            x_pv_size = new_pv_mw_array
        # print('new_x_pv_mw =', sum(x_pv_size))

        # ------------------------ PV Penalty ------------------------
        # Adding penalty for PV gen over 7 MW. 100MW is max CIGRE MV can converge. Max bus-bars = 14
        # 100 MW / 14 = 7 MW for each Bus-bar.
        pv_violation = 0
        for i, (idx, row) in enumerate((pd.DataFrame(x_pv_size).iterrows())):
            violation = max(0 - row.values, row.values - 7)
            if violation > 0:
                pv_violation += violation
                penalty += 1e6 * pv_violation

        # ------------------------ Repair function for PV capacity ------------------------
        # x_pv_mw_repair = repair_function(net=net, x_pv_mw=x_pv_size, x_pv_bus=x_pv_bus)
        # x_pv_size = x_pv_mw_repair.repair_pv_capacity()
        # print('x_pv_mw_NEW =', x_pv_size.sum())
        # res_p_balance_2023 = res_2023[1]

        # -------------------------- WT --------------------------
        carried_cap_wt_mw = self.carried_capacity['WT']
        # print('carried_cap_wt_mw =', carried_cap_wt_mw)
        if self.year != years[0]:
            total_cap_wt_mw = x_wt_mw + carried_cap_wt_mw
            x_wt_mw = total_cap_wt_mw
        else:
            x_wt_mw = x_wt_mw
        # print('new_wt_mw =', x_wt_mw)

        # -------------------------- BESS --------------------------
        # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        carried_cap_bess_mwh = self.carried_capacity['BESS']
        if self.year != years[0]:
            total_cap_bess_mwh = x_bess_mw + carried_cap_bess_mwh
            x_bess_mw = total_cap_bess_mwh
        else:
            x_bess_mw = x_bess_mw
        # print('New_x_bess_mw =', x_bess_mw)

        # -------------------------- CHP --------------------------
        # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        carried_cap_chp_mw = self.carried_capacity['CHP']
        # print('carried_capacity_CHP =', carried_cap_chp_mw)
        if self.year != years[0]:
            total_cap_chp_mw = x_chp_mw     # + carried_cap_chp_mw
            # not adding carried capacity, because it is conflicting with the g2026_heat_balance_jan &
            # g2026_heat_balance_jul calculation, as this will not allow the models to find the current capacity.
            x_chp_mw = total_cap_chp_mw
            # print('total_cap_chp_new_mw =', x_chp_mw)
        else:
            x_chp_mw = x_chp_mw
        # print('new_x_chp_mw =', x_chp_mw)

        # -------------------------- HP --------------------------
        # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        carried_cap_hp_mw = self.carried_capacity['HP']
        if self.year != years[0]:
            total_cap_hp_mw = x_hp_size + carried_cap_hp_mw
            x_hp_size = total_cap_hp_mw
        else:
            x_hp_size = x_hp_size

        # -------------------------- TH-Storage --------------------------
        # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        carried_cap_storage_th_mw = self.carried_capacity['TH_Storage']
        if self.year != years[0]:
            total_cap_storage_th_mw = x_storage_th_size + carried_cap_storage_th_mw
            x_storage_th_size = total_cap_storage_th_mw
        else:
            x_storage_th_size = x_storage_th_size

        # # -------------------------- Gas Gen at Bus 12 --------------------------
        # # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        # carried_cap_gas_gen12_mwh = self.carried_capacity['Gas_Gen_b12']
        # if self.year != years[0]:
        #     total_cap_gas_gen12_mwh = x_gen_bus_12_mw #+ carried_cap_gas_gen12_mwh
        #     x_gen_bus_12_mw = total_cap_gas_gen12_mwh
        # else:
        #     x_gen_bus_12_mw = x_gen_bus_12_mw
        #
        # # -------------------------- Gas Gen at Bus 1 --------------------------
        # # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        # carried_cap_gas_gen1_mwh = self.carried_capacity['Gas_Gen_b1']
        # if self.year != years[0]:
        #     total_cap_gas_gen1_mwh = x_gen_bus_1_mw #+ carried_cap_gas_gen1_mwh
        #     x_gen_bus_1_mw = total_cap_gas_gen1_mwh
        # else:
        #     x_gen_bus_1_mw = x_gen_bus_1_mw

        # -------------------------- P2G --------------------------
        # NOTE: change: carried_cap_?_mw, carried_capacity['?'], x_?_mw, total_cap_?_mw
        carried_cap_p2g_mw = self.carried_capacity['P2G']
        if self.year != years[0]:
            total_cap_p2g_mw = x_p2g_size_mw + carried_cap_p2g_mw
            x_p2g_size_mw = total_cap_p2g_mw
        else:
            x_p2g_size_mw = x_p2g_size_mw

        if self.year == 2025:
            year = 1
            obj_value_2025_eur_npv = 0

            # ======================================= 2025 - January =======================================
            # ******************** CHP ********************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]
            # print('x_chp_input_mw =', x_chp_mw)
            # print("res_chp_p_mwh =", res_chp_p_mwh)
            # print("res_chp_th_mwh =", res_chp_th_mwh)  # mw/h
            # print("res_chp_gas_import_m3 =", res_chp_gas_import_m3)

            # ******************** HP ********************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()
            # print("x_hp_input_mw=", x_hp_size)
            # print("res_hp_th_mwh =", res_hp_th_mwh)

            # ******************** Thermal Energy System, Storage Management & Heat Flow ********************
            # -------------------------- 2025 Jan ----------------------------------
            # either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # how to integrate in the TES function?
            # print("TES 2025 Jan:")
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # tes_th_flow_res = tes_res.heat_storage()
            # if -ve "producing less than demand - add constraint"
            # if +ve "producing more than demand - added to storage system"

            # NEW Thermal management model:
            res_tes_jan = tes_res.th_management_system_2025_jan_update()
            res_tes_ch4_import_2025_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2025_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2025_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh'].sum())  # values are negative,
            # so I am making them +Ve to calculate the Penalty price.

            # print(res_tes_jan)
            # print(res_tes_ch4_import_2025_jan_mwh)
            # print(res_tes_th_loss_2025_jan_mwh)
            # print(res_tes_th_deficit_2025_jan_mwh)

            # -------------------------- 2025 Jul ----------------------------------
            # print("TES 2025 July:")
            res_tes_2025_jul = tes_res.th_management_system_2025_jul_update()
            res_tes_ch4_import_2025_jul_mwh = res_tes_2025_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2025_jul_mwh = res_tes_2025_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2025_jul_mwh = np.abs(res_tes_2025_jul['th_energy_deficit_mwh'].sum())

            # NEW from 20241116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_2025_jul['heat_balance'].sum()

            # print(res_tes_2025_jul)
            # print(res_tes_ch4_import_2025_jul_mwh)
            # print(res_tes_th_loss_2025_jul_mwh)
            # print(res_tes_th_deficit_2025_jul_mwh)

            # ************************* P2G *********************************
            # print("P2G:")
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ************************* H2 Energy System, Storage Management & Hy Flow *****************************
            # print("GES:")
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)

            # -------------------------- 2025 Jan ----------------------------------
            res_ges_2025_jan = ges_res.h2_management_system_2025_jan_update()
            h2_blue_import_2025_jan_mwh = np.abs(res_ges_2025_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2025_jan_mwh = res_ges_2025_jan['h2_energy_loss_mwh'].sum()
            # print(res_ges_2025_jan)
            # print(h2_blue_import_2025_jan_mwh)

            # -------------------------- 2025 Jul ----------------------------------
            res_ges_2025_jul = ges_res.h2_management_system_2025_jul()
            h2_blue_import_2025_jul_mwh = np.abs(res_ges_2025_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2025_jul_mwh = res_ges_2025_jul['h2_energy_loss_mwh'].sum()
            # print(res_ges_2025_jul)
            # print(h2_blue_import_2025_jul_mwh)

            # ***************************************** POWER SYSTEM & BESS ****************************************
            # print("Power System 2025 Jan:")
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)
            res_p_sys_2023_jan = p_sys.power_flow_2025_jan()
            vm_jan = res_p_sys_2023_jan.iloc[:, 6:20]
            # print("vm =", vm)
            power_balance_2023_jan = res_p_sys_2023_jan.iloc[:, 0:7]
            res_line_loss_mw_2025_jan_mwh = res_p_sys_2023_jan['line_loss_mw'].sum()
            # print(power_balance_2023_jan)
            # print(res_line_loss_mw_2025_jan_mwh)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ------------------------- POWER SYSTEM July 2025 -------------------------
            res_p_sys_2025_jul = p_sys.power_flow_2025_jul()
            vm_jul = res_p_sys_2025_jul.iloc[:, 6:20]
            power_balance_2025_jul = res_p_sys_2025_jul.iloc[:, 0:6]
            res_line_loss_mw_2025_jul_mwh = power_balance_2025_jul['line_loss_mw'].sum()

            # print(power_balance_2025_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ================================================= F1 2025 ===========================================
            # --------------------------------------- CAPEX 2025 --------------------------------------
            # print("CAPEX for 19 years:")

            cost = PRICE(stage=self.stage, year=year,
                         x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                         x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                         x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                         x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                         x_storage_th_size=capex_x_storage_th_mw,
                         x_p2g_size_mw=capex_x_p2g_mw,
                         x_storage_h2_mwh=capex_x_storage_h2_mwh,
                         x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw
                         )

            price_invest_pv_2025 = cost.price_capex_pv_2025()
            price_invest_wt_2025 = cost.price_capex_wt_2025()
            price_invest_chp_2025 = cost.price_capex_chp_2025()
            price_invest_hp_2025 = cost.price_capex_hp_2025()
            price_invest_storage_th_2025 = cost.price_capex_storage_th_2025()
            price_invest_p2g_2025 = cost.price_capex_p2g_2025()
            price_invest_storage_h2_2025 = cost.price_capex_h2_storage_2025()
            price_invest_bess_2025 = cost.price_capex_bess_2025()
            # print("capex_pv_2025_eur =", price_invest_pv_2025)
            # print("capex_chp_2025_eur =", price_invest_chp_2025)

            price_invest_2025_tot = price_invest_pv_2025 + price_invest_wt_2025 + price_invest_chp_2025 + price_invest_hp_2025 + \
                                    price_invest_storage_th_2025 + price_invest_p2g_2025 + price_invest_storage_h2_2025 \
                                    + price_invest_bess_2025
            # print("price_invest_2025_tot =", price_invest_2025_tot)

            capex_2025_pv = price_invest_2025_tot * (1 / (1 + discount_rate) ** self.stage)
            # print("capex_pv_2025 =", price_invest_2025_tot)
            # capex_pv_2025_eac = price_invest_pv_2025 / ((1-(1/(1+discount_rate)**stage_num))/discount_rate)

            # -------------------------------------------- O-PEX 2025 ----------------------------------------------
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2025_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2025_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2025_jan_mwh,
                             h2_import_jul=h2_blue_import_2025_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2023_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2023_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2023_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2023_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2023_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2025_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2025_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2025_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2025_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2025_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2025 = cost_opex.opex_var_loc_elem_2025()
            opex_fix_loc_elem_2025 = cost_opex.opex_fixed_loc_elem_2025()
            opex_e_net_2025 = cost_opex.opex_e_net_2025()

            # print(opex_var_loc_elem_2025)
            # print('opex_fix_loc_elem_2025 =', opex_fix_loc_elem_2025)
            # print(opex_e_net_2025)

            opex_2025 = opex_var_loc_elem_2025 + opex_fix_loc_elem_2025 + opex_e_net_2025  # for 24 h and 1 year
            # print('opex_2025_total =', opex_2025)

            opex_2025_pv = opex_2025 * (1 / (1 + discount_rate) ** year)
            # print("cost_opex_2025_pv =", opex_2025_pv)
            # opex_2025_annuity = opex_2025 * ((1-(1+discount_rate)**-project_life)/discount_rate)
            # print("cost_opex_2025_annuity =", opex_2025_annuity)

            obj_value_2025_eur_npv += capex_2025_pv + opex_2025_pv
            # print("obj_value_2023 =", obj_value_2023)

            obj_value += obj_value_2025_eur_npv
            # print("obj_value_2025_eur_npv =", obj_value)

            # =============================================== F2 2025 ==============================================
            emission_2025 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2023_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2023_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2025_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2025_jul['gas_gen_mw'])

            emission_chp_2025 = emission_2025.emission_chp_2025()
            # print('emission_chp_2025 =', emission_chp_2025)
            emission_enet_2025 = emission_2025.emission_enet_2025()
            # print('emission_enet_2025 =', emission_enet_2025)
            emission_gas_gen_2025 = emission_2025.emission_gas_gen_2025()
            # print('emission_gas_gen_2025 =', emission_gas_gen_2025)

            obj_value_emission_tCO2 += emission_chp_2025 + emission_enet_2025 + emission_gas_gen_2025
            # print('f2_emission_2025 =', obj_value_emission)

            # ------------------------------------------- Constraints 2025 -----------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            g2025_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                g2025_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            g2025_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                g2025_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Note: This will calculate g1 based on the maximum deviation of the voltage
            # values from the acceptable range [0.90, 1.10].
            g1_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)

                    if violation > 0:
                        g1_jan += violation
                        penalty += 1e6 * violation

            g1_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        g1_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2025 -----------------------------
            g2025_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                g2025_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2025 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2023_jan['demand_mw'].sum() +
                                      power_balance_2025_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2023_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2025_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            g2025_re_share = max(0, g2025_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # -------------------------------------------- penalty_cost -------------------------------------------
            penalty += 10e6 * (max(0, res_tes_th_loss_2025_jan_mwh) + max(0, res_tes_th_loss_2025_jul_mwh) +
                               max(0, res_tes_th_deficit_2025_jan_mwh) + max(0, res_tes_th_deficit_2025_jul_mwh)
                               + max(0, h2_energy_loss_2025_jan_mwh) + max(0, h2_energy_loss_2025_jul_mwh) +
                               max(0, res_line_loss_mw_2025_jan_mwh) + max(0, res_line_loss_mw_2025_jul_mwh))
            # print('Penalty_2025 =', penalty)

        elif self.year == 2026:
            year = 2
            obj_value_2026_eur_npv = 0

            # ======================================= 2026 - January =======================================

            # ************************** CHP **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]
            # print('x_chp_input_mw =', x_chp_mw)
            # print("res_chp_p_mwh =", res_chp_p_mwh)
            # print("res_chp_th_mwh =", res_chp_th_mwh)  # mw/h
            # print("res_chp_gas_import_m3 =", res_chp_gas_import_m3)

            # ************************** HP **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()
            # print("x_hp_input_mw=", x_hp_size)
            # print("res_hp_th_mwh =", res_hp_th_mwh)

            # ************************** Thermal Energy System, Storage Management & Heat Flow *********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)

            # if -ve "producing less than demand - add constraint"
            # if +ve "producing more than demand - added to storage system"

            # -------------------------- 2026 Jan ----------------------------------
            # Thermal management model:
            res_tes_2026_jan = tes_res.th_management_system_2026_jan()
            res_tes_ch4_import_2026_jan_mwh = res_tes_2026_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2026_jan_mwh = res_tes_2026_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2026_jan_mwh = np.abs(res_tes_2026_jan['th_energy_deficit_mwh']).sum()

            # print(res_tes_2026_jan)
            # print('res_tes_ch4_import_2026_jan_mwh =', res_tes_ch4_import_2026_jan_mwh)
            # print('res_tes_th_loss_2026_jan_mwh =', res_tes_th_loss_2026_jan_mwh)
            # print('res_tes_th_deficit_2026_jan_mwh =', res_tes_th_deficit_2026_jan_mwh)

            # -------------------------- 2026 Jul ----------------------------------
            res_tes_2026_jul = tes_res.th_management_system_2026_jul()
            res_tes_ch4_import_2026_jul_mwh = res_tes_2026_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2026_jul_mwh = res_tes_2026_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2026_jul_mwh = np.abs(res_tes_2026_jul['th_energy_deficit_mwh']).sum()

            # print(res_tes_2026_jul)
            # print('res_tes_ch4_import_2026_jul_mwh =', res_tes_ch4_import_2026_jul_mwh)
            # print('res_tes_th_loss_2026_jul_mwh =', res_tes_th_loss_2026_jul_mwh)
            # print('res_tes_th_deficit_2026_jul_mwh =', res_tes_th_deficit_2026_jul_mwh)

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_2026_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_2026_jul['heat_balance'].sum()

            # ================================================ P2G ================================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            # print("GES:")
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)

            # -------------------------- 2026 Jan ----------------------------------
            res_ges_2026_jan = ges_res.h2_management_system_2026_jan()
            h2_blue_import_2026_jan_mwh = np.abs(res_ges_2026_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2026_jan_mwh = res_ges_2026_jan['h2_energy_loss_mwh'].sum()

            # print('res_ges_2026_jan =', res_ges_2026_jan)
            # print(h2_blue_import_2025_jan_mwh)

            # -------------------------- 2026 Jul ----------------------------------
            res_ges_2026_jul = ges_res.h2_management_system_2026_jul()
            h2_blue_import_2026_jul_mwh = np.abs(res_ges_2026_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2026_jul_mwh = res_ges_2026_jul['h2_energy_loss_mwh'].sum()

            # print(res_ges_2026_jul)
            # print(h2_blue_import_2025_jul_mwh)

            # ============================================ Power System ============================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM Jan 2026 -----------------------------------
            res_p_sys_2026_jan = p_sys.power_flow_2026_jan()
            vm_jan = res_p_sys_2026_jan.iloc[:, 6:20]
            power_balance_2026_jan = res_p_sys_2026_jan.iloc[:, 0:6]
            res_line_loss_mw_2026_jan_mwh = res_p_sys_2026_jan['line_loss_mw'].sum()
            # res_bess_power_loss_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_deficit_mwh'].sum()

            # print(power_balance_2026_jan)
            # print("vm_2026_jan =", vm_jan)
            # print('res_bess_power_loss_2026_jan_mwh =', res_bess_power_loss_2026_jan_mwh)
            # print('res_bess_power_deficit_2026_jan_mwh =', res_bess_power_deficit_2026_jan_mwh)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ----------------------------------- POWER SYSTEM July 2026 -----------------------------------
            res_p_sys_2026_jul = p_sys.power_flow_2026_jul()
            vm_jul = res_p_sys_2026_jul.iloc[:, 6:20]
            power_balance_2026_jul = res_p_sys_2026_jul.iloc[:, 0:6]
            res_line_loss_mw_2026_jul_mwh = res_p_sys_2026_jul['line_loss_mw'].sum()

            # print(power_balance_2026_jul)
            # print("vm_2026_jul =", vm_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2026 =========================================
            # --------------------------------------- CAPEX 2026 --------------------------------------
            # NOTE: Change the Capex Function not any parameters of the PRICE function.

            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            capex_tot_2026 = cost_capex.price_capex_2026()
            capex_2026_pv = capex_tot_2026 * (1 / (1 + discount_rate) ** self.stage)
            # capex_2026_pv = 0
            # print("capex_2026_eur =", capex_tot_2026)

            # -------------------------------------------- O-PEX ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul: ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2026_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2026_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2026_jan_mwh,
                             h2_import_jul=h2_blue_import_2026_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2026_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2026_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2026_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2026_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2026_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2026_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2026_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2026_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2026_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2026_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2026 = cost_opex.opex_var_loc_elem_2026()
            opex_fix_loc_elem_2026 = cost_opex.opex_fixed_loc_elem_2026()
            opex_e_net_2026 = cost_opex.opex_e_net_2026()
            # print(opex_var_loc_elem_2026)
            # print('opex_fix_loc_elem_2026 =', opex_fix_loc_elem_2026)
            # print(opex_e_net_2026)

            opex_2026 = opex_var_loc_elem_2026 + opex_fix_loc_elem_2026 + opex_e_net_2026  # for 24 h and 1 year
            # print('opex_2025_total =', opex_2025)

            opex_2026_pv = opex_2026 * (1 / (1 + discount_rate) ** year)

            obj_value_2026_eur_npv += capex_2026_pv + opex_2026_pv

            obj_value += obj_value_2026_eur_npv
            # print("obj_value_2026_eur_npv =", obj_value)

            # ========================================= F2 =========================================
            emission_2026 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2026_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2026_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2026_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2026_jul['gas_gen_mw'])

            emission_chp_2026 = emission_2026.emission_chp_2026()
            emission_enet_2026 = emission_2026.emission_enet_2026()
            emission_gas_gen_2026 = emission_2026.emission_gas_gen_2026()
            # print('emission_chp_2026 =', emission_chp_2026)
            # print('emission_enet_2026 =', emission_enet_2026)
            # print('emission_gas_gen_2026 =', emission_gas_gen_2026)

            obj_value_emission_tCO2 += emission_chp_2026 + emission_enet_2026 + emission_gas_gen_2026
            # print('f2_emission_2026 =', obj_value_emission)

            # ------------------------------------------ Constraints 2026 -----------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2026_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2026_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2026_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2026_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Note: This will calculate g1 based on the maximum deviation of the voltage
            # values from the acceptable range [0.90, 1.10].

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g2_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)

                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g2_jan += violation
                        penalty += 1e6 * violation
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g2_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g2_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2026 -----------------------------
            g2026_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                g2026_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2026 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2026_jan['demand_mw'].sum() +
                                      power_balance_2026_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2026_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2026_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # NOTE: Change gYEAR_re_share
            g2026_re_share = max(0, g2026_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty ----------------------------------------
            penalty += 10e6 * (max(0, res_tes_th_loss_2026_jan_mwh) + max(0, res_tes_th_loss_2026_jul_mwh) +
                               max(0, res_tes_th_deficit_2026_jan_mwh) + max(0, res_tes_th_deficit_2026_jul_mwh)
                               + max(0, h2_energy_loss_2026_jan_mwh) + max(0, h2_energy_loss_2026_jul_mwh) +
                               max(0, res_line_loss_mw_2026_jan_mwh) + max(0, res_line_loss_mw_2026_jul_mwh))
            # print('penalty_2026 =', penalty)

        elif self.year == 2027:
            year = 3
            obj_value_2027_eur_npv = 0

            # ======================================= 2027 - January =======================================
            # ************************** CHP 2027 **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]
            # print('x_chp_input_mw =', x_chp_mw)
            # print("res_chp_p_mwh =", res_chp_p_mwh)
            # print("res_chp_th_mwh =", res_chp_th_mwh)  # mw/h
            # print("res_chp_gas_import_m3 =", res_chp_gas_import_m3)

            # ************************** HP 2027 **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()
            # print("x_hp_input_mw=", x_hp_size)
            # print("res_hp_th_mwh =", res_hp_th_mwh)

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2027 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2027 Jan ----------------------------------
            # Thermal management model:
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jan = tes_res.th_management_system_2027_jan()
            res_tes_ch4_import_2027_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2027_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2027_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # print(res_tes_jan)
            # print('res_tes_ch4_import_2026_jan_mwh =', res_tes_ch4_import_2026_jan_mwh)
            # print('res_tes_th_loss_2026_jan_mwh =', res_tes_th_loss_2026_jan_mwh)
            # print('res_tes_th_deficit_2026_jan_mwh =', res_tes_th_deficit_2026_jan_mwh)
            # -------------------------- 2027 Jul ----------------------------------
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jul = tes_res.th_management_system_2027_jul()
            res_tes_ch4_import_2027_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2027_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2027_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # print(res_tes_2026_jul)
            # print('res_tes_ch4_import_2026_jul_mwh =', res_tes_ch4_import_2026_jul_mwh)
            # print('res_tes_th_loss_2026_jul_mwh =', res_tes_th_loss_2026_jul_mwh)
            # print('res_tes_th_deficit_2026_jul_mwh =', res_tes_th_deficit_2026_jul_mwh)

            # ============================================ P2G 2027 =============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            # print("GES:")
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # -------------------------- 2027 Jan ----------------------------------
            # NOTE: Change the Function "h2_management_system_YEAR_MONTH"
            res_ges_jan = ges_res.h2_management_system_2027_jan()
            h2_blue_import_2027_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2027_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()

            # print('res_ges_2026_jan =', res_ges_2026_jan)
            # print(h2_blue_import_2025_jan_mwh)
            # -------------------------- 2027 Jul ----------------------------------
            # NOTE: Change the Function "h2_management_system_YEAR_MONTH"
            res_ges_jul = ges_res.h2_management_system_2027_jul()
            h2_blue_import_2027_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2027_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()

            # print(res_ges_2026_jul)
            # print(h2_blue_import_2025_jul_mwh)

            # ========================================== Power System 2027 ========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2027 Jan -----------------------------------
            res_p_sys_jan = p_sys.power_flow_2027_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2027_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2027_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()
            # res_bess_power_loss_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_deficit_mwh'].sum()
            # print(power_balance_2027_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2027 Jul -----------------------------------
            res_p_sys_2027_jul = p_sys.power_flow_2027_jul()
            vm_jul = res_p_sys_2027_jul.iloc[:, 6:20]
            power_balance_2027_jul = res_p_sys_2027_jul.iloc[:, 0:6]
            res_line_loss_mw_2027_jul_mwh = res_p_sys_2027_jul['line_loss_mw'].sum()
            # print(power_balance_2027_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2027 =========================================
            # --------------------------------------- CAPEX 2027 --------------------------------------
            # NOTE: Do not change the PRICE function. Change the price_capex_YEAR!
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            capex_tot_2027 = cost_capex.price_capex_2027()
            capex_2027_pv = capex_tot_2027 * (1 / (1 + discount_rate) ** self.stage)
            # print("capex_2027_eur =", capex_tot_2027)
            # print("capex_pv_2025_pv =", capex_2027_pv)

            # -------------------------------------------- O-PEX 2027 ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul: ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2027_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2027_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2027_jan_mwh,
                             h2_import_jul=h2_blue_import_2027_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2027_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2027_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2027_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2027_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2027_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2027_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2027_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2027_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2027_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2027_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2027 = cost_opex.opex_var_loc_elem_2027()
            opex_fix_loc_elem_2027 = cost_opex.opex_fixed_loc_elem_2027()
            opex_e_net_2027 = cost_opex.opex_e_net_2027()
            # print(opex_var_loc_elem_2027)
            # print('opex_fix_loc_elem_2027 =', opex_fix_loc_elem_2027)
            # print(opex_e_net_2027)

            opex_2027 = opex_var_loc_elem_2027 + opex_fix_loc_elem_2027 + opex_e_net_2027  # for 24 h and 1 year
            # print('opex_2025_total =', opex_2025)

            opex_2027_pv = opex_2027 * (1 / (1 + discount_rate) ** year)

            obj_value_2027_eur_npv += capex_2027_pv + opex_2027_pv

            obj_value += obj_value_2027_eur_npv
            # print("obj_value_2027_eur_npv =", obj_value)

            # ========================================= F2 =========================================
            # NOTE" Change power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul
            emission_2027 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2027_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2027_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2027_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2027_jul['gas_gen_mw'])

            emission_chp_2027 = emission_2027.emission_chp_2027()
            emission_enet_2027 = emission_2027.emission_enet_2027()
            emission_gas_gen_2027 = emission_2027.emission_gas_gen_2027()
            # print('emission_chp_2026 =', emission_chp_2026)
            # print('emission_enet_2026 =', emission_enet_2026)
            # print('emission_gas_gen_2026 =', emission_gas_gen_2026)

            obj_value_emission_tCO2 += emission_chp_2027 + emission_enet_2027 + emission_gas_gen_2027
            # print('f2_emission_2027 =', obj_value_emission)

            # ---------------------------------------- Constraints 2027 ------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2027_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2027_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2027_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2027_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Note: This will calculate g1 based on the maximum deviation of the voltage
            # values from the acceptable range [0.90, 1.10].

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g3_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g3_jan += violation
                        penalty += 1e6 * violation
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g3_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g3_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2027 -----------------------------
            g2027_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                g2027_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2027 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2027_jan['demand_mw'].sum() +
                                      power_balance_2027_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2027_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2027_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            g2027_re_share = max(0, g2027_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            penalty += 10e6 * (max(0, res_tes_th_loss_2027_jan_mwh) + max(0, res_tes_th_loss_2027_jul_mwh) +
                               max(0, res_tes_th_deficit_2027_jan_mwh) + max(0, res_tes_th_deficit_2027_jul_mwh)
                               + max(0, h2_energy_loss_2027_jan_mwh) + max(0, h2_energy_loss_2027_jul_mwh) +
                               max(0, res_line_loss_mw_2027_jan_mwh) + max(0, res_line_loss_mw_2027_jul_mwh))
            # print('penalty_2027 =', penalty)

        elif self.year == 2028:

            year = 4
            obj_value_2028_eur_npv = 0

            # ======================================= 2028 - January =======================================
            # ************************** CHP 2028 **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]

            # ************************** HP 2028 **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2027 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint/Penalty"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2027 Jan ----------------------------------
            # Thermal management model:
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jan = tes_res.th_management_system_2028_jan()
            res_tes_ch4_import_2028_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2028_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2028_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # print('res_tes_ch4_import_2028_jan_mwh =', res_tes_ch4_import_2028_jan_mwh)
            # print('res_tes_th_loss_2028_jan_mwh =', res_tes_th_loss_2028_jan_mwh)
            # print('res_tes_th_deficit_2028_jan_mwh =', res_tes_th_deficit_2028_jan_mwh)
            # -------------------------- 2027 Jul ----------------------------------
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jul = tes_res.th_management_system_2028_jul()
            res_tes_ch4_import_2028_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2028_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2028_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # print('res_tes_ch4_import_2028_jul_mwh =', res_tes_ch4_import_2028_jul_mwh)
            # print('res_tes_th_loss_2028_jul_mwh =', res_tes_th_loss_2028_jul_mwh)
            # print('res_tes_th_deficit_2028_jul_mwh =', res_tes_th_deficit_2028_jul_mwh)

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # ============================================= P2G 2028 ==============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # -------------------------- 2028 Jan ----------------------------------
            # NOTE: Change the Function "h2_management_system_YEAR_MONTH"
            res_ges_jan = ges_res.h2_management_system_2028_jan()
            h2_blue_import_2028_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2028_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()
            # print('res_ges_2028_jan =', res_ges_jan)
            # print(h2_blue_import_2028_jan_mwh)
            # -------------------------- 2028 Jul ----------------------------------
            # NOTE: Change the Function "h2_management_system_YEAR_MONTH"
            res_ges_jul = ges_res.h2_management_system_2028_jul()
            h2_blue_import_2028_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2028_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()
            # print(res_ges_jul)
            # print(h2_blue_import_2028_jul_mwh)

            # ========================================== Power System 2028 ========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2028 Jan -----------------------------------
            res_p_sys_jan = p_sys.power_flow_2028_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2028_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2028_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()
            # res_bess_power_loss_2028_jan_mwh = res_p_sys_2028_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2028_jan_mwh = res_p_sys_2028_jan['res_bess_power_deficit_mwh'].sum()

            # print("2028 Jan:")
            # print(power_balance_2028_jan)
            # print("vm_2028_jan =", vm_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2028 Jul -----------------------------------
            res_p_sys_2028_jul = p_sys.power_flow_2028_jul()
            vm_jul = res_p_sys_2028_jul.iloc[:, 6:20]
            power_balance_2028_jul = res_p_sys_2028_jul.iloc[:, 0:6]
            res_line_loss_mw_2028_jul_mwh = res_p_sys_2028_jul['line_loss_mw'].sum()

            # print("2027 July:")
            # print(power_balance_2028_jul)
            # print("vm_2028_jul:")
            # print(vm_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2028 =========================================
            # --------------------------------------- CAPEX 2028 --------------------------------------
            # NOTE: Do not change the PRICE function. Change the price_capex_YEAR!
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            capex_tot_2028 = cost_capex.price_capex_2028()
            capex_2028_pv = capex_tot_2028 * (1 / (1 + discount_rate) ** self.stage)  # PV = Present value
            # capex_2028_pv = 0
            # print("capex_2028_eur =", capex_tot_2028)
            # print("capex_pv_2028_pv =", capex_2028_pv)

            # -------------------------------------------- O-PEX 2028 ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul: ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2028_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2028_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2028_jan_mwh,
                             h2_import_jul=h2_blue_import_2028_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2028_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2028_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2028_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2028_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2028_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2028_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2028_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2028_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2028_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2028_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2028 = cost_opex.opex_var_loc_elem_2028()
            opex_fix_loc_elem_2028 = cost_opex.opex_fixed_loc_elem_2028()
            opex_e_net_2028 = cost_opex.opex_e_net_2028()
            # print(opex_var_loc_elem_2027)
            # print('opex_fix_loc_elem_2027 =', opex_fix_loc_elem_2027)
            # print(opex_e_net_2027)

            opex_2028 = opex_var_loc_elem_2028 + opex_fix_loc_elem_2028 + opex_e_net_2028  # for 24 h and 1 year
            # print('opex_2025_total =', opex_2025)

            opex_2028_pv = opex_2028 * (1 / (1 + discount_rate) ** year)

            obj_value_2028_eur_npv += capex_2028_pv + opex_2028_pv

            obj_value += obj_value_2028_eur_npv
            # print("obj_value_2028_eur_npv =", obj_value_2028_eur_npv)

            # ================================================= F2 =================================================
            # NOTE: Change emission_YEAR, power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul,
            # Change the Functions: emission_chp/enet/gas_gen_YEAR
            emission_2028 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2028_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2028_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2028_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2028_jul['gas_gen_mw'])

            emission_chp_2028 = emission_2028.emission_chp_2028()
            emission_enet_2028 = emission_2028.emission_enet_2028()
            emission_gas_gen_2028 = emission_2028.emission_gas_gen_2028()
            # print('emission_chp_2028 =', emission_chp_2028)
            # print('emission_enet_2028 =', emission_enet_2028)
            # print('emission_gas_gen_2028 =', emission_gas_gen_2028)

            obj_value_emission_tCO2 += emission_chp_2028 + emission_enet_2028 + emission_gas_gen_2028
            # print('f2_emission_tot =', obj_value_emission_tCO2)
            # print('f2_emission_2028 =', emission_chp_2028 + emission_enet_2028 + emission_gas_gen_2028)

            # -------------------------------------------- Constraints ---------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2028_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2028_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2028_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2028_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Note: This will calculate g1 based on the maximum deviation of the voltage
            # values from the acceptable range [0.90, 1.10].

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g4_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g4_jan += violation
                        penalty += 1e6 * violation
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g4_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g4_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2028 -----------------------------
            # NOTE: Change gYEAR_pv_bound, and the range of PV size
            g2028_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                g2028_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2028 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2028_jan['demand_mw'].sum() +
                                      power_balance_2028_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2028_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2028_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # NOTE: Change gYEAR_re_share
            g2028_re_share = max(0, g2028_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            # Change the YEARS
            penalty += 10e6 * (max(0, res_tes_th_loss_2028_jan_mwh) + max(0, res_tes_th_loss_2028_jul_mwh) +
                               max(0, res_tes_th_deficit_2028_jan_mwh) + max(0, res_tes_th_deficit_2028_jul_mwh)
                               + max(0, h2_energy_loss_2028_jan_mwh) + max(0, h2_energy_loss_2028_jul_mwh) +
                               max(0, res_line_loss_mw_2028_jan_mwh) + max(0, res_line_loss_mw_2028_jul_mwh))
            # print('penalty_2028 =', penalty)

        elif self.year == 2029:
            year = 5

            # Change YEAR
            obj_value_2029_eur_npv = 0

            # ======================================= 2029 - January =======================================
            # ************************** CHP **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]

            # ************************** HP **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2029 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2029 Jan ----------------------------------
            # Thermal management model:
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jan = tes_res.th_management_system_2029_jan()
            res_tes_ch4_import_2029_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2029_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2029_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # -------------------------- 2029 Jul ----------------------------------
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jul = tes_res.th_management_system_2029_jul()
            res_tes_ch4_import_2029_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2029_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2029_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # ============================================ P2G =============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            # print("GES:")
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # -------------------------- 2029 Jan ----------------------------------
            # NOTE: Change the Function "h2_management_system_YEAR_MONTH"
            res_ges_jan = ges_res.h2_management_system_2029_jan()
            h2_blue_import_2029_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2029_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()

            # -------------------------- 2029 Jul ----------------------------------
            # NOTE: Change the Function "h2_management_system_YEAR_MONTH"
            res_ges_jul = ges_res.h2_management_system_2029_jul()
            h2_blue_import_2029_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2029_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()

            # ============================================= Power System ===========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2029 Jan -----------------------------------
            res_p_sys_jan = p_sys.power_flow_2029_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2029_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2029_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()

            # res_bess_power_loss_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_deficit_mwh'].sum()

            # print(power_balance_2029_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2029 Jul -----------------------------------
            res_p_sys_2029_jul = p_sys.power_flow_2029_jul()
            vm_jul = res_p_sys_2029_jul.iloc[:, 6:20]
            power_balance_2029_jul = res_p_sys_2029_jul.iloc[:, 0:6]
            res_line_loss_mw_2029_jul_mwh = res_p_sys_2029_jul['line_loss_mw'].sum()

            # print(power_balance_2029_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2029 =========================================
            # --------------------------------------- CAPEX 2029 --------------------------------------
            # NOTE: Do not change the PRICE function. Change the price_capex_YEAR!
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            capex_tot_2029 = cost_capex.price_capex_2029()
            capex_2029_pv = capex_tot_2029 * (1 / (1 + discount_rate) ** self.stage)
            # print("capex_2029_eur =", capex_tot_2029)
            # print("capex_pv_2029_pv =", capex_2029_pv)

            # -------------------------------------------- O-PEX 2029 ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul:
            # ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2029_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2029_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2029_jan_mwh,
                             h2_import_jul=h2_blue_import_2029_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2029_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2029_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2029_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2029_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2029_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2029_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2029_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2029_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2029_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2029_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2029 = cost_opex.opex_var_loc_elem_2029()
            opex_fix_loc_elem_2029 = cost_opex.opex_fixed_loc_elem_2029()
            opex_e_net_2029 = cost_opex.opex_e_net_2029()
            # print(opex_var_loc_elem_2029)
            # print('opex_fix_loc_elem_2029 =', opex_fix_loc_elem_2029)
            # print(opex_e_net_2029)

            opex_2029 = opex_var_loc_elem_2029 + opex_fix_loc_elem_2029 + opex_e_net_2029  # for 24 h and 1 year

            opex_2029_pv = opex_2029 * (1 / (1 + discount_rate) ** year)

            obj_value_2029_eur_npv += capex_2029_pv + opex_2029_pv

            obj_value += obj_value_2029_eur_npv
            # print("obj_value_2029_eur_npv =", obj_value)

            # ========================================= F2 =========================================
            # NOTE" Change power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul
            emission_2029 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2029_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2029_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2029_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2029_jul['gas_gen_mw'])

            emission_chp_2029 = emission_2029.emission_chp_2029()
            emission_enet_2029 = emission_2029.emission_enet_2029()
            emission_gas_gen_2029 = emission_2029.emission_gas_gen_2029()

            obj_value_emission_tCO2 += emission_chp_2029 + emission_enet_2029 + emission_gas_gen_2029
            # print('f2_emission_2029 =', obj_value_emission)

            # ---------------------------------------- Constraints 2029 ------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2029_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2029_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2029_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2029_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g5_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g5_jan += violation
                        penalty += 1e6 * violation

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g5_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g5_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2029 -----------------------------
            g2029_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                # Change: gYEAR_pv_bound -->>>>>>>>>>>>>>>>
                g2029_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2029 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2029_jan['demand_mw'].sum() +
                                      power_balance_2029_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2029_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2029_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # Change: gYEAR_re_share -->>>>>>>>>>>>>>>>
            g2029_re_share = max(0, g2029_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            penalty += 10e6 * (max(0, res_tes_th_loss_2029_jan_mwh) + max(0, res_tes_th_loss_2029_jul_mwh) +
                               max(0, res_tes_th_deficit_2029_jan_mwh) + max(0, res_tes_th_deficit_2029_jul_mwh)
                               + max(0, h2_energy_loss_2029_jan_mwh) + max(0, h2_energy_loss_2029_jul_mwh) +
                               max(0, res_line_loss_mw_2029_jan_mwh) + max(0, res_line_loss_mw_2029_jul_mwh))
            # print('penalty_2029 =', penalty)

        elif self.year == 2030:
            year = 6
            obj_value_2030_eur_npv = 0
            # ======================================= 2030 - January =======================================
            # ************************** CHP 2030 **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]

            # ************************** HP 2030 **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2030 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint/Penalty"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2030 Jan ----------------------------------
            # Thermal management model:
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jan = tes_res.th_management_system_2030_jan()
            res_tes_ch4_import_2030_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2030_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2030_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # -------------------------- 2030 Jul ----------------------------------
            # Note: Change the function: "th_management_system_YEAR_MONTH"
            res_tes_jul = tes_res.th_management_system_2030_jul()
            res_tes_ch4_import_2030_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2030_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2030_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # ============================================= P2G 2030 ==============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # ------------------------------------ 2030 Jan --------------------------------------------
            # ---->>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" ---->>>>>>>>>>>>>>>>>>>>
            res_ges_jan = ges_res.h2_management_system_2030_jan()
            h2_blue_import_2030_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2030_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()

            # ------------------------------------ 2030 Jul --------------------------------------------
            # ---->>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" ---->>>>>>>>>>>>>>>>>>>>
            res_ges_jul = ges_res.h2_management_system_2030_jul()
            h2_blue_import_2030_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2030_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()

            # ========================================== Power System 2030 ========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2030 Jan -----------------------------------
            # ---->>>>>>>>>>> NOTE: Change "power_flow_YEAR_jan" ---->>>>>>>>>>>>>>>>>>>>
            res_p_sys_jan = p_sys.power_flow_2030_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2030_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2030_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()
            # res_bess_power_loss_2030_jan_mwh = res_p_sys_2030_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2030_jan_mwh = res_p_sys_2030_jan['res_bess_power_deficit_mwh'].sum()

            # print("2028 Jan:")
            # print(power_balance_2028_jan)
            # print("vm_2028_jan =", vm_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2030 Jul -----------------------------------
            res_p_sys_2030_jul = p_sys.power_flow_2030_jul()
            vm_jul = res_p_sys_2030_jul.iloc[:, 6:20]
            power_balance_2030_jul = res_p_sys_2030_jul.iloc[:, 0:6]
            res_line_loss_mw_2030_jul_mwh = res_p_sys_2030_jul['line_loss_mw'].sum()

            # print("2027 July:")
            # print(power_balance_2028_jul)
            # print("vm_2028_jul:")
            # print(vm_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2030 =========================================
            # --------------------------------------- CAPEX 2030 --------------------------------------
            # NOTE: Do not change the PRICE function. Change the price_capex_YEAR!
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            # ---->>>>>>>>>>> NOTE: Change "price_capex_YEAR" ---->>>>>>>>>>>>>>>>>>>>
            capex_tot_2030 = cost_capex.price_capex_2030()
            capex_2030_pv = capex_tot_2030 * (1 / (1 + discount_rate) ** self.stage)  # PV = Present value
            # capex_2028_pv = 0
            # print("capex_2028_eur =", capex_tot_2028)
            # print("capex_pv_2028_pv =", capex_2028_pv)

            # -------------------------------------------- O-PEX 2030 ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul:
            # ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2030_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2030_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2030_jan_mwh,
                             h2_import_jul=h2_blue_import_2030_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2030_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2030_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2030_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2030_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2030_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2030_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2030_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2030_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2030_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2030_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2030 = cost_opex.opex_var_loc_elem_2030()
            opex_fix_loc_elem_2030 = cost_opex.opex_fixed_loc_elem_2030()
            opex_e_net_2030 = cost_opex.opex_e_net_2030()
            # print(opex_var_loc_elem_2027)
            # print('opex_fix_loc_elem_2027 =', opex_fix_loc_elem_2027)
            # print(opex_e_net_2027)

            opex_2030 = opex_var_loc_elem_2030 + opex_fix_loc_elem_2030 + opex_e_net_2030  # for 24 h and 1 year
            # print('opex_2025_total =', opex_2025)

            opex_2030_pv = opex_2030 * (1 / (1 + discount_rate) ** year)

            obj_value_2030_eur_npv += capex_2030_pv + opex_2030_pv

            obj_value += obj_value_2030_eur_npv
            # print("obj_value_2028_eur_npv =", obj_value_2028_eur_npv)

            # ================================================= F2 =================================================
            # NOTE: Change emission_YEAR, power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul,
            # Change the Functions: emission_chp/enet/gas_gen_YEAR
            emission_2030 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2030_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2030_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2030_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2030_jul['gas_gen_mw'])

            emission_chp_2030 = emission_2030.emission_chp_2030()
            emission_enet_2030 = emission_2030.emission_enet_2030()
            emission_gas_gen_2030 = emission_2030.emission_gas_gen_2030()
            # print('emission_chp_2028 =', emission_chp_2028)
            # print('emission_enet_2028 =', emission_enet_2028)
            # print('emission_gas_gen_2028 =', emission_gas_gen_2028)

            obj_value_emission_tCO2 += emission_chp_2030 + emission_enet_2030 + emission_gas_gen_2030
            # print('f2_emission_tot =', obj_value_emission_tCO2)
            # print('f2_emission_2028 =', emission_chp_2028 + emission_enet_2028 + emission_gas_gen_2028)

            # ---------------------------------------- Constraints 2030 ------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2030_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2030_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2030_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2030_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g6_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g6_jan += violation
                        penalty += 1e6 * violation

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g6_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g6_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2030 -----------------------------
            # >>>>>>>>>>>>>> NOTE: Change gYEAR_pv_bound, and the range of PV size
            g2030_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                # >> >> >> >> >> >> >> NOTE: Change gYEAR_pv_bound
                g2030_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2030 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2030_jan['demand_mw'].sum() +
                                      power_balance_2030_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2030_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2030_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # >>>>>>>>>>>>>> NOTE: Change gYEAR_re_share
            g2030_re_share = max(0, g2030_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            # Change the YEARS
            penalty += 10e6 * (max(0, res_tes_th_loss_2030_jan_mwh) + max(0, res_tes_th_loss_2030_jul_mwh) +
                               max(0, res_tes_th_deficit_2030_jan_mwh) + max(0, res_tes_th_deficit_2030_jul_mwh)
                               + max(0, h2_energy_loss_2030_jan_mwh) + max(0, h2_energy_loss_2030_jul_mwh) +
                               max(0, res_line_loss_mw_2030_jan_mwh) + max(0, res_line_loss_mw_2030_jul_mwh))
            # print('penalty_2028 =', penalty)

        # =================================================== 2031 =================================================
        if self.year == 2031:
            year = 7

            # ---->>>>>>>>>>>>>> Change: obj_value_YEAR_eur_npv <<<<<<<<<<<<<<<---
            obj_value_2031_eur_npv = 0

            # ======================================= 2031 - January =======================================
            # ************************** CHP **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]

            # ************************** HP **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2031 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2031 Jan ----------------------------------
            # Thermal management model:
            # ---->>>>>>>>>>>>>> Note: Change the function: "th_management_system_YEAR_MONTH" <<<<<<<<<<<<<<<---
            res_tes_jan = tes_res.th_management_system_2031_jan()
            res_tes_ch4_import_2031_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2031_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2031_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # -------------------------- 2031 Jul ----------------------------------
            # ---->>>>>>>>>>>>>> Note: Change the function: "th_management_system_YEAR_MONTH"<<<<<<<<<<<<<<<---
            res_tes_jul = tes_res.th_management_system_2031_jul()
            res_tes_ch4_import_2031_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2031_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2031_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # ============================================ P2G =============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # -------------------------- 2031 Jan ----------------------------------
            # ---->>>>>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" <<<<<<<<<<<<<<<---
            res_ges_jan = ges_res.h2_management_system_2031_jan()
            h2_blue_import_2031_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2031_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()

            # -------------------------- 2031 Jul ----------------------------------
            # --->>>>>>>>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" <<<<<<<<<<<<<<----
            res_ges_jul = ges_res.h2_management_system_2031_jul()
            h2_blue_import_2031_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2031_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()

            # ============================================= Power System ===========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2031 Jan -----------------------------------
            # ----->>>>>> Change: power_flow_YEAR_jan <<<<<<<-----
            res_p_sys_jan = p_sys.power_flow_2031_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2031_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2031_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()

            # res_bess_power_loss_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2026_jan_mwh = res_p_sys_2026_jan['res_bess_power_deficit_mwh'].sum()
            # print(power_balance_2031_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2031 Jul -----------------------------------
            # ----->>>>>> Change: power_flow_YEAR_jul <<<<<<<-----
            res_p_sys_2031_jul = p_sys.power_flow_2031_jul()
            vm_jul = res_p_sys_2031_jul.iloc[:, 6:20]
            power_balance_2031_jul = res_p_sys_2031_jul.iloc[:, 0:6]
            res_line_loss_mw_2031_jul_mwh = res_p_sys_2031_jul['line_loss_mw'].sum()
            # print(power_balance_2031_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2031 =========================================
            # --------------------------------------- CAPEX 2031 --------------------------------------
            # ---->>>>>>> NOTE: Do not change the PRICE function. Change the price_capex_YEAR!<<<<<<<-----
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            capex_tot_2031 = cost_capex.price_capex_2031()
            capex_2031_pv = capex_tot_2031 * (1 / (1 + discount_rate) ** self.stage)
            # print("capex_2031_eur =", capex_tot_2031)
            # print("capex_pv_2031_pv =", capex_2031_pv)

            # -------------------------------------------- O-PEX 2031 ----------------------------------------------
            # ----->>>>>>>>>>>>> NOTE: Change the Opex Function parameters for Jan&Jul: <<<<<<<<<<<<<<-----
            # ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2031_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2031_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2031_jan_mwh,
                             h2_import_jul=h2_blue_import_2031_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2031_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2031_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2031_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2031_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2031_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2031_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2031_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2031_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2031_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2031_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----->>>>>>>> Change:opex_var_loc_elem_YEAR, opex_fixed_loc_elem_2031, opex_e_net_2031 <<<<<<<<-----
            opex_var_loc_elem_2031 = cost_opex.opex_var_loc_elem_2031()
            opex_fix_loc_elem_2031 = cost_opex.opex_fixed_loc_elem_2031()
            opex_e_net_2031 = cost_opex.opex_e_net_2031()
            # print(opex_var_loc_elem_2031)
            # print('opex_fix_loc_elem_2031 =', opex_fix_loc_elem_2031)
            # print(opex_e_net_2031)

            # ----->>>>>>>>>> Change: <<<<<<<<<-----
            opex_2031 = opex_var_loc_elem_2031 + opex_fix_loc_elem_2031 + opex_e_net_2031  # for 24 h and 1 year

            opex_2031_pv = opex_2031 * (1 / (1 + discount_rate) ** year)  # pv = present value

            obj_value_2031_eur_npv += capex_2031_pv + opex_2031_pv

            obj_value += obj_value_2031_eur_npv
            # print("obj_value_2031_eur_npv =", obj_value)

            # ========================================= F2 =========================================
            # NOTE" Change power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul
            emission_2031 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2031_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2031_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2031_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2031_jul['gas_gen_mw'])

            emission_chp_2031 = emission_2031.emission_chp_2031()
            emission_enet_2031 = emission_2031.emission_enet_2031()
            emission_gas_gen_2031 = emission_2031.emission_gas_gen_2031()

            obj_value_emission_tCO2 += emission_chp_2031 + emission_enet_2031 + emission_gas_gen_2031
            # print('f2_emission_2031 =', obj_value_emission)

            # ---------------------------------------- Constraints 2031 ------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2031_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2031_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2031_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2031_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g7_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g7_jan += violation
                        penalty += 1e6 * violation

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g7_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g7_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2031 -----------------------------
            g2031_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                # Change: gYEAR_pv_bound -->>>>>>>>>>>>>>>>
                g2031_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2031 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2031_jan['demand_mw'].sum() +
                                      power_balance_2031_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2031_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2031_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # Change: gYEAR_re_share -->>>>>>>>>>>>>>>>
            g2031_re_share = max(0, g2031_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            penalty += 10e6 * (max(0, res_tes_th_loss_2031_jan_mwh) + max(0, res_tes_th_loss_2031_jul_mwh) +
                               max(0, res_tes_th_deficit_2031_jan_mwh) + max(0, res_tes_th_deficit_2031_jul_mwh)
                               + max(0, h2_energy_loss_2031_jan_mwh) + max(0, h2_energy_loss_2031_jul_mwh) +
                               max(0, res_line_loss_mw_2031_jan_mwh) + max(0, res_line_loss_mw_2031_jul_mwh))
            # print('penalty_2031 =', penalty)

        # =================================================== 2032 =================================================
        elif self.year == 2032:

            year = 8

            # ---->>>>>>>>>>>>>> Change: obj_value_YEAR_eur_npv <<<<<<<<<<<<<<<---
            obj_value_2032_eur_npv = 0

            # ======================================= January 2032 =======================================
            # ************************** CHP 2032 **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]

            # ************************** HP 2032 **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2032 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint/Penalty"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2032 Jan ----------------------------------
            # Thermal management model:
            # ----->>>>>>>>>>> Note: Change the function: "th_management_system_YEAR_MONTH" <<<<<<<<<<<<-----
            res_tes_jan = tes_res.th_management_system_2032_jan()
            res_tes_ch4_import_2032_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2032_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2032_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # -------------------------- 2032 Jul ----------------------------------
            # ----->>>>>>>>>>>Note: Change the function: "th_management_system_YEAR_MONTH"<<<<<<<<<<<<-----
            res_tes_jul = tes_res.th_management_system_2032_jul()
            res_tes_ch4_import_2032_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2032_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2032_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # ============================================= P2G 2032 ==============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # ------------------------------------ 2032 Jan --------------------------------------------
            # ---->>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" ---->>>>>>>>>>>>>>>>>>>>
            res_ges_jan = ges_res.h2_management_system_2032_jan()
            h2_blue_import_2032_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2032_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()

            # ------------------------------------ 2032 Jul --------------------------------------------
            # ---->>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" ---->>>>>>>>>>>>>>>>>>>>
            res_ges_jul = ges_res.h2_management_system_2032_jul()
            h2_blue_import_2032_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2032_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()

            # ========================================== Power System 2032 ========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2032 Jan -----------------------------------
            # ---->>>>>>>>>>> NOTE: Change "power_flow_YEAR_jan" ---->>>>>>>>>>>>>>>>>>>>
            res_p_sys_jan = p_sys.power_flow_2032_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2032_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2032_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()
            # res_bess_power_loss_2032_jan_mwh = res_p_sys_2032_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2032_jan_mwh = res_p_sys_2032_jan['res_bess_power_deficit_mwh'].sum()
            # print(power_balance_2032_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2032 Jul -----------------------------------
            res_p_sys_2032_jul = p_sys.power_flow_2032_jul()
            vm_jul = res_p_sys_2032_jul.iloc[:, 6:20]
            power_balance_2032_jul = res_p_sys_2032_jul.iloc[:, 0:6]
            res_line_loss_mw_2032_jul_mwh = res_p_sys_2032_jul['line_loss_mw'].sum()
            # print(power_balance_2032_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2032 =========================================
            # --------------------------------------- CAPEX 2032 --------------------------------------
            # NOTE: Do not change the PRICE function. Change the price_capex_YEAR!
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            # ---->>>>>>>>>>> NOTE: Change "price_capex_YEAR" ---->>>>>>>>>>>>>>>>>>>>
            capex_tot_2032 = cost_capex.price_capex_2032()
            capex_2032_pv = capex_tot_2032 * (1 / (1 + discount_rate) ** self.stage)  # PV = Present value
            # capex_2032_pv = 0
            # print("capex_2032_eur =", capex_tot_2032)
            # print("capex_pv_2032_pv =", capex_2032_pv)

            # -------------------------------------------- O-PEX 2032 ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul:
            # ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2032_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2032_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2032_jan_mwh,
                             h2_import_jul=h2_blue_import_2032_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2032_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2032_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2032_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2032_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2032_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2032_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2032_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2032_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2032_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2032_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2032 = cost_opex.opex_var_loc_elem_2032()
            opex_fix_loc_elem_2032 = cost_opex.opex_fixed_loc_elem_2032()
            opex_e_net_2032 = cost_opex.opex_e_net_2032()
            # print(opex_var_loc_elem_2032)
            # print('opex_fix_loc_elem_2032 =', opex_fix_loc_elem_2032)
            # print(opex_e_net_2032)

            opex_2032 = opex_var_loc_elem_2032 + opex_fix_loc_elem_2032 + opex_e_net_2032  # for 24 h and 1 year
            # print('opex_2032_total =', opex_2032)

            opex_2032_pv = opex_2032 * (1 / (1 + discount_rate) ** year)

            obj_value_2032_eur_npv += capex_2032_pv + opex_2032_pv

            obj_value += obj_value_2032_eur_npv
            # print("obj_value_2032_eur_npv =", obj_value_2032_eur_npv)

            # ================================================= F2 =================================================
            # NOTE: Change emission_YEAR, power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul,
            # Change the Functions: emission_chp/enet/gas_gen_YEAR
            emission_2032 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2032_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2032_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2032_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2032_jul['gas_gen_mw'])

            emission_chp_2032 = emission_2032.emission_chp_2032()
            emission_enet_2032 = emission_2032.emission_enet_2032()
            emission_gas_gen_2032 = emission_2032.emission_gas_gen_2032()

            obj_value_emission_tCO2 += emission_chp_2032 + emission_enet_2032 + emission_gas_gen_2032
            # print('f2_emission_tot =', obj_value_emission_tCO2)
            # print('f2_emission_2032 =', emission_chp_2032 + emission_enet_2032 + emission_gas_gen_2032)

            # ---------------------------------------- Constraints 2032 ------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2032_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2032_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2032_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2032_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g8_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g8_jan += violation
                        penalty += 1e6 * violation

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g8_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g8_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2032 -----------------------------
            # >>>>>>>>>>>>>> NOTE: Change gYEAR_pv_bound, and the range of PV size
            g2032_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                # >> >> >> >> >> >> >> NOTE: Change gYEAR_pv_bound
                g2032_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2032 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2032_jan['demand_mw'].sum() +
                                      power_balance_2032_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2032_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2032_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # >>>>>>>>>>>>>> NOTE: Change gYEAR_re_share
            g2032_re_share = max(0, g2032_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            # Change the YEARS
            penalty += 10e6 * (max(0, res_tes_th_loss_2032_jan_mwh) + max(0, res_tes_th_loss_2032_jul_mwh) +
                               max(0, res_tes_th_deficit_2032_jan_mwh) + max(0, res_tes_th_deficit_2032_jul_mwh)
                               + max(0, h2_energy_loss_2032_jan_mwh) + max(0, h2_energy_loss_2032_jul_mwh) +
                               max(0, res_line_loss_mw_2032_jan_mwh) + max(0, res_line_loss_mw_2032_jul_mwh))
            # print('penalty_2032 =', penalty)

        # =================================================== 2033 =================================================
        if self.year == 2033:
            year = 9
            # ---->>>>>>>>>>>>>> Change: obj_value_YEAR_eur_npv <<<<<<<<<<<<<<<---
            obj_value_2033_eur_npv = 0

            # ======================================= January 2033 =======================================
            # ************************** CHP 2033 **************************
            chp = CHP(chp_mw=x_chp_mw)
            chp_res = chp.chp_calc()  # [MW/h & m3/hr]
            res_chp_p_mwh = chp_res[0]
            res_chp_th_mwh = chp_res[1]
            res_chp_gas_import_mwh = chp_res[2]

            # ************************** HP 2033 **************************
            hp_res = hp_model(hp_bus=x_hp_bus, hp_mw=x_hp_size)
            res_hp_th_mwh = hp_res.hp()

            # ********************** Thermal Energy System, Storage Management & Heat Flow 2033 ********************
            # Either produce th_energy from CHP or HP - 2025 only CHP - rest years CHP or HP.
            # How to integrate in the TES function? --> we are adding HP in 2026 and check the optimisation results.
            tes_res = TES(chp_th_mwh=res_chp_th_mwh, chp_gas_import_mwh=res_chp_gas_import_mwh,
                          hp_th_mwh=res_hp_th_mwh, storage_th_max_mwh=x_storage_th_size)
            # if -ve "producing less than demand - add constraint/Penalty"
            # if +ve "producing more than demand - added to storage system"
            # -------------------------- 2033 Jan ----------------------------------
            # Thermal management model:
            # ----->>>>>>>>>>> Note: Change the function: "th_management_system_YEAR_MONTH" <<<<<<<<<<<<-----
            res_tes_jan = tes_res.th_management_system_2033_jan()
            res_tes_ch4_import_2033_jan_mwh = res_tes_jan['gas_import_mwh'].sum()
            res_tes_th_loss_2033_jan_mwh = res_tes_jan['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2033_jan_mwh = np.abs(res_tes_jan['th_energy_deficit_mwh']).sum()

            # -------------------------- 2033 Jul ----------------------------------
            # ----->>>>>>>>>>>Note: Change the function: "th_management_system_YEAR_MONTH"<<<<<<<<<<<<-----
            res_tes_jul = tes_res.th_management_system_2033_jul()
            res_tes_ch4_import_2033_jul_mwh = res_tes_jul['gas_import_mwh'].sum()
            res_tes_th_loss_2033_jul_mwh = res_tes_jul['th_energy_loss_mwh'].sum()
            res_tes_th_deficit_2033_jul_mwh = np.abs(res_tes_jul['th_energy_deficit_mwh']).sum()

            # NEW 2024116
            res_tes_th_balance_jan = res_tes_jan['heat_balance'].sum()
            res_tes_th_balance_jul = res_tes_jul['heat_balance'].sum()

            # ============================================= P2G 2033 ==============================================
            p2g_model = P2G(p2g_input_mw=x_p2g_size_mw)
            # h2_production_m3_s = p2g_model.p2g_model()[0]
            # h2_production_m3_hr = p2g_model.p2g_model()[1]
            h2_production_mwh = p2g_model.p2g_model()[2]

            # ============================= H2 Energy System, Storage Management & Hy Flow ========================
            ges_res = HyES(p2g_input_mw=x_p2g_size_mw, h2_production_mwh=h2_production_mwh,
                           storage_h2_max_mwh=x_storage_h2_mwh)
            # ------------------------------------ 2033 Jan --------------------------------------------
            # ---->>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" ---->>>>>>>>>>>>>>>>>>>>
            res_ges_jan = ges_res.h2_management_system_2033_jan()
            h2_blue_import_2033_jan_mwh = np.abs(res_ges_jan['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2033_jan_mwh = res_ges_jan['h2_energy_loss_mwh'].sum()
            # print("Jan 2033")
            # print(res_ges_jan)

            # ------------------------------------ 2033 Jul --------------------------------------------
            # ---->>>>>>>>>>> NOTE: Change the Function "h2_management_system_YEAR_MONTH" ---->>>>>>>>>>>>>>>>>>>>
            res_ges_jul = ges_res.h2_management_system_2033_jul()
            h2_blue_import_2033_jul_mwh = np.abs(res_ges_jul['blue_h2_mwh'].sum())  # Covert to +Ve
            h2_energy_loss_2033_jul_mwh = res_ges_jul['h2_energy_loss_mwh'].sum()
            # print("Jul 2033")
            # print(res_ges_jul)

            # ========================================== Power System 2033 ========================================
            p_sys = power_system(net=net, x=x, x_pv_bus=x_pv_bus, x_pv_mw=x_pv_size,
                                 x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                                 chp_bus=x_chp_bus, chp_p_mw=res_chp_p_mwh,
                                 hp_bus=x_hp_bus, hp_cap_mw=x_hp_size,
                                 p2g_input_mw=x_p2g_size_mw, bess_bus=x_bess_bus, bess_p_mw=x_bess_mw,
                                 x_gen_bus_12=x_gen_bus_12, x_gen_bus_12_mw=x_gen_bus_12_mw,
                                 x_gen_bus_1=x_gen_bus_1, x_gen_bus_1_mw=x_gen_bus_1_mw)

            # ----------------------------------- POWER SYSTEM 2033 Jan -----------------------------------
            # ---->>>>>>>>>>> NOTE: Change "power_flow_YEAR_jan" ---->>>>>>>>>>>>>>>>>>>>
            res_p_sys_jan = p_sys.power_flow_2033_jan()
            vm_jan = res_p_sys_jan.iloc[:, 6:20]
            power_balance_2033_jan = res_p_sys_jan.iloc[:, 0:6]
            res_line_loss_mw_2033_jan_mwh = res_p_sys_jan['line_loss_mw'].sum()
            # res_bess_power_loss_2033_jan_mwh = res_p_sys_2033_jan['res_bess_power_loss_mwh'].sum()
            # res_bess_power_deficit_2033_jan_mwh = res_p_sys_2033_jan['res_bess_power_deficit_mwh'].sum()
            # print(power_balance_2033_jan)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()
            # ----------------------------------- POWER SYSTEM 2033 Jul -----------------------------------
            res_p_sys_2033_jul = p_sys.power_flow_2033_jul()
            vm_jul = res_p_sys_2033_jul.iloc[:, 6:20]
            power_balance_2033_jul = res_p_sys_2033_jul.iloc[:, 0:6]
            res_line_loss_mw_2033_jul_mwh = res_p_sys_2033_jul['line_loss_mw'].sum()
            # print(power_balance_2033_jul)

            p_sys.remove_sgen()
            p_sys.remove_gen()
            p_sys.remove_load()
            p_sys.remove_bess()

            # ========================================= F1: 2033 =========================================
            # --------------------------------------- CAPEX 2033 --------------------------------------
            # NOTE: Do not change the PRICE function. Change the price_capex_YEAR!
            cost_capex = PRICE(stage=self.stage, year=year,
                               x_pv_bus=x_pv_bus, x_pv_size=capex_x_pv_mw,
                               x_wt_bus=x_wt_bus, x_wt_mw=capex_x_wt_mw,
                               x_chp_bus=x_chp_bus, x_chp_mw=capex_x_chp_mw,
                               x_hp_bus=x_hp_bus, x_hp_size=capex_x_hp_mw,
                               x_storage_th_size=capex_x_storage_th_mw,
                               x_p2g_size_mw=capex_x_p2g_mw,
                               x_storage_h2_mwh=capex_x_storage_h2_mwh,
                               x_bess_bus=x_bess_bus, x_bess_mw=capex_x_bess_mw)

            # ---->>>>>>>>>>> NOTE: Change "price_capex_YEAR" ---->>>>>>>>>>>>>>>>>>>>
            capex_tot_2033 = cost_capex.price_capex_2033()
            capex_2033_pv = capex_tot_2033 * (1 / (1 + discount_rate) ** self.stage)  # PV = Present value
            # capex_2033_pv = 0
            # print("capex_2033_eur =", capex_tot_2033)
            # print("capex_pv_2033_pv =", capex_2033_pv)

            # -------------------------------------------- O-PEX 2033 ----------------------------------------------
            # NOTE: Change the Opex Function parameters for Jan&Jul:
            # ch4 import, e_demand, sgen, bess, gas_gen,ext_grid.
            cost_opex = OPEX(stage=self.stage, year=year, net=net,
                             x_pv_bus=x_pv_bus, x_pv_size=x_pv_size,
                             x_wt_bus=x_wt_bus, x_wt_mw=x_wt_mw,
                             x_chp_bus=x_chp_bus, x_chp_mw=x_chp_mw,
                             chp_ch4_import_jan=res_tes_ch4_import_2033_jan_mwh,
                             chp_ch4_import_jul=res_tes_ch4_import_2033_jul_mwh,
                             x_hp_bus=x_hp_bus, x_hp_size=x_hp_size,
                             x_storage_th_size=x_storage_th_size,
                             x_p2g_size_mw=x_p2g_size_mw,
                             h2_import_jan=h2_blue_import_2033_jan_mwh,
                             h2_import_jul=h2_blue_import_2033_jul_mwh,
                             x_storage_h2_mwh=x_storage_h2_mwh,
                             x_bess_bus=x_bess_bus, x_bess_mw=x_bess_mw,
                             demand_e_mwh_jan=power_balance_2033_jan['demand_mw'],
                             sgen_mwh_jan=power_balance_2033_jan['pv_wt_chp_mw'],
                             bess_mwh_jan=power_balance_2033_jan['bess_mw'],
                             gas_gen_mwh_jan=power_balance_2033_jan['gas_gen_mw'],
                             ext_e_mwh_jan=power_balance_2033_jan['ext_grid_mw'],
                             demand_e_mwh_jul=power_balance_2033_jul['demand_mw'],
                             sgen_mwh_jul=power_balance_2033_jul['pv_wt_chp_mw'],
                             bess_mwh_jul=power_balance_2033_jul['bess_mw'],
                             gas_gen_mwh_jul=power_balance_2033_jul['gas_gen_mw'],
                             ext_e_mwh_jul=power_balance_2033_jul['ext_grid_mw'],
                             x_gen_bus_12_mw=x_gen_bus_12_mw,
                             x_gen_bus_1_mw=x_gen_bus_1_mw)

            opex_var_loc_elem_2033 = cost_opex.opex_var_loc_elem_2033()
            opex_fix_loc_elem_2033 = cost_opex.opex_fixed_loc_elem_2033()
            opex_e_net_2033 = cost_opex.opex_e_net_2033()
            # print(opex_var_loc_elem_2033)
            # print('opex_fix_loc_elem_2033 =', opex_fix_loc_elem_2033)
            # print(opex_e_net_2033)

            opex_2033 = opex_var_loc_elem_2033 + opex_fix_loc_elem_2033 + opex_e_net_2033  # for 24 h and 1 year
            # print('opex_2033_total =', opex_2033)

            opex_2033_pv = opex_2033 * (1 / (1 + discount_rate) ** year)

            obj_value_2033_eur_npv += capex_2033_pv + opex_2033_pv

            obj_value += obj_value_2033_eur_npv
            # print("obj_value_2033_eur_npv =", obj_value_2033_eur_npv)

            # ================================================= F2 =================================================
            # NOTE: Change emission_YEAR, power_balance_YEAR_jan, power_balance_YEAR_jan, power_balance_YEAR_jul, &
            # power_balance_YEAR_jul,
            # Change the Functions: emission_chp/enet/gas_gen_YEAR
            emission_2033 = emission_calc(stage=self.stage, year=year,
                                          e_chp_jan=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jan=power_balance_2033_jan['ext_grid_mw'],
                                          e_gas_gen_jan=power_balance_2033_jan['gas_gen_mw'],
                                          e_chp_jul=x_chp_mw * 24,  # CHP MW is fixed for 24 hrs operation
                                          e_net_import_jul=power_balance_2033_jul['ext_grid_mw'],
                                          e_gas_gen_jul=power_balance_2033_jul['gas_gen_mw'])

            emission_chp_2033 = emission_2033.emission_chp_2033()
            emission_enet_2033 = emission_2033.emission_enet_2033()
            emission_gas_gen_2033 = emission_2033.emission_gas_gen_2033()

            obj_value_emission_tCO2 += emission_chp_2033 + emission_enet_2033 + emission_gas_gen_2033
            # print('f2_emission_tot =', obj_value_emission_tCO2)
            # print('f2_emission_2033 =', emission_chp_2033 + emission_enet_2033 + emission_gas_gen_2033)

            # ---------------------------------------- Constraints 2033 ------------------------------------------
            # ----------------------------------- Heat balance -----------------------------------
            # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2033_heat_balance_jan = 0
            violation_heat_balance_mw_jan = max(0, -res_tes_th_balance_jan)
            # print('violation_heat_balance =', violation_heat_balance_mw_jan)
            if violation_heat_balance_mw_jan > 0:
                # --------- Change gYEAR_heat_balance_jan --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2033_heat_balance_jan += violation_heat_balance_mw_jan
                penalty += 1e6 * violation_heat_balance_mw_jan

            # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            g2033_heat_balance_jul = 0
            violation_heat_balance_mw_jul = max(0, -res_tes_th_balance_jul)
            # print('violation_heat_balance =', violation_heat_balance_mw_jul)
            if violation_heat_balance_mw_jul > 0:
                # --------- Change gYEAR_heat_balance_jul --------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                g2033_heat_balance_jul += violation_heat_balance_mw_jul
                penalty += 1e6 * violation_heat_balance_mw_jul

            # ----------------------------------- Power grid -----------------------------------
            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g9_jan = 0
            for idx, row in vm_jan.iterrows():
                for col in vm_jan.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g9_jan += violation
                        penalty += 1e6 * violation

            # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
            g9_jul = 0
            for idx, row in vm_jul.iterrows():
                for col in vm_jul.columns[1:]:
                    val = row[col]
                    violation = max(min_v_drop - val, val - max_v_drop)
                    if violation > 0:
                        # Change: gXXX_XXX -->>>>>>>>>>>>>>>>
                        g9_jul += violation
                        penalty += 1e6 * violation

            # ----------------------------- Constraint for the PV upper bound 2033 -----------------------------
            # >>>>>>>>>>>>>> NOTE: Change gYEAR_pv_bound, and the range of PV size
            g2033_pv_bound = 0
            violation_pv_mw = max(0, 100 < x_pv_size.sum())
            if violation_pv_mw > 0:
                # >> >> >> >> >> >> >> NOTE: Change gYEAR_pv_bound
                g2033_pv_bound += violation_pv_mw
                penalty += 1e6 * violation_pv_mw

            # ----------------------------- Constraint for RE share 2033 -----------------------------
            # NOTE: Change power_balance_YEAR_jan, power_balance_YEAR_jul, Max. RE share
            tot_e_demand_annum_mwh = (power_balance_2033_jan['demand_mw'].sum() +
                                      power_balance_2033_jul['demand_mw'].sum()) / 2 * 365
            tot_re_gen_annum_mwh = (power_balance_2033_jan['pv_wt_chp_mw'].sum() +
                                    power_balance_2033_jul['pv_wt_chp_mw'].sum()) / 2 * 365

            # >>>>>>>>>>>>>> NOTE: Change gYEAR_re_share
            g2033_re_share = max(0, g2033_re_share_max_limit * tot_e_demand_annum_mwh - tot_re_gen_annum_mwh)

            # ---------------------------------------- penalty --------------------------------------
            # Change the YEARS
            penalty += 10e6 * (max(0, res_tes_th_loss_2033_jan_mwh) + max(0, res_tes_th_loss_2033_jul_mwh) +
                               max(0, res_tes_th_deficit_2033_jan_mwh) + max(0, res_tes_th_deficit_2033_jul_mwh)
                               + max(0, h2_energy_loss_2033_jan_mwh) + max(0, h2_energy_loss_2033_jul_mwh) +
                               max(0, res_line_loss_mw_2033_jan_mwh) + max(0, res_line_loss_mw_2033_jul_mwh))
            # print('penalty_2033 =', penalty)

        out["penalty"] = penalty
        out["G"] = [g1_jan, g1_jul, g2025_heat_balance_jan, g2025_heat_balance_jul, g2025_pv_bound, g2025_re_share,
                    g2_jan, g2_jul, g2026_heat_balance_jan, g2026_heat_balance_jul, g2026_pv_bound, g2026_re_share,
                    g3_jan, g3_jul, g2027_heat_balance_jan, g2027_heat_balance_jul, g2027_pv_bound, g2027_re_share,
                    g4_jan, g4_jul, g2028_heat_balance_jan, g2028_heat_balance_jul, g2028_pv_bound, g2028_re_share,
                    g5_jan, g5_jul, g2029_heat_balance_jan, g2029_heat_balance_jul, g2029_pv_bound, g2029_re_share,
                    g6_jan, g6_jul, g2030_heat_balance_jan, g2030_heat_balance_jul, g2030_pv_bound, g2030_re_share,
                    g7_jan, g7_jul, g2031_heat_balance_jan, g2031_heat_balance_jul, g2031_pv_bound, g2031_re_share,
                    g8_jan, g8_jul, g2032_heat_balance_jan, g2032_heat_balance_jul, g2032_pv_bound, g2032_re_share,
                    g9_jan, g9_jul, g2033_heat_balance_jan, g2033_heat_balance_jul, g2033_pv_bound, g2033_re_share,
                    g10_jan, g10_jul, g2034_heat_balance_jan, g2034_heat_balance_jul, g2034_pv_bound, g2034_re_share]
        # out["F"] = [obj_value + penalty, obj_value_emission_tCO2]
        out["F"] = [obj_value, obj_value_emission_tCO2]


from pymoo.algorithms.moo.nsga2 import NSGA2, RankAndCrowdingSurvival
from pymoo.core.mixed import MixedVariableMating, MixedVariableGA, MixedVariableSampling, \
    MixedVariableDuplicateElimination
from pymoo.optimize import minimize
from pymoo.factory import get_termination

# from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.operators.crossover.sbx import SimulatedBinaryCrossover
from pymoo.operators.mutation.pm import PolynomialMutation

# Simulated Binary Crossover (SBX) with a custom eta and probability
crossover = SimulatedBinaryCrossover(prob=0.9, eta=20)
mutation = PolynomialMutation(prob=0.1, eta=20)  # prob is the mutation probability, eta controls mutation spread

stages = {
    1: [2025, 2026, 2027],    # Stage 1
    2: [2028, 2029, 2030],    # Stage 2
    3: [2031, 2032, 2033],    # Stage 3
}
years = list(range(2025, 2034))

gen_size = 100
pop_size = 50

all_X = []
all_F = []
results = []

installed_capacities_per_year_mw = {
    2025: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},  # Initial capacities
    2026: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2027: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2028: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2029: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2030: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2031: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2032: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2033: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2034: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2035: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2036: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2037: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2038: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0}
}

tot_installed_capacities_mw = {
    2025: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},  # Initial capacities
    2026: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2027: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2028: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2029: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2030: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2031: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2032: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2033: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2034: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2035: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2036: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2037: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0},
    2038: {'WT': 0, 'CHP': 0, 'HP': 0, 'TH_Storage': 0, 'P2G': 0, 'H2_Storage': 0, 'BESS': 0, 'Gas_Gen_b12': 0,
           'Gas_Gen_b1': 0}
}

installed_capacities_pv_per_year_mw = {
    2025: {}, 2026: {}, 2027: {}, 2028: {}, 2029: {}, 2030: {}, 2031: {}, 2032: {}, 2033: {}, 2034: {}, 2035: {},
    2036: {}, 2037: {}, 2038: {}
}

# carried_cap_pv_array_mw = np.array([])
cumulative_capacities_pv = {}
carried_cap_pv_array_mw = np.zeros(14)  # Preallocate array for 14 PV capacities
# carried_cap_pv_test_mw = []
# history_F = []
results_df = pd.DataFrame(columns=["Year", "Cost (EUR)", "CO2 (tCO2)"])

for year in years:
    print("----------------- YEAR: ----------------------")
    print('------------------', year, '---------------------')
    print("----------------------------------------------")

    if year == 2025 and 2026 and 2027:
        stage = 1
    elif year == 2028 and 2029 and 2030:
        stage = 2
    elif year == 2031 and 2032 and 2033:
        stage = 3


    # Pass carried capacity for the current year
    carried_capacity = installed_capacities_per_year_mw[year - 1] if year > 2025 else {'WT': 0, 'CHP': 0,
                                                                                       'HP': 0, 'TH_Storage': 0, 'P2G': 0,
                                                                                       'H2_Storage': 0, 'BESS': 0,
                                                                                       'Gas_Gen_b12': 0, 'Gas_Gen_b1': 0
                                                                                       }

    prob = MyProblem(year=year, stage=stage, carried_capacity=carried_capacity, carried_capacity_pv=0,
                     carried_cap_pv_array_mw=carried_cap_pv_array_mw)

    algorithm = MixedVariableGA(pop_size=pop_size,
                                Sampling=MixedVariableSampling(),
                                mating=MixedVariableMating(eliminate_duplicates=MixedVariableDuplicateElimination()),
                                element_duplicates=MixedVariableDuplicateElimination(),
                                survival=RankAndCrowdingSurvival(),
                                crossover=crossover,
                                mutation=mutation,
                                eliminate_duplicates=False
                                )

    termination = get_termination("n_gen", gen_size)

    res = minimize(prob,
                   algorithm,
                   termination,
                   seed=1,
                   # output=MyOutput(),
                   save_history=True,
                   verbose=True)

    # Check the structure of res.X and res.F
    # print(f"res.X for year {year}: {res.X}")
    # print(f"res.F for year {year}: {res.F}")

    # Ensure res.X and res.F are numpy arrays
    # X = np.array([list(r.values()) for r in res.X])
    # X = np.array(res.X)
    # F = np.array(res.F)

    # print(f"Converted X for year {year}: {X}")
    # print(f"Converted F for year {year}: {F}")
    # print(type(X))

    X = res.X
    F = res.F
    Penalty = res.algorithm.pop.get("penalty")[0]
    # # print("Best solutions found: \nX = %s\nF = %s" % (res.X, res.F))
    # print(f"Best solutions found for {year}: \nX = {X}\nF = {F}")   # 06.09.2024
    print("F =", F)

    # Extract F1 and F2 from the optimization history
    # for entry in res.history:
    #     F_ = entry.opt.get("F")  # Get objective values from the population
    #     for f in F_:
    #         history_F.append({"F1": f[0] - Penalty if Penalty < f[0] else f[0], "F2": f[1]})  # Assuming F is 2-dimensional

    # Convert F to a DataFrame and add the year
    year_df = pd.DataFrame(F, columns=["Cost (EUR)", "CO2 (tCO2)"])
    year_df["Year"] = year

    # Sort the DataFrame by "Cost (EUR)" (F1) in descending order
    year_df = year_df.sort_values(by="Cost (EUR)", ascending=False)

    # Append the results to the main DataFrame
    results_df = pd.concat([results_df, year_df], ignore_index=True)
    print(results_df)

    # Choose the best solution for this year # 06.09.2024
    best_idx = np.argmin(F[:, 0])
    best_solution = X[best_idx]  # old: X
    best_objective = F[best_idx]

    print("Best Solution:", best_solution)
    print("Best Objective Value:", best_objective)
    print("Penalty =", Penalty)
    # print("History_F =", history_F)
    # print("Len_history_F", len(history_F))
    print()

    all_X.append(best_solution)
    all_F.append(best_objective)

    # ------------------------------ Update installed capacities for next year ------------------------------
    # ------------- PV -------------
    pv_mw = {key: best_solution[key] for key in best_solution if key in [f'x{i}' for i in range(14, 28)]}

    best_solution_pv_production = list(pv_mw.values())
    # print('best solu PV =', sum(best_solution_pv_production))

    for idx, best_solution_pv in enumerate(best_solution_pv_production):
        installed_capacities_pv_per_year_mw[year][f'PV{idx + 1}'] = best_solution_pv
        carried_cap_pv_array_mw[idx] = installed_capacities_pv_per_year_mw[year][f'PV{idx + 1}']
        cumulative_capacities_pv[year] = carried_cap_pv_array_mw.copy()  # Store a copy to avoid overwriting
    # print('carried_cap_pv_mw =', carried_cap_pv_array_mw)
    # Store each year's cumulative carried PV array
    total_future_capacity_pv = np.sum(list(cumulative_capacities_pv.values()), axis=0)
    # print('total_future_capacity_pv =', total_future_capacity_pv)

    if year != 2025:
        carried_cap_pv_array_mw = total_future_capacity_pv
    # print('carried_cap_pv_mw_sum =', sum(carried_cap_pv_array_mw))

    # -------------------------- WT --------------------------
    best_solution_wt_mw = best_solution['x29']
    carried_cap_wt_mw = carried_capacity['WT']
    # print('best_solution_wt_mw', best_solution_wt_mw)
    # print('carried_cap_wt_mw', carried_cap_wt_mw)
    installed_capacities_per_year_mw[year]['WT'] = best_solution_wt_mw + carried_cap_wt_mw
    tot_installed_capacities_mw[year]['WT'] = best_solution_wt_mw + carried_cap_wt_mw
    # print('tot_installed_capacities_mw[S1]', tot_installed_capacities_mw[year]['WT'])

    # -------------------------- BESS --------------------------
    best_solution_bess_mwh = best_solution['x38']
    carried_cap_bess_mwh = carried_capacity['BESS']
    installed_capacities_per_year_mw[year]['BESS'] = best_solution_bess_mwh + carried_cap_bess_mwh
    tot_installed_capacities_mw[year]['BESS'] = carried_cap_bess_mwh + best_solution_bess_mwh
    # print('installed_capacities_per_year_mw =', installed_capacities_per_year_mw[year]['BESS'])

    # -------------------------- CHP --------------------------
    best_solution_chp_mw = best_solution['x31']
    carried_cap_chp_mw = carried_capacity['CHP']
    # print('best_solution_chp_mw', best_solution_chp_mw)
    # print('carried_cap_chp_mw', carried_cap_chp_mw)
    installed_capacities_per_year_mw[year]['CHP'] = best_solution_chp_mw + carried_cap_chp_mw
    tot_installed_capacities_mw[year]['CHP'] = carried_cap_chp_mw + best_solution_chp_mw

    # -------------------------- HP --------------------------
    best_solution_hp_mw = best_solution['x33']
    carried_cap_hp_mw = carried_capacity['HP']
    installed_capacities_per_year_mw[year]['HP'] = best_solution_hp_mw + carried_cap_hp_mw
    tot_installed_capacities_mw[year]['HP'] = carried_cap_hp_mw + best_solution_hp_mw

    # -------------------------- H2-Storage --------------------------
    best_solution_storage_h2_mw = best_solution['x36']
    carried_cap_storage_h2_mw = carried_capacity['H2_Storage']
    installed_capacities_per_year_mw[year]['H2_Storage'] = best_solution_storage_h2_mw + carried_cap_storage_h2_mw
    tot_installed_capacities_mw[year]['H2_Storage'] = carried_cap_storage_h2_mw + best_solution_storage_h2_mw

    # # # -------------------------- Gas_Gen_b12 --------------------------
    # best_solution_gas_gen12_mw = best_solution['x40']
    # carried_cap_gas_gen12_mw = carried_capacity['Gas_Gen_b12']
    # # NOTE: Not adding best_solution_gas_gen12_mw below, because we expect this to reduce in the future.
    # # Addition gives a wrong representation in the result.
    # installed_capacities_per_year_mw[year]['Gas_Gen_b12'] = best_solution_gas_gen12_mw #+ best_solution_gas_gen12_mw
    # tot_installed_capacities_mw[year]['Gas_Gen_b12'] = carried_cap_gas_gen12_mw #+ best_solution_gas_gen12_mw
    #
    # # # -------------------------- Gas_Gen_b1 --------------------------
    # best_solution_gas_gen1_mw = best_solution['x42']
    # carried_cap_gas_gen1_mw = carried_capacity['Gas_Gen_b1']
    # # NOTE: Not adding best_solution_gas_gen1_mw below, because we expect this to reduce in the future.
    # # Addition gives a wrong representation in the result.
    # installed_capacities_per_year_mw[year]['Gas_Gen_b1'] = best_solution_gas_gen1_mw #+ best_solution_gas_gen12_mw
    # tot_installed_capacities_mw[year]['Gas_Gen_b1'] = carried_cap_gas_gen1_mw #+ best_solution_gas_gen1_mw

    # -------------------------- P2G --------------------------
    best_solution_p2g_mw = best_solution['x35']
    carried_cap_p2g_mw = carried_capacity['P2G']
    installed_capacities_per_year_mw[year]['P2G'] = best_solution_p2g_mw + carried_cap_p2g_mw
    tot_installed_capacities_mw[year]['P2G'] = carried_cap_p2g_mw + best_solution_p2g_mw
    # print("tot_installed_capacities_mw[year]['P2G'] =", tot_installed_capacities_mw[year]['P2G'])

    cost_eur = best_objective[0] - Penalty if Penalty < best_objective[0] else best_objective[0]

    # Installed capacities: Append the results for the current year into the results list
    results.append({
        "Year": year,
        "PV (MW)": sum(best_solution_pv_production),    # taken from total_future_capacity_pv
        # "PV (MW)": sum(installed_capacities_pv_per_year_mw[year].values()),
        "Wind (MW)": best_solution['x29'],
        "CHP (MW)": best_solution['x31'],
        "HP (MW)": best_solution['x33'],
        "TH-Storage (MWh)": best_solution['x34'],
        "P2G (MW)": best_solution['x35'],
        "H2-Storage (MWh)": best_solution['x36'],
        "BESS (MW)": best_solution['x38'],
        "GasG bus12 (MW)": best_solution['x40'],
        "GasG bus1 (MW)": best_solution['x42'],
        "Cost (EUR)": cost_eur,
        "CO2 (tCO2)": best_objective[1]
    })


# Create a DataFrame to display results
df_results = pd.DataFrame(results)
print(df_results)
pd.DataFrame(df_results.to_csv('results/res_FINAL_50-100_20250117.csv', index=False))


# print('pv_capacities_mw =', installed_capacities_pv_per_year_mw)
# print('installed_capacities_mw =', tot_installed_capacities_mw)
print('all_X =', all_X)
all_x_df = pd.DataFrame(all_X)
pd.DataFrame(all_x_df.to_csv('results/res_all_x_50-100_20250117.csv', index=False))

# Convert to a DataFrame
# df_history_data_F = pd.DataFrame(history_F)
# print(df_history_data_F)
# df_history_data_F.to_csv("results/res_history_F_30-60_20250115.csv", index=False)
results_df.to_csv("results/res_pareto_front_50-100_20250117.csv", index=False)

end_time = time.time()  # End the simulation
elapsed_time = end_time - start_time
print(f"Simulation ran for {elapsed_time:.2f} seconds")