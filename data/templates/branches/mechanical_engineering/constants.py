# E is the Modulus of Elasticity.
MATERIAL_PROPERTIES = {
    # Metals (Common)
    'Steel': {'E_GPa': 200, 'E_ksi': 29000, 'nu': 0.30},
    'Stainless Steel': {'E_GPa': 190, 'E_ksi': 27500, 'nu': 0.30}, # 304 Stainless
    'Aluminum': {'E_GPa': 69, 'E_ksi': 10000, 'nu': 0.33}, # General purpose 1100, 3003 Al
    'Aluminum 6061-T6': {'E_GPa': 68.9, 'E_ksi': 10000, 'nu': 0.33}, # A common specific alloy
    'Copper': {'E_GPa': 117, 'E_ksi': 17000, 'nu': 0.34},
    'Brass': {'E_GPa': 102, 'E_ksi': 14800, 'nu': 0.34}, # Yellow Brass (CuZn37)
    'Bronze': {'E_GPa': 110, 'E_ksi': 16000, 'nu': 0.34}, # Phosphor Bronze
    'Titanium': {'E_GPa': 116, 'E_ksi': 16800, 'nu': 0.34}, # Commercially Pure
    'Titanium Alloy (6Al-4V)': {'E_GPa': 114, 'E_ksi': 16500, 'nu': 0.34},
    'Magnesium': {'E_GPa': 45, 'E_ksi': 6500, 'nu': 0.29}, # AZ31B alloy
    'Tungsten': {'E_GPa': 411, 'E_ksi': 59600, 'nu': 0.28},
    'Cast Iron': {'E_GPa': 170, 'E_ksi': 24600, 'nu': 0.26}, # Gray Cast Iron
    'Nickel': {'E_GPa': 207, 'E_ksi': 30000, 'nu': 0.31},
    'Lead': {'E_GPa': 16, 'E_ksi': 2300, 'nu': 0.44}, # Added a common soft metal
    
    # Polymers/Plastics
    'Nylon': {'E_GPa': 2.1, 'E_ksi': 300, 'nu': 0.39}, # Nylon 6/6
    'Polycarbonate': {'E_GPa': 2.3, 'E_ksi': 334, 'nu': 0.38},
    'ABS': {'E_GPa': 2.0, 'E_ksi': 290, 'nu': 0.35},
    'PVC (rigid)': {'E_GPa': 3.0, 'E_ksi': 435, 'nu': 0.38},
    'PTFE (Teflon)': {'E_GPa': 0.5, 'E_ksi': 72, 'nu': 0.46},
    'Polyethylene (HDPE)': {'E_GPa': 1.1, 'E_ksi': 160, 'nu': 0.42},
    'Epoxy': {'E_GPa': 3.0, 'E_ksi': 435, 'nu': 0.38}, # Unreinforced epoxy resin
    'Natural Rubber': {'E_GPa': 0.0015, 'E_ksi': 0.22, 'nu': 0.4999}, # ~0.5 (nearly incompressible)
    
    # Composites & Other
    'Carbon Fiber Reinforced Polymer (CFRP)': {'E_GPa': 150, 'E_ksi': 21750, 'nu': 0.30}, # Direction-dependent, this is a typical in-plane value
    'Fiberglass (GFRP)': {'E_GPa': 45, 'E_ksi': 6500, 'nu': 0.25}, # Direction-dependent, typical in-plane value
    'Concrete': {'E_GPa': 30, 'E_ksi': 4350, 'nu': 0.15}, # Highly variable, common approx.
    'Glass (Borosilicate)': {'E_GPa': 70, 'E_ksi': 10150, 'nu': 0.20},
    'Ceramic (Alumina Al2O3)': {'E_GPa': 370, 'E_ksi': 53700, 'nu': 0.22},
}
