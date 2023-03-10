import csv

# Returns the list of students who have the given free period first

class Student:
    def __init__(self, grade, signedIn=False):
        self.grade = grade
        self.signedIn = signedIn

def getStudents(period):
    students = {}
    nameIndex = 1
    gradeIndex = 2
    periodIndex = 3

    # CSV data as a multi-line string
    csv_data = """ID,name,grade,free,
WANG022,"Wang, Evan ( Evan )",VI,A
VOLL011,"Vollmer, George ( George )",VI,A
COOP051,"Cooper, Gavin ( Gavin )",IV,A
GERG011,"Gergo, Peter ( Peter )",IV,A
BONA011,"Bonaparte, Jai ( Jai )",V,A
GIBS021,"Gibson, Edward ( Edward )",V,A
GREE131,"Green, William ( Clayton )",V,A
GROS031,"Gross, Adon ( Adon )",V,A
HARR061,"Harrington, Jackson ( Jackson )",V,A
INNI011,"Inniss, Andre ( Andre )",V,A
MILE011,"Miles, Michael ( Brady )",V,A
MORA031,"Moran, Ryan ( Ryan )",V,A
NELS041,"Nelson, Chase ( Chase )",V,A
NEMO011,"Nemo, Alexander ( Alex )",V,A
NEWH012,"Newhall, Henry ( Henry )",V,A
NOLE012,"Nolen, Connor ( Connor )",V,A
PAUL031,"Paul, Blake ( Blake )",V,A
PERE011,"Perez-Gasiba, Sebastian ( Sebastian )",V,A
PESH011,"Peshek-Percec, Alexander ( Alexander )",V,A
RAYE011,"Rayer, William ( Billy )",V,A
SHAF011,"Shaffer, Reilly ( Reilly )",V,A
TREX011,"Trexler, Noah ( Noah )",V,A
ZHAN031,"Zhang, Max ( Max )",V,A
ACCH011,"Acchione, Joseph Lucio ( Lucio )",VI,A
ASCH013,"Aschkenasy, Charles ( Charlie )",VI,A
ATKI031,"Atkinson, Louis ( Louie )",VI,A
BODL011,"Bodle, Benjamin ( Ben )",VI,A
BRID011,"Briddell, Aidan ( Aidan )",VI,A
CHEN071,"Chen, Jingyuan ( Jingyuan )",VI,A
COLL041,"Collier, Matthew ( Matthew )",VI,A
DEAN041,"Dean, Michael ( Michael )",VI,A
DOUG041,"Douglas, Cameron ( Cameron )",VI,A
DUGE011,"Dugery, Sean ( Sean )",VI,A
HARL011,"Harlamov, Ivan ( Ivan )",VI,A
HARR071,"Harris, Safiyy ( Papi )",VI,A
HERD023,"Herd, John ( Johnny )",VI,A
ISLA011,"Islam, Ali ( Ali )",VI,A
KNOX021,"Knox, Derrick ( Chace )",VI,A
LUTE011,"Luterman, Andrew ( Andrew )",VI,A
MCCU041,"McCullough, Harrison ( Harrison )",VI,A
MIRI011,"Mirin, Nathan ( Nate )",VI,A
OBRI022,"O'Brien, Charles ( Charlie )",VI,A
PANT012,"Pante, Matthew ( Matt )",VI,A
PARI021,"Pariano, Joseph ( Joe )",VI,A
PENN021,"Pennewill, Joseph ( Joey )",VI,A
PLUM011,"Plumer-Butler, Jasir ( Jasir )",VI,A
PRES031,"Pressman, Brandon ( Cole )",VI,A
RASM011,"Rasmussen, Luke ( Luke )",VI,A
ROSE081,"Rosenberg, Charles ( Charlie )",VI,A
SEKU012,"Sekulic, Luka ( Luka )",VI,A
SHAH013,"Shah, Zachary ( Zachary )",VI,A
STRA021,"Straub, Matthew ( Matthew )",VI,A
TELL011,"Tellez, Nathaniel ( Nathaniel )",VI,A
NYE011,"Nye, Thomas ( Thomas )",III,B
GAFF021,"Gaffney, Thomas ( Mac )",IV,B
GILL081,"Gillis, Sebastian ( Sebastian )",IV,B
HALP012,"Halpert, Charles ( Charlie )",IV,B
LARG021,"Large, Evan ( Evan )",IV,B
STAI011,"Stait, Jamie ( Jamie )",IV,B
ANDR041,"Andrewson, Noah ( Noah )",V,B
BROS012,"Brosko, Matthew ( Matt )",V,B
BROW171,"Brown, Jey ( Jey )",V,B
BURF011,"Burfeind, William ( Will )",V,B
CART031,"Carter, Anthony ( Anthony )",V,B
CIMI011,"Cimino, Richard ( Jack )",V,B
CONK011,"Conklin, Mitchell ( Tate )",V,B
DELU011,"DeLuca, Alexander ( Alec )",V,B
DUNB012,"Dunbar, Brandon ( Brandon )",V,B
FEIL011,"Feild, Dalton ( Dalton )",V,B
FORD031,"Ford, Render ( Render )",V,B
GILD011,"Gildea, Thomas ( Tom )",V,B
GOLD051,"Golderer, Sebastian ( Sebastian )",V,B
GROS031,"Gross, Adon ( Adon )",V,B
HAYN011,"Hayne, Nicholas ( Nicholas )",V,B
HERD022,"Herd, Joseph ( Joseph )",V,B
IBRA011,"Ibrahim, Amir ( Amir )",V,B
JACO032,"Jacobs, Keegan ( Keegan )",V,B
JONE071,"Jones, Matthew ( Matty )",V,B
JONE141,"Jones-Blisard, Matthew ( Matthew )",V,B
KAPL042,"Kaplan, Thomas ( Thomas )",V,B
KRIE011,"Kriebel, Garrett ( Garrett )",V,B
LAWR021,"Lawrence, Peter ( Finn )",V,B
LEE081,"Lee, Ethan ( Ethan )",V,B
LYON031,"Lyon, Andrew ( Andrew )",V,B
MARR011,"Marr, Maximillian ( Max )",V,B
MCCL032,"McCloskey, Nolan ( Nolan )",V,B
MCCO071,"McCoy, John ( Thacher )",V,B
MORR081,"Morris, Kyle ( Kyle )",V,B
NAYA012,"Nayak, Adiyan ( Adi )",V,B
NGO012,"Ngo, Sean ( Sean )",V,B
OKAN011,"O'Kane, Brady ( Brady )",V,B
PUTT011,"Putter, Lucas ( Luke )",V,B
RALE012,"Raleigh, Jackson ( Jackson )",V,B
STAM022,"Stamps, Gavin ( Gavin )",V,B
VALE011,"Valentino, Anthony ( Anthony )",V,B
WINI013,"Winikur, Asa ( Asa )",V,B
ACCH011,"Acchione, Joseph Lucio ( Lucio )",VI,B
ARIA012,"Arias, Joaquin ( Joaquin )",VI,B
CHEN071,"Chen, Jingyuan ( Jingyuan )",VI,B
COLL041,"Collier, Matthew ( Matthew )",VI,B
CURT021,"Curtis, Dylan ( Dylan )",VI,B
DENM011,"Denmark, Yasir ( Yasir )",VI,B
DONN011,"Donnelly, Cole ( Cole )",VI,B
FRAN021,"Franz, Matthew ( Matthew )",VI,B
GETZ011,"Getz, Ryan ( Ryan )",VI,B
GHAN011,"Ghanem, Yonas ( Yonas )",VI,B
HARR071,"Harris, Safiyy ( Papi )",VI,B
HERD012,"Herdler, Owen ( Owen )",VI,B
KAUF011,"Kauffman, Joseph ( Joey )",VI,B
KELL071,"Kelly, Colin ( Colin )",VI,B
KESZ012,"Keszeli, Nicholas ( Nicholas )",VI,B
NEK0011,"Nekoumand, Alexander ( Z )",VI,B
POWE031,"Powell, Zachary ( Zach )",VI,B
SILV031,"Silvers, Willys ( Willys )",VI,B
SULL012,"Sullivan, Jack ( Jack )",VI,B
WANG022,"Wang, Evan ( Evan )",VI,B
BAKE032,"Baker, Chase ( Chase )",III,C
CHAK022,"Chakraborty, Ajay ( AJ )",III,C
CLAR061,"Clarke, Rauden ( Rauden )",III,C
CURR051,"Curran, Sean ( Sean )",III,C
DANI011,"Daniels, Luke ( Luke )",III,C
DANI021,"Danisi, Gabriel ( Gabe )",III,C
DUVE011,"Duvernay, Lamar ( Lamar )",III,C
FRAZ011,"Frazier, Walter ( Walt )",III,C
GOIN021,"Goins, Ahijah ( Ahijah )",III,C
OLSO011,"Olson, Max ( Max )",III,C
PHIL021,"Phillips, Destin ( Destin )",III,C
RISC011,"Rischitelli, John ( Jack )",III,C
ROME031,"Romeo, Jovanni ( Jovanni )",III,C
ROUS011,"Rouse, Patrick ( Packy )",III,C
SHAM021,"Shams, Ryan ( Ryan )",III,C
TOTH011,"Toth, Colin ( Colin )",III,C
CUDD021,"Cuddeback, John ( Jack )",V,C
HENG011,"Hengst, Austan ( Austan )",V,C
JABA011,"Jabateh, Musa ( Musa )",V,C
LAVE021,"Laveran, Pierce ( Pierce )",V,C
MCCA102,"McCarthy, Benjamin ( Ben )",V,C
REAV011,"Reavey, Kevin ( Kevin )",V,C
RONO011,"Ronon, Gerald ( Tripp )",V,C
ROUS012,"Rouse, John ( John )",V,C
YOH022,"Yoh, Russell ( Russell )",V,C
DOUG051,"Dougherty, Sean ( Sean )",VI,C
ELDE011,"Elder, Zachary ( Zach )",VI,C
KHAN032,"Khan, Ebaad ( Ebaad )",VI,C
KIRW011,"Kirwan, Andrew ( Andrew )",VI,C
MARS021,"Marshall, Adam ( Adam )",VI,C
NESB012,"Nesbitt, Rory ( Rory )",VI,C
PANT012,"Pante, Matthew ( Matt )",VI,C
PARA031,"Parayre, Roch ( Roch )",VI,C
SELL012,"Sellari, Jacob ( Jacob )",VI,C
SHEA031,"Shea, Aedan ( Aedan )",VI,C
SHUC012,"Shuchman, Jaiden ( Jaiden )",VI,C
SILV031,"Silvers, Willys ( Willys )",VI,C
YU031,"Yu, Owen ( Owen )",VI,C
CARR051,"Carrasco, Andrew ( Drew )",III,D
GREE141,"Greenberg, Brady ( Brady )",III,D
HOBA012,"Hoban, Matthew ( Matt )",III,D
NEMO012,"Nemo, Nicholas ( Nicky )",III,D
OLIV031,"Oliver, Grant ( Grant )",III,D
POWE051,"Powers, Maximilian ( Max )",III,D
SHAN011,"Shannon, William ( Will )",III,D
SIEV011,"Siever, Caleb ( Caleb )",III,D
SMYT021,"Smyth, Jaxen ( Jaxen )",III,D
STIN031,"Stinchon, Oliver ( Oliver )",III,D
THOM131,"Thomas, Ian ( Ian )",III,D
DECK031,"Decker, Colin ( Colin )",IV,D
KREY011,"Krey, Alexander ( Alex )",IV,D
ROME021,"Romero, Thomas ( TJ )",IV,D
STOD011,"Stoddard, Ryan ( Ryan )",IV,D
ANDR041,"Andrewson, Noah ( Noah )",V,D
CRES031,"Cresswell, Connor ( Connor )",V,D
DIRO012,"DiRocco, Aydan ( Aydan )",V,D
DUNB012,"Dunbar, Brandon ( Brandon )",V,D
FAN011,"Fan, Justin ( Justin )",V,D
LONG041,"Long, Jackson ( Jack )",V,D
SCHW031,"Schwarting, Christopher ( Christopher )",V,D
WHIT111,"White, Michael ( Ian )",V,D
ASCH013,"Aschkenasy, Charles ( Charlie )",VI,D
BEIF011,"Beifeld, William ( Billy )",VI,D
BIRD012,"Birdsall, Nicholas ( Nicholas )",VI,D
BURT032,"Burt, William ( Wills )",VI,D
DIRO011,"DiRocco, Ryan ( Ryan )",VI,D
DOUG041,"Douglas, Cameron ( Cameron )",VI,D
FALK011,"Falk, James ( James )",VI,D
GETZ011,"Getz, Ryan ( Ryan )",VI,D
GLAD011,"Gladden, Alir ( Alir )",VI,D
HANS061,"Hans, Joshua ( Josh )",VI,D
KAO011,"Kao, Dylan ( Dylan )",VI,D
NEK0011,"Nekoumand, Alexander ( Z )",VI,D
RALL011,"Rall, Connor ( Connor )",VI,D
RANT012,"Rantanen, Grady ( Grady )",VI,D
SARD012,"Sardesai, Arnav ( Arnav )",VI,D
SAWH011,"Sawhney, Neil ( Neil )",VI,D
SHUC011,"Shuchman, Isaiah ( Isaiah )",VI,D
SULL012,"Sullivan, Jack ( Jack )",VI,D
TANK011,"Tank, Megh ( Megh )",VI,D
WIST011,"Astorga Wister, William ( Orion )",VI,D
WOOD012,"Wood, Ronan ( Ronan )",VI,D
MCCL053,"McClave, Jude ( Jude )",IV,E
BARN071,"Barnes-Pace, Michael ( Mick )",V,E
BONG011,"Bongiovanni, Joseph ( Quin )",V,E
BOWE031,"Bowers, Quintin ( Quintin )",V,E
GLAS032,"Glaser, Andrew ( Drew )",V,E
HERB011,"Herbert, Graeme ( Graeme )",V,E
LYON031,"Lyon, Andrew ( Andrew )",V,E
SHAT012,"Shatzman, Chase ( Chase )",V,E
VOGE011,"Vogel, Tanner ( Tanner )",V,E
WALK062,"Walker, William ( William )",V,E
WU021,"Wu, Preston ( Preston )",V,E
BALA011,"Balachandran, Miles ( Miles )",VI,E
CAMP071,"Campbell, James ( Jac )",VI,E
CARR041,"Carrillo, Jonathan ( Jonathan )",VI,E
CHAN031,"Chan, Ethan ( Ethan )",VI,E
CURT021,"Curtis, Dylan ( Dylan )",VI,E
DENM011,"Denmark, Yasir ( Yasir )",VI,E
DIRO011,"DiRocco, Ryan ( Ryan )",VI,E
DONN011,"Donnelly, Cole ( Cole )",VI,E
DUNC011,"Dunckel, Peter ( Pete )",VI,E
FALK011,"Falk, James ( James )",VI,E
FORD022,"Ford, Bryce ( Bryce )",VI,E
FRAN031,"Francis, Jamir ( Jamir )",VI,E
HANS061,"Hans, Joshua ( Josh )",VI,E
HERD012,"Herdler, Owen ( Owen )",VI,E
KAO011,"Kao, Dylan ( Dylan )",VI,E
LEAR012,"Leary, Brendan ( Brendan )",VI,E
MARS021,"Marshall, Adam ( Adam )",VI,E
MIRI011,"Mirin, Nathan ( Nate )",VI,E
PARA031,"Parayre, Roch ( Roch )",VI,E
PEND032,"Pendergast, Thomas ( Thomas )",VI,E
QUAT011,"Quatrani, Mark ( Mark )",VI,E
ROSE081,"Rosenberg, Charles ( Charlie )",VI,E
SUTE011,"Suter, John ( Jack )",VI,E
AGGA012,"Aggarwal, Arsh ( Arsh )",V,F
BELD011,"Belden, Daniel ( Daniel )",V,F
BRAD061,"Bradley, Andrew ( Andrew )",V,F
BREW012,"Brewington, Ryan ( Ryan )",V,F
CERN011,"Cerniglia, Robert ( Robert )",V,F
CRES031,"Cresswell, Connor ( Connor )",V,F
ETHE011,"Etherington, Lowen ( Lowen )",V,F
FESN011,"Fesnak, Luke ( Luke )",V,F
FORT021,"Forte, Jackson ( Jackson )",V,F
GATE011,"Gates, James ( James )",V,F
GILL061,"Gillespie, Connor ( Connor )",V,F
HOYT013,"Hoyt, Benjamin ( Benjamin )",V,F
JIRU011,"Jiru, Samuel ( Samuel )",V,F
JORD011,"Jordan, Frederick ( Fred )",V,F
KAIS021,"Kaiser, Daniel ( Daniel )",V,F
KEID011,"Keidel, Philip ( Charlie )",V,F
KOHL022,"Kohlenberg, John ( John )",V,F
KOHN011,"Kohn, Edwin ( Eddie )",V,F
MCCO051,"McComb, Benjamin ( Ben )",V,F
MIGN012,"Mignucci, Nicholas ( Nicholas )",V,F
PRYM011,"Pryma, Reilly ( Reilly )",V,F
ROUS012,"Rouse, John ( John )",V,F
SEWA021,"Seward, William ( Henry )",V,F
SMIT151,"Smith, Holden ( Holden )",V,F
STEW061,"Stewart, David ( David )",V,F
WILL072,"Williams, Casey ( Casey )",V,F
WOLI011,"Wolitarsky, James ( William )",V,F
WYLI011,"Wylie, Michael ( Michael )",V,F
YOUN052,"Young, Banks ( Banks )",V,F
BROS011,"Brosko, William ( Billy )",VI,F
CARR041,"Carrillo, Jonathan ( Jonathan )",VI,F
HERR023,"Herrmann, Alex ( Alex )",VI,F
KANG031,"Kang, Matthew ( Matthew )",VI,F
LEAR012,"Leary, Brendan ( Brendan )",VI,F
PENN013,"Pennington, Harvey ( Harvey )",VI,F
PLUM011,"Plumer-Butler, Jasir ( Jasir )",VI,F
QUAT011,"Quatrani, Mark ( Mark )",VI,F
ZELL022,"Zeller, Colin ( Colin )",VI,F
CLOR023,"Cloran, Duke ( Duke )",IV,G
DOMB011,"Dombar, Simon ( Simon )",IV,G
JONE072,"Jones, Preston ( Preston )",IV,G
LEE101,"Lee, Semaj ( Semaj )",IV,G
LU011,"Lu, Nicholas ( Nicholas )",IV,G
BAKE031,"Baker, Dawson ( Dawson )",V,G
BART021,"Bartholdson, Anders ( Anders )",V,G
BROD031,"Brodnik, Sean ( Sean )",V,G
COLS011,"Colsher, Ryan ( Ryan )",V,G
CUDD021,"Cuddeback, John ( Jack )",V,G
FEIG011,"Feigenberg, Matthew ( Matthew )",V,G
FORT021,"Forte, Jackson ( Jackson )",V,G
GLAS032,"Glaser, Andrew ( Drew )",V,G
KAHA011,"Kahana, Nathan ( Nathan )",V,G
KELL081,"Kelly, William ( William )",V,G
MCCA102,"McCarthy, Benjamin ( Ben )",V,G
MCCO051,"McComb, Benjamin ( Ben )",V,G
MURP021,"Murphy, Brody ( Brody )",V,G
POPK011,"Popky, Robert ( Bobby )",V,G
ROSE072,"Rosenberger, Anthony ( A.J. )",V,G
SCAN011,"Scanlan, Connor ( Connor )",V,G
STAL031,"Stallkamp, Brady ( Brady )",V,G
WATS041,"Watson, Luke ( Luke )",V,G
ATKI031,"Atkinson, Louis ( Louie )",VI,G
BALA011,"Balachandran, Miles ( Miles )",VI,G
BIRD012,"Birdsall, Nicholas ( Nicholas )",VI,G
BROS011,"Brosko, William ( Billy )",VI,G
BUSS011,"Busser, Thaddeus ( Teddy )",VI,G
CAES011,"Caesar, Julian ( Julian )",VI,G
CALL031,"Callahan, Jeremy ( Jeremy )",VI,G
CAMP071,"Campbell, James ( Jac )",VI,G
CASE023,"Case, Andrew ( Andrew )",VI,G
CHEN071,"Chen, Jingyuan ( Jingyuan )",VI,G
COOL012,"Cooleen, Brendan ( Brendan )",VI,G
CROW031,"Crowther, Jay ( Jay )",VI,G
DAVE032,"Davey, Ryan ( Ryan )",VI,G
EVAN041,"Evans, Alphonso ( Alphonso )",VI,G
FLIN022,"Flinn, Wells ( Wells )",VI,G
FORD022,"Ford, Bryce ( Bryce )",VI,G
FRAN021,"Franz, Matthew ( Matthew )",VI,G
GHAN011,"Ghanem, Yonas ( Yonas )",VI,G
GOWE012,"Gowen, Henry ( Henry )",VI,G
HEND041,"Henderson, Jason ( Jason )",VI,G
KAUF011,"Kauffman, Joseph ( Joey )",VI,G
KIM071,"Kim, Geonho ( Brian )",VI,G
KIRW011,"Kirwan, Andrew ( Andrew )",VI,G
MCCU021,"McCune, Love ( Love )",VI,G
MCCU041,"McCullough, Harrison ( Harrison )",VI,G
MCDO041,"McDonnell, James ( Jay )",VI,G
MIST011,"Mistry, Kiran ( Kiran )",VI,G
NDEG011,"Ndegwa-Brown, Amani ( Amani )",VI,G
PARA031,"Parayre, Roch ( Roch )",VI,G
PENN021,"Pennewill, Joseph ( Joey )",VI,G
PINS011,"Pinsk, Connor ( Connor )",VI,G
POWE031,"Powell, Zachary ( Zach )",VI,G
SARD012,"Sardesai, Arnav ( Arnav )",VI,G
SHAH013,"Shah, Zachary ( Zachary )",VI,G
SHEA031,"Shea, Aedan ( Aedan )",VI,G
SQUI011,"Squillaro, Jack ( Jack )",VI,G
TOUE011,"Touey, Brendan ( Brendan )",VI,G
WEIN012,"Weinstein, Luke ( Luke )",VI,G
WRIG031,"Wright, Gavin ( Gavin )",VI,G
YU031,"Yu, Owen ( Owen )",VI,G"""

    # creating a csv reader object from the multi-line string
    csvreader = csv.reader(csv_data.split('\n'))

    # extracting field names through first row,
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        print(row)
        free = row[periodIndex]
        if free == period:
            name = row[nameIndex]
            grade = row[gradeIndex]
            students[name] = Student(grade)

    return students
print(getStudents("B"))