# +-----------------------------------+
# |          Heat Pump Model          |
# +-----------------------------------+

import pandas as pd

# Time series
heat_demand_jan = pd.read_csv("th_load_38_household_dec15.csv")
heat_demand_jul = pd.read_csv("th_load_38_household_jul15.csv")
# print(heat_demand_jan)

# Fixed parameters:
a = 2.852525
b = 2.868282
c = -0.017015
d = -0.037951
pl = 0.6
dTemp = 105 - 50

# COP:
cop = a + b*pl + c*dTemp + d*pl*dTemp
# print("cop =", cop)      # COP = 2.78


class hp_model:
    def __init__(self, hp_bus, hp_mw, **kwargs):
        self.hp_bus = hp_bus
        self.hp_mw = hp_mw

    def hp(self):

        hp_th_mw = cop * self.hp_mw  # cop =
        # print(hp_th_mw)

        return hp_th_mw


""" moved to file name tes_dhnet_lp_storage_20240723 """

#     def dh_network(self):
#
#         # Pipe loss coefficients - based on the paper from Finland
#         k1 = 0.2331  # [W/mK] - watt per meter Kelvin
#         k2 = 0.0066  # W/mK
#         t_supply = 105  # [degree centigrade]
#         t_soil = 5  # degree centigrade
#         t_return = 50  # degree centigrade
#
#         # Heat loss calculation
#         heat_loss_sending_side = (k1 - k2) * (t_supply - t_soil) + (k2 * (t_supply - t_return))  # [W/meter]
#         heat_loss_return_side = (k1 - k2) * (t_return - t_soil) - (k2 * (t_supply - t_return))  # [W/meter]
#
#         heat_loss_w_m = (heat_loss_sending_side + heat_loss_return_side)
#         heat_loss_mw_m = (heat_loss_sending_side + heat_loss_return_side) * 1e-6  # [W/meter] --> [MW/meter]
#
#         # print("loss_w =", heat_loss_w_m)
#         # print("loss_mw =", heat_loss_mw_m)
#         # heat_loss_pipe_bend = 0.025  # [%] for 90 degree bend of pipes
#
#         length_pipe_line_m = 4800     # [m] Residential block at bus 6 - designed in PowerPoint, named Journal
#
#         heat_loss_mw = heat_loss_mw_m * length_pipe_line_m  # [MW]
#
#         # Heat storage:
#
#         # print("DH Net:")
#         # print("heat_loss_mw =", heat_loss_mw)
#
#         return heat_loss_mw
#
#     def heat_power_flow(self):
#
#         results = pd.DataFrame()
#
#         hp_th_mw_res = self.hp()
#
#         heat_loss_mw = self.dh_network()
#
#         for load_idx, load_row in heat_demand_jan.iterrows():
#
#             heat_production_hp_mw = hp_th_mw_res
#             heat_flow_balance_hp_mw = (load_row['th_load_38_household'] + heat_loss_mw) - hp_th_mw_res
#
#             result = {
#                 'heat_production_hp_mw': heat_production_hp_mw,  # heat production at each hour (t) [mw/h]
#                 'heat_flow_balance_mw': heat_flow_balance_hp_mw  # heat P balance at each hour (t) [mw/h]
#             }
#             results = results.append(result, ignore_index=True)
#
#         return results

# ****************** Model Test ********************
# hp = hp_model(hp_bus=1, hp_mw=0.5096834789351485)
# print(hp.hp())