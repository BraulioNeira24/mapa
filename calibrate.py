# ============================================================
# PUNTOS CONFIRMADOS: (nombre, lat, lon, tikz_x_frac, tikz_y_frac)
# ============================================================
confirmed = [
    ("Poly U NY",               40.6933,  -73.9903, -0.195,  0.154),
    ("U of Toledo",             41.6639,  -83.5552, -0.219,  0.161),
    ("Virginia Military",       37.7840,  -79.4220, -0.210,  0.143),
    ("U of Evansville",         37.9677,  -87.5496, -0.231,  0.144),
    ("U of West Indies Mona",   18.0070,  -76.7666, -0.2035, 0.068),
    ("Boise State",             43.6035, -116.1990, -0.307,  0.169),
    ("Eastern Washington",      47.4420, -117.5911, -0.310,  0.175),
    ("Montana State",           45.6770, -111.0420, -0.300,  0.175),
    ("Portland State",          45.5118, -122.6839, -0.324,  0.175),
    ("Seattle U",               47.6097, -122.3200, -0.323,  0.181),
    ("Western Washington",      48.7474, -122.4913, -0.323,  0.177),
    ("U of Alaska Fairbanks",   64.8583, -147.8167, -0.390,  0.245),
]

# ============================================================
# TODAS las universidades de regiones 1-6
# ============================================================
universities = [
    # Region 1
    ("Boston U",                 42.3505,  -71.1054, 1, "Kappa Sigma"),
    ("City College NY",          40.8200,  -73.9490, 1, "Beta Pi"),
    ("Clarkson",                 44.6669,  -74.9107, 1, "Gamma Gamma"),
    ("Columbia",                 40.8075,  -73.9626, 1, "Gamma Lambda"),
    ("Cooper Union",             40.7267,  -73.9907, 1, "Delta Chi"),
    ("Cornell",                  42.4482,  -76.4817, 1, "Kappa"),
    ("Fairleigh Dickinson",      40.8656,  -74.0033, 1, "Theta Gamma"),
    ("Greater NY Alumni",        40.7580,  -73.9855, 1, "Greater NY Alumni"),
    ("Hofstra",                  40.7174,  -73.6015, 1, "Lambda Xi"),
    ("Manhattan",                40.8210,  -73.9390, 1, "Gamma Alpha"),
    ("MIT",                      42.3601,  -71.0942, 1, "Beta Theta"),
    ("Monmouth",                 40.2907,  -74.0267, 1, "Zeta Alpha"),
    ("NJIT",                     40.7424,  -74.1794, 1, "Gamma Kappa"),
    ("NYIT Old Westbury",        40.7835,  -73.6473, 1, "Iota Psi"),
    ("NYIT",                     40.7580,  -73.9855, 1, "Kappa Zeta"),
    ("NY Poly School Eng",       40.7267,  -73.9907, 1, "Theta Theta"),
    ("New York Poly",            40.7350,  -73.9950, 1, "Beta Beta"),
    ("NYU",                      40.7295,  -73.9965, 1, "Beta Zeta"),
    ("Northeastern",             42.3398,  -71.0892, 1, "Gamma Beta"),
    ("Norwich",                  44.1690,  -72.6517, 1, "Theta Xi"),
    ("Poly U NY",                40.6933,  -73.9903, 1, "Zeta Sigma"),
    ("Pratt",                    40.6920,  -73.9630, 1, "Delta Theta"),
    ("Princeton",                40.3431,  -74.6551, 1, "Epsilon Pi"),
    ("Rensselaer",               42.7298,  -73.6782, 1, "Beta Nu"),
    ("Rochester IT",             43.1249,  -77.6342, 1, "Iota Iota"),
    ("Rutgers",                  40.5007,  -74.4478, 1, "Gamma Epsilon"),
    ("SUNY Binghamton",          42.0897,  -75.9686, 1, "Kappa Epsilon"),
    ("SUNY New Paltz",           41.7446,  -74.0799, 1, "Kappa Omicron"),
    ("SUNY Buffalo",             42.9991,  -78.8478, 1, "Zeta Pi"),
    ("Stevens IT",               40.7449,  -74.0267, 1, "Iota Delta"),
    ("SUNY Stony Brook",         40.9176,  -73.1293, 1, "Theta Mu"),
    ("Syracuse",                 43.0386,  -76.1331, 1, "Gamma Eta"),
    ("College of NJ",            40.2682,  -74.7291, 1, "Nu Gamma"),
    ("Tufts",                    42.4085,  -71.1183, 1, "Epsilon Delta"),
    ("Union College",            42.8142,  -73.9788, 1, "Phi"),
    ("US Military Academy",      41.3900,  -73.9500, 1, "Iota Phi"),
    ("U of Bridgeport",          41.1807,  -73.1880, 1, "Theta Sigma"),
    ("U of Connecticut",         41.8069,  -72.2523, 1, "Beta Omega"),
    ("U of Hartford",            41.7709,  -72.6954, 1, "Iota Epsilon"),
    ("U of Maine",               44.9013,  -68.6706, 1, "Delta Kappa"),
    ("UMass Dartmouth",          41.6270,  -70.9833, 1, "Zeta Xi"),
    ("UMass Amherst",            42.3890,  -72.5275, 1, "Delta Eta"),
    ("UMass Lowell",             42.6530,  -71.3180, 1, "Epsilon Zeta"),
    ("U of New Haven",           41.2909,  -72.8970, 1, "Zeta Rho"),
    ("U of Rhode Island",        41.4863,  -71.5223, 1, "Zeta Gamma"),
    ("U of Rochester",           43.1249,  -77.6342, 1, "Nu Rho"),
    ("Wentworth IT",             42.3398,  -71.0950, 1, "Mu Mu"),
    ("Western New England",      42.1054,  -72.6301, 1, "Nu Lambda"),
    ("Worcester Poly",           42.2797,  -71.8111, 1, "Gamma Delta"),
    # Region 2
    ("Air Force IT",             39.0119,  -84.4975, 2, "Delta Xi"),
    ("Capitol Tech U",           38.9745,  -76.9308, 2, "Kappa Mu"),
    ("Carnegie Mellon",          40.4433,  -79.9433, 2, "Sigma"),
    ("Case Western Reserve",     41.5056,  -81.6086, 2, "Zeta"),
    ("Cleveland State",          41.5012,  -81.6753, 2, "Epsilon Alpha"),
    ("Drexel",                   39.9567,  -75.1899, 2, "Beta Alpha"),
    ("Gannon",                   42.1219,  -80.0828, 2, "Iota Nu"),
    ("George Mason",             38.8298,  -77.3075, 2, "Iota Mu"),
    ("George Washington",        38.8997,  -77.0490, 2, "Theta Iota"),
    ("Howard",                   38.9217,  -77.0197, 2, "Lambda Gamma"),
    ("Johns Hopkins",            39.3297,  -76.6205, 2, "Gamma Upsilon"),
    ("Lafayette",                40.6908,  -75.2095, 2, "Gamma Psi"),
    ("Lehigh",                   40.6122,  -75.3802, 2, "Chi"),
    ("Miami U Ohio",             39.5092,  -84.7761, 2, "Lambda Omicron"),
    ("Ohio State",               40.0019,  -83.0236, 2, "Gamma"),
    ("Ohio U",                   39.3247,  -82.1032, 2, "Delta Epsilon"),
    ("Penn State",               40.7982,  -77.8599, 2, "Epsilon"),
    ("Temple",                   39.9985,  -75.1547, 2, "Iota Sigma"),
    ("U of Akron",               41.0713,  -81.5138, 2, "Zeta Zeta"),
    ("U of Cincinnati",          39.1329,  -84.5150, 2, "Tau"),
    ("U of Dayton",              39.7292,  -84.1956, 2, "Iota Eta"),
    ("U of Delaware",            39.6837,  -75.7497, 2, "Epsilon Omicron"),
    ("U of DC",                  38.9310,  -77.0159, 2, "Iota Tau"),
    ("U of Maryland",            38.9869,  -76.9426, 2, "Gamma Xi"),
    ("U of Pennsylvania",        39.9522,  -75.1932, 2, "Lambda"),
    ("U of Pittsburgh",          40.4442,  -79.9582, 2, "Beta Delta"),
    ("U of Scranton",            41.4051,  -75.6534, 2, "Lambda Nu"),
    ("US Naval Academy",         38.9837,  -76.4822, 2, "Lambda Kappa"),
    ("Villanova",                40.0390,  -75.3488, 2, "Delta Mu"),
    ("WV Inst Tech",             37.7757,  -81.1808, 2, "Zeta Omicron"),
    ("West Virginia U",          39.6479,  -79.9693, 2, "Beta Rho"),
    ("Wilkes",                   41.2509,  -75.8804, 2, "Kappa Beta"),
    # Region 3
    ("Auburn",                   32.6022,  -85.4890, 3, "Xi"),
    ("Christopher Newport",      37.0660,  -76.4822, 3, "Mu Omicron"),
    ("Clemson",                  34.6767,  -82.8362, 3, "Zeta Iota"),
    ("Duke",                     36.0014,  -78.9382, 3, "Delta Lambda"),
    ("East Carolina",            35.6070,  -77.3680, 3, "Mu Lambda"),
    ("Embry-Riddle Daytona",     29.1735,  -81.0495, 3, "Lambda Upsilon"),
    ("FAMU-FSU",                 30.4427,  -84.2977, 3, "Lambda Delta"),
    ("Florida Atlantic",         26.3642,  -80.1158, 3, "Nu Omicron"),
    ("Florida IT",               28.0628,  -80.6248, 3, "Zeta Epsilon"),
    ("Florida International",    25.7559,  -80.3745, 3, "Kappa Delta"),
    ("Florida Poly",             28.0266,  -81.6678, 3, "Mu Omega"),
    ("Georgia Tech",             33.7755,  -84.3963, 3, "Beta Mu"),
    ("Hampton",                  37.0126,  -76.3469, 3, "Lambda Chi"),
    ("Kennesaw State",           34.0278,  -84.5778, 3, "Nu Epsilon"),
    ("Mississippi State",        33.4586,  -88.7923, 3, "Gamma Omega"),
    ("NC A&T",                   36.0716,  -79.8107, 3, "Theta Nu"),
    ("NC State",                 35.7848,  -78.6821, 3, "Beta Eta"),
    ("Old Dominion",             36.8853,  -76.3033, 3, "Zeta Upsilon"),
    ("Tennessee State",          36.1715,  -86.8110, 3, "Zeta Kappa"),
    ("Tennessee Tech",           36.1653,  -85.4928, 3, "Epsilon Rho"),
    ("U of West Indies Mona",    18.0070,  -76.7666, 3, "Nu Sigma"),
    ("Tuskegee",                 32.4282,  -85.7045, 3, "Epsilon Upsilon"),
    ("Union University",         35.6142,  -88.5209, 3, "Lambda Pi"),
    ("U of Alabama Birmingham",  33.5063,  -86.8053, 3, "Iota Alpha"),
    ("U of Alabama Huntsville",  34.7257,  -86.6450, 3, "Theta Eta"),
    ("U of Alabama",             33.2110,  -87.5406, 3, "Delta Nu"),
    ("U of Central Florida",     28.6024,  -81.2001, 3, "Zeta Chi"),
    ("U of Evansville",          37.9677,  -87.5496, 3, "Mu Chi"),
    ("U of Florida",             29.6436,  -82.3549, 3, "Epsilon Sigma"),
    ("U of Kentucky",            38.0353,  -84.5037, 3, "Beta Upsilon"),
    ("U of Louisville",          38.2118,  -85.7597, 3, "Epsilon Chi"),
    ("U of Memphis",             35.2058,  -89.9319, 3, "Kappa Lambda"),
    ("U of Miami",               25.7188,  -80.2775, 3, "Epsilon Kappa"),
    ("U of Mississippi",         34.3650,  -89.5347, 3, "Epsilon Omega"),
    ("U of NC Charlotte",        35.3074,  -80.7760, 3, "Kappa Phi"),
    ("U of North Florida",       30.2563,  -81.5108, 3, "Kappa Nu"),
    ("U of South Alabama",       30.7123,  -88.1593, 3, "Theta Lambda"),
    ("U of South Carolina",      34.0199,  -81.0423, 3, "Delta Phi"),
    ("U of South Florida",       28.0587,  -82.4138, 3, "Kappa Xi"),
    ("U of Tennessee",           35.9541,  -83.9286, 3, "Beta Phi"),
    ("U of Virginia",            38.0367,  -78.5050, 3, "Gamma Pi"),
    ("U of West Florida",        30.4835,  -87.2136, 3, "Lambda Alpha"),
    ("Vanderbilt",               36.1490,  -86.8026, 3, "Epsilon Lambda"),
    ("Virginia Commonwealth",    37.7822,  -77.4546, 3, "Kappa Chi"),
    ("Virginia Military",        37.7840,  -79.4220, 3, "Theta Phi"),
    ("Virginia Tech",            37.2284,  -80.4234, 3, "Beta Lambda"),
    # Region 4
    ("Bradley",                  40.7934,  -89.6140, 4, "Delta Upsilon"),
    ("Illinois IT",              41.7435,  -87.7521, 4, "Delta"),
    ("Iowa State",               42.0270,  -93.6460, 4, "Nu"),
    ("Kettering",                43.0080,  -83.7142, 4, "Theta Epsilon"),
    ("Lawrence Tech",            42.4560,  -83.2360, 4, "Theta Upsilon"),
    ("Marquette",                43.0401,  -87.9323, 4, "Beta Omicron"),
    ("Michigan State",           42.7319,  -84.4773, 4, "Gamma Zeta"),
    ("Michigan Tech",            47.1216,  -88.5563, 4, "Beta Gamma"),
    ("Milwaukee School Eng",     43.0419,  -87.9089, 4, "Iota Beta"),
    ("North Dakota State",       46.8951,  -96.8004, 4, "Gamma Tau"),
    ("Northern Illinois",        41.9343,  -88.7846, 4, "Kappa Alpha"),
    ("Northwestern",             42.0565,  -87.6748, 4, "Beta Tau"),
    ("Oakland U",                42.6866,  -83.2326, 4, "Iota Chi"),
    ("Purdue Northwest",         41.5481,  -87.3810, 4, "Nu Theta"),
    ("Purdue Indianapolis",      39.7714,  -86.1800, 4, "Kappa Rho"),
    ("Purdue",                   40.4286,  -86.9122, 4, "Beta"),
    ("Rose-Hulman",              39.4471,  -87.3686, 4, "Epsilon Eta"),
    ("SE Michigan Alumni",       42.3314,  -83.0458, 4, "SE Michigan Alumni"),
    ("St Cloud State",           45.5430,  -94.1632, 4, "Iota Omicron"),
    ("Trine U",                  41.6650,  -85.0200, 4, "Zeta Phi"),
    ("U of Detroit Mercy",       42.4400,  -83.1310, 4, "Beta Sigma"),
    ("U of Illinois Urbana",     40.1080,  -88.2272, 4, "Alpha"),
    ("U of Illinois Chicago",    41.8708,  -87.6505, 4, "Iota Lambda"),
    ("U of Iowa",                41.6611,  -91.5362, 4, "Beta Iota"),
    ("U of Michigan Dearborn",   42.3004,  -83.2335, 4, "Theta Tau"),
    ("U of Michigan",            42.2780,  -83.7382, 4, "Beta Epsilon"),
    ("U of Minnesota",           44.9730,  -93.2320, 4, "Omicron"),
    ("U of Nebraska",            40.7932,  -96.6728, 4, "Beta Psi"),
    ("U of North Dakota",        47.9251,  -97.0792, 4, "Delta Rho"),
    ("U of Notre Dame",          41.7042,  -86.2363, 4, "Delta Sigma"),
    ("U of Wisconsin Platteville",42.7635, -90.4814, 4, "Kappa Theta"),
    ("U of Wisconsin",           43.0766,  -89.4018, 4, "Theta"),
    ("Valparaiso",               41.4524,  -87.0334, 4, "Mu Rho"),
    ("Wayne State",              42.3584,  -83.0696, 4, "Delta Alpha"),
    ("Western Michigan",         42.2833,  -85.6081, 4, "Kappa Omega"),
    # Region 5
    ("Baylor",                   31.5488,  -97.1176, 5, "Kappa Tau"),
    ("Colorado School Mines",    39.7504, -105.2240, 5, "Nu Pi"),
    ("Colorado State",           40.5734, -105.0860, 5, "Delta Pi"),
    ("Kansas State",             39.2330,  -96.5749, 5, "Beta Kappa"),
    ("Lamar U Beaumont",         30.0810,  -94.1368, 5, "Delta Beta"),
    ("Louisiana State",          30.4200,  -91.1820, 5, "Delta Iota"),
    ("Louisiana Tech",           32.5249,  -92.6429, 5, "Delta Gamma"),
    ("Missouri S&T",             37.9539,  -91.7756, 5, "Gamma Theta"),
    ("Oklahoma State",           36.1272,  -97.0779, 5, "Omega"),
    ("Prairie View A&M",         30.0819,  -95.9786, 5, "Zeta Lambda"),
    ("South Dakota Mines",       44.0836, -103.2053, 5, "Beta Chi"),
    ("South Dakota State",       44.3166,  -96.7809, 5, "Gamma Rho"),
    ("Southern IL Carbondale",   37.7119,  -89.2200, 5, "Lambda Epsilon"),
    ("Southern IL Edwardsville", 38.7774,  -89.9884, 5, "Theta Omicron"),
    ("Southern Methodist",       32.8515,  -96.7884, 5, "Gamma Omicron"),
    ("Southern U A&M",           30.5084,  -91.1900, 5, "Zeta Psi"),
    ("St Louis U",               38.6481,  -90.3067, 5, "Delta Psi"),
    ("Texas A&M Kingsville",     27.4699,  -97.8672, 5, "Zeta Beta"),
    ("Texas A&M",                30.6179,  -96.3384, 5, "Gamma Mu"),
    ("Texas State",              29.8637,  -97.9367, 5, "Mu Upsilon"),
    ("Texas Tech",               33.5842, -101.8760, 5, "Gamma Nu"),
    ("Tulane",                   29.9634,  -90.1216, 5, "Theta Alpha"),
    ("U of Arkansas",            36.0708,  -94.1750, 5, "Gamma Phi"),
    ("U of Colorado CS",         40.5496, -105.0802, 5, "Theta Chi"),
    ("U of Colorado Denver",     39.7471, -104.9972, 5, "Theta Zeta"),
    ("U of Colorado Boulder",    40.0094, -105.2655, 5, "Rho"),
    ("U of Denver",              39.6781, -104.9619, 5, "Delta Delta"),
    ("U of Houston",             29.7199,  -95.3427, 5, "Epsilon Epsilon"),
    ("U of Kansas",              38.9561,  -95.2509, 5, "Gamma Iota"),
    ("U of Missouri Columbia",   38.9469,  -92.3293, 5, "Iota"),
    ("U of Missouri KC",         39.0250,  -94.5844, 5, "Theta Pi"),
    ("U of New Orleans",         29.9832,  -90.0658, 5, "Iota Rho"),
    ("U of North Texas",         33.2075,  -97.1526, 5, "Lambda Zeta"),
    ("U of Oklahoma",            35.2063,  -97.4437, 5, "Beta Xi"),
    ("U of Southwestern LA",     30.2120,  -92.0198, 5, "Delta Tau"),
    ("U of Texas Arlington",     32.7316,  -97.1106, 5, "Epsilon Mu"),
    ("U of Texas El Paso",       31.7710, -106.4380, 5, "Zeta Delta"),
    ("U of Texas SA",            29.5786,  -98.5970, 5, "Kappa Upsilon"),
    ("U of Texas Dallas",        32.9948,  -96.7505, 5, "Kappa Kappa"),
    ("U of Texas Austin",        30.2849,  -97.7341, 5, "Psi"),
    ("U of Tulsa",               36.1530,  -95.9470, 5, "Zeta Nu"),
    ("Washington U St Louis",    38.6493,  -90.3085, 5, "Delta Zeta"),
    ("Wichita State",            37.7179,  -97.2901, 5, "Epsilon Xi"),
    ("William Marsh Rice",       29.7174,  -95.4018, 5, "Theta Rho"),
    # Region 6
    ("Arizona State",            33.4242, -111.9281, 6, "Epsilon Beta"),
    ("Boise State",              43.6035, -116.1990, 6, "Kappa Pi"),
    ("Brigham Young",            40.2496, -111.6485, 6, "Zeta Eta"),
    ("Caltech",                  34.1378, -118.1253, 6, "Iota Pi"),
    ("Cal Poly SLO",             35.2790, -120.6545, 6, "Epsilon Phi"),
    ("Cal Poly Pomona",          34.0617, -117.7630, 6, "Zeta Theta"),
    ("Cal State Long Beach",     33.7866, -118.1170, 6, "Epsilon Theta"),
    ("Cal State Northridge",     34.2410, -118.5280, 6, "Lambda Beta"),
    ("Cal State Chico",          39.7291, -121.8471, 6, "Iota Zeta"),
    ("Cal State Fullerton",      33.8823, -117.8853, 6, "Iota Omega"),
    ("Cal State Fresno",         36.7378, -119.7870, 6, "Theta Kappa"),
    ("Cal State LA",             34.0650, -118.1700, 6, "Epsilon Nu"),
    ("Cal State Sacramento",     38.5615, -121.4238, 6, "Nu Upsilon"),
    ("Eastern Washington",       47.4420, -117.5911, 6, "Mu Delta"),
    ("Embry-Riddle Prescott",    34.5731, -112.4660, 6, "Kappa Iota"),
    ("LA Alumni Chapter",        34.0522, -118.2437, 6, "LA Alumni"),
    ("Montana State",            45.6770, -111.0420, 6, "Iota Kappa"),
    ("Naval Postgraduate",       36.5920, -121.8800, 6, "Theta Delta"),
    ("New Mexico State",         32.2811, -106.7470, 6, "Gamma Chi"),
    ("Northrop U",               33.9200, -118.3200, 6, "Zeta Mu"),
    ("Oregon State",             44.5646, -123.2620, 6, "Pi"),
    ("Portland State",           45.5118, -122.6839, 6, "Iota Theta"),
    ("San Diego State",          32.7748, -117.0711, 6, "Zeta Tau"),
    ("San Francisco Alumni",     37.7749, -122.4194, 6, "SF Alumni"),
    ("San Jose State",           37.3354, -121.8874, 6, "Epsilon Iota"),
    ("Santa Clara",              37.3496, -121.9390, 6, "Epsilon Psi"),
    ("Seattle U",                47.6097, -122.3200, 6, "Mu Iota"),
    ("U of Alaska Fairbanks",    64.8583, -147.8167, 6, "Kappa Gamma"),
    ("U of Arizona",             32.2283, -110.9559, 6, "Iota Xi"),
    ("UC San Diego",             32.8801, -117.2340, 6, "Kappa Psi"),
    ("UC Santa Barbara",         34.4130, -119.8498, 6, "Epsilon Tau"),
    ("UC Berkeley",              37.8721, -122.2594, 6, "Mu"),
    ("UC Irvine",                33.6450, -117.8428, 6, "Zeta Omega"),
    ("UCLA",                     34.0689, -118.4452, 6, "Iota Gamma"),
    ("UC Santa Cruz",            36.9880, -122.0600, 6, "Mu Phi"),
    ("UC Davis",                 38.5382, -121.7617, 6, "Nu Mu"),
    ("UC Riverside",             33.9738, -117.3270, 6, "Lambda Sigma"),
    ("U of Hawaii Manoa",        21.2976, -157.8190, 6, "Delta Omega"),
    ("U of Nevada Las Vegas",    36.1087, -115.1440, 6, "Nu Xi"),
    ("U of Nevada Reno",         39.5406, -119.8168, 6, "Theta Psi"),
    ("U of New Mexico",          35.0841, -106.6510, 6, "Delta Omicron"),
    ("U of Portland",            45.5718, -122.7250, 6, "Theta Beta"),
    ("U of San Diego",           32.7710, -117.1850, 6, "Kappa Eta"),
    ("U of Southern California", 34.0224, -118.2851, 6, "Upsilon"),
    ("U of Pacific",             37.9730, -121.2880, 6, "Theta Omega"),
    ("U of Toledo",              41.6639,  -83.5552, 6, "Epsilon Gamma"),
    ("U of Utah",                40.7649, -111.8450, 6, "Gamma Sigma"),
    ("U of Washington Tacoma",   47.1170, -122.4870, 6, "Nu Delta"),
    ("U of Washington",          47.6555, -122.3060, 6, "Iota Upsilon"),
    ("Western Washington",       48.7474, -122.4913, 6, "Mu Zeta"),
]

# ============================================================
# REGRESION LINEAL MANUAL: y = slope*x + intercept
# ============================================================
def linear_regression(xs, ys):
    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(a*b for a, b in zip(xs, ys))
    sum_x2 = sum(a*a for a in xs)
    denom = n * sum_x2 - sum_x * sum_x
    if denom == 0:
        return 0, sum_y / n if n else 0
    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

# ============================================================
# CALIBRAR con puntos confirmados
# ============================================================
lon_c = [p[2] for p in confirmed]
lat_c = [p[1] for p in confirmed]
tx_c  = [p[3] for p in confirmed]
ty_c  = [p[4] for p in confirmed]

a_x, b_x = linear_regression(lon_c, tx_c)
c_y, d_y = linear_regression(lat_c, ty_c)

print(f"Transformacion calibrada:")
print(f"  x = {a_x:.6f} * lon + ({b_x:.6f})")
print(f"  y = {c_y:.6f} * lat + ({d_y:.6f})")

print("\nErrores en puntos confirmados:")
for name, lat_p, lon_p, tx_p, ty_p in confirmed:
    x_pred = a_x * lon_p + b_x
    y_pred = c_y * lat_p + d_y
    print(f"  {name}: err_x={abs(x_pred - tx_p):.4f}, err_y={abs(y_pred - ty_p):.4f}")

# ============================================================
# GENERAR codigo LaTeX para regiones 1-6
# ============================================================
region_colors = {
    1: "blue", 2: "cyan!70!black", 3: "green!60!black",
    4: "olive", 5: "orange!80!black", 6: "red",
}
region_names = {
    1: "Northeastern USA", 2: "Eastern USA", 3: "Southern USA",
    4: "Central USA", 5: "Southwestern USA", 6: "Western USA",
}

counts = {}
for p in universities:
    counts[p[3]] = counts.get(p[3], 0) + 1

confirmed_set = set((p[1], p[2]) for p in confirmed)

output_lines = []
for region in range(1, 7):
    output_lines.append(f"  % ===== Region {region}: {region_names[region]} ({counts[region]} capitulos) =====")
    for name, lat_p, lon_p, reg, cap in universities:
        if reg != region:
            continue
        x = a_x * lon_p + b_x
        y = c_y * lat_p + d_y
        is_conf = any(abs(lat_p - cp[1]) < 0.01 and abs(lon_p - cp[2]) < 0.01 for cp in confirmed)
        mark = " % CONFIRMED" if is_conf else ""
        output_lines.append(f"  \\node[circle, fill={region_colors[region]}, inner sep=1mm, opacity=0.9] at ($(current page.center) + ({x:.3f}*\\paperwidth, {y:.3f}*\\paperheight)$) {{}}; % {name}, {cap}{mark}")

print("\n\n===== LATEX OUTPUT =====\n")
for line in output_lines:
    print(line)
