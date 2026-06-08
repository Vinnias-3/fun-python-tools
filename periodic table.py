import periodictable
import os
import textwrap

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def element_details(el):
    print("\n" + "═"*55)
    print(f"  🧪  {el.name.upper()} ({el.symbol})")
    print("═"*55)
    print(f"  Atomic Number:    {el.number}")
    print(f"  Atomic Mass:      {el.mass} u")
    print(f"  Symbol:           {el.symbol}")
    
    # Density
    try:
        print(f"  Density:          {el.density:.4f} g/cm³")
    except:
        print(f"  Density:          Data unavailable")
    
    # Category / Type
    category = "Unknown"
    if el.number in [1,2,3,4,5,6,7,8,9,10]:
        if el.number in [1]: category = "Nonmetal (Diatomic Gas)"
        elif el.number == 2: category = "Noble Gas"
        else: category = "Nonmetal"
    elif 3 <= el.number <= 5: category = "Metal"
    elif el.number == 6: category = "Nonmetal (Essential for Life)"
    elif el.number == 7: category = "Nonmetal (Diatomic Gas - 78% of Air)"
    elif el.number == 8: category = "Nonmetal (Diatomic Gas - 21% of Air)"
    elif el.number == 9: category = "Halogen (Most Reactive)"
    elif el.number == 10: category = "Noble Gas"
    elif 11 <= el.number <= 12: category = "Alkali Metal" if el.number==11 else "Alkaline Earth Metal"
    elif el.number == 13: category = "Post-transition Metal"
    elif el.number == 14: category = "Metalloid (Semiconductor)"
    elif el.number == 15: category = "Nonmetal (Essential for DNA)"
    elif el.number == 16: category = "Nonmetal"
    elif el.number == 17: category = "Halogen"
    elif el.number == 18: category = "Noble Gas"
    elif 19 <= el.number <= 20: category = "Alkali Metal" if el.number==19 else "Alkaline Earth Metal"
    elif 21 <= el.number <= 30: category = "Transition Metal"
    elif el.number == 26: category = "Transition Metal (Most Abundant on Earth)"
    elif el.number == 29: category = "Transition Metal (Excellent Conductor)"
    elif el.number == 30: category = "Transition Metal"
    elif el.number == 47: category = "Transition Metal (Best Electrical Conductor)"
    elif el.number == 79: category = "Transition Metal (Precious)"
    elif el.number == 80: category = "Transition Metal (Liquid at Room Temp)"
    elif el.number == 82: category = "Post-transition Metal (Toxic)"
    elif el.number == 92: category = "Actinide (Nuclear Fuel)"
    elif el.number == 94: category = "Actinide (Nuclear Weapons)"
    elif 57 <= el.number <= 71: category = "Lanthanide (Rare Earth)"
    elif 89 <= el.number <= 103: category = "Actinide (Radioactive)"
    elif el.number > 103: category = "Superheavy (Synthetic)"
    
    print(f"  Category:         {category}")
    
    # State at room temperature
    if el.number in [1,2,7,8,9,10,17,18,36,54,86]: state = "Gas"
    elif el.number in [35,80]: state = "Liquid"
    else: state = "Solid"
    print(f"  State (20°C):     {state}")
    
    # Electron configuration placeholder
    shells = [2,8,8,18,18,32,32]
    print(f"  Electron Shells:  {el.number} electrons")
    
    # Fun facts
    facts = {
        1: "Lightest element. Makes up 75% of the universe.",
        2: "Second lightest. Used in balloons and airships.",
        3: "Lightest metal. Used in batteries and mood stabilizers.",
        6: "Basis of all organic life. Found in diamonds and graphite.",
        7: "Makes up 78% of Earth's atmosphere.",
        8: "Essential for respiration. 21% of the air we breathe.",
        11: "Explodes in water! Found in table salt with chlorine.",
        12: "Burns with a brilliant white flame. Used in fireworks.",
        13: "Most abundant metal in Earth's crust.",
        14: "Semiconductor. The foundation of computer chips.",
        15: "Glows in the dark (white phosphorus). Essential for DNA.",
        16: "Smells like rotten eggs when combined with hydrogen.",
        17: "Used in water purification and as a chemical weapon in WWI.",
        19: "Reactive metal. Essential for plant growth (fertilizers).",
        20: "Builds strong bones and teeth.",
        22: "Strong as steel but 45% lighter. Used in aircraft.",
        24: "Makes rubies red and emeralds green.",
        25: "Essential trace mineral. Named after magnesium (confusing!).",
        26: "Most abundant element on Earth by mass. Blood is red because of iron.",
        27: "Essential for vitamin B12. Named after goblins (kobold).",
        28: "Used in coins and guitar strings.",
        29: "First metal used by humans. Excellent electrical conductor.",
        30: "Essential for immune system. Used in sunscreens.",
        47: "Best electrical conductor. Used in jewelry and photography.",
        50: "Used to make bronze. The 'tin cry' is a crackling sound when bent.",
        74: "Highest melting point of all metals. Used in light bulb filaments.",
        78: "Precious metal. Used in catalytic converters.",
        79: "The most malleable metal. 1 gram can be beaten into a 1m² sheet.",
        80: "Only liquid metal at room temperature. Toxic.",
        82: "Used in car batteries. Poisonous to humans.",
        92: "Heaviest naturally occurring element. Nuclear reactor fuel.",
        94: "Used in nuclear weapons and space probe power sources.",
    }
    
    if el.number in facts:
        print(f"  💡 Fun Fact:      {facts[el.number]}")
    
    print("═"*55)

def search_by_property():
    print("\n" + "═"*55)
    print("  🔍 ADVANCED SEARCH")
    print("═"*55)
    print("  1. Search by density range")
    print("  2. Search by mass range")
    print("  3. Search by name contains")
    print("  4. List all elements")
    print("  5. Category overview")
    print("═"*55)
    
    choice = input("  Choose option (1-5): ").strip()
    
    if choice == '1':
        try:
            low = float(input("  Minimum density (g/cm³): "))
            high = float(input("  Maximum density (g/cm³): "))
            print(f"\n  Elements with density between {low} and {high} g/cm³:\n")
            for el in periodictable.elements:
                try:
                    if low <= el.density <= high:
                        print(f"    {el.symbol:3s} - {el.name:15s} ({el.density:.3f} g/cm³)")
                except:
                    pass
        except ValueError:
            print("  Invalid input!")
    
    elif choice == '2':
        try:
            low = float(input("  Minimum atomic mass (u): "))
            high = float(input("  Maximum atomic mass (u): "))
            print(f"\n  Elements with mass between {low} and {high} u:\n")
            for el in periodictable.elements:
                if low <= el.mass <= high:
                    print(f"    {el.symbol:3s} - {el.name:15s} ({el.mass:.4f} u)")
        except ValueError:
            print("  Invalid input!")
    
    elif choice == '3':
        substring = input("  Enter part of element name: ").strip().lower()
        print(f"\n  Elements containing '{substring}':\n")
        count = 0
        for el in periodictable.elements:
            if substring in el.name.lower():
                print(f"    {el.symbol:3s} - {el.name:15s} (Z={el.number})")
                count += 1
        print(f"\n  Found {count} element(s).")
    
    elif choice == '4':
        print("\n  ALL ELEMENTS:\n")
        for i, el in enumerate(periodictable.elements, 1):
            if el.number > 0:
                print(f"    {el.number:3d}. {el.symbol:3s} - {el.name:15s} (Mass: {el.mass:.3f})")
                if i % 20 == 0:
                    input("\n  Press Enter for next page...")
        print("\n  End of list.")
    
    elif choice == '5':
        print("\n  📚 ELEMENT CATEGORIES:\n")
        print("  • Alkali Metals (Group 1)     - Highly reactive, soft")
        print("  • Alkaline Earths (Group 2)   - Reactive, harder")
        print("  • Transition Metals           - Hard, high melting points")
        print("  • Lanthanides                 - Rare earth elements")
        print("  • Actinides                   - Radioactive")
        print("  • Metalloids                  - Semiconductor properties")
        print("  • Nonmetals                   - Gases or brittle solids")
        print("  • Halogens (Group 17)         - Very reactive nonmetals")
        print("  • Noble Gases (Group 18)      - Chemically inert")
    
    input("\n  Press Enter to continue...")

def quiz_mode():
    import random
    print("\n" + "═"*55)
    print("  🎮 QUIZ MODE")
    print("═"*55)
    print("  Test your knowledge of the periodic table!")
    print("═"*55)
    
    score = 0
    questions = 5
    
    # Get real elements (skip neutrons and other non-elements)
    real_elements = [el for el in periodictable.elements if el.number > 0 and el.number <= 103]
    
    for q in range(1, questions + 1):
        el = random.choice(real_elements)
        question_type = random.randint(1, 3)
        
        if question_type == 1:
            answer = input(f"\n  Q{q}: What is the SYMBOL for '{el.name}'? ").strip()
            correct = el.symbol
        elif question_type == 2:
            answer = input(f"\n  Q{q}: What is the ATOMIC NUMBER of '{el.symbol}'? ").strip()
            correct = str(el.number)
        else:
            answer = input(f"\n  Q{q}: What is the NAME of element '{el.symbol}'? ").strip()
            correct = el.name
        
        if answer.lower() == correct.lower():
            print(f"  ✅ Correct! +1 point")
            score += 1
        else:
            print(f"  ❌ Wrong! The answer was: {correct}")
    
    print(f"\n  🏆 Quiz Complete! Score: {score}/{questions}")
    if score == questions:
        print("  🎉 Perfect! You're a chemistry genius!")
    elif score >= questions//2:
        print("  👍 Good job! Keep studying!")
    else:
        print("  📚 Time to hit the books!")
    
    input("\n  Press Enter to continue...")

def compare_elements():
    print("\n" + "═"*55)
    print("  ⚖️  ELEMENT COMPARISON")
    print("═"*55)
    
    el1_str = input("  Enter first element (name/symbol/number): ").strip()
    el2_str = input("  Enter second element (name/symbol/number): ").strip()
    
    def find_element(query):
        if query.isdigit():
            return periodictable.elements[int(query)]
        for el in periodictable.elements:
            if el.symbol.lower() == query.lower() or el.name.lower() == query.lower():
                return el
        return None
    
    el1 = find_element(el1_str)
    el2 = find_element(el2_str)
    
    if not el1 or not el2:
        print("  ❌ One or both elements not found!")
        input("\n  Press Enter to continue...")
        return
    
    print(f"\n  {'Property':30s} {el1.name:15s} {el2.name:15s}")
    print("  " + "-"*62)
    print(f"  {'Atomic Number':30s} {el1.number:<15d} {el2.number:<15d}")
    print(f"  {'Atomic Mass':30s} {el1.mass:<15.4f} {el2.mass:<15.4f}")
    
    try:
        print(f"  {'Density (g/cm³)':30s} {el1.density:<15.4f} {el2.density:<15.4f}")
    except:
        print(f"  {'Density (g/cm³)':30s} {'N/A':15s} {'N/A':15s}")
    
    ratio = el1.mass / el2.mass if el2.mass > 0 else 0
    if ratio > 1:
        print(f"\n  📊 {el1.name} is {ratio:.2f}x heavier than {el2.name}")
    elif ratio > 0:
        print(f"\n  📊 {el2.name} is {1/ratio:.2f}x heavier than {el1.name}")
    
    input("\n  Press Enter to continue...")

# ============================================
# MAIN MENU
# ============================================
while True:
    clear()
    print("╔" + "═"*53 + "╗")
    print("║" + "  🧪  PERIODIC TABLE EXPLORER  ".center(53) + "║")
    print("║" + "  Built by Vinnias Mbuthia (TechGlobal)  ".center(53) + "║")
    print("╠" + "═"*53 + "╣")
    print("║" + "  1. 🔍 Look up an element                ".ljust(53) + "║")
    print("║" + "  2. ⚖️  Compare two elements              ".ljust(53) + "║")
    print("║" + "  3. 📊 Advanced search                   ".ljust(53) + "║")
    print("║" + "  4. 🎮 Quiz mode                         ".ljust(53) + "║")
    print("║" + "  5. 🚪 Exit                              ".ljust(53) + "║")
    print("╚" + "═"*53 + "╝")
    
    choice = input("\n  Choose option (1-5): ").strip()
    
    if choice == '1':
        query = input("  Enter element name, symbol, or atomic number: ").strip()
        element = None
        
        if query.isdigit():
            element = periodictable.elements[int(query)]
        
        if not element:
            for el in periodictable.elements:
                if el.symbol.lower() == query.lower():
                    element = el
                    break
        
        if not element:
            for el in periodictable.elements:
                if el.name.lower() == query.lower():
                    element = el
                    break
        
        if element:
            element_details(element)
        else:
            print(f"\n  ❌ Element '{query}' not found!")
        
        input("\n  Press Enter to continue...")
    
    elif choice == '2':
        compare_elements()
    
    elif choice == '3':
        search_by_property()
    
    elif choice == '4':
        quiz_mode()
    
    elif choice == '5':
        print("\n  👋 Goodbye! Keep exploring chemistry!")
        break
    
    else:
        print("\n  ❌ Invalid choice! Try again.")
        input("  Press Enter to continue...")
