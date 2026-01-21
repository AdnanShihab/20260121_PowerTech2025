"""
P2G model
"""
# Electrolyser type: polymer electrolyte membrane eletrolysis


h = 12.46   # [Mj/m3] Collaborative optimization for a multi-energy system considering carbon capture system...
n = 0.82    # Source: Source: Book - "Power to gas: Tech and business model (page: 37)"
tau = 0.99  # 330-350 degree and 10 bar pressure <source: Endbericht-PowertoGas-eineSystemanalyse-2014; pg: 178>
# 101 kPa/1 bar is the atmospheric pressure <source: google>

# p_surplus unit = [MW]


class P2G:

    def __init__(self, p2g_input_mw, **kwargs):
        self.p2g_input_mw = p2g_input_mw

    def p2g_model(self):
        h2_production_m3_s = (n * self.p2g_input_mw)/h              # unit: meter3/s
        h2_production_m3_hr = (n * self.p2g_input_mw * 3600) / h     # [meter3/h]

        # q_h2_day = q_h2*86400                             # unit: meter3/day

        h2_production_kg_h = h2_production_m3_hr * 0.08988  # [meter3/h * kg/m³]
        # The density of hydrogen gas at standard temperature and pressure
        # (STP, 0°C and 1 atm) is approximately 0.08988 kg/m³.

        h2_production_mwh = h2_production_m3_hr/3600                 # [MWh] [MW/h]

        # q_h2_kg = (q_h2 * 1000 * 24)            # kg/24 hr [<https://www.easyunitconverter.com/m3-to-kg>]
        # q_ch4 = (tau * q_h2)                    # unit: meter3/s
        # q_ch4 = q_ch4*3600                      # [m3/hr]
        # q_ch4_MW = (q_ch4*10.55)/1000           # 1 m3/hr = 10.55 kWh

        # print("q_h2_Nm3/s", q_h2)
        # print("q_h2_Nm3/day", q_h2_day)
        # print("q_h2_MWh", q_h2_MWh)

        return h2_production_m3_s, h2_production_m3_hr, h2_production_mwh

# *************** model test *******************

# p2g = P2G(p2g_input_mw=2.45)
# h2_production_mwh = p2g.p2g_model()
# print(h2_production_mwh)