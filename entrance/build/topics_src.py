# Source for universal_topics.json.
# One line per unit:  Unit name | class | flags | topic; topic{FLAGS}; ...
# Unit flags apply to every topic unless a topic carries its own {FLAGS}.
#
# Flags (which syllabus family uses the topic):
#   N  current (rationalised 2023 onwards) NCERT class 11-12 textbook
#   J  JEE Main (NTA syllabus)          A  JEE Advanced
#   M  NEET UG (NMC syllabus)           S  state-board style CETs and private-university tests
#   D  NDA mathematics
# Exams pick topics with a selector: a flag letter, "C" (NCERT and class 12, the CUET UG
# domain papers), or "*" (every topic of the subject).
# The mapping is at unit level from the official syllabi as last published; a topic-by-topic
# check against each 2027 bulletin is still needed (see REPORT.md, gaps).

PHYSICS = """
Units and Measurements|11|NJAMS|SI units and the international system; Dimensional analysis and its applications; Significant figures; Errors in measurement
Kinematics|11|NJAMS|Frame of reference, position and displacement; Speed, velocity and acceleration; Motion in a straight line and its graphs; Scalars, vectors, addition and resolution of vectors; Relative velocity; Projectile motion; Uniform circular motion
Laws of Motion|11|NJAMS|Newton's laws and inertia; Momentum, impulse and conservation of momentum; Equilibrium of concurrent forces; Static, kinetic and rolling friction; Dynamics of circular motion and banking of roads
Work, Energy and Power|11|NJAMS|Work done by constant and variable forces; Kinetic and potential energy, work-energy theorem; Power; Conservation of mechanical energy, conservative forces; Motion in a vertical circle; Elastic and inelastic collisions
Rotational Motion|11|NJAMS|Centre of mass of a two-particle system and a rigid body; Torque and angular momentum; Moment of inertia and radius of gyration; Parallel and perpendicular axis theorems; Equilibrium of rigid bodies; Rotational kinematics, dynamics and rolling motion
Gravitation|11|NJAMS|Universal law of gravitation; Acceleration due to gravity and its variation; Kepler's laws; Gravitational potential energy and potential; Escape velocity; Orbital velocity, satellites and their energy
Properties of Solids and Liquids|11|NJAMS|Elastic behaviour, stress-strain, Hooke's law and moduli; Pressure in fluids and Pascal's law; Viscosity, Stokes' law and terminal velocity; Streamline and turbulent flow, Bernoulli's principle; Surface tension and capillarity; Thermal expansion, specific heat and calorimetry; Heat transfer: conduction, convection and radiation
Thermodynamics|11|NJAMS|Thermal equilibrium and the zeroth law; Heat, work and internal energy; First law, isothermal and adiabatic processes; Second law, reversible and irreversible processes; Heat engines, Carnot cycle and efficiency{AS}
Kinetic Theory of Gases|11|NJAMS|Equation of state of an ideal gas; Kinetic theory assumptions and pressure of a gas; RMS speed and kinetic interpretation of temperature; Degrees of freedom and equipartition of energy; Specific heats of gases; Mean free path and Avogadro's number
Oscillations and Waves|11|NJAMS|Periodic motion, simple harmonic motion and its equation; Energy in simple harmonic motion; Spring oscillations and the simple pendulum; Wave motion, longitudinal and transverse waves, speed of a wave; Superposition, reflection, standing waves in strings and organ pipes; Beats; Doppler effect in sound{AS}; Damped and forced oscillations, resonance{AS}
Electrostatics|12|NJAMS|Electric charge and Coulomb's law; Electric field, field lines and dipole; Electric flux and Gauss's law with applications; Electric potential and potential energy; Conductors, dielectrics and polarisation; Capacitors, combinations and energy stored
Current Electricity|12|NJAMS|Electric current, drift velocity and Ohm's law; Resistance, resistivity and temperature dependence; Series and parallel combinations of resistors; EMF, internal resistance, cells in series and parallel; Kirchhoff's laws; Wheatstone bridge and metre bridge; Potentiometer{AS}; Electrical energy and power
Magnetic Effects of Current and Magnetism|12|NJAMS|Biot-Savart law and applications; Ampere's law and the solenoid; Force on a moving charge and on a current-carrying conductor; Torque on a current loop and moving coil galvanometer; Bar magnet, magnetic dipole and field lines; Para-, dia- and ferromagnetic substances; Cyclotron{AS}; Earth's magnetism{S}
Electromagnetic Induction and Alternating Currents|12|NJAMS|Faraday's law, Lenz's law and induced EMF; Eddy currents; Self and mutual inductance; Alternating current: peak and RMS values, reactance and impedance; LCR series circuit, resonance and power factor; AC generator and transformer
Electromagnetic Waves|12|NJAMS|Displacement current; Characteristics of electromagnetic waves; Electromagnetic spectrum and its uses
Optics|12|NJAMS|Reflection, spherical mirrors and the mirror formula; Refraction and total internal reflection; Lenses, lens maker's formula and combinations; Prism and dispersion; Microscope and telescope; Wavefronts and Huygens' principle; Interference and Young's double slit experiment; Diffraction at a single slit; Polarisation and Brewster's law
Dual Nature of Matter and Radiation|12|NJAMS|Photoelectric effect, Hertz and Lenard observations; Einstein's photoelectric equation; Particle nature of light; Matter waves and the de Broglie relation
Atoms and Nuclei|12|NJAMS|Alpha-scattering and Rutherford's model; Bohr model, energy levels and hydrogen spectrum; Composition and size of the nucleus; Mass-energy relation, mass defect and binding energy; Nuclear fission and fusion; Radioactivity and the decay law{AS}
Electronic Devices|12|NJAMS|Semiconductors, p-n junction diode and I-V characteristics; Diode as a rectifier; LED, photodiode, solar cell and Zener diode; Logic gates (OR, AND, NOT, NAND, NOR); Transistors and amplifier action{S}
Communication Systems|12|S|Elements of a communication system and modulation
Experimental Skills|11-12|JAM|Vernier calipers and screw gauge; Simple pendulum, metre scale and Young's modulus; Surface tension, viscosity, speed of sound and specific heat; Metre bridge, Ohm's law and galvanometer experiments; Focal length of mirrors and lenses, prism and refractive index; Diode and Zener diode characteristics
"""

CHEMISTRY = """
Some Basic Concepts in Chemistry|11|NJAMS|Matter and its nature, Dalton's atomic theory; Laws of chemical combination; Atomic and molecular masses, mole concept and molar mass; Percentage composition, empirical and molecular formulae; Stoichiometry and limiting reagent; Concentration terms
Atomic Structure|11|NJAMS|Electromagnetic radiation and photoelectric effect; Hydrogen spectrum and Bohr model; Dual nature of matter, de Broglie and Heisenberg; Quantum numbers and shapes of orbitals; Aufbau principle, Pauli principle, Hund's rule and electronic configuration
Chemical Bonding and Molecular Structure|11|NJAMS|Ionic bonding and lattice enthalpy; Covalent bonding, electronegativity, Fajans' rule and dipole moment; VSEPR theory and shapes of molecules; Valence bond theory and hybridisation; Molecular orbital theory and bond order; Hydrogen bonding and metallic bonding
Chemical Thermodynamics|11|NJAMS|System, surroundings and state functions; First law, internal energy, enthalpy and heat capacity; Hess's law and enthalpies of reaction; Second law, entropy and spontaneity; Gibbs energy and the equilibrium constant
Solutions|12|NJAMS|Ways of expressing concentration; Vapour pressure, Raoult's law, ideal and non-ideal solutions; Colligative properties; Abnormal molar mass and van't Hoff factor
Equilibrium|11|NJAMS|Dynamic equilibrium, physical equilibria and Henry's law; Law of chemical equilibrium, Kp, Kc and Le Chatelier's principle; Acids and bases (Arrhenius, Bronsted-Lowry, Lewis) and ionisation; pH, hydrolysis of salts and buffer solutions; Solubility product and common ion effect
Redox Reactions and Electrochemistry|11-12|NJAMS|Oxidation number and balancing redox reactions; Conductance, molar conductivity and Kohlrausch's law; Electrochemical cells, electrode potentials and EMF; Nernst equation and Gibbs energy; Batteries and fuel cells; Electrolysis and Faraday's laws{NAS}; Corrosion{NAS}
Chemical Kinetics|12|NJAMS|Rate of reaction and the factors affecting it; Order, molecularity, rate law and rate constant; Integrated rate equations for zero and first order, half-life; Temperature dependence, Arrhenius equation and activation energy; Collision theory
States of Matter (Gases and Liquids)|11|AS|Gas laws and the ideal gas equation; Kinetic molecular theory, real gases and van der Waals equation; Liquefaction and critical constants; Liquid state: vapour pressure, viscosity and surface tension
Solid State|12|AS|Crystalline and amorphous solids, unit cells; Packing efficiency, voids and density calculations; Imperfections in solids; Electrical and magnetic properties of solids
Surface Chemistry|12|AS|Adsorption and adsorption isotherms; Catalysis; Colloids and emulsions
Classification of Elements and Periodicity|11|NJAMS|Modern periodic law and the periodic table; s, p, d and f blocks; Periodic trends: radii, ionisation enthalpy, electron gain enthalpy, valence, oxidation states and reactivity
p-Block Elements|11-12|NJAMS|Groups 13 and 14: trends and important compounds; Group 15: nitrogen and phosphorus compounds; Group 16: oxygen and sulphur compounds; Group 17: halogens and interhalogen compounds; Group 18: noble gases
d- and f-Block Elements|12|NJAMS|Transition elements: configuration, oxidation states, colour, magnetism and catalysis; Potassium dichromate and potassium permanganate; Lanthanoids and lanthanoid contraction; Actinoids
Coordination Compounds|12|NJAMS|Werner's theory, ligands, coordination number and IUPAC nomenclature; Isomerism in coordination compounds; Valence bond and crystal field theory, colour and magnetism; Importance in analysis, metallurgy and biology
Hydrogen and s-Block Elements|11|AS|Hydrogen, hydrides, water and hydrogen peroxide; Alkali metals and their compounds; Alkaline earth metals and their compounds
General Principles of Metallurgy|12|AS|Occurrence and concentration of ores; Extraction: thermodynamic and electrochemical principles; Refining of metals; Extraction of aluminium, copper, zinc and iron
Purification and Characterisation of Organic Compounds|11|NJAMS|Crystallisation, sublimation, distillation and chromatography; Qualitative detection of nitrogen, sulphur, phosphorus and halogens; Quantitative analysis of elements; Empirical and molecular formula calculations
Basic Principles of Organic Chemistry|11|NJAMS|Tetravalency, hybridisation, classification and functional groups; IUPAC nomenclature; Structural isomerism and stereoisomerism; Bond fission, carbocations, carbanions and free radicals; Inductive, electromeric, resonance and hyperconjugation effects; Types of organic reactions
Hydrocarbons|11|NJAMS|Alkanes: conformations and halogenation; Alkenes: geometrical isomerism, electrophilic addition, Markovnikov rule, peroxide effect and ozonolysis; Alkynes: acidic character and addition reactions; Aromatic hydrocarbons: benzene, aromaticity, electrophilic substitution and directive influence
Organic Compounds Containing Halogens|12|NJAMS|Preparation, properties and reactions of haloalkanes and haloarenes; Nature of the C-X bond, SN1 and SN2 mechanisms; Uses and environmental effects of chloroform, iodoform, freons and DDT
Organic Compounds Containing Oxygen|12|NJAMS|Alcohols: preparation, properties and mechanism of dehydration; Phenols: acidity, electrophilic substitution and Reimer-Tiemann reaction; Ethers; Aldehydes and ketones: nucleophilic addition, aldol, Cannizzaro and tests; Carboxylic acids and acidic strength
Organic Compounds Containing Nitrogen|12|NJAMS|Amines: classification, basicity, preparation and reactions; Identification of primary, secondary and tertiary amines; Diazonium salts and their synthetic importance
Biomolecules|12|NJAMS|Carbohydrates: classification, glucose, fructose and oligosaccharides; Proteins: amino acids, peptide bond, structure levels, denaturation and enzymes; Vitamins; Nucleic acids: DNA and RNA; Hormones
Polymers|12|AS|Classification and methods of polymerisation; Natural and synthetic rubber, vulcanisation; Important polymers: polythene, nylon, polyesters and bakelite
Chemistry in Everyday Life|12|S|Drugs and their classes; Chemicals in food; Cleansing agents: soaps and detergents
Environmental Chemistry|11|S|Atmospheric, water and soil pollution; Ozone depletion and the greenhouse effect; Green chemistry
Principles Related to Practical Chemistry|11-12|JAM|Detection of extra elements and functional groups; Preparation of inorganic and organic compounds; Titrimetric exercises; Qualitative salt analysis; Enthalpy and kinetics experiments
"""

MATHS = """
Sets, Relations and Functions|11-12|NJAMSD|Sets and their representation, union, intersection and complement; Power set and algebraic properties of sets; Relations and equivalence relations; Functions: one-one, into, onto and composition
Complex Numbers and Quadratic Equations|11|NJAMSD|Complex numbers, Argand diagram and algebra of complex numbers; Modulus and argument; Quadratic equations in real and complex number systems; Relation between roots and coefficients, nature of roots
Matrices and Determinants|12|NJAMSD|Matrix algebra and types of matrices; Determinants of order two and three; Area of a triangle using determinants; Adjoint and inverse of a square matrix; Consistency and solution of simultaneous linear equations
Permutations and Combinations|11|NJAMSD|Fundamental principle of counting; Permutations as arrangements; Combinations as selections; Meaning and applications of P(n,r) and C(n,r)
Binomial Theorem|11|NJAMSD|Binomial theorem for a positive integral index; General and middle terms; Simple applications of the binomial theorem
Sequences and Series|11|NJAMSD|Arithmetic progression; Geometric progression; Insertion of arithmetic and geometric means; Relation between AM and GM
Limits, Continuity and Differentiability|11-12|NJAMSD|Real-valued functions and their graphs; Limits and continuity; Differentiation of sums, products, quotients, composite, implicit and logarithmic functions; Derivatives up to order two; Rate of change and monotonic functions; Maxima and minima
Integral Calculus|12|NJAMSD|Integral as an antiderivative and standard integrals; Integration by substitution, by parts and by partial fractions; Fundamental theorem of calculus; Properties of definite integrals; Area under simple curves
Differential Equations|12|NJAMSD|Order and degree of a differential equation; Solution by separation of variables; Homogeneous differential equations; Linear differential equations
Coordinate Geometry|11|NJAMSD|Cartesian coordinates, distance formula, section formula and locus; Straight lines: forms of equation, angle between lines, distance of a point from a line; Circle: standard and general form; Parabola, ellipse and hyperbola in standard form
Three Dimensional Geometry|11-12|NJAMSD|Coordinates in space, distance and section formulae; Direction ratios, direction cosines and angle between lines; Equations of a line, skew lines and shortest distance; Planes{NAS}
Vector Algebra|12|NJAMSD|Vectors and scalars, addition of vectors; Components of a vector in two and three dimensions; Scalar and vector products; Triple products{AS}
Statistics and Probability|11-12|NJAMSD|Mean, median and mode; Standard deviation, variance and mean deviation; Probability of events, addition and multiplication theorems; Bayes' theorem; Probability distribution of a random variable; Binomial distribution{NAS}
Trigonometry|11-12|NJAMSD|Trigonometric identities and functions; Trigonometric equations{AS}; Inverse trigonometric functions and their properties; Heights and distances{SD}; Properties of triangles{AS}
Linear Programming|12|NS|Formulation of a linear programming problem; Graphical solution, feasible region and optimal solution
Linear Inequalities|11|NS|Linear inequalities in one and two variables; Graphical solution of linear inequalities
Mathematical Induction and Reasoning|11|S|Principle of mathematical induction; Statements, logical connectives and truth tables
"""

BIOLOGY = """
Diversity in Living World|11|NMS|The living world, taxonomy and binomial nomenclature; Five kingdom classification: Monera, Protista and Fungi; Lichens, viruses and viroids; Plant kingdom: algae to angiosperms; Animal kingdom: non-chordates and chordates
Structural Organisation in Animals and Plants|11|NMS|Morphology of flowering plants; Anatomy of flowering plants; Plant families (Malvaceae, Cruciferae, Leguminosae, Compositae, Gramineae){M}; Animal tissues; Frog; Cockroach{M}
Cell Structure and Function|11|NMS|Cell theory, prokaryotic and eukaryotic cells; Cell organelles and the cell membrane; Biomolecules and enzymes; Cell cycle, mitosis and meiosis
Plant Physiology|11|NMS|Photosynthesis in higher plants; Respiration in plants; Plant growth, development and growth regulators; Transport in plants{S}; Mineral nutrition{S}
Human Physiology|11|NMS|Breathing and exchange of gases; Body fluids and circulation; Excretory products and their elimination; Locomotion and movement; Neural control and coordination; Chemical coordination and integration; Digestion and absorption{S}
Reproduction|12|NMS|Sexual reproduction in flowering plants; Human reproduction; Reproductive health; Reproduction in organisms{S}
Genetics and Evolution|12|NMS|Principles of inheritance and variation; Molecular basis of inheritance; Evolution
Biology and Human Welfare|12|NMS|Human health and disease; Microbes in human welfare; Strategies for enhancement in food production{S}
Biotechnology and Its Applications|12|NMS|Biotechnology: principles and processes; Biotechnology and its applications
Ecology and Environment|12|NMS|Organisms and populations; Ecosystem; Biodiversity and conservation; Environmental issues{S}
"""

# Class 9-10 level, used by polytechnic CETs, school-stage talent and military-school tests.
FOUNDATION_MATHS = """
Number Systems|9-10|F|Real numbers, irrational numbers and decimal expansions; HCF, LCM and the fundamental theorem of arithmetic; Laws of exponents and surds
Algebra|9-10|F|Polynomials and their zeroes; Pair of linear equations in two variables; Quadratic equations; Arithmetic progressions
Coordinate Geometry (class 10)|9-10|F|Cartesian plane, distance and section formulae; Area of a triangle from coordinates
Geometry|9-10|F|Lines, angles and triangles, congruence; Similar triangles and Pythagoras theorem; Circles, chords and tangents; Quadrilaterals and constructions
Trigonometry (class 10)|10|F|Trigonometric ratios and identities; Heights and distances
Mensuration|9-10|F|Areas related to circles; Surface areas and volumes of solids
Statistics and Probability (class 10)|9-10|F|Mean, median and mode of grouped data; Simple probability
"""

FOUNDATION_SCIENCE = """
Physics (class 9-10)|9-10|F|Motion, force and laws of motion; Gravitation, work, energy and sound; Light: reflection and refraction; The human eye and the colourful world; Electricity; Magnetic effects of electric current
Chemistry (class 9-10)|9-10|F|Matter, atoms, molecules and structure of the atom; Chemical reactions and equations; Acids, bases and salts; Metals and non-metals; Carbon and its compounds; Periodic classification of elements
Biology (class 9-10)|9-10|F|Cell, tissues and diversity of living organisms; Life processes; Control and coordination; How organisms reproduce; Heredity; Our environment and natural resources
Social Science (class 8-10)|8-10|F|History: India and the modern world; Geography: resources, agriculture and industries; Civics: democracy and the Constitution; Economics: development and sectors of the economy
"""

QUANT = """
Number System|-|Q|Divisibility, HCF and LCM; Remainders and factors; Surds, indices and simplification; Number series
Arithmetic|-|Q|Percentages; Ratio, proportion and partnership; Profit, loss and discount; Simple and compound interest; Averages, mixtures and alligations; Time and work, pipes and cisterns; Time, speed and distance, boats and trains
Algebra (aptitude)|-|Q|Linear and quadratic equations; Inequalities; Functions and graphs; Logarithms; Progressions
Geometry and Mensuration (aptitude)|-|Q|Lines, angles and triangles; Circles and polygons; Coordinate geometry basics; Areas and volumes; Basic trigonometry
Modern Maths|-|Q|Permutations and combinations (aptitude); Probability (aptitude); Set theory and Venn diagrams
Data Interpretation|-|Q|Tables; Bar, line and pie charts; Caselets and mixed graphs; Data sufficiency
"""

REASONING = """
Verbal Reasoning|-|R|Analogies and classification; Number and letter series; Coding-decoding; Blood relations; Direction sense; Ranking and order; Syllogisms; Calendars and clocks
Analytical Reasoning|-|R|Seating arrangements; Puzzles and scheduling; Input-output; Binary logic, games and tournaments
Critical Reasoning|-|R|Statements and assumptions; Arguments: strengthening and weakening; Inferences and conclusions; Cause and effect
Non-Verbal Reasoning|-|R|Figure series and analogies; Mirror and water images; Paper folding and cutting; Embedded figures, cubes and dice
"""

ENGLISH = """
Reading Comprehension|-|E|Passage-based comprehension; Inference, tone and main idea; Paragraph summary
Grammar and Usage|-|E|Parts of speech and tenses; Subject-verb agreement; Voice and narration; Error spotting and sentence improvement
Vocabulary|-|E|Synonyms and antonyms; Idioms and phrases; One-word substitution; Cloze test and fill in the blanks
Verbal Ability|-|E|Para jumbles; Sentence completion; Odd sentence out; Sentence rearrangement
"""

GK = """
History and Culture|-|G|Ancient and medieval India; Modern India and the freedom struggle; World history basics; Art and culture
Geography|-|G|Physical geography; Indian geography; World geography
Polity and Constitution|-|G|Constitution and fundamental rights; Union and state government; Judiciary and local government
Economy|-|G|Basic economic concepts; Indian economy, budget and banking
General Science|-|G|Everyday physics; Everyday chemistry; Biology and health; Science and technology
Current Affairs|-|G|National and international events; Awards, sports, books and persons; Government schemes
"""

LEGAL = """
Legal Reasoning|-|L|Principle and fact passages; Constitution-based passages; Contracts and torts basics; Criminal law basics; Legal current affairs
"""

DESIGN = """
Design Aptitude|-|Z|Visualisation and spatial ability; Observation and design sensitivity; Drawing and sketching; Environmental and social awareness; Creativity and design thinking; Analytical and logical reasoning in design
Architecture Aptitude|-|Z|Perspective and three-dimensional perception; Architectural awareness; Composition and colour; Building materials and textures
"""

TEACHING = """
Teaching and Research Aptitude|-|T|Teaching aptitude; Research aptitude; Comprehension; Communication; Mathematical reasoning and aptitude; Logical reasoning (Indian logic included); Data interpretation; Information and communication technology; People, development and environment; Higher education system
"""

COMPUTER = """
Computer Awareness|-|K|Computer fundamentals and organisation; Data representation and number systems; Operating systems, networks and the internet; Office tools and basic programming concepts
"""

# Commerce: NCERT class 11-12 (CUET domain papers) plus CA Foundation papers.
COMMERCE = """
Accountancy|11-12|NC|Accounting for partnership firms; Accounting for companies: shares and debentures; Analysis of financial statements and ratios; Cash flow statement; Basic accounting process and final accounts{NC}
Business Studies|11-12|NC|Nature, principles and functions of management; Business finance and financial markets; Marketing and consumer protection; Forms of business organisation{NC}
Economics|11-12|NC|Introductory microeconomics; Introductory macroeconomics; Indian economic development; Statistics for economics
Business Laws (CA Foundation)|-|X|Indian Contract Act; Sale of Goods Act; Partnership and LLP Acts; Companies Act basics
"""

HUMANITIES = """
Humanities (CUET domain papers)|12|NH|History (Themes in Indian History); Political Science; Geography; Sociology; Psychology
"""

SUBJECTS = [
    ("physics", "Physics (class 11-12)", PHYSICS),
    ("chemistry", "Chemistry (class 11-12)", CHEMISTRY),
    ("maths", "Mathematics (class 11-12)", MATHS),
    ("biology", "Biology (class 11-12)", BIOLOGY),
    ("f_maths", "Mathematics (class 9-10)", FOUNDATION_MATHS),
    ("f_science", "Science and Social Science (class 8-10)", FOUNDATION_SCIENCE),
    ("quant", "Quantitative Aptitude", QUANT),
    ("reasoning", "Reasoning", REASONING),
    ("english", "English", ENGLISH),
    ("gk", "General Knowledge and Current Affairs", GK),
    ("legal", "Legal Reasoning", LEGAL),
    ("design", "Design and Architecture Aptitude", DESIGN),
    ("teaching", "Teaching and Research Aptitude", TEACHING),
    ("computer", "Computer Awareness", COMPUTER),
    ("commerce", "Commerce (class 11-12 and CA Foundation)", COMMERCE),
    ("humanities", "Humanities (class 12)", HUMANITIES),
]

# NCERT book for a (subject, class) pair, for the overlap column.
NCERT_BOOK = {
    "physics": "NCERT Physics Part I and II",
    "chemistry": "NCERT Chemistry Part I and II",
    "maths": "NCERT Mathematics",
    "biology": "NCERT Biology",
    "commerce": "NCERT Accountancy / Business Studies / Economics",
    "humanities": "NCERT class 12 humanities textbooks",
}

# CBSE Free N Easy lesson skills seen in this workspace (class and subject). Used to mark
# whether NCERT overlap is confirmed as already produced or only assumed from the brief.
CBSE_SKILLS_SEEN = {
    ("physics", "12"), ("chemistry", "12"), ("maths", "12"), ("biology", "12"),
    ("commerce", "12"), ("commerce", "11"),
}

# GATE paper -> B.Tech universal subject ids (pack/universal.json). Subject-level mapping.
ENGG_MATHS = ["m-linalg", "m-calculus", "m-de", "m-complex", "m-prob", "m-numerical"]
GATE_MAP = {
    "CS": ["m-discrete", "m-linalg", "m-calculus", "m-prob", "c-digital", "c-coa", "e-prog", "c-ds", "c-algo", "c-toc", "c-compiler", "c-os", "c-dbms", "c-cn"],
    "DA": ["m-prob", "m-linalg", "m-calculus", "m-optim", "e-python", "c-ds", "c-algo", "c-dbms", "c-ml", "c-ai", "c-data", "c-dl"],
    "EC": ENGG_MATHS + ["m-transforms", "ec-circuits", "ec-signals", "ec-devices", "ec-analog", "c-digital", "ec-mp", "ec-control", "ec-comm", "ec-emf", "ec-antenna"],
    "EE": ENGG_MATHS + ["m-transforms", "ec-circuits", "ec-emf", "ec-signals", "ee-machines", "ee-psys", "ee-gtd", "ee-protect", "ec-control", "ec-measure", "ec-analog", "c-digital", "ee-pe", "ee-drives"],
    "ME": ENGG_MATHS + ["e-mech", "me-som", "me-tom", "me-design", "me-fluid", "me-ht", "me-thermo", "me-ic", "me-rac", "me-power", "me-materials", "me-mfg", "me-metro", "me-cad", "me-ie", "m-optim"],
    "CE": ENGG_MATHS + ["e-mech", "me-som", "ce-struct", "ce-mat", "ce-cm", "ce-rcc", "ce-steel", "ce-geo", "me-fluid", "ce-water", "ce-env", "ce-trans", "ce-survey"],
    "CH": ENGG_MATHS + ["ch-calc", "ch-thermo", "me-fluid", "ch-unitop", "me-ht", "ch-mass", "ch-cre", "ic-proc", "ch-design", "ch-tech", "ch-transport"],
    "IN": ENGG_MATHS + ["ec-circuits", "ec-signals", "ec-control", "ec-analog", "c-digital", "ec-mp", "ec-measure", "ei-sensor", "ei-ind", "ei-anal", "ec-comm", "ic-proc"],
    "BT": ["m-calculus", "m-prob", "bt-biochem", "bt-micro", "bt-cell", "bt-mol", "bt-gen", "bt-immuno", "bt-gene", "bt-bioinfo", "bt-bioproc", "bt-dsp", "bt-plant", "bt-animal", "bt-enzyme"],
    "AE": ENGG_MATHS + ["ae-flight", "ae-space", "ae-aero", "ae-struct", "ae-prop"],
    "BM": ENGG_MATHS + ["ec-circuits", "ec-signals", "ec-analog", "c-digital", "ec-measure", "ei-sensor", "bm-anat", "bm-instr", "bm-imaging", "bm-mech", "bt-biomat", "bm-signal"],
    "MT": ENGG_MATHS + ["mm-thermo", "mm-phys", "mm-mech", "mm-extract", "me-materials", "mm-char", "mm-corr", "me-mfg", "mm-func", "mm-ceramic", "mm-poly", "me-composite"],
    "PI": ENGG_MATHS + ["me-materials", "me-mfg", "me-metro", "me-ie", "m-optim", "me-cad", "e-mech", "me-som", "me-tom", "me-design", "me-thermo", "me-fluid", "me-ht", "h-mgmt"],
    "XE": ENGG_MATHS + ["me-fluid", "me-materials", "me-som", "me-thermo", "mm-poly", "bt-food"],
    "ES": ["m-prob", "ce-env", "s-env", "bt-env", "ce-water"],
    "MA": ["m-calculus", "m-linalg", "sc-real", "m-complex", "m-de", "sc-algebra", "m-numerical", "m-prob", "m-optim"],
    "PH": ["sc-mathphys", "sc-mech", "sc-em", "ec-emf", "sc-quantum", "sc-thermal", "sc-modern", "nm-solid", "sc-optics", "ec-devices"],
    "CY": ["sc-organic", "sc-analytical", "sc-quantum", "mm-corr"],
    "ST": ["m-prob", "m-calculus", "m-linalg", "sc-real"],
    "XL": ["bt-biochem", "bt-micro", "bt-cell", "bt-food", "s-chem"],
}
# GATE papers the B.Tech pack does not cover at all.
GATE_UNMAPPED = ["AG", "AR", "EY", "GE", "GG", "MN", "NM", "PE", "TF", "XH"]
