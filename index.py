from tabulate import tabulate

def elementInfo():
    #period table info
    periodicElements = [
    [1, "H", "Hydrogen", "1.0078", "Nonmetal", "-252.87°C", "-259.16°C"],
    [2, "He", "Helium", "4.0026", "Noble Gas", "-268.9°C", "-272.2°C"],
    [3, "Li", "Lithium", "6.941", "Alkali Metal", "1,342°C", "180.5°C"],
    [4, "Be", "Beryllium", "9.0122", "Alkaline Earth Metal", "2,970°C", "1,287°C"],
    [5, "B", "Boron", "10.81", "Metalloid", "2,550°C", "2,300°C"],
    [6, "C", "Carbon", "12.011", "Nonmetal", "4,827°C", "3,550°C"],
    [7, "N", "Nitrogen", "14.007", "Nonmetal", "-195.8°C", "-210.0°C"],
    [8, "O", "Oxygen", "15.999", "Nonmetal", "-182.9°C", "-218.4°C"],
    [9, "F", "Fluorine", "18.998", "Halogen", "-188.1°C", "-219.6°C"],
    [10, "Ne", "Neon", "20.180", "Noble Gas", "-246.1°C", "-248.7°C"],
    [11, "Na", "Sodium", "22.990", "Alkali Metal", "883°C", "97.8°C"],
    [12, "Mg", "Magnesium", "24.305", "Alkaline Earth Metal", "1,109°C", "650°C"],
    [13, "Al", "Aluminum", "26.982", "Post-Transition Metal", "2,519°C", "660°C"],
    [14, "Si", "Silicon", "28.085", "Metalloid", "3,265°C", "1,414°C"],
    [15, "P", "Phosphorus", "30.974", "Nonmetal", "280.5°C", "44.1°C"],
    [16, "S", "Sulfur", "32.06", "Nonmetal", "444.6°C", "115.2°C"],
    [17, "Cl", "Chlorine", "35.45", "Halogen", "-34.04°C", "-101.5°C"],
    [18, "Ar", "Argon", "39.948", "Noble Gas", "-185.8°C", "-189.4°C"],
    [19, "K", "Potassium", "39.098", "Alkali Metal", "759°C", "63.5°C"],
    [20, "Ca", "Calcium", "40.078", "Alkaline Earth Metal", "1,484°C", "842°C"],
    [21, "Sc", "Scandium", "44.956", "Transition Metal", "2,927°C", "1,538°C"],
    [22, "Ti", "Titanium", "47.867", "Transition Metal", "3,287°C", "1,668°C"],
    [23, "V", "Vanadium", "50.942", "Transition Metal", "3,000°C", "1,890°C"],
    [24, "Cr", "Chromium", "51.996", "Transition Metal", "2,672°C", "1,907°C"],
    [25, "Mn", "Manganese", "54.938", "Transition Metal", "2,083°C", "1,244°C"],
    [26, "Fe", "Iron", "55.845", "Transition Metal", "2,861°C", "1,538°C"],
    [27, "Co", "Cobalt", "58.933", "Transition Metal", "2,927°C", "1,495°C"],
    [28, "Ni", "Nickel", "58.693", "Transition Metal", "2,730°C", "1,455°C"],
    [29, "Cu", "Copper", "63.546", "Transition Metal", "2,567°C", "1,085°C"],
    [30, "Zn", "Zinc", "65.38", "Transition Metal", "907°C", "419.5°C"],
    [31, "Ga", "Gallium", "69.723", "Post-Transition Metal", "2,403°C", "29.8°C"],
    [32, "Ge", "Germanium", "72.63", "Metalloid", "2,830°C", "937.4°C"],
    [33, "As", "Arsenic", "74.922", "Metalloid", "613°C", "817°C"],
    [34, "Se", "Selenium", "78.971", "Nonmetal", "685°C", "221°C"],
    [35, "Br", "Bromine", "79.904", "Halogen", "58.8°C", "-7.2°C"],
    [36, "Kr", "Krypton", "83.798", "Noble Gas", "-152.3°C", "-157.2°C"],
    [37, "Rb", "Rubidium", "85.468", "Alkali Metal", "688°C", "39.3°C"],
    [38, "Sr", "Strontium", "87.62", "Alkaline Earth Metal", "1,382°C", "769°C"],
    [39, "Y", "Yttrium", "88.906", "Transition Metal", "3,338°C", "1,522°C"],
    [40, "Zr", "Zirconium", "91.224", "Transition Metal", "4,460°C", "1,852°C"],
    [41, "Nb", "Niobium", "92.906", "Transition Metal", "4,927°C", "2,477°C"],
    [42, "Mo", "Molybdenum", "95.95", "Transition Metal", "4,639°C", "2,623°C"],
    [43, "Tc", "Technetium", "98", "Transition Metal", "4,877°C", "2,200°C"],
    [44, "Ru", "Ruthenium", "101.07", "Transition Metal", "4,196°C", "2,310°C"],
    [45, "Rh", "Rhodium", "102.91", "Transition Metal", "3,719°C", "1,964°C"],
    [46, "Pd", "Palladium", "106.42", "Transition Metal", "2,962°C", "1,555°C"],
    [47, "Ag", "Silver", "107.87", "Transition Metal", "2,212°C", "961.8°C"],
    [48, "Cd", "Cadmium", "112.41", "Transition Metal", "767°C", "321.1°C"],
    [49, "In", "Indium", "114.82", "Post-Transition Metal", "2,070°C", "156.6°C"],
    [50, "Sn", "Tin", "118.71", "Post-Transition Metal", "2,270°C", "231.9°C"],
    [51, "Sb", "Antimony", "121.76", "Metalloid", "1,635°C", "630.5°C"],
    [52, "Te", "Tellurium", "127.6", "Metalloid", "989.8°C", "449.5°C"],
    [53, "I", "Iodine", "126.90", "Halogen", "184.0°C", "113.5°C"],
    [54, "Xe", "Xenon", "131.29", "Noble Gas", "-108.0°C", "-111.9°C"],
    [55, "Cs", "Cesium", "132.91", "Alkali Metal", "671°C", "28.5°C"],
    [56, "Ba", "Barium", "137.33", "Alkaline Earth Metal", "1,441°C", "727°C"],
    [57, "La", "Lanthanum", "138.91", "Lanthanide", "3,464°C", "918°C"],
    [58, "Ce", "Cerium", "140.12", "Lanthanide", "3,175°C", "798°C"],
    [59, "Pr", "Praseodymium", "140.91", "Lanthanide", "3,430°C", "931°C"],
    [60, "Nd", "Neodymium", "144.24", "Lanthanide", "3,460°C", "1,021°C"],
    [61, "Pm", "Promethium", "145", "Lanthanide", "3,000°C", "1,100°C"],
    [62, "Sm", "Samarium", "150.36", "Lanthanide", "1,795°C", "1,072°C"],
    [63, "Eu", "Europium", "151.96", "Lanthanide", "1,822°C", "826°C"],
    [64, "Gd", "Gadolinium", "157.25", "Lanthanide", "3,233°C", "1,312°C"],
    [65, "Tb", "Terbium", "158.93", "Lanthanide", "3,230°C", "1,356°C"],
    [66, "Dy", "Dysprosium", "162.50", "Lanthanide", "2,562°C", "1,412°C"],
    [67, "Ho", "Holmium", "164.93", "Lanthanide", "2,700°C", "1,474°C"],
    [68, "Er", "Erbium", "167.26", "Lanthanide", "2,860°C", "1,529°C"],
    [69, "Tm", "Thulium", "168.93", "Lanthanide", "1,950°C", "1,545°C"],
    [70, "Yb", "Ytterbium", "173.05", "Lanthanide", "1,465°C", "824°C"],
    [71, "Lu", "Lutetium", "174.97", "Lanthanide", "3,402°C", "1,663°C"],
    [72, "Hf", "Hafnium", "178.49", "Transition Metal", "5,471°C", "2,223°C"],
    [73, "Ta", "Tantalum", "180.95", "Transition Metal", "5,425°C", "2,996°C"],
    [74, "W", "Tungsten", "183.84", "Transition Metal", "5,555°C", "3,422°C"],
    [75, "Re", "Rhenium", "186.21", "Transition Metal", "5,597°C", "3,180°C"],
    [76, "Os", "Osmium", "190.23", "Transition Metal", "5,012°C", "3,033°C"],
    [77, "Ir", "Iridium", "192.22", "Transition Metal", "4,527°C", "2,442°C"],
    [78, "Pt", "Platinum", "195.08", "Transition Metal", "3,827°C", "1,772°C"],
    [79, "Au", "Gold", "196.97", "Transition Metal", "2,970°C", "1,064°C"],
    [80, "Hg", "Mercury", "200.59", "Transition Metal", "-38.83°C", "-37.89°C"],
    [81, "Tl", "Thallium", "204.38", "Post-Transition Metal", "1,473°C", "304°C"],
    [82, "Pb", "Lead", "207.2", "Post-Transition Metal", "1,740°C", "327.5°C"],
    [83, "Bi", "Bismuth", "208.98", "Post-Transition Metal", "1,564°C", "271.4°C"],
    [84, "Po", "Polonium", "209", "Metalloid", "962°C", "254°C"],
    [85, "At", "Astatine", "210", "Halogen", "337°C", "302°C"],
    [86, "Rn", "Radon", "222", "Noble Gas", "-61.8°C", "-71.0°C"],
    [87, "Fr", "Francium", "223", "Alkali Metal", "677°C", "27°C"],
    [88, "Ra", "Radium", "226", "Alkaline Earth Metal", "1,737°C", "700°C"],
    [89, "Ac", "Actinium", "227", "Actinide", "4,000°C", "1,050°C"],
    [90, "Th", "Thorium", "232.04", "Actinide", "4,788°C", "1,750°C"],
    [91, "Pa", "Protactinium", "231.04", "Actinide", "4,027°C", "1,568°C"],
    [92, "U", "Uranium", "238.03", "Actinide", "4,142°C", "1,135°C"],
    [93, "Np", "Neptunium", "237", "Actinide", "4,730°C", "640°C"],
    [94, "Pu", "Plutonium", "244", "Actinide", "3,100°C", "640°C"],
    [95, "Am", "Americium", "243", "Actinide", "2,600°C", "994°C"],
    [96, "Cm", "Curium", "247", "Actinide", "2,467°C", "1,340°C"],
    [97, "Bk", "Berkelium", "247", "Actinide", "2,590°C", "986°C"],
    [98, "Cf", "Californium", "251", "Actinide", "1,470°C", "900°C"],
    [99, "Es", "Einsteinium", "252", "Actinide", "1,260°C", "-"],
    [100, "Fm", "Fermium", "257", "Actinide", "-", "-"],
    [101, "Md", "Mendelevium", "258", "Actinide", "-", "-"],
    [102, "No", "Nobelium", "259", "Actinide", "-", "-"],
    [103, "Lr", "Lawrencium", "262", "Actinide", "-", "-"],
    [104, "Rf", "Rutherfordium", "267", "Transition Metal", "-", "-"],
    [105, "Db", "Dubnium", "268", "Transition Metal", "-", "-"],
    [106, "Sg", "Seaborgium", "269", "Transition Metal", "-", "-"],
    [107, "Bh", "Bohrium", "270", "Transition Metal", "-", "-"],
    [108, "Hs", "Hassium", "269", "Transition Metal", "-", "-"],
    [109, "Mt", "Meitnerium", "278", "Unknown", "-", "-"],
    [110, "Ds", "Darmstadtium", "281", "Unknown", "-", "-"],
    [111, "Rg", "Roentgenium", "282", "Unknown", "-", "-"],
    [112, "Cn", "Copernicium", "285", "Transition Metal", "-", "-"],
    [113, "Nh", "Nihonium", "286", "Unknown", "-", "-"],
    [114, "Fl", "Flerovium", "289", "Post-Transition Metal", "-", "-"],
    [115, "Mc", "Moscovium", "290", "Unknown", "-", "-"],
    [116, "Lv", "Livermorium", "293", "Post-Transition Metal", "-", "-"],
    [117, "Ts", "Tennessine", "294", "Unknown", "-", "-"],
    [118, "Og", "Oganesson", "294", "Unknown", "-", "-"]
    ]

    atomic_masses = {
            'H': 1.008,
            'He': 4.0026,
            'Li': 6.941,
            'Be': 9.0122,
            'B': 10.81,
            'C': 12.011,
            'N': 14.007,
            'O': 15.999,
            'F': 18.998,
            'Ne': 20.180,
            'Na': 22.990,
            'Mg': 24.305,
            'Al': 26.982,
            'Si': 28.085,
            'P': 30.974,
            'S': 32.06,
            'Cl': 35.45,
            'Ar': 39.948,
            'K': 39.098,
            'Ca': 40.078,
            'Sc': 44.956,
            'Ti': 47.867,
            'V': 50.942,
            'Cr': 51.996,
            'Mn': 54.938,
            'Fe': 55.845,
            'Co': 58.933,
            'Ni': 58.693,
            'Cu': 63.546,
            'Zn': 65.38,
            'Ga': 69.723,
            'Ge': 72.64,
            'As': 74.922,
            'Se': 78.971,
            'Br': 79.904,
            'Kr': 83.798,
            'Rb': 85.468,
            'Sr': 87.62,
            'Y': 88.906,
            'Zr': 91.224,
            'Nb': 92.906,
            'Mo': 95.95,
            'Tc': 98,
            'Ru': 101.07,
            'Rh': 102.91,
            'Pd': 106.42,
            'Ag': 107.87,
            'Cd': 112.41,
            'In': 114.82,
            'Sn': 118.71,
            'Sb': 121.76,
            'Te': 127.6,
            'I': 126.90,
            'Xe': 131.29,
            'Cs': 132.91,
            'Ba': 137.33,
            'La': 138.91,
            'Ce': 140.12,
            'Pr': 140.91,
            'Nd': 144.24,
            'Pm': 145,
            'Sm': 150.36,
            'Eu': 151.96,
            'Gd': 157.25,
            'Tb': 158.93,
            'Dy': 162.50,
            'Ho': 164.93,
            'Er': 167.26,
            'Tm': 168.93,
            'Yb': 173.05,
            'Lu': 174.97,
            'Hf': 178.49,
            'Ta': 180.95,
            'W': 183.84,
            'Re': 186.21,
            'Os': 190.23,
            'Ir': 192.22,
            'Pt': 195.08,
            'Au': 196.97,
            'Hg': 200.59,
            'Tl': 204.38,
            'Pb': 207.2,
            'Bi': 208.98,
            'Po': 209,
            'At': 210,
            'Rn': 222,
            'Fr': 223,
            'Ra': 226,
            'Ac': 227,
            'Th': 232.04,
            'Pa': 231.04,
            'U': 238.03,
            'Np': 237,
            'Pu': 244,
            'Am': 243,
            'Cm': 247,
            'Bk': 247,
            'Cf': 251,
            'Es': 252,
            'Fm': 257,
            'Md': 258,
            'No': 259,
            'Lr': 262,
            'Rf': 267,
            'Db': 268,
            'Sg': 269,
            'Bh': 270,
            'Hs': 269,
            'Mt': 278,
            'Ds': 281,
            'Rg': 282,
            'Cn': 285,
            'Nh': 286,
            'Fl': 289,
            'Mc': 290,
            'Lv': 293,
            'Ts': 294,
            'Og': 294
        }


#Function to sort elements based on user input
    def elementSort(sort_by=None, search=None):
        # Sort the elements if a sorting criterion is specified
        if sort_by:
            periodicElements.sort(key=lambda x: x[sort_by])

        # Search for elements if a search term is specified
        if search:
            search_results = [element for element in periodicElements if search.lower() in [str(attr).lower() for attr in element]]
            print(tabulate(search_results, headers=["Atomic Number", "Symbol", "Name", "Atomic Mass", "Chemical Group Block","Boiling Point", "Melting Point"]))
        else:
            print(tabulate(periodicElements, headers=["Atomic Number", "Symbol", "Name", "Atomic Mass", "Chemical Group Block","Boiling Point", "Melting Point"]))

    # Call elementSort function
    elementSort()

    # Loop function and stops under user input
    start = 'y'
    while start == 'y':
        choose = input('1 - Display All\n2 - Sort\n3 - Compute Molar Mass\n4 - Exit Elements Info\n>')
        if choose == '1':
            # Display all elements
            print(tabulate(periodicElements, headers=["Atomic Number", "Symbol", "Name", "Atomic Mass", "Chemical Group Block"]))
        elif choose == '2':
            # Call elementSort function
            elementSort(search=input('Enter Atomic number or Symbol or Name or Chemical Group Name to Sort: '))
        elif choose == '3':
            # Compute molar mass of a compound
            compound = input("Enter compound formula (e.g., H2O): ")
            molar_mass = compute_molar_mass(compound, atomic_masses)
            if molar_mass is not None:
                print(f"The molar mass of {compound} is {molar_mass} g/mol.")
        elif choose == '4':
            # Exit program
            return 0
        start = input('Try Again? (y/n): ')

# Function to compute molar mass of a compound
def compute_molar_mass(compound, atomic_masses):
    mass = 0
    i = 0
    while i < len(compound):
        # Check if the current character is an element symbol
        if compound[i] in atomic_masses:
            element = compound[i]
            i += 1
            num = ""
            # Check if the next character is a digit
            while i < len(compound) and compound[i].isdigit():
                num += compound[i]
                i += 1
            # Add the molar mass of the element with the appropriate multiplier
            mass += atomic_masses[element] * (int(num) if num else 1)
        else:
            print(f"Unknown element '{compound[i]}'")
            return None
    return mass


# Call the elementInfo display function, STARTS HERE
elementInfo()
