
# ........... NOT USING IT ...............2024.07.26
# ........... NOT USING IT ...............
# ........... NOT USING IT ...............


import pandas as pd

# pd.set_option('display.max_columns', None)

# Time series

# print(gas_demand_jan)


class BESS:
    def __init__(self, net, bess_mw, bess_mwh, sgen_mwh, demand_e_mwh, bess_update_mwh, **kwargs):
        # current_energy, bess_max_energy,
        # bess_min_energy,
        self.net = net
        self.bess_mw = bess_mw
        self.bess_mwh = bess_mwh
        # self.bess_soc = bess_soc
        # self.surplus_mw = surplus_mw
        # self.current_energy = current_energy
        # self.bess_max_energy = bess_max_energy
        # self.bess_min_energy = bess_min_energy
        self.sgen_mwh = sgen_mwh
        self.demand_e_mwh = demand_e_mwh
        self.bess_update_mwh = bess_update_mwh

    def adjust_bess(self):

        ch_dis_rate_mw = self.bess_mw
        bess_max_ch_energy_mwh = self.bess_mwh * 12 * 0.9  # C rate 0.5 - 90% max limit; 12 = total cycle per 24 hrs
        bess_max_dis_energy_mwh = self.bess_mwh * 12 * 0.1  # C rate 0.5 - 10% max limit
        # 0.5 C rate means that it will take two hours to fully charge or discharge,
        # i.e.: 12 cycle of charging and discharging for 24 hr operation.

        res_bess_mw = 0
        res_bess_mwh = self.bess_update_mwh  # Initialize with the current energy state

        current_bess_update_mwh = res_bess_mwh
        # print("BESS from Net Func:")
        # print("ch_dis_rate_mw =", ch_dis_rate_mw)
        # print("current_bess_update_mwh =", current_bess_update_mwh)
        # print("bess_max_ch_energy_mwh =", bess_max_ch_energy_mwh)
        # print("bess_max_dis_energy_mwh =", bess_max_dis_energy_mwh)
        # print()

        eta_storage_ch = 0.95
        eta_storage_dis = 0.95

        # bess_max_energy = 0.9 * self.bess_capacity_mwh
        # bess_min_energy = 0.1 * self.bess_capacity_mwh
        # current_energy = self.bess_capacity_mwh * self.bess_soc    #self.net.storage['soc_percent']   # soc = 50%
        # print("current_energy", current_energy)
        # print()

        surplus_mw = self.sgen_mwh - self.demand_e_mwh
        # print("surplus_mw =", surplus_mw)

        # surplus_mw = self.net.sgen['p_mw'].sum() - self.net.load['p_mw'].sum()

        # for bess_idx, bess_idx in enumerate(self.bess_capacity_mwh):
        if surplus_mw > 0:
            # Charging
            # print("Charging:")
            charge_power = ch_dis_rate_mw * eta_storage_ch

            if current_bess_update_mwh < bess_max_ch_energy_mwh:
                # print("current_energy < bess_max_energy")
                res_bess_mw = charge_power   # Charging power (positive because it's charging)
                res_bess_mwh = current_bess_update_mwh + charge_power  # -> charging

                if res_bess_mwh > bess_max_ch_energy_mwh:
                    res_bess_mw = charge_power
                    res_bess_mwh = bess_max_ch_energy_mwh
                else:
                    pass
            else:   # current_energy >= max_ch_mwh
                res_bess_mw = 0
                res_bess_mwh = bess_max_ch_energy_mwh

            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        else:  # surplus_mw < 0
            # Discharging
            # print("Discharging:")
            # deficit_mw = self.demand_e_mwh - self.sgen_mwh
            discharge_power = ch_dis_rate_mw * eta_storage_dis

            if current_bess_update_mwh > bess_max_dis_energy_mwh:

                # print("current_energy > bess_min_energy")

                res_bess_mw = -discharge_power  # DisCharging power (negative because it's discharging)
                res_bess_mwh = current_bess_update_mwh - discharge_power   # -> discharging

                if res_bess_mwh < bess_max_dis_energy_mwh:
                    res_bess_mw = -discharge_power
                    res_bess_mwh = bess_max_dis_energy_mwh
                else:
                    pass
            else:   # current_bess_energy <= min_bess_dis_energy
                # print("current_bess_update_mwh", current_bess_update_mwh)
                res_bess_mw = 0
                res_bess_mwh = current_bess_update_mwh

                # bess_update_mw = 0
                # current_energy_update_mwh = current_energy_update_mwh + bess_update_mw

            # # res_bess_mw += bess_update_mwh
            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        # print()
        # print("res_bess_mw=", res_bess_mw)
        # print("current_energy_update_mwh=", res_bess_mwh)
        # print()
        return res_bess_mw, res_bess_mwh

    def bms_update(self):

        ch_dis_rate_mw = self.bess_mw       # with C rate 1 = max capacity charge and discharge in 1 hr.
        bess_max_ch_energy_mwh = self.bess_mwh * 0.9  # 90% max charge energy
        bess_min_dis_energy_mwh = self.bess_mwh * 0.1  # 10% nin discharge energy

        res_bess_mw = 0
        res_bess_mwh = self.bess_update_mwh  # Initialize with the current energy state

        current_bess_update_mwh = res_bess_mwh    # Current energy state
        # print("BESS from Net Func:")
        # print("ch_dis_rate_mw =", ch_dis_rate_mw)
        # print("current_bess_update_mwh =", current_bess_update_mwh)
        # print("bess_max_ch_energy_mwh =", bess_max_ch_energy_mwh)
        # print("bess_max_dis_energy_mwh =", bess_max_dis_energy_mwh)
        # print()

        eta_storage_ch = 0.90   # Source: MANGO
        eta_storage_dis = 0.90  # Source: MANGO

        # bess_max_energy = 0.9 * self.bess_capacity_mwh
        # bess_min_energy = 0.1 * self.bess_capacity_mwh
        # current_energy = self.bess_capacity_mwh * self.bess_soc    #self.net.storage['soc_percent']   # soc = 50%
        # print("current_energy", current_energy)
        # print()

        surplus_mw = self.sgen_mwh - self.demand_e_mwh
        # print("surplus_mw =", surplus_mw)

        # surplus_mw = self.net.sgen['p_mw'].sum() - self.net.load['p_mw'].sum()

        # for bess_idx, bess_idx in enumerate(self.bess_capacity_mwh):
        if surplus_mw > 0:
            # Charging
            # print("Charging:")
            charge_power = ch_dis_rate_mw * eta_storage_ch

            res_bess_power_deficit_mwh = 0

            if current_bess_update_mwh < bess_max_ch_energy_mwh:        # Can charge
                # print("current_energy < bess_max_energy")
                res_bess_mw = charge_power   # Charging power (positive because it's charging)
                res_bess_mwh = current_bess_update_mwh + charge_power  # -> charging
                # print('bess capacity at ch', res_bess_mwh)

                if res_bess_mwh > bess_max_ch_energy_mwh:       # Can charge, but cannot go over the max limit
                    # print('power loss mwh =', res_bess_mwh - bess_max_ch_energy_mwh)
                    res_bess_power_loss_mwh = res_bess_mwh - bess_max_ch_energy_mwh
                    res_bess_mw = charge_power
                    res_bess_mwh = bess_max_ch_energy_mwh
                else:           # Can charge
                    res_bess_power_loss_mwh = 0
                    res_bess_mw = charge_power
                    res_bess_mwh = res_bess_mwh
            else:   # current_energy >= max_ch_mwh      # Cannot charge, BESS is full
                res_bess_mw = 0
                res_bess_mwh = res_bess_mwh
                res_bess_power_loss_mwh = 0
                # print('bess capacity FULL =', res_bess_mwh)

                # add mwh and power loss in the main output results....

            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        else:  # surplus_mw < 0 == Demand > PV+WT
            # Discharging
            # print("Can discharge?:")
            # print('current_bess_update_mwh =', current_bess_update_mwh)
            # deficit_mw = self.demand_e_mwh - self.sgen_mwh
            discharge_power = ch_dis_rate_mw * eta_storage_dis

            res_bess_power_loss_mwh = 0     # No charging, so no power loss for bess is possible.

            if current_bess_update_mwh > bess_min_dis_energy_mwh:

                res_bess_mw = -discharge_power  # DisCharging power (negative because it's discharging)
                res_bess_mwh = current_bess_update_mwh - discharge_power   # -> discharging

                if res_bess_mwh < bess_min_dis_energy_mwh:  # BESS capacity cant be less than min capacity 10%

                    res_bess_power_deficit_mwh = bess_min_dis_energy_mwh - res_bess_mwh
                    res_bess_mw = -discharge_power
                    res_bess_mwh = bess_min_dis_energy_mwh

                    # print("YES")
                    # print('res_bess_power_deficit_mwh =', res_bess_power_deficit_mwh)
                else:   # res_bess_mwh > bess_min_dis_energy_mwh and
                    res_bess_power_deficit_mwh = 0      # No deficit, because enough charge in BESS
                    res_bess_mw = -discharge_power
                    res_bess_mwh = res_bess_mwh

            else:   # current_bess_energy <= min_bess_dis_energy
                # print("NO")
                res_bess_mw = 0
                res_bess_mwh = current_bess_update_mwh
                res_bess_power_deficit_mwh = 0
                # print('res_bess_mwh =', res_bess_mwh)

                # bess_update_mw = 0
                # current_energy_update_mwh = current_energy_update_mwh + bess_update_mw

            # # res_bess_mw += bess_update_mwh
            # res_bess_mw += bess_update_mw
            # current_energy_update_mwh += current_energy_update_mwh

        # print()
        # print("res_bess_mw=", res_bess_mw)
        # print("current_energy_update_mwh=", res_bess_mwh)
        # print()
        return res_bess_mw, res_bess_mwh, res_bess_power_loss_mwh, res_bess_power_deficit_mwh

# ************************************* Model Testing *************************************
# import pandapower.networks as pn
#
# # Power grid:
# net = pn.create_cigre_network_mv(with_der=False)
#
# net.load.drop(index=net.load.index, inplace=True)
# net.sgen.drop(index=net.sgen.index, inplace=True)
# net.gen.drop(index=net.gen.index, inplace=True)
# net.xward.drop(net.xward.index, inplace=True)
# net.shunt.drop(index=net.shunt.index, inplace=True)
#
# bess = BESS(net=net, sgen_mwh=100, demand_e_mwh=0.20,
#                         bess_mw=10,
#                         bess_mwh=10*1,
#                         bess_soc=0.5,
#                         # current_energy=bess_current_energy,
#                         # bess_max_energy=bess_max_energy,
#                         # bess_min_energy=bess_min_energy,
#                         bess_update_mwh=10*0.5)
# bess_mwh = bess.adjust_bess()
#
# print(bess_mwh)
