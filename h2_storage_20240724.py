
import pandas as pd

pd.set_option('display.max_columns', None)

# Time series
# --------------------------------- 2025 ---------------------------------
gas_demand_test = pd.read_csv("gas_load_industries_v2.csv")
gas_demand_jan = pd.DataFrame(gas_demand_test['jan'])
gas_demand_jul = pd.DataFrame(gas_demand_test['jul'])
# --------------------------------- 2026 ---------------------------------
gas_demand_2026_jan = pd.DataFrame(gas_demand_test['2026_jan'])
gas_demand_2026_jul = pd.DataFrame(gas_demand_test['2026_jul'])
# --------------------------------- 2027 ---------------------------------
gas_demand_2027_jan = pd.DataFrame(gas_demand_test['2027_jan'])
gas_demand_2027_jul = pd.DataFrame(gas_demand_test['2027_jul'])
# --------------------------------- 2028 ---------------------------------
gas_demand_2028_jan = pd.DataFrame(gas_demand_test['2028_jan'])
gas_demand_2028_jul = pd.DataFrame(gas_demand_test['2028_jul'])
# --------------------------------- 2029 ---------------------------------
gas_demand_2029_jan = pd.DataFrame(gas_demand_test['2029_jan'])
gas_demand_2029_jul = pd.DataFrame(gas_demand_test['2029_jul'])
# --------------------------------- 2030 ---------------------------------
gas_demand_2030_jan = pd.DataFrame(gas_demand_test['2030_jan'])
gas_demand_2030_jul = pd.DataFrame(gas_demand_test['2030_jul'])
# --------------------------------- 2031 ---------------------------------
gas_demand_2031_jan = pd.DataFrame(gas_demand_test['2031_jan'])
gas_demand_2031_jul = pd.DataFrame(gas_demand_test['2031_jul'])
# --------------------------------- 2032 ---------------------------------
gas_demand_2032_jan = pd.DataFrame(gas_demand_test['2032_jan'])
gas_demand_2032_jul = pd.DataFrame(gas_demand_test['2032_jul'])
# --------------------------------- 2033 ---------------------------------
gas_demand_2033_jan = pd.DataFrame(gas_demand_test['2033_jan'])
gas_demand_2033_jul = pd.DataFrame(gas_demand_test['2033_jul'])
# --------------------------------- 2034 ---------------------------------
gas_demand_2034_jan = pd.DataFrame(gas_demand_test['2034_jan'])
gas_demand_2034_jul = pd.DataFrame(gas_demand_test['2034_jul'])
# print(gas_demand_2030_jan)


class HyES:
    def __init__(self, p2g_input_mw, h2_production_mwh, storage_h2_max_mwh, **kwargs):
        # self.gas_input = gas_input
        self.p2g_input_mw = p2g_input_mw
        self.h2_production_mwh = h2_production_mwh
        self.storage_h2_max_mwh = storage_h2_max_mwh

    # def h2_storage_jan(self):
    #
    #     results_ges_mwh = pd.DataFrame()
    #
    #     eta_storage_ch = 0.60
    #     eta_storage_dis = 0.60
    #
    #     storage_h2_init = 0     # [MWh]
    #
    #     for load_idx, load_row in gas_demand_jan.iterrows():
    #         # print(load_row['jan'])
    #
    #         storage_h2_mwh = storage_h2_init
    #
    #         if storage_h2_mwh >= self.storage_h2_max_mwh:
    #             # print("storage_h2_mwh > self.storage_h2_max_mwh")
    #             storage_h2_mwh = storage_h2_mwh - (load_row['jan'] / eta_storage_dis)
    #
    #             # ********************** Calculating if storage is negative **********************
    #             blue_h2_import_mwh = 0
    #             if storage_h2_mwh < 0:
    #                 blue_h2_import_mwh = -storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
    #                 # print("blue_h2_import_mwh =", blue_h2_import_mwh)
    #                 storage_h2_mwh = 0  # After importing Blue H2, the storage should be zero
    #
    #             result = {
    #                 'ges_init_mwh': storage_h2_init,
    #                 'h2_prod_mwh': 0,
    #                 'demand_h2_mwh': load_row['jan'],
    #                 'storage_h2_mwh': storage_h2_mwh,
    #                 'blue_h2_mwh': blue_h2_import_mwh,
    #             }
    #             results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)
    #
    #             # Update the storage_th_init for the next iteration
    #             storage_h2_init = storage_h2_mwh
    #         else:
    #             # print("storage_h2_mwh < self.storage_h2_max_mwh")
    #             storage_h2_mwh = storage_h2_mwh + (self.h2_production_mwh * eta_storage_ch) - \
    #                              (load_row['jan'] / eta_storage_dis)
    #
    #             # ********************** Calculating if storage is negative **********************
    #             blue_h2_import_mwh = 0
    #             if storage_h2_mwh < 0:
    #                 blue_h2_import_mwh = -storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
    #                 # print("blue_h2_import_mwh =", blue_h2_import_mwh)
    #                 storage_h2_mwh = 0  # After importing Blue H2, the storage should be zero
    #
    #             result = {
    #                 'ges_init_mwh': storage_h2_init,
    #                 'h2_prod_mwh': self.h2_production_mwh * eta_storage_ch,
    #                 'demand_h2_mwh': load_row['jan'],
    #                 'storage_h2_mwh': storage_h2_mwh,
    #                 'blue_h2_mwh': blue_h2_import_mwh,
    #             }
    #             results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)
    #
    #             # Update the storage_th_init for the next iteration
    #             storage_h2_init = storage_h2_mwh
    #
    #     return results_ges_mwh

    def h2_management_system_2025_jan_update(self):
        # NOTE: Do not change the order of the parameters, i.e.:
        # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0     # [MWh]

        for load_idx, load_row in gas_demand_jan.iterrows():
            # print(load_row['jan'])

            demand_h2_jan_mwh = load_row['jan']
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:      # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh     # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': load_row['jan'],
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                 }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:       # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (load_row['jan'] / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:        # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': load_row['jan'],
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    def h2_management_system_2025_jul(self):
        # NOTE: Do not change the order of the parameters, i.e.:
        # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0     # [MWh]

        for load_idx, load_row in gas_demand_jul.iterrows():
            # print(load_row['jan'])

            demand_h2_jul_mwh = load_row['jul']
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:      # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh     # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                 }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:       # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:        # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # ===================================================== 2026 ======================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    def h2_management_system_2026_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0     # [MWh]

        for load_idx, load_row in gas_demand_2026_jan.iterrows():
            # print(load_row['jan'])

            demand_h2_jan_mwh = load_row['2026_jan']
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:      # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh     # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                 }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:       # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:        # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # ------------------------------------------- 2026 July -------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    def h2_management_system_2026_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        for load_idx, load_row in gas_demand_2026_jul.iterrows():
            # print(load_row['jan'])

            demand_h2_jul_mwh = load_row['2026_jul']
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2027 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop also the file ['Ýear_MONTH']
    def h2_management_system_2027_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0     # [MWh]

        for load_idx, load_row in gas_demand_2027_jan.iterrows():
            # print(load_row['jan'])

            demand_h2_jan_mwh = load_row['2027_jan']        # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:      # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh     # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                 }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:       # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:        # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # ------------------------------------------- 2027 July -------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop
    def h2_management_system_2027_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        for load_idx, load_row in gas_demand_2027_jul.iterrows():
            # print(load_row['jan'])

            demand_h2_jul_mwh = load_row['2027_jul']        # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2028 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2028_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0     # [MWh]

        for load_idx, load_row in gas_demand_2028_jan.iterrows():
            # print(load_row['jan'])

            demand_h2_jan_mwh = load_row['2028_jan']        # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:      # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh     # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                 }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:       # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:        # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2028 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2028_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        for load_idx, load_row in gas_demand_2028_jul.iterrows():
            # print(load_row['jan'])

            demand_h2_jul_mwh = load_row['2028_jul']        # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2029 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2029_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0     # [MWh]

        for load_idx, load_row in gas_demand_2029_jan.iterrows():
            # print(load_row['jan'])

            demand_h2_jan_mwh = load_row['2029_jan']        # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:      # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh     # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                 }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:       # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:        # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2029 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2029_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        for load_idx, load_row in gas_demand_2029_jul.iterrows():
            # print(load_row['jan'])

            demand_h2_jul_mwh = load_row['2029_jul']        # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2030 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2030_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2030_jan.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jan_mwh = load_row['2030_jan']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2030 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2030_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2030_jul.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jul_mwh = load_row['2030_jul']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2031 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2031_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2031_jan.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jan_mwh = load_row['2031_jan']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2031 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2031_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2031_jul.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jul_mwh = load_row['2031_jul']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2032 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2032_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2032_jan.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jan_mwh = load_row['2032_jan']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2032 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2032_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2032_jul.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jul_mwh = load_row['2032_jul']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2033 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2033_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2033_jan.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jan_mwh = load_row['2033_jan']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2033 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2033_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2033_jul.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jul_mwh = load_row['2033_jul']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # =================================================== 2034 Jan ====================================================
    # NOTE: Do not change the order of the parameters, i.e.:
    # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameter "gas_demand_YEAR_MONTH" in the for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2034_jan(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2034_jan.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jan ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jan_mwh = load_row['2034_jan']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jan_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jan_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jan_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

    # --------------------------------------------------- 2034 July ---------------------------------------------------
    # NOTE: Do not change the order of the parameters, i.e.: # storage_h2_mwh, blue_h2_import_mwh & h2_energy_loss_mwh
    # NOTE: Change the parameters: gas_demand_YEAR_MONTH in for-loop & ['YEAR_MONTH'] inside the for-loop
    def h2_management_system_2034_jul(self):

        results_ges_mwh = pd.DataFrame()

        eta_storage_ch = 0.60
        eta_storage_dis = 0.60

        storage_h2_init = 0  # [MWh]

        # ----- CHANGE: gas_demand_YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>
        for load_idx, load_row in gas_demand_2034_jul.iterrows():
            # print(load_row['jan'])

            # ----- CHANGE: YEAR_jul ------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            demand_h2_jul_mwh = load_row['2034_jul']  # ----- <-- Change the ['YEAR_MONTH'] -----
            h2_production_mwh = self.h2_production_mwh
            storage_h2_mwh = storage_h2_init

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            # -------------- Storage management ---------------
            if storage_h2_mwh > demand_h2_jul_mwh:  # Discharging
                storage_h2_mwh = storage_h2_mwh - (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am only using discharging equation, because the storage can only be discharged here.
                # The h2-storage cannot be charged, because no h2-generation is active here.

                # ----------------- checking if the storage is negative/blue H2 import --------------------
                if storage_h2_mwh < 0:
                    # Control storage not to go below 0
                    # Note: since discharging, need to prevent storage to be negative.
                    blue_h2_import_mwh = storage_h2_mwh  # amount of Blue H2 needed to cover the deficit
                    storage_h2_mwh = 0  # storage cannot be -Ve
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage
                else:
                    storage_h2_mwh = storage_h2_mwh
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0  # because no H2 is produced, as demand is supplied from storage

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': 0,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

            # NOTE: NO MORE Changes needed ------>>>>>>>>>>>>>>>>>>>>>>>>
            else:  # Charging
                # print("storage_h2_mwh < self.storage_h2_max_mwh")
                storage_h2_mwh = storage_h2_mwh + (h2_production_mwh * eta_storage_ch) - \
                                 (demand_h2_jul_mwh / eta_storage_dis)
                # Note: here I am adding the charging & discharging the same equation,
                # because the storage can charge while the th-generators are active, and at the same time
                # it needs to discharge for the respected demand

                # --------- Control strategies for ... ---------
                if storage_h2_mwh > self.storage_h2_max_mwh:
                    h2_energy_loss_mwh = storage_h2_mwh - self.storage_h2_max_mwh
                    storage_h2_mwh = self.storage_h2_max_mwh
                    blue_h2_import_mwh = 0

                elif storage_h2_mwh < self.storage_h2_max_mwh and storage_h2_mwh > 0:
                    # h2-storage is lower than the max-storage, but in between max and 0 (!-Ve)
                    blue_h2_import_mwh = 0
                    h2_energy_loss_mwh = 0
                    storage_h2_mwh = storage_h2_mwh

                elif storage_h2_mwh < 0:  # h2-storage is -Ve
                    blue_h2_import_mwh = storage_h2_mwh
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                else:  # Incase some errors, making all zero.
                    blue_h2_import_mwh = 0
                    storage_h2_mwh = 0
                    h2_energy_loss_mwh = 0

                result = {
                    'ges_init_mwh': storage_h2_init,
                    'h2_prod_mwh': h2_production_mwh * eta_storage_ch,
                    'demand_h2_mwh': demand_h2_jul_mwh,
                    'storage_h2_mwh': storage_h2_mwh,
                    'blue_h2_mwh': blue_h2_import_mwh,
                    'h2_energy_loss_mwh': h2_energy_loss_mwh
                }
                results_ges_mwh = results_ges_mwh.append(result, ignore_index=True)

                # Update the storage_th_init for the next iteration
                storage_h2_init = storage_h2_mwh

        return results_ges_mwh

# ************************************* Model Testing *************************************
# hyes = HyES(p2g_input_mw=0, h2_production_mwh=5, storage_h2_max_mwh=0)
# h2_storage_res = hyes.h2_storage_jan()
# hms = hyes.h2_management_system_2025_jan_update()
#
# print(h2_storage_res)
# print(hms)
