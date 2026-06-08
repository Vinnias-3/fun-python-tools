#!/usr/bin/env python3
"""
ADVANCED CHEMISTRY LAB
Built by Vinnias Mbuthia (TechGlobal)
Features: Element lookup, reaction equations, compound info, 
          balanced equations, molar mass calculator, pH calculator
"""

import requests
import json
import os
import random
from urllib.parse import quote

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================
# API FUNCTIONS
# ============================================

def get_element_data(query):
    """Fetch element data from PubChem API"""
    try:
        # Try as atomic number
        if query.isdigit():
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/element/atomicnumber/{query}/JSON"
        else:
            # Try as symbol or name
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/element/symbol/{query}/JSON"
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/element/name/{query}/JSON"
        
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['Record']
    except:
        pass
    return None

def get_compound_info(compound_name):
    """Search for a chemical compound"""
    try:
        # Search by name
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{quote(compound_name)}/JSON"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            cid = data['PC_Compounds'][0]['id']['id']['cid']
            
            # Get detailed info
            detail_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON"
            detail_response = requests.get(detail_url, timeout=5)
            
            return {
                'cid': cid,
                'name': compound_name,
                'url': f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}"
            }
    except:
        pass
    return None

def get_reaction_info(reaction_query):
    """Search for chemical reactions"""
    try:
        # PubChem doesn't have a direct reaction API, but we can search
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/assayid/1/JSON"
        # Fallback: return known reactions
        return None
    except:
        return None

# ============================================
# REACTION DATABASE (Common Reactions)
# ============================================

REACTIONS = {
    "combustion methane": {
        "equation": "CH₄ + 2O₂ → CO₂ + 2H₂O",
        "type": "Combustion",
        "description": "Methane burns in oxygen to produce carbon dioxide and water. This is the main reaction in natural gas stoves.",
        "energy": "Exothermic (-890 kJ/mol)",
        "balanced": True
    },
    "photosynthesis": {
        "equation": "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
        "type": "Photosynthesis",
        "description": "Plants convert carbon dioxide and water into glucose and oxygen using sunlight energy.",
        "energy": "Endothermic (requires light energy)",
        "balanced": True
    },
    "rust formation": {
        "equation": "4Fe + 3O₂ → 2Fe₂O₃",
        "type": "Oxidation",
        "description": "Iron reacts with oxygen to form iron(III) oxide (rust). This is a slow oxidation process.",
        "energy": "Exothermic (slow release)",
        "balanced": True
    },
    "neutralization hcl naoh": {
        "equation": "HCl + NaOH → NaCl + H₂O",
        "type": "Neutralization",
        "description": "Hydrochloric acid reacts with sodium hydroxide to form table salt and water.",
        "energy": "Exothermic (-57 kJ/mol)",
        "balanced": True
    },
    "water electrolysis": {
        "equation": "2H₂O → 2H₂ + O₂",
        "type": "Decomposition (Electrolysis)",
        "description": "Water is split into hydrogen and oxygen gases by passing an electric current through it.",
        "energy": "Endothermic (requires electricity)",
        "balanced": True
    },
    "haber process": {
        "equation": "N₂ + 3H₂ → 2NH₃",
        "type": "Synthesis (Industrial)",
        "description": "The Haber process produces ammonia from nitrogen and hydrogen. Critical for fertilizer production.",
        "energy": "Exothermic (-92 kJ/mol)",
        "balanced": True
    },
    "limestone decomposition": {
        "equation": "CaCO₃ → CaO + CO₂",
        "type": "Thermal Decomposition",
        "description": "Limestone (calcium carbonate) decomposes when heated to produce quicklime and carbon dioxide.",
        "energy": "Endothermic (requires heat)",
        "balanced": True
    },
    "respiration": {
        "equation": "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O",
        "type": "Cellular Respiration",
        "description": "Glucose reacts with oxygen to produce energy, carbon dioxide, and water. This is how your body gets energy!",
        "energy": "Exothermic (-2880 kJ/mol)",
        "balanced": True
    },
    "sodium water": {
        "equation": "2Na + 2H₂O → 2NaOH + H₂",
        "type": "Single Displacement",
        "description": "Sodium reacts violently with water to produce sodium hydroxide and hydrogen gas. The hydrogen often ignites!",
        "energy": "Highly Exothermic (explosive)",
        "balanced": True
    },
    "baking soda vinegar": {
        "equation": "NaHCO₃ + CH₃COOH → CH₃COONa + H₂O + CO₂",
        "type": "Acid-Base",
        "description": "Baking soda reacts with vinegar (acetic acid) to produce sodium acetate, water, and carbon dioxide bubbles.",
        "energy": "Endothermic (feels cold)",
        "balanced": True
    },
    "formation ammonia": {
        "equation": "N₂ + 3H₂ ⇌ 2NH₃",
        "type": "Equilibrium (Haber Process)",
        "description": "Nitrogen and hydrogen reach equilibrium with ammonia. Pressure and temperature affect the yield.",
        "energy": "Exothermic (-92 kJ/mol)",
        "balanced": True
    },
    "esterification": {
        "equation": "CH₃COOH + C₂H₅OH ⇌ CH₃COOC₂H₅ + H₂O",
        "type": "Esterification (Condensation)",
        "description": "Acetic acid reacts with ethanol to form ethyl acetate (fruity smell) and water. Requires acid catalyst.",
        "energy": "Slightly endothermic",
        "balanced": True
    }
}

# ============================================
# MOLAR MASS CALCULATOR
# ============================================

def calculate_molar_mass(formula):
    """Calculate molar mass from a simple formula like H2O, NaCl, H2SO4"""
    # Simplified parser for common formulas
    element_masses = {
        'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811,
        'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
        'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.086, 'P': 30.974,
        'S': 32.065, 'Cl': 35.453, 'K': 39.098, 'Ca': 40.078, 'Fe': 55.845,
        'Cu': 63.546, 'Zn': 65.380, 'Br': 79.904, 'Ag': 107.868, 'I': 126.904,
        'Ba': 137.327, 'Au': 196.967, 'Hg': 200.590, 'Pb': 207.200
    }
    
    mass = 0.0
    i = 0
    formula = formula.strip()
    
    while i < len(formula):
        # Get element symbol (1 or 2 letters)
        element = formula[i]
        i += 1
        while i < len(formula) and formula[i].islower():
            element += formula[i]
            i += 1
        
        # Get count
        count = 0
        while i < len(formula) and formula[i].isdigit():
            count = count * 10 + int(formula[i])
            i += 1
        
        if count == 0:
            count = 1
        
        if element in element_masses:
            mass += element_masses[element] * count
        else:
            return None  # Unknown element
    
    return mass

# ============================================
# pH CALCULATOR
# ============================================

def ph_calculator():
    print("\n" + "═"*55)
    print("  🔬 pH CALCULATOR")
    print("═"*55)
    print("  1. Calculate pH from [H⁺] concentration")
    print("  2. Calculate [H⁺] from pH")
    print("  3. pH of common substances")
    print("═"*55)
    
    choice = input("  Choose (1-3): ").strip()
    
    if choice == '1':
        try:
            h_conc = float(input("  Enter [H⁺] concentration (mol/L): "))
            import math
            ph = -math.log10(h_conc)
            print(f"\n  pH = {ph:.2f}")
            if ph < 7:
                print(f"  This is ACIDIC (strong acid)" if ph < 3 else "  This is ACIDIC (weak acid)")
            elif ph == 7:
                print(f"  This is NEUTRAL (pure water)")
            else:
                print(f"  This is BASIC/ALKALINE (strong base)" if ph > 11 else "  This is BASIC/ALKALINE (weak base)")
        except:
            print("  Invalid input!")
    
    elif choice == '2':
        try:
            ph = float(input("  Enter pH value: "))
            import math
            h_conc = 10**(-ph)
            print(f"\n  [H⁺] = {h_conc:.6e} mol/L")
        except:
            print("  Invalid input!")
    
    elif choice == '3':
        common = {
            "Stomach Acid": 1.5,
            "Lemon Juice": 2.0,
            "Vinegar": 2.9,
            "Orange Juice": 3.5,
            "Tomato Juice": 4.0,
            "Black Coffee": 5.0,
            "Urine": 6.0,
            "Pure Water": 7.0,
            "Blood": 7.4,
            "Seawater": 8.0,
            "Baking Soda": 8.5,
            "Soap": 10.0,
            "Household Ammonia": 11.5,
            "Bleach": 12.5,
            "Drain Cleaner": 14.0
        }
        print("\n  COMMON SUBSTANCES pH:\n")
        for substance, ph in common.items():
            bar = "█" * int(ph * 2)
            print(f"  {substance:20s}  pH {ph:4.1f}  {bar}")
    
    input("\n  Press Enter to continue...")

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_element_from_api(query):
    """Display element data from API or local database"""
    print("\n  🔍 Searching PubChem API...")
    data = get_element_data(query)
    
    if data:
        print("\n" + "═"*55)
        print(f"  🧪 {data.get('ElementName', 'Unknown')}")
        print("═"*55)
        print(f"  Atomic Number: {data.get('AtomicNumber', 'N/A')}")
        print(f"  Symbol:        {data.get('ElementSymbol', 'N/A')}")
        print(f"  Atomic Mass:   {data.get('AtomicMass', 'N/A')} u")
        print(f"  Group:         {data.get('GroupBlock', {}).get('Group', 'N/A')}")
        print(f"  Period:        {data.get('Period', 'N/A')}")
        print(f"  Block:         {data.get('GroupBlock', {}).get('Block', 'N/A')}")
        print(f"  Electronegativity: {data.get('Electronegativity', 'N/A')}")
        print(f"  Melting Point: {data.get('MeltingPointKelvin', 'N/A')} K")
        print(f"  Boiling Point: {data.get('BoilingPointKelvin', 'N/A')} K")
        print(f"  Density:       {data.get('Density', 'N/A')} g/cm³")
        print("═"*55)
        print(f"  📚 More info: https://pubchem.ncbi.nlm.nih.gov/element/{data.get('ElementName', '')}")
    else:
        print("  ❌ Element not found in API. Check your spelling or try the symbol.")

def display_reaction(search_term):
    """Find and display reaction equations"""
    search_term = search_term.lower().strip()
    
    # Search through reactions
    found = None
    for key, reaction in REACTIONS.items():
        if search_term in key or search_term in reaction['equation'].lower():
            found = reaction
            break
    
    if found:
        print("\n" + "═"*55)
        print(f"  ⚗️  REACTION EQUATION")
        print("═"*55)
        print(f"\n  {found['equation']}")
        print(f"\n  Type:        {found['type']}")
        print(f"  Energy:      {found['energy']}")
        print(f"  Description: {found['description']}")
        print(f"  Balanced:    {'✅ Yes' if found['balanced'] else '❌ No'}")
        print("═"*55)
    else:
        print(f"\n  ❌ No reaction found for '{search_term}'.")
        print("  Try: photosynthesis, rust formation, neutralization, respiration, etc.")
        print("  Available reactions:")
        for key in sorted(REACTIONS.keys()):
            print(f"    • {key}")

def compound_search():
    """Search for chemical compounds"""
    compound = input("  Enter compound name (e.g., water, caffeine, aspirin): ").strip()
    print("\n  🔍 Searching PubChem...")
    
    info = get_compound_info(compound)
    if info:
        print(f"\n  ✅ Found: {info['name']}")
        print(f"  PubChem CID: {info['cid']}")
        print(f"  More details: {info['url']}")
    else:
        print(f"  ❌ Compound not found or API unavailable.")
    
    input("\n  Press Enter to continue...")

# ============================================
# MAIN MENU
# ============================================

def main():
    while True:
        clear()
        print("╔" + "═"*53 + "╗")
        print("║" + "  ⚗️  ADVANCED CHEMISTRY LAB  ".center(53) + "║")
        print("║" + "  Built by Vinnias Mbuthia (TechGlobal)  ".center(53) + "║")
        print("╠" + "═"*53 + "╣")
        print("║  1. 🧪 Element Lookup (PubChem API)        ║")
        print("║  2. ⚗️  Reaction Equations                  ║")
        print("║  3. 🧬 Compound Search (PubChem API)       ║")
        print("║  4. ⚖️  Molar Mass Calculator               ║")
        print("║  5. 🔬 pH Calculator                       ║")
        print("║  6. 🎮 Chemistry Quiz                      ║")
        print("║  7. 🚪 Exit                                ║")
        print("╚" + "═"*53 + "╝")
        
        choice = input("\n  Choose (1-7): ").strip()
        
        if choice == '1':
            query = input("\n  Enter element name, symbol, or number: ").strip()
            display_element_from_api(query)
            input("\n  Press Enter to continue...")
        
        elif choice == '2':
            print("\n  📚 REACTION DATABASE")
            print("  Try: photosynthesis, rust, neutralization, respiration, haber process")
            print("  Or: sodium water, baking soda vinegar, combustion methane, electrolysis")
            search = input("\n  Enter reaction name or keyword: ").strip()
            display_reaction(search)
            input("\n  Press Enter to continue...")
        
        elif choice == '3':
            compound_search()
        
        elif choice == '4':
            print("\n" + "═"*55)
            print("  ⚖️  MOLAR MASS CALCULATOR")
            print("═"*55)
            print("  Enter chemical formula (e.g., H2O, NaCl, H2SO4, C6H12O6)")
            formula = input("  Formula: ").strip()
            mass = calculate_molar_mass(formula)
            if mass:
                print(f"\n  Molar Mass of {formula} = {mass:.4f} g/mol")
            else:
                print(f"\n  ❌ Could not parse formula '{formula}'")
            input("\n  Press Enter to continue...")
        
        elif choice == '5':
            ph_calculator()
        
        elif choice == '6':
            chemistry_quiz()
        
        elif choice == '7':
            print("\n  👋 Goodbye! Keep exploring chemistry! 🔬")
            break
        
        else:
            print("\n  ❌ Invalid choice!")
            input("  Press Enter to continue...")

def chemistry_quiz():
    questions = [
        ("What is the chemical formula for water?", "H2O"),
        ("What element has the symbol 'Fe'?", "Iron"),
        ("What is the pH of pure water?", "7"),
        ("What gas do plants take in during photosynthesis?", "CO2"),
        ("What is the most abundant element in the universe?", "Hydrogen"),
        ("What acid is found in vinegar?", "Acetic acid"),
        ("What is the chemical formula for table salt?", "NaCl"),
        ("What element is diamond made of?", "Carbon"),
        ("What is the lightest element?", "Hydrogen"),
        ("What element has atomic number 8?", "Oxygen"),
        ("What process converts sugar to energy in cells?", "Respiration"),
        ("What gas makes up 78% of Earth's atmosphere?", "Nitrogen"),
        ("What is the chemical symbol for gold?", "Au"),
        ("What type of bond shares electrons?", "Covalent"),
        ("What is the formula for baking soda?", "NaHCO3"),
    ]
    
    print("\n" + "═"*55)
    print("  🎮 CHEMISTRY QUIZ")
    print("═"*55)
    
    score = 0
    total = 5
    selected = random.sample(questions, min(total, len(questions)))
    
    for i, (question, answer) in enumerate(selected, 1):
        user_answer = input(f"\n  Q{i}: {question}\n  > ").strip()
        if user_answer.lower() == answer.lower():
            print("  ✅ Correct!")
            score += 1
        else:
            print(f"  ❌ Wrong! Answer: {answer}")
    
    print(f"\n  🏆 Score: {score}/{total}")
    if score == total:
        print("  🎉 Perfect! You're a chemistry master!")
    elif score >= total//2:
        print("  👍 Good job!")
    else:
        print("  📚 Keep studying!")
    
    input("\n  Press Enter to continue...")

if __name__ == "__main__":
    main()
