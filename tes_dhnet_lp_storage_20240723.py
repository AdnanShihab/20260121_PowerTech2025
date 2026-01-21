import pandas as pd

pd.set_option('display.max_columns', None)

# --------------------------------- Time series ---------------------------------
# --------------------------------- 2025 ---------------------------------
# heat_demand_test = pd.read_csv("th_load_38_household_dec15_test.csv")
heat_demand_2025_jan = pd.read_csv("th_load_38_household_dec15.csv")
heat_demand_2025_jul = pd.read_csv("th_load_38_household_jul15.csv")
# print(heat_demand_2025_jan)
# --------------------------------- 2026 ---------------------------------
heat_demand_2026_jan = heat_demand_2025_jan*(1 - 0.0094)    # reduction of heat demand 0.94% from 2025
heat_demand_2026_jul = heat_demand_2025_jul*(1 - 0.0094)    # reduction of heat demand 0.94% from 2025
# --------------------------------- 2027 ---------------------------------
heat_demand_2027_jan = heat_demand_2026_jan*(1 - 0.0095)    # reduction of heat demand 0.95% from 2026
heat_demand_2027_jul = heat_demand_2026_jul*(1 - 0.0095)    # reduction of heat demand 0.95% from 2026
# --------------------------------- 2028 ---------------------------------
heat_demand_2028_jan = heat_demand_2027_jan*(1 - 0.0096)    # reduction of heat demand 0.96% from 2027
heat_demand_2028_jul = heat_demand_2027_jul*(1 - 0.0096)    # reduction of heat demand 0.96% from 2027
# --------------------------------- 2029 ---------------------------------
heat_demand_2029_jan = heat_demand_2028_jan*(1 - 0.0109)    # reduction of heat demand 1.09% from 2028
heat_demand_2029_jul = heat_demand_2028_jul*(1 - 0.0109)    # reduction of heat demand 1.09% from 2028
# --------------------------------- 2030 ---------------------------------
heat_demand_2030_jan = heat_demand_2029_jan*(1 - 0.0)    # reduction of heat demand 0% from 2029
heat_demand_2030_jul = heat_demand_2029_jul*(1 - 0.0)    # reduction of heat demand 0% from 2029
# --------------------------------- 2031 ---------------------------------
heat_demand_2031_jan = heat_demand_2030_jan*(1 - 0.0115)    # reduction of heat demand 0% from 2030
heat_demand_2031_jul = heat_demand_2030_jul*(1 - 0.0115)    # reduction of heat demand 0% from 2030
# --------------------------------- 2032 ---------------------------------
heat_demand_2032_jan = heat_demand_2031_jan*(1 - 0.0117)    # reduction of heat demand 0% from 2031
heat_demand_2032_jul = heat_demand_2031_jul*(1 - 0.0117)    # reduction of heat demand 0% from 2031
# --------------------------------- 2033 ---------------------------------
heat_demand_2033_jan = heat_demand_2032_jan*(1 - 0.0118)    # reduction of heat demand 0% from 2032
heat_demand_2033_jul = heat_demand_2032_jul*(1 - 0.0118)    # reduction of heat demand 0% from 2032
# --------------------------------- 2034 ---------------------------------
heat_demand_2034_jan = heat_demand_2033_jan*(1 - 0.0119)    # reduction of heat demand 0% from 2033
heat_demand_2034_jul = heat_demand_2033_jul*(1 - 0.0116)    # reduction of heat demand 0% from 2033

# print(heat_demand_2027_jan['th_load_38_household'])
# print(heat_demand_2027_jul['th_load_38_household'])


class TES:
    def __init__(self, chp_th_mwh, chp_gas_import_mwh, hp_th_mwh, storage_th_max_mwh, **kwargs):
        # self.gas_input = gas_input
        self.chp_th_mwh = chp_th_mwh
        self.chp_gas_import_mwh = chp_gas_import_mwh
        self.hp_th_mwh = hp_th_mwh
        self.storage_th_max_mwh = storage_th_max_mwh

        # print(self.chp_th_mwh)
        # print(self.chp_gas_import_mwh)
        # print(self.hp_th_mwh)
        # print(self.storage_th_max_mwh)

    def dh_network(self):   # fixed output based on the parameters and pipe-line total length

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

    def linepack(self):     # fixed output based on the pipe-line total length
        cp = 0.000001162    # [ MWh/kg·K]
        v = 43.23           # [m3] -> converted from 2560m 23.06m3 to 4800m lines; paper: Kuosa, Finland
        rho = 1000          # [kg/m3]
        dTemp = 15          # [K] an approximation

        dhn_linepack_mwh = cp * (v/2) * rho * dTemp     # [MW/h]

        return dhn_linepack_mwh     # [MW/h]

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2025 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # def th_management_system_2025_jan(self):
    #     results_tes_mwh = pd.DataFrame()
    #
    #     eta_storage_ch = 0.88
    #     eta_storage_dis = 0.88
    #
    #     chp_th_mwh = self.chp_th_mwh
    #     hp_th_mwh = self.hp_th_mwh
    #
    #     chp_gas_import_mwh = self.chp_gas_import_mwh
    #
    #     storage_line_pack = self.linepack()
    #     # print("line_pack_mwh =", storage_line_pack)
    #     #
    #     # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)
    #     # print()
    #
    #     storage_th_init = storage_line_pack
    #
    #     for load_idx, load_row in heat_demand_2025_jan.iterrows():
    #         # print("idx =", load_idx)
    #
    #         demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
    #         # print("demand_th_jan_mwh =", demand_th_jan_mwh)
    #
    #         heat_production_mwh = chp_th_mwh + hp_th_mwh
    #         # print("heat_production =", heat_production_mwh)
    #
    #         storage_th_mwh = storage_th_init
    #         # print("storage_init =", storage_th_mwh)
    #         # storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - demand_th_jan_mwh / eta_storage_dis
    #
    #         # storage management
    #         if storage_th_mwh > demand_th_jan_mwh:
    #             # discharge:
    #             storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
    #             # Note: here I am only using discharging equation, because the storage can only be discharged here.
    #
    #             # Control storage not to exceed the limit.
    #             # Note: since discharging, need to prevent storage to be negative.
    #             if storage_th_mwh < 0:
    #                 storage_th_mwh = 0
    #
    #             result = {
    #                 'tes_init_mwh': storage_th_init,
    #                 'chp_th_mwh': 0,        # only taking thermal power from storage, so CHP is not working
    #                 'hp_th_mwh': hp_th_mwh,
    #                 'demand_th_mwh': demand_th_jan_mwh,
    #                 'storage_th_mwh': storage_th_mwh,
    #                 'gas_import_mwh': 0,     # only taking thermal power from storage, so CHP is not working
    #                 'th_energy_loss_mwh': 0
    #             }
    #             results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
    #             # print()
    #
    #         else:
    #             # print()
    #             # print("storage charging")
    #             # charging
    #             storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
    #                              demand_th_jan_mwh / eta_storage_dis
    #             # Note: here I am adding the charging & discharging the same equation,
    #             # because the storage can charge and at the same time
    #             # it needs to discharge for the respected demand
    #
    #             # print("charge mwh =", storage_th_mwh)
    #
    #             # Control storage not to exceed the limit
    #             if storage_th_mwh > self.storage_th_max_mwh:
    #                 th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
    #                 # print("th_energy_loss_mwh =", th_energy_loss_mwh)
    #                 storage_th_mwh = self.storage_th_max_mwh
    #                 # print(storage_th_mwh)
    #             else:
    #                 th_energy_loss_mwh = 0
    #
    #             result = {
    #                 'tes_init_mwh': storage_th_init,
    #                 'chp_th_mwh': chp_th_mwh,
    #                 'hp_th_mwh': hp_th_mwh,
    #                 'demand_th_mwh': demand_th_jan_mwh,
    #                 'storage_th_mwh': storage_th_mwh,
    #                 'gas_import_mwh': chp_gas_import_mwh, #+ (gas_import_mwh / 0.01055)
    #                 'th_energy_loss_mwh': th_energy_loss_mwh
    #             }
    #             results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
    #             # print()
    #
    #         storage_th_init = storage_th_mwh
    #     # print("th_storage_mwh =", storage_th_init)
    #     return results_tes_mwh

    def th_management_system_2025_jan_update(self):
        # NOTE: Do not change the order of the parameters,
        # i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2025_jan.iterrows():

            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand_th_jan_mwh =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:      # Discharge
                # print('discharging')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,        # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,     # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,    # no heat is produced, so not needed
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            else:   # the-storage charging
                # print('Charging')
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # print("storage_th_mwh =", storage_th_mwh)
                # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:
                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th-generation is less than th-demand

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)

                    storage_th_mwh = 0  # Storage cannot be -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh, #+ (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # --------------------------------------- 2025 - July -----------------------------------------
    # def TES_2025_jul(self):  # heat storage management with heat generator
    #     results_tes_mwh = pd.DataFrame()
    #
    #     eta_storage_ch = 0.88
    #     eta_storage_dis = 0.88
    #
    #     chp_th_mwh = self.chp_th_mwh
    #     hp_th_mwh = self.hp_th_mwh
    #
    #     chp_gas_import_mwh = self.chp_gas_import_mwh
    #
    #     storage_line_pack = self.linepack()
    #     # print("line_pack_mwh =", storage_line_pack)
    #     #
    #     # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)
    #     # print()
    #
    #     storage_th_init = storage_line_pack
    #
    #     for load_idx, load_row in heat_demand_2025_jul.iterrows():
    #         # print("idx =", load_idx)
    #
    #         demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()
    #         # print("demand_th_jul_mwh =", demand_th_jul_mwh)
    #
    #         heat_production_mwh = chp_th_mwh + hp_th_mwh
    #         # print("heat_production =", heat_production_mwh)
    #
    #         storage_th_mwh = storage_th_init
    #         # print("storage_init =", storage_th_mwh)
    #         # storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - demand_th_jan_mwh / eta_storage_dis
    #
    #         # storage management
    #         if storage_th_mwh > demand_th_jul_mwh:
    #             # discharge:
    #             storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
    #             # Note: here I am only using discharging equation, because the storage can only be discharged here.
    #
    #             # Control storage not to exceed the limit.
    #             # Note: since discharging, need to prevent storage to be negative.
    #             if storage_th_mwh < 0:
    #                 storage_th_mwh = 0
    #
    #             result = {
    #                 'tes_init_mwh': storage_th_init,
    #                 'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
    #                 'hp_th_mwh': 0,
    #                 'demand_th_mwh': demand_th_jul_mwh,
    #                 'storage_th_mwh': storage_th_mwh,
    #                 'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
    #                 'th_energy_loss_mwh': 0
    #             }
    #             results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
    #             # print()
    #
    #         else:
    #             # print()
    #             # print("storage charging")
    #             # charging
    #             storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
    #                              demand_th_jul_mwh / eta_storage_dis
    #             # Note: here I am adding the charging & discharging the same equation,
    #             # because the storage can charge and at the same time
    #             # it needs to discharge for the respected demand
    #
    #             # print("charge mwh =", storage_th_mwh)
    #
    #             # Control storage not to exceed the limit
    #             if storage_th_mwh > self.storage_th_max_mwh:
    #                 th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
    #                 # print("th_energy_loss_mwh =", th_energy_loss_mwh)
    #                 storage_th_mwh = self.storage_th_max_mwh
    #                 # print(storage_th_mwh)
    #             else:
    #                 th_energy_loss_mwh = 0
    #
    #             result = {
    #                 'tes_init_mwh': storage_th_init,
    #                 'chp_th_mwh': chp_th_mwh,
    #                 'hp_th_mwh': hp_th_mwh,
    #                 'demand_th_mwh': demand_th_jul_mwh,
    #                 'storage_th_mwh': storage_th_mwh,
    #                 'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
    #                 'th_energy_loss_mwh': th_energy_loss_mwh
    #             }
    #             results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
    #             # print()
    #
    #         storage_th_init = storage_th_mwh
    #     # print("th_storage_mwh =", storage_th_init)
    #     return results_tes_mwh

    def th_management_system_2025_jul_update(self):  # heat storage management with heat generator
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh
        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2025_jul.iterrows():
            # print("idx =", load_idx)

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand_th_jul_mwh =", demand_th_jul_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:      # discharge:

                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.

                # Control storage not to exceed the limit.
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            else:       # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge and at the same time it needs to discharge for the respected demand.

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:  # and storage_th_mwh > 0:
                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)

                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:       # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2026 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    def th_management_system_2026_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)
        # print()

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2026_jan.iterrows():
            # print(load_idx)

            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)
            # print("CHP =", chp_th_mwh)
            # print("HP =", hp_th_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:   # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:   # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            else:   # charging
                # print("storage charging")

                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:        # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:       # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2026 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    def th_management_system_2026_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2026_jul.iterrows():
            # print(load_idx)

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:   # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:   # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            else:   # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:        # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:       # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2027 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH
    def th_management_system_2027_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2027_jan.iterrows():
            # print(load_idx)

            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            else:  # charging
                # print("storage charging")

                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2027 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH
    def th_management_system_2027_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2027_jul.iterrows():
            # print(load_idx)

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2028 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for loop
    def th_management_system_2028_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2028_jan.iterrows():
            # print(load_idx)

            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            else:  # charging
                # print("storage charging")

                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2028 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop
    def th_management_system_2028_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2028_jul.iterrows():
            # print(load_idx)

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2029 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for loop
    def th_management_system_2029_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2029_jan.iterrows():
            # print(load_idx)

            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            else:  # charging
                # print("storage charging")

                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2029 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop
    def th_management_system_2029_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        for load_idx, load_row in heat_demand_2029_jul.iterrows():
            # print(load_idx)

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2030 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
    def th_management_system_2030_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2030_jan.iterrows():

            # NOTE: No change needed --->>>>>
            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0
                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            # NOTE: No more change needed --->>>>>
            else:  # charging
                # print("storage charging")
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:
                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)
                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)
                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)
                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2030 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop --->>>>>>>>>>>>>>>
    def th_management_system_2030_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2030_jul.iterrows():

            # NOTE: No more change needed --->>>>>

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            # NOTE: No more change needed --->>>>>
            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2031 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
    def th_management_system_2031_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2031_jan.iterrows():

            # NOTE: No change needed --->>>>>
            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0
                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            # NOTE: No more change needed --->>>>>
            else:  # charging
                # print("storage charging")
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:
                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)
                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)
                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)
                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2031 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop --->>>>>>>>>>>>>>>
    def th_management_system_2031_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2031_jul.iterrows():

            # NOTE: No more change needed --->>>>>

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            # NOTE: No more change needed --->>>>>
            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2032 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
    def th_management_system_2032_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2032_jan.iterrows():

            # NOTE: No change needed --->>>>>
            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0
                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            # NOTE: No more change needed --->>>>>
            else:  # charging
                # print("storage charging")
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:
                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)
                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)
                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)
                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2032 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop --->>>>>>>>>>>>>>>
    def th_management_system_2032_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2032_jul.iterrows():

            # NOTE: No more change needed --->>>>>

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            # NOTE: No more change needed --->>>>>
            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2033 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
    def th_management_system_2033_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2033_jan.iterrows():

            # NOTE: No change needed --->>>>>
            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0
                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            # NOTE: No more change needed --->>>>>
            else:  # charging
                # print("storage charging")
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:
                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)
                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)
                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)
                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2033 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop --->>>>>>>>>>>>>>>
    def th_management_system_2033_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2033_jul.iterrows():

            # NOTE: No more change needed --->>>>>

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            # NOTE: No more change needed --->>>>>
            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2034 - Jan %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
    def th_management_system_2034_jan(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()
        # print("line_pack_mwh =", storage_line_pack)
        # print("x_storage_th_max_mwh =", self.storage_th_max_mwh)

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2034_jan.iterrows():

            # NOTE: No change needed --->>>>>
            demand_th_jan_mwh = load_row['th_load_38_household'] + self.dh_network()
            # print("demand =", demand_th_jan_mwh)

            heat_production_mwh = chp_th_mwh + hp_th_mwh
            # print("heat_production =", heat_production_mwh)

            storage_th_mwh = storage_th_init
            # print("storage_init =", storage_th_mwh)

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jan_mwh:  # discharge:
                # print('storage discharge')
                storage_th_mwh = storage_th_init - demand_th_jan_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0
                # print('if_storage_th_mwh =', storage_th_mwh)

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
                # print()

            # NOTE: No more change needed --->>>>>
            else:  # charging
                # print("storage charging")
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jan_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:
                    # print("storage_th_mwh =", storage_th_mwh)
                    # print("self.storage_th_max_mwh =", self.storage_th_max_mwh)
                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)
                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)
                    th_energy_deficit_mwh = 0  # if th Generation is not enough
                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0

                    storage_th_mwh = storage_th_mwh

                    # print('storage in between')
                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh =', th_energy_deficit_mwh)
                    # else:
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                    # print('storage -Ve')
                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jan_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jan_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            storage_th_init = storage_th_mwh
            # print("th_storage_mwh_LOOP =", storage_th_init)
        return results_tes_mwh

    # =================================================== 2034 July ===================================================
    # NOTE: Do not change the order of the parameters, i.e.: storage_th_mwh, th_energy_loss_mwh & th_energy_deficit_mwh
    # NOTE: change the heat_demand_YEAR_MONTH in the for loop --->>>>>>>>>>>>>>>
    def th_management_system_2034_jul(self):
        results_tes_mwh = pd.DataFrame()

        eta_storage_ch = 0.88
        eta_storage_dis = 0.88

        chp_th_mwh = self.chp_th_mwh
        hp_th_mwh = self.hp_th_mwh

        chp_gas_import_mwh = self.chp_gas_import_mwh

        storage_line_pack = self.linepack()

        storage_th_init = storage_line_pack

        # change the heat_demand_YEAR_MONTH in for-loop --->>>>>>>>>>>>>>>
        for load_idx, load_row in heat_demand_2034_jul.iterrows():

            # NOTE: No more change needed --->>>>>

            demand_th_jul_mwh = load_row['th_load_38_household'] + self.dh_network()

            heat_production_mwh = chp_th_mwh + hp_th_mwh

            storage_th_mwh = storage_th_init

            # -------------- Storage management ---------------
            if storage_th_mwh > demand_th_jul_mwh:  # discharge:
                storage_th_mwh = storage_th_init - demand_th_jul_mwh / eta_storage_dis
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The th-storage cannot be charged, because no th-generation is active here.

                # Control storage not to go below 0
                # Note: since discharging, need to prevent storage to be negative.
                if storage_th_mwh < 0:
                    th_energy_deficit_mwh = storage_th_mwh
                    # print('th_energy_deficit_mwh_charging =', th_energy_deficit_mwh)
                    storage_th_mwh = 0
                else:  # Storage is +Ve
                    storage_th_mwh = storage_th_mwh
                    th_energy_deficit_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'hp_th_mwh': 0,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': 0,  # only taking thermal power from storage, so CHP is not working
                    'th_energy_loss_mwh': 0,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)

            # NOTE: No more change needed --->>>>>
            else:  # charging
                storage_th_mwh = storage_th_init + heat_production_mwh * eta_storage_ch - \
                                 demand_th_jul_mwh / eta_storage_dis
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for storage_th_mwh, th_energy_deficit_mwh & th_energy_loss_mwh ---------
                if storage_th_mwh > self.storage_th_max_mwh:

                    # print("storage_th_mwh =", storage_th_mwh)

                    th_energy_loss_mwh = storage_th_mwh - self.storage_th_max_mwh
                    # print('th_energy_loss_mwh =', th_energy_loss_mwh)

                    storage_th_mwh = self.storage_th_max_mwh
                    # print('storage_th_mwh =', storage_th_mwh)

                    th_energy_deficit_mwh = 0  # if th Generation is not enough

                elif storage_th_mwh < self.storage_th_max_mwh and storage_th_mwh > 0:
                    # th-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    th_energy_deficit_mwh = 0
                    th_energy_loss_mwh = 0
                    storage_th_mwh = storage_th_mwh

                elif storage_th_mwh < 0:  # th-storage is -Ve
                    th_energy_deficit_mwh = storage_th_mwh
                    storage_th_mwh = 0  # maybe its -Ve
                    th_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    th_energy_deficit_mwh = 0
                    storage_th_mwh = 0
                    th_energy_loss_mwh = 0

                result = {
                    'tes_init_mwh': storage_th_init,
                    'chp_th_mwh': chp_th_mwh,
                    'hp_th_mwh': hp_th_mwh,
                    'demand_th_mwh': demand_th_jul_mwh,
                    'storage_th_mwh': storage_th_mwh,
                    'gas_import_mwh': chp_gas_import_mwh,  # + (gas_import_mwh / 0.01055)
                    'th_energy_loss_mwh': th_energy_loss_mwh,
                    'th_energy_deficit_mwh': th_energy_deficit_mwh,
                    'heat_balance': (heat_production_mwh + storage_th_mwh) - demand_th_jul_mwh
                }
                results_tes_mwh = results_tes_mwh.append(result, ignore_index=True)
            storage_th_init = storage_th_mwh
        return results_tes_mwh

# ************************************* Model Testing *************************************
# tes = TES(chp_th_mwh=0.205554, chp_gas_import_mwh=0.4, hp_th_mwh=0.046196, storage_th_max_mwh=0.0)
# th_storage = tes.th_management_system_2026_jul()
# print(th_storage)

# th_storage_old = tes.TES_2025_jul()
# print(th_storage_old)