from projects.models import Project

p1 = Project(
    title = 'Investigating the Effect of GT61 Family Genes on Cell Wall Strength in the Wheat Starchy Endosperm',
    description = """During my Year in Research sandwich year I worked at Rothamsted Research under the supervision 
    of Dr Jaquline Freeman and Dr Rowan Mitchell in the Cell Walls group in the Division of Plant Biology and Crop
    Science. We investigated the effect of genetic manipulation of members of the Glycosyl Transferase 61 (GT61) family
    on the tensile strength and chemical configuration of cell walls in the wheat starchy endosperm. We looked 
    especially at the effect of GT61:9 which we hypothesized to be involved in the addition of Ferulic Acid which crosslinked
    arabinoxylan chains, thereby increasing tensile strength. We cultivated genetically modified wheat lines and used a 
    combination of High Performance Liquid Chromatography (HPLC) and Polyacrylamide Carbohydrate Gel Electrophoresis (PACE) 
    to investigate cell wall properties, as well as performing phylogenetic analysis of the GT61 family.""",
    technology = 'HPLC, PACE, Bioinformatics, PCR',
    image = 'img/wheat.jpg'
)

p2 = Project(
    title = 'Investigating the Role of the Essential Light Chain in The Gliding Motility of the Malaria Parasite',
    description = """For my undergraduate project I worked for 3 months in the lab of Prof. Jake Baum, we were interested in the
    mechanism by which the maliarial parasite, Plasmodium falciparum, moves by dragging itself across other surfaces.
    In this project we investigated the Essential Light Chain, a small protein which associates with malarial myosin V
    aiding motility. In this project I worked on purifying the protein, unsuccessfully at first in an E.coli expression
    system, and then successfully in a baculoviral insect cell expression system. This protein was used for binding studies
    with a myosin peptide using Differential Scanning Fluorimetry (DSF), we were able to verify that ELC binds to this
    peptide, suggesting that this may be the location of binding to malarial myosin V.\n\nI also performed docking of 
    ELC onto myosin V, looked into predicted interactions and performed some phylogenetic analyses.""",
    technology = 'Protein Purification, DSF, Bioinformatics',
    image = 'img/malaria.jpg'
)

p3 = Project(
    title = 'In-Cell Chemical Crosslinking Mass Spectrometry of Human Endophillin-A2',
    description = """In the first of my 3 month rotations on the Wellcome Trust PhD programme I worked with Prof. Konstantinos
    Thalassinos and Dr Emmanuel Bourot. The aim of the project was to gain structural and interaction insight into the
    human Endophillin-A2 protein. This protein is known to be involved in clathrin mediated endocytosis as well as Fast
    Endophilin Mediated Endocytosis (FEME), it consists of an SH3 proline sensitive domain connected by a flexible linker
    region to a BAR domain. When dimerised upon SH3 domain activation the BAR domains begin to induce membrane curvature
    assissting endocytosis. We wanted to investigate via In-Cell Chemical Crosslinking Mass Spectrometry (XLMS) any 
    interactions with other proteins, by this method we can also approximate the interaction surface of these interacting
    partners. The project itself was inconclusive.""",
    technology = 'XLMS, Protein Preparation, Western Blotting, SDS-PAGE',
    image = 'img/endophilin.png'
)

p4 = Project(
    title = 'Cell Targeting with Weak Binding Ligands',
    description = """Targeting cancer cells is a problem which has led to a large body of research. This project, a 3 month
    rotation project in the labs of Dr Salvador Thomas and Dr Emmanuel Boucrot, aimed to produce a drug nano-carrier to 
    target drugs to cancer cells. This carrier would take the form of a liposome with a small organic molecule embedded
    in the membrane, previous studies sugest that these molecules will converge upon contact with receptors on a cancer 
    cell membrane and fuse with it releasing its cargo into the cell.\n\nI performed an organic synthesis procedure to 
    synthesise and purify this simple membrane receptor, after this I produced liposomes and conducted binding assays
    on human retina cells using confocal microscopy. The project was inconclusive.""",
    technology = 'Organic Synthesis, Cell Preparation, Confocal Microscopy, Image Analysis',
    image = 'img/cancer.jpg'
)

p5 = Project(
    title = 'Building an MNXL Scoring Function for Zero-Length Crosslinks',
    description = """In my final 3 month rotation I worked in the labs of Prof. Maya Topf and Prof. Konstantinos Thalassinos 
    on producing a scoring function for zero-length crosslinks. In Chemical Cross-Linking Mass Spectrometry (XLMS) the objective 
    is to discover residues which are proximal in space, this is done by using a crosslinking reagent to crosslink solvent accessible 
    residues on the protein surface and using Mass Spectrometry to identify them.\n\nThe Matched and Non-Accessible Crosslink (MNXL) Score 
    was designed to score structural models of a protein based on crosslinking information. MNXL will first take in a list of Solvent Accessible 
    Surface Distances (SASDs) for the model, if a crosslink obtained experimentally is not in this list it is penalised because it is not accesible 
    in the model. Next the length of the crosslinker is looked at, MNXL was benchmarked on data using the BS3 crosslinker which has a maximum length 
    of 33 Angstrom, if a crosslink SASD is greater than 33 Angstrom in the model it will be penalised. Finally if a crosslink 
    passes those two checks it will be scored positively based on a probability distribution, this is a normal distribution determined by the expected 
    length of a crosslink obtained from previous data.\n\nThe aim of this project then was to devise a new function to score zero-length crosslinkers, 
    these are shorter crosslinkers which generate tighter distance restraints. Due to lack of publically available data it was not possible to obtain a 
    reliable probability distribution for a scoring function, however we did manage to produce a potenital scoring function which could be developed once 
    future data becomes available.""",
    technology = 'Python, R',
    image = 'img/mnxl.png'
)

p6 = Project(
    title = 'Computational Methods in Chemical Crosslinkng Mass Spectrometry',
    description = """For my main PhD project I am working with Prof. Maya Topf and Prof. Konstantinos Thalassinos. The main thrust of the project is to continue 
    the previous work of the Topf lab in developing computational tools for the analysis of Chemical Crosslinking Mass Spectrometry (XLMS) information. One area 
    of interest is in developing and testing a score to utilise monolinks, solvent accessible labels which are generated as a by-product in a crosslinking reaction 
    which are present in greater numbers than crosslinks. The project also aims to look into using confidence scores which are output from crosslink search algorithms 
    (e.g. Xquest/Xprophet) and looking into the effect of crosslink positioning on the protein sequence on scoring of models. This project is ongoing.""",
    technology = 'Python, XLMS, Bioinformatics, Structural Biology',
    image = 'img/monolink.png'
)

p7 = Project(
    title = 'Structural modelling of the Human Kinesin V Motor Domain using Quantitative XLMS',
    description = """Human Kinesin V (KinV) is an essential protein involved in pulling apart spindle fibres during mitosis. In this side project in my PhD I am using quantitative 
    XLMS (qXLMS) data collected by Dr Tanya Prentis (formerlly of the Thalassinos lab) to model the motor domain of KinV in two states: ADP-bound and apo. qXLMS data can be used to 
    show if a crosslink is in higher quantity in one state compared to another. This data shows differntial crosslinking between the ADP and apo states, this information will be used to 
    build missing regions in the existing KinV ADP-Bound structure and furthermore to model the apo structure. This project is ongoing.""",
    technology = 'Python, Structural Modelling',
    image = 'img/kinesin.jpg'
)

# for p in [p6,p7]:
#     p.save()

p = Project.objects.get(pk=11)
p.title = 'Computational Methods in Chemical Crosslinking'
p.save()