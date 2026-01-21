
import pandas as pd

pd.set_option('display.max_columns', None)

# Time series
# heat_demand_test = pd.read_csv("th_load_38_household_dec15_test.csv")
heat_demand_jan = pd.read_csv("th_load_38_household_dec15.csv")
heat_demand_jul = pd.read_csv("th_load_38_household_jul15.csv")
# print(heat_demand_jan)


class CHP:
    def __init__(self, chp_mw, **kwargs):
        # self.gas_input = gas_input
        self.chp_mw = chp_mw
        # self.storage_th_max_mwh = storage_th_max_mwh

    def chp_calc(self):

        # p_e = self.gas_input*0.35        # electrical energy; unit: [MW/h]
        # p_q = self.gas_input*0.50        # heat energy; unit: [MW/h]

        p_e_mw = self.chp_mw
        p_th_mw = self.chp_mw*(1/0.7)    # A CHP system with a 0.7 power-to-heat ratio

        # print()
        # print(p_e_mw)
        # print(p_th_mw)

        # gas_import = based on the demand

        # loss_line = 0.0339 * 2       # 33.9 kWh loss per km distance == 0.0339 MWh/km & 2 km is the
        # max distance from CHP to demand side

        gas_import_mw = (p_e_mw + p_th_mw) / 0.85   # chp_system_efficiency = 0.85
        # print(gas_import_mw)
        gas_import_m3 = gas_import_mw/0.01055    # Energy content of natural gas = 10.55 kWh/m³ = 0.01055 MWh/m3 [m3/hr]
        # print("CHP:", gas_import_m3)
        # print()

        return p_e_mw, p_th_mw, gas_import_mw


""" Made new file called - tes_dhnet_lp_storage_20240723 """

"""
    def dh_network(self):

        # Pipe loss coefficients - based on the paper from Finland
        k1 = 0.2331  # [W/mK] - watt per meter Kelvin
        k2 = 0.0066  # W/mK
        t_supply = 105  # [degree centigrade]
        t_soil = 5  # degree centigrade
        t_return = 50  # degree centigrade

        # Heat loss calculation
        heat_loss_sending_side = (k1 - k2) * (t_supply - t_soil) + (k2 * (t_supply - t_return))  # [W/meter]
        heat_loss_return_side = (k1 - k2) * (t_return - t_soil) - (k2 * (t_supply - t_return))  # [W/meter]

        heat_loss_w_m = (heat_loss_sending_side + heat_loss_return_side)
        heat_loss_mw_m = (heat_loss_sending_side + heat_loss_return_side) * 1e-6  # [W/meter] --> [MW/meter]

        # print("loss_w =", heat_loss_w_m)
        # print("loss_mw =", heat_loss_mw_m)
        # heat_loss_pipe_bend = 0.025  # [%] for 90 degree bend of pipes

        length_pipe_line_m = 4800     # [m] Residential block at bus 6 - designed in PowerPoint, named Journal

        heat_loss_mw = heat_loss_mw_m * length_pipe_line_m  # [MW]

        # Heat storage:

        # print("DH Net:")
        # print("heat_loss_mw =", heat_loss_mw)

        return heat_loss_mw

    def linepack(self):
        cp = 0.000001162    # [ MWh/kg·K]
        v = 43.23           # [m3] -> converted from 2560m 23.06m3 to 4800m lines; paper: Kuosa, Finland
        rho = 1000          # [kg/m3]
        dTemp = 15          # [K] an approximation

        dhn_linepack_mwh = cp * (v/2) * rho * dTemp     # [MW/h]

        return dhn_linepack_mwh     # [MW/h]

    def heat_storage(self):     # with management
        # print("heat storage")

        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_res = self.chp_calc()
        chp_th_mwh = chp_res[1]
        dhn_linepack_th_mwh = self.linepack()
        # dhn_linepack_th_mwh = heat_flow.linepack()
        heat_loss_mwh = self.dh_network()

        storage_th_init = dhn_linepack_th_mwh

        for load_idx, load_row in heat_demand_jan.iterrows():
            # storage_th_mwh = (storage_th_init+dhn_linepack_th_mwh) + (chp_th_mwh*eta_storage_ch) - \
            #                 ((load_row['th_load_38_household']+heat_loss_mwh)/eta_storage_dis)
            # # storage_th_mwh = (storage_th_init) + (chp_th_mwh * eta_storage_ch) - \
            # #                  ((load_row['SFH24']) * eta_storage_dis)
            #
            # result = {
            #     'tes_init_mwh': storage_th_init+dhn_linepack_th_mwh,  # fixed at the beginning of the time step
            #     'chp_th_mwh': chp_th_mwh,
            #     'demand_th_mwh': load_row['th_load_38_household']+heat_loss_mwh,
            #     'storage_th_mwh': storage_th_mwh
            #     # 'heat_flow_balance_mw': heat_flow_balance_mw  # heat P balance at each hour (t) [mw]
            # }
            # results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            #
            # # Update the storage_th_init for the next iteration
            # storage_th_init = storage_th_mwh
            storage_th_mwh = storage_th_init

            # Update the maximum storage capacity if current storage is greater
            if storage_th_mwh >= self.storage_th_max_mwh: #+ dhn_linepack_th_mwh:
                # storage_th_init = self.storage_th_max_mwh

                # print('tot storage =', storage_th_init + dhn_linepack_th_mwh)
                # print('demand =', load_row['th_load_38_household'] + heat_loss_mwh)
                # print('storage_t =', (storage_th_init + dhn_linepack_th_mwh) - \
                #                  ((load_row['th_load_38_household'] + heat_loss_mwh) / eta_storage_dis))
                # print()

                storage_th_mwh = storage_th_mwh - \
                                 ((load_row['th_load_38_household'] + heat_loss_mwh) / eta_storage_dis)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,
                    'demand_th_mwh': load_row['th_load_38_household'] + heat_loss_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_m3': 0  # [mwh]
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_th_init = storage_th_mwh
            else:

                # print("storage_init =", storage_th_init)
                # print('tot storage =', storage_th_init + dhn_linepack_th_mwh)
                # print('demand =', load_row['th_load_38_household'] + heat_loss_mwh)
                # print('storage_t =', (storage_th_init + dhn_linepack_th_mwh) - \
                #       ((load_row['th_load_38_household'] + heat_loss_mwh) / eta_storage_dis))
                # print()

                storage_th_mwh = (storage_th_init) + (chp_th_mwh * eta_storage_ch) - \
                                 ((load_row['th_load_38_household'] + heat_loss_mwh) / eta_storage_dis)
                result = {
                    'tes_init_mwh': storage_th_init, #+ dhn_linepack_th_mwh,  # fixed at the beginning of the time step
                    'chp_th_mwh': chp_th_mwh,
                    'demand_th_mwh': load_row['th_load_38_household'] + heat_loss_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_m3': self.chp_calc()[2]  # [mwh]
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_th_init = storage_th_mwh
            # storage_th_init = storage_th_mwh

        return results_tes_mwh

    # def heat_power_flow(self):
    #
    #     results = pd.DataFrame()
    #
    #     chp_res = self.chp_calc()
    #     chp_th = chp_res[1]
    #
    #     heat_loss_mw = self.dh_network()
    #
    #     for load_idx, load_row in heat_demand_jan.iterrows():
    #         # print(load_idx)
    #         # print(load_row['th_load_38_household'])
    #
    #         ####################################add line pack
    #         ##################################add heat storage
    #
    #         heat_production_chp_mw = chp_th
    #         heat_flow_balance_mw = (load_row['th_load_38_household']+heat_loss_mw) - chp_th
    #         # if -ve "producing more than demand - can be stored"
    #         # if +ve "below heat demand - need external heat support"
    #
    #         # print(heat_balance)
    #         result = {
    #             'heat_production_chp_mw': heat_production_chp_mw,  # heat production at each hour (t) [mw/h]
    #             'heat_flow_balance_mw': heat_flow_balance_mw  # heat P balance at each hour (t) [mw]
    #         }
    #         results = results.append(result, ignore_index=True)
    #
    #     return results

"""
# ************************************* Model Testing *************************************
# heat_flow = CHP(chp_mw=0.6, storage_th_max_mwh=1)
# chp_res = heat_flow.chp_calc()
# chp_th_mwh = chp_res[1]
# # print('chp_th_mwh =', chp_th_mwh)
# print(heat_flow.heat_storage())