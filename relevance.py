import pandas as pd
from tabulate import tabulate


def tabulated_data_to_list(tabulated_data):
    # Split the tabulated data into lines
    lines = tabulated_data.strip().split("\n")

    # Initialize an empty list to store the data
    data = []

    # Determine the column widths based on the first non-dash line
    for line in lines:
        if not all(char == "-" for char in line):
            col_widths = [len(word.strip()) for word in line.split()]
            break

    # Iterate through the remaining lines to extract the data rows
    for line in lines:
        if not all(char == "-" for char in line):
            row_data = [item.strip() for item in line.split()]

            # handle multi-word entries
            if len(row_data) > 5:
                row_data[0] = " ".join(row_data[:-4])
                row_data = [row_data[0]] + row_data[-4:]

            data.append(row_data)

    table_as_list = data

    return table_as_list


# Example usage:
word2vec_data = """
 query                                                           ground truth    semantic search    common articles    common links
------------------------------------------------------------  --------------  -----------------  -----------------  --------------
„weird al“ yankovic                                                        0                 10                  0               0
π (aðgreining)                                                             0                 10                  0               0
π dagur                                                                    1                 10                  0              58
vagna                                                                     15                 10                  0             249
vagn                                                                      29                 10                  0             665
vaktir                                                                     4                 10                  0              95
vaka                                                                      21                 10                  0             321
vaka (nafn)                                                                0                 10                  0               0
vafri                                                                      5                 10                  0             126
vatnshellir                                                                0                 10                  0               0
vatn                                                                     636                 10                  0           10833
vatnalíffræði                                                              2                 10                  0             113
vatnsmýri                                                                  0                 10                  0               0
vattarsaumur                                                               0                 10                  0               0
vatnajökulsþjóðgarður                                                      0                 10                  0               0
vatnafræði                                                                 2                 10                  0              94
vatnshlot                                                                  1                 10                  0              42
vatnaskógur                                                                0                 10                  0               0
vatnsorka                                                                  1                 10                  0              57
vatnsdæla saga                                                             0                 10                  0               0
vatnajökull                                                                0                 10                  0               0
vatnar                                                                     0                 10                  0               0
vatnsveita reykjavíkur                                                     0                 10                  0               0
vatt                                                                      13                 10                  0             322
vaðmál                                                                     4                 10                  0              94
varppípa                                                                   0                 10                  0               0
varða                                                                    181                 10                  0            2881
varna                                                                    101                 10                  0            1657
varta                                                                     72                 10                  0            1186
varalið lögreglunnar                                                       0                 10                  0               0
varúlfur                                                                   0                 10                  0               0
varnarræða sókratesar (xenofon)                                            0                 10                  0               0
varnarstríð                                                                2                 10                  0              53
varðhundur                                                                 4                 10                  0              79
varmafræði                                                                 9                 10                  0             257
varmajafnvægi                                                              0                 10                  0               0
varmi                                                                      3                 10                  0             120
varmárskóli                                                                0                 10                  0               0
varpasveifgras                                                             1                 10                  0              22
varðskip                                                                   7                 10                  0             128
varsjá                                                                     0                 10                  0               0
varaforseti bandaríkjanna                                                  0                 10                  0               0
varg vikernes                                                              0                 10                  0               0
varið land                                                                 1                 10                  0              16
varði goes europe                                                          0                 10                  0               0
varmaland                                                                  0                 10                  0               0
vajana tríó tungumál                                                       0                 10                  0               0
valdimar atterdag                                                          0                 10                  0               0
vallaskóli                                                                 2                 10                  0              32
vallarsveifgras                                                            2                 10                  0              51
valentínusar bræðurnir                                                     0                 10                  0               0
valgerður gunnarsdóttir                                                    0                 10                  0               0
vala                                                                      80                 10                  0            1274
valgerður dan                                                              0                 10                  0               0
vallhnúfa                                                                  0                 10                  0               0
valdís óskarsdóttir                                                        0                 10                  0               0
valgeir                                                                    0                 10                  0               0
valréttarsamningur                                                         2                 10                  0              49
valgerður bjarnadóttir                                                     0                 10                  0               0
valgerður sverrisdóttir                                                    0                 10                  0               0
vallarrýgresi                                                              0                 10                  0               0
valladolid                                                                 0                 10                  0               0
vallarfoxgras                                                              2                 10                  0              53
valgerður                                                                  0                 10                  0               0
valdimar sigursæli                                                         0                 10                  0               0
valtýr guðmundsson                                                         0                 10                  0               0
valdís arnardóttir                                                         0                 10                  0               0
valdís                                                                     0                 10                  0               0
valkyrja                                                                   0                 10                  0               0
val                                                                     1347                 10                  0           20676
vallarheiði                                                                0                 10                  0               0
valur gunnarsson                                                           0                 10                  0               0
vald                                                                     610                 10                  0            9494
valur (mannsnafn)                                                          0                 10                  0               0
valgarður egilsson                                                         0                 10                  0               0
vala þórsdóttir                                                            0                 10                  0               0
val di chiana                                                              0                 10                  0               0
valur ingimundarson                                                        0                 10                  0               0
valur                                                                     13                 10                  0             206
valdimar indriðason                                                        0                 10                  0               0
valdi                                                                    155                 10                  0            2837
valva                                                                     14                 10                  0             226
valdimar                                                                   0                 10                  0               0
vanadín                                                                    0                 10                  0               0
van morrison                                                               0                 10                  0               0
vantrú                                                                     0                 10                  0               0
vanda                                                                     78                 10                  0            1312
vantaa                                                                     0                 10                  0               0
vanessa hudgens                                                            0                 10                  0               0
vanúatú                                                                    0                 10                  0               0
vanir                                                                     14                 10                  0             381
vampíra                                                                    3                 10                  0             138
vamm                                                                      40                 10                  0             607
vaduz                                                                      0                 10                  0               0
vax                                                                      242                 10                  0            4004
vaxtavextir                                                                0                 10                  0               0
vasco da gama                                                              0                 10                  0               0
vasco da gama brúin                                                        0                 10                  0               0
væntigildi                                                                 0                 10                  0               0
vænisýki                                                                   0                 10                  0               0
vænghaf                                                                    9                 10                  0             153
vögguprent                                                                 1                 10                  0              56
vöggur                                                                     0                 10                  0               0
vöggudauði                                                                 0                 10                  0               0
vökvi                                                                     22                 10                  0             383
vötnin miklu                                                               0                 10                  0               0
vöðuselur                                                                  0                 10                  0               0
vöðvi                                                                      5                 10                  0              99
vörður                                                                    38                 10                  0             637
vörtusvín                                                                  2                 10                  0             114
vörtubaugur                                                                1                 10                  0              34
vörumerki                                                                 20                 10                  0             360
vörubíll                                                                   1                 10                  0              16
vörpun                                                                    28                 10                  0             559
völundur                                                                   0                 10                  0               0
völuspá                                                                    0                 10                  0               0
vönun                                                                      0                 10                  0               0
viva la bam                                                                0                 10                  0               0
viasat history                                                             0                 10                  0               0
vigur                                                                     38                 10                  0             689
vigdís grímsdóttir                                                         0                 10                  0               0
vigri                                                                      4                 10                  0              60
viggó                                                                      0                 10                  0               0
vigdís finnbogadóttir                                                      0                 10                  0               0
viggó viðutan                                                              0                 10                  0               0
vigfús                                                                     1                 10                  0              18
vigdís gunnarsdóttir                                                       0                 10                  0               0
vignir svavarsson                                                          0                 10                  0               0
vigur (mannsnafn)                                                          0                 10                  0               0
vigur (eyja)                                                               0                 10                  0               0
vigdís                                                                     0                 10                  0               0
vigur (stærðfræði)                                                         0                 10                  0               0
vigdís hrefna pálsdóttir                                                   0                 10                  0               0
viktor dyk                                                                 0                 10                  0               0
vikivaki (aðgreining)                                                      0                 10                  0               0
viktoría bretadrottning                                                    0                 10                  0               0
viktor                                                                     1                 10                  0              16
viktor emmanúel 2.                                                         0                 10                  0               0
vika bókarinnar                                                            0                 10                  0               0
vikur                                                                     20                 10                  0             391
vikivaki                                                                   2                 10                  0              44
vikar                                                                      5                 10                  0              74
viktor arnar ingólfsson                                                    0                 10                  0               0
viktoría spans - íslenzk lög gömul og ný                                   0                 10                  0               0
vika                                                                      42                 10                  0             937
vitinn í faros við alexandríu                                              0                 10                  0               0
vitis vinifera                                                             1                 10                  0              45
viti                                                                      36                 10                  0             684
viðskeyti                                                                 10                 10                  0             250
viðurlag                                                                   1                 10                  0              44
viðskiptaráð íslands                                                       0                 10                  0               0
viðbót maxwells                                                            0                 10                  0               0
viðtalsbil                                                                 0                 10                  0               0
viðskipti                                                                 22                 10                  0             359
viðtengingarháttur                                                         3                 10                  0              51
viðar eggertsson                                                           0                 10                  0               0
viðskiptafræði                                                            12                 10                  0             274
viðbót                                                                    24                 10                  0             415
viðskiptabann bandaríkjanna gegn kúbu                                      0                 10                  0               0
viðar                                                                     47                 10                  0             954
viðja                                                                      0                 10                  0               0
viðarkol                                                                   3                 10                  0              51
viðskiptavild                                                              0                 10                  0               0
viðmótshönnun                                                              1                 10                  0              60
viðskiptaáætlun                                                            1                 10                  0              46
viðlíking                                                                  2                 10                  0              76
viðurnefni                                                                27                 10                  0             533
viðey                                                                      0                 10                  0               0
virgill (mannsnafn)                                                        0                 10                  0               0
virginía (fylki)                                                           0                 10                  0               0
virki (stærðfræði)                                                         0                 10                  0               0
virðisaukaskattur                                                          0                 10                  0               0
virk skilyrðing                                                            0                 10                  0               0
virtual console (wii)                                                      0                 10                  0               0
virginía (mannsnafn)                                                       0                 10                  0               0
virginia woolf                                                             0                 10                  0               0
virgill                                                                    0                 10                  0               0
vilhjálmur stefánsson                                                      0                 10                  0               0
vilhjálmur bretaprins                                                      0                 10                  0               0
villa (mannsnafn)                                                          0                 10                  0               0
vilníus                                                                    0                 10                  0               0
vilhjálmur 4. bretakonungur                                                0                 10                  0               0
villa park                                                                 0                 10                  0               0
vilhjálmur vilhjálmsson - glugginn hennar kötu                             0                 10                  0               0
villi                                                                     21                 10                  0             331
vilma                                                                      0                 10                  0               0
vilhjálmur og elly vilhjálms syngja jólalög                                0                 10                  0               0
vilhjálmur og ellý vilhjálms - lög sigfúsar halldórssonar                  0                 10                  0               0
villiljós                                                                  0                 10                  0               0
vilhjálmur                                                                 0                 10                  0               0
vilmundur gylfason                                                         0                 10                  0               0
vilhjálmur 2. þýskalandskeisari                                            0                 10                  0               0
vilhjálmur vilhjálmsson - hún hring minn ber                               0                 10                  0               0
villanueva de azoague                                                      0                 10                  0               0
vilhjálmur þ. vilhjálmsson                                                 0                 10                  0               0
vilborg                                                                    0                 10                  0               0
viljar                                                                     0                 10                  0               0
vilhjálmur tell                                                            0                 10                  0               0
vilhelm                                                                    0                 10                  0               0
villiköttur                                                                1                 10                  0              85
vilji (norræn goðafræði)                                                   0                 10                  0               0
vilhjálmur einarsson                                                       0                 10                  0               0
vilborg halldórsdóttir                                                     0                 10                  0               0
villutrú                                                                   6                 10                  0             265
vilhjálmur árnason                                                         0                 10                  0               0
vila nova de gaia                                                          0                 10                  0               0
vilhjálmur vilhjálmsson - allt er breytt                                   0                 10                  0               0
vilhjálmur vilhjálmsson - myndin af þér - einni þér ég ann                 0                 10                  0               0
vilpa                                                                      0                 10                  0               0
vilji                                                                     15                 10                  0             315
vilhjálmur vilhjálmsson - fjórtán fyrstu lögin                             0                 10                  0               0
vilhjálmur þögli                                                           0                 10                  0               0
vilhjálmur og elly vilhjálms - lög tólfta september                        0                 10                  0               0
vilhelm marstrand                                                          0                 10                  0               0
vilhjálmur alexander hollandsprins                                         0                 10                  0               0
vindrós                                                                    2                 10                  0              61
vindhani                                                                   0                 10                  0               0
vinir einkabílsins                                                         0                 10                  0               0
vingjarnlegar tölur                                                        1                 10                  0              15
vinaleið                                                                   0                 10                  0               0
vinsælasti sjónvarpsmaður ársins                                           0                 10                  0               0
vinarþel ókunnugra                                                         0                 10                  0               0
vinna                                                                    188                 10                  0            3201
vinir                                                                     12                 10                  0             196
vinnsluminni                                                               4                 10                  0             108
vinstrihreyfingin – grænt framboð                                          0                 10                  0               0
vincent van gogh                                                           0                 10                  0               0
vindur                                                                    15                 10                  0             271
vindauga                                                                   1                 10                  0              26
vindhraði                                                                  4                 10                  0             111
vinstristefna                                                              0                 10                  0               0
vinstri                                                                   50                 10                  0             768
vindar og breytingar                                                       0                 10                  0               0
vindmylla                                                                  2                 10                  0              35
vinnusálfræði                                                              1                 10                  0              47
vinnuveitendaábyrgð                                                        1                 10                  0              29
vindátt                                                                    8                 10                  0             169
vindorka                                                                   0                 10                  0               0
victoria                                                                   0                 10                  0               0
victor cilia                                                               0                 10                  0               0
victor                                                                     0                 10                  0               0
victor hugo                                                                0                 10                  0               0
victor moses                                                               0                 10                  0               0
victor williams                                                            0                 10                  0               0
vistfræði                                                                  7                 10                  0             259
visa-bikar karla 2008                                                      0                 10                  0               0
visa-bikar karla                                                           0                 10                  0               0
vistfang                                                                   3                 10                  0             149
vistmenning                                                                0                 10                  0               0
visa-bikar karla 2007                                                      0                 10                  0               0
vistuð stefja                                                              0                 10                  0               0
vistkerfi                                                                 10                 10                  0             276
visual basic .net                                                          0                 10                  0               0
vogar                                                                     10                 10                  0             186
vogarstöng                                                                 2                 10                  0              86
voice                                                                      1                 10                  0              17
vopnadómur                                                                 0                 10                  0               0
vopnuð átök                                                                9                 10                  0             181
vopnafjörður                                                               0                 10                  0               0
vopn                                                                     121                 10                  0            1992
vopni                                                                     10                 10                  0             155
vottar jehóva                                                              0                 10                  0               0
vordís                                                                     0                 10                  0               0
vorm                                                                       5                 10                  0              83
vorperla                                                                   1                 10                  0              55
vorpunktur                                                                 3                 10                  0              82
vorlaukur                                                                  0                 10                  0               0
volvo                                                                      0                 10                  0               0
voltaire                                                                   0                 10                  0               0
voltakross                                                                 0                 10                  0               0
volt                                                                      11                 10                  0             290
volga                                                                      2                 10                  0              50
volta                                                                      2                 10                  0              37
volfram                                                                    4                 10                  0             316
von (mannsnafn)                                                            0                 10                  0               0
von                                                                      236                 10                  0            3621
vonlenska                                                                  0                 10                  0               0
von neumann arkitektúr                                                     0                 10                  0               0
vodka                                                                      0                 10                  0               0
vodafone                                                                   0                 10                  0               0
vélbátur                                                                   2                 10                  0              74
vélhyggja                                                                  0                 10                  0               0
vélbúnaður                                                                 2                 10                  0             129
vélamál                                                                    7                 10                  0             128
vélinda                                                                    3                 10                  0              73
vélbyssa                                                                   3                 10                  0             115
vél                                                                      246                 10                  0            4162
véltækni hf.                                                               0                 10                  0               0
vé                                                                       353                 10                  0            6194
vladímír lenín                                                             0                 10                  0               0
vlad drakúla                                                               0                 10                  0               0
vladímír pútín                                                             0                 10                  0               0
vladimir nabokov                                                           0                 10                  0               0
vegir liggja til allra átta                                                0                 10                  0               0
vegur                                                                    168                 10                  0            2568
veggfóður (kvikmynd)                                                       0                 10                  0               0
veggfóður                                                                  1                 10                  0              41
vegamót (hús)                                                              0                 10                  0               0
vegamót                                                                    3                 10                  0              46
vegabréfsáritun                                                            2                 10                  0              72
vegalengd                                                                 22                 10                  0             382
veik beyging                                                               0                 10                  0               0
veigrunarorð                                                               1                 10                  0              16
veira                                                                      6                 10                  0              93
veirufræði                                                                 1                 10                  0              66
veigar                                                                    11                 10                  0             182
veiðar                                                                    32                 10                  0             601
veiki kjarnakraftur                                                        1                 10                  0              18
veigur                                                                     1                 10                  0              15
veiðimenn og safnarar                                                      0                 10                  0               0
veiga                                                                     18                 10                  0             278
veisla                                                                     7                 10                  0             106
veitingahús                                                                8                 10                  0             187
veitur                                                                     1                 10                  0              16
vefur                                                                     49                 10                  0             847
vefsíða                                                                   13                 10                  0             222
vefverslun                                                                 1                 10                  0              14
vefrit                                                                     8                 10                  0             132
veffang                                                                    0                 10                  0               0
vefleiðangur                                                               1                 10                  0              39
vetrarólympíuleikarnir 1980                                                0                 10                  0               0
vetrarólympíuleikarnir 1968                                                0                 10                  0               0
vetur                                                                     92                 10                  0            1610
vetrarólympíuleikarnir 1936                                                0                 10                  0               0
veturliði                                                                  0                 10                  0               0
vetrarólympíuleikarnir 2002                                                0                 10                  0               0
vetni                                                                     52                 10                  0            1593
vetrarólympíuleikarnir 2006                                                0                 10                  0               0
vetrarólympíuleikarnir 1952                                                0                 10                  0               0
vetrarólympíuleikarnir 1984                                                0                 10                  0               0
veðurathugunarstöð                                                        32                 10                  0             670
veðurstofa íslands                                                         0                 10                  0               0
veðurathugunarmaður                                                        1                 10                  0              23
veðkall                                                                    0                 10                  0               0
veðramót                                                                   0                 10                  0               0
veðurathugun                                                              34                 10                  0             630
veður                                                                    127                 10                  0            2069
veðurfarsfræði                                                             3                 10                  0             116
veðurspá                                                                   3                 10                  0             144
veðrun                                                                     7                 10                  0             215
veðurfræði                                                                25                 10                  0             508
verðlaun                                                                 336                 10                  0            7354
vernon g. little                                                           0                 10                  0               0
verslunarmannahelgi                                                        0                 10                  0               0
verkfæri                                                                  18                 10                  0             400
verðbréf                                                                  11                 10                  0             174
ver                                                                     6923                 10                  0          115399
verðbólga                                                                  3                 10                  0             143
verkfall                                                                   7                 10                  0             135
verkmenntaskólinn á akureyri                                               0                 10                  0               0
verslunarleið                                                              6                 10                  0             175
vera                                                                    1056                 10                  0           15463
vertíð                                                                     4                 10                  0              76
vera (tímarit)                                                             0                 10                  0               0
verkstæði jólasveinanna                                                    0                 10                  0               0
verksmiðja                                                                20                 10                  0             396
verzlunarskóli íslands                                                     0                 10                  0               0
vera (mannsnafn)                                                           0                 10                  0               0
veronika                                                                   0                 10                  0               0
ver (mannsnafn)                                                            0                 10                  0               0
verkstæði jólasveinanna - barnaleikrit eftir thorbjörn egner               0                 10                  0               0
verkfall grunnskólakennara 2004                                            0                 10                  0               0
vertigo                                                                    0                 10                  0               0
verund                                                                     3                 10                  0              58
verufræði                                                                 10                 10                  0             188
verk og dagar                                                              0                 10                  0               0
veröld andrésar andar                                                      0                 10                  0               0
verkfræði                                                                 70                 10                  0            1404
vernharður                                                                 0                 10                  0               0
verðtrygging                                                               0                 10                  0               0
vermont                                                                    0                 10                  0               0
verónika                                                                   0                 10                  0               0
verkakvennafélagið framsókn                                                0                 10                  0               0
verkamannabústaðir                                                         2                 10                  0              55
vertollur                                                                  1                 10                  0              24
vejle                                                                      0                 10                  0               0
velskur corgi                                                              0                 10                  0               0
veldi (stærðfræði)                                                         0                 10                  0               0
vellir                                                                    16                 10                  0             255
veldisfall                                                                 7                 10                  0             116
velvet revolver                                                            0                 10                  0               0
velska                                                                     5                 10                  0             107
venus (mannsnafn)                                                          0                 10                  0               0
venus (reikistjarna)                                                       0                 10                  0               0
veni, vidi, vici                                                           0                 10                  0               0
venus                                                                      0                 10                  0               0
venus (gyðja)                                                              0                 10                  0               0
vesturnorræn mál                                                           1                 10                  0              22
vestri                                                                   245                 10                  0            5403
vestmannsvatn                                                              0                 10                  0               0
vestnorræna ráðið                                                          0                 10                  0               0
vestfirskur einhljóðaframburður                                            0                 10                  0               0
vesturbær                                                                  0                 10                  0               0
vestar                                                                    25                 10                  0             503
vestmannaeyjar                                                             0                 10                  0               0
vesturland                                                                19                 10                  0             363
vestfirðir                                                                 1                 10                  0              21
vesturbyggð                                                                0                 10                  0               0
vesturgata                                                                 0                 10                  0               0
vestræn heimspeki                                                          0                 10                  0               0
vesturamt                                                                  2                 10                  0              39
vágur                                                                      3                 10                  0              56
vátrygging                                                                 3                 10                  0              95
váli                                                                       0                 10                  0               0
vma                                                                        0                 10                  0               0
v-2 flugskeyti                                                             0                 10                  0               0
víghóll                                                                    0                 10                  0               0
vígslubiskup                                                               7                 10                  0             143
vígslustig klerka                                                          0                 10                  0               0
vígvöllur                                                                  1                 10                  0              15
víkurkirkja (reykjavík)                                                    0                 10                  0               0
vík í mýrdal                                                               0                 10                  0               0
víkingaskip                                                                3                 10                  0             160
vík                                                                     1317                 10                  0           21773
víkingur                                                                   4                 10                  0              63
víkingar                                                                   8                 10                  0             132
víkingur (mannsnafn)                                                       0                 10                  0               0
víkin (noregi)                                                             0                 10                  0               0
víkin (reykjavík)                                                          0                 10                  0               0
víkur                                                                    452                 10                  0            7095
vífill (þræll)                                                             0                 10                  0               0
vífill (mannsnafn)                                                         0                 10                  0               0
víf                                                                       14                 10                  0             231
vítamín                                                                   15                 10                  0             324
vítaspyrnukeppni (knattspyrna)                                             0                 10                  0               0
víðir (mannsnafn)                                                          0                 10                  0               0
víðar (mannsnafn)                                                          0                 10                  0               0
víðavangshlaup ír                                                          0                 10                  0               0
víðar                                                                     43                 10                  0             651
víðnet                                                                     1                 10                  0              80
víðar (norræn goðafræði)                                                   0                 10                  0               0
víðir                                                                      5                 10                  0             141
vín (austurríki)                                                           0                 10                  0               0
vínber                                                                     3                 10                  0              74
vínarterta                                                                 1                 10                  0              30
vínland                                                                    0                 10                  0               0
vín                                                                      149                 10                  0            2601
víetnam                                                                    9                 10                  0             268
víetnamska                                                                 6                 10                  0             143
vímara peres                                                               0                 10                  0               0
vímuefni                                                                   1                 10                  0              70
víóletta                                                                   0                 10                  0               0
víóla                                                                      0                 10                  0               0
vídalín                                                                    0                 10                  0               0
víxlverkun                                                                14                 10                  0             300
víxlregla                                                                  1                 10                  0              72
vísindagrein                                                              27                 10                  0             523
vísir (stærðfræði)                                                         0                 10                  0               0
vísitala um þróun lífsgæða                                                 0                 10                  0               0
vísindaheimspeki                                                          16                 10                  0             372
vísir (dagblað)                                                            0                 10                  0               0
vísir (aðgreiningarsíða)                                                   0                 10                  0               0
vísindaleg aðferð                                                          1                 10                  0              15
vísindi                                                                   51                 10                  0            1319
vísitala                                                                  12                 10                  0             237
vísa                                                                     176                 10                  0            3326
vísitala neysluverðs                                                       2                 10                  0              92
vísitala atvinnufrelsis                                                    0                 10                  0               0
vísindaleg flokkun                                                         1                 10                  0              16
vúdú                                                                       0                 10                  0               0
v for vendetta                                                             0                 10                  0               0
v for vendetta (kvikmynd)                                                  0                 10                  0               0
v                                                                      17953                 10                  0          301614
avril lavigne                                                              0                 10                  0               0
aveiro (borg)                                                              0                 10                  0               0
aarbøger for nordisk oldkyndighed og historie                              0                 10                  0               0
aa                                                                       280                 10                  0            4399
aachen                                                                     0                 10                  0               0
agat                                                                      44                 10                  0             851
against me!                                                                0                 10                  0               0
agatha                                                                     0                 10                  0               0
agile                                                                      0                 10                  0               0
agða                                                                      72                 10                  0            1089
agrippa (heimspekingur)                                                    0                 10                  0               0
agla                                                                      12                 10                  0             185
agnes (nafn)                                                               0                 10                  0               0
agnar kofoed-hansen                                                        0                 10                  0               0
agnieszka włodarczyk                                                       0                 10                  0               0
agni                                                                     163                 10                  0            2395
agnar már magnússon                                                        0                 10                  0               0
agnes (kvikmynd)                                                           0                 10                  0               0
agnar jón egilsson                                                         0                 10                  0               0
agnar                                                                    193                 10                  0            2979
agnes                                                                     10                 10                  0             154
agent fresco                                                               0                 10                  0               0
akademían                                                                  4                 10                  0              60
akademískt frelsi                                                          0                 10                  0               0
akkadíska                                                                  3                 10                  0             148
akranes                                                                    0                 10                  0               0
akrafjall                                                                  0                 10                  0               0
akershus                                                                   0                 10                  0               0
akbar mikli                                                                0                 10                  0               0
akureyrarflugvöllur                                                        0                 10                  0               0
akureyri                                                                   0                 10                  0               0
akurhæna                                                                   1                 10                  0              85
akmeð 1.                                                                   0                 10                  0               0
aikido                                                                     1                 10                  0              84
airbus a380                                                                0                 10                  0               0
airport                                                                    0                 10                  0               0
aino freyja järvelä                                                        0                 10                  0               0
apavatn                                                                    0                 10                  0               0
apalhraun                                                                  3                 10                  0              87
apar                                                                      94                 10                  0            1835
apaplánetan (1968 kvikmynd)                                                0                 10                  0               0
apa                                                                      552                 10                  0            8877
apple ii                                                                   0                 10                  0               0
appelsínusafi                                                              0                 10                  0               0
apple cinema display                                                       0                 10                  0               0
apple mighty mouse                                                         0                 10                  0               0
apple inc.                                                                 0                 10                  0               0
apple i                                                                    0                 10                  0               0
apple store                                                                0                 10                  0               0
apple tv                                                                   0                 10                  0               0
apple (aðgreining)                                                         0                 10                  0               0
appelsína                                                                  3                 10                  0             136
apocalypse now                                                             0                 10                  0               0
aprílgabb                                                                  1                 10                  0              20
apríl                                                                    507                 10                  0            9380
aphex twin                                                                 0                 10                  0               0
aperture                                                                   0                 10                  0               0
apókrýf rit                                                                0                 10                  0               0
afganistan                                                                 0                 10                  0               0
aftaka                                                                     6                 10                  0             132
afturbrennari                                                              0                 10                  0               0
afturbolur                                                                 0                 10                  0               0
afturvirk hömlun                                                           1                 10                  0              21
afturbeygt fornafn                                                         1                 10                  0              18
afródíta                                                                   0                 10                  0               0
afréttur                                                                   2                 10                  0              35
afríska þjóðarráðið                                                        0                 10                  0               0
afríka sunnan sahara                                                       0                 10                  0               0
africa united                                                              0                 10                  0               0
afríkanska                                                                 3                 10                  0             212
afrískur svartviður                                                        0                 10                  0               0
afríka                                                                     3                 10                  0              66
afríka (skattland)                                                         0                 10                  0               0
afhöfðun                                                                   1                 10                  0              19
afhending                                                                 18                 10                  0             297
afleiðing                                                                 41                 10                  0             685
afleiðsla                                                                  1                 10                  0              15
afleiða (fjármál)                                                          0                 10                  0               0
afl                                                                     1067                 10                  0           16935
afleiða (stærðfræði)                                                       0                 10                  0               0
afleiða                                                                   19                 10                  0             335
afbygging                                                                  0                 10                  0               0
afbrigði latneska stafrófsins                                              0                 10                  0               0
afc suður                                                                  0                 10                  0               0
afc vestur                                                                 0                 10                  0               0
afc norður                                                                 0                 10                  0               0
afc austur                                                                 0                 10                  0               0
afþreying                                                                 15                 10                  0             241
afskautun                                                                  0                 10                  0               0
afs                                                                      790                 10                  0           12775
afstæðishyggja                                                             1                 10                  0              66
afstæðiskenning                                                           11                 10                  0             187
atvinnuvegir á íslandi                                                     0                 10                  0               0
atvinnubótavinna                                                           0                 10                  0               0
atviksorð                                                                  9                 10                  0             201
atviksliður                                                                0                 10                  0               0
atvinna                                                                    3                 10                  0              49
atvinnumálaráðherrar á íslandi                                             0                 10                  0               0
atferlisgreining                                                           2                 10                  0              83
atferlishyggja                                                             1                 10                  0             108
atferlismeðferð                                                            1                 10                  0              17
atom heart mother                                                          0                 10                  0               0
atorka group                                                               0                 10                  0               0
attention (gusgus plata)                                                   0                 10                  0               0
atti katti nóa                                                             0                 10                  0               0
athyglisbrestur                                                            1                 10                  0              80
athygli                                                                   81                 10                  0            1518
atlanta                                                                    0                 10                  0               0
atli (mannsnafn)                                                           0                 10                  0               0
atlas (mannsnafn)                                                          0                 10                  0               0
atlas                                                                      1                 10                  0              18
atli húnakonungur                                                          0                 10                  0               0
atli valason                                                               0                 10                  0               0
atli (ritverk)                                                             0                 10                  0               0
atlantis                                                                   0                 10                  0               0
atla                                                                      40                 10                  0             698
atli gíslason                                                              0                 10                  0               0
atlantsskip                                                                0                 10                  0               0
atli harðarson                                                             0                 10                  0               0
atli                                                                       4                 10                  0              60
atlantshaf                                                                 2                 10                  0              43
atli rafn sigurðarson                                                      0                 10                  0               0
atlantshafsþorskur                                                         0                 10                  0               0
ate                                                                      439                 10                  0            7067
atburðaminni                                                               2                 10                  0              56
atburður (líkindafræði)                                                    0                 10                  0               0
atómmassi                                                                  3                 10                  0             157
atómstöðin (kvikmynd)                                                      0                 10                  0               0
atómstöðin (skáldsaga)                                                     0                 10                  0               0
aðventa                                                                    0                 10                  0               0
aðventukrans                                                               1                 10                  0              17
aðalstræti                                                                 0                 10                  0               0
aðalsteinn                                                                 0                 10                  0               0
aðalvík                                                                    0                 10                  0               0
aðalsögn                                                                   3                 10                  0              61
aðalborg                                                                   1                 10                  0              16
aðalsveldi                                                                 0                 10                  0               0
aðalsetning                                                                5                 10                  0             125
aðalheiður                                                                 0                 10                  0               0
aðaltenging                                                                5                 10                  0             130
aðalskipulag                                                               9                 10                  0            1122
aðalsteinn bergdal                                                         0                 10                  0               0
aðalorð                                                                    2                 10                  0              40
aðalsöngvari                                                               8                 10                  0             128
aðgerð pólstjarnan                                                         0                 10                  0               0
aðgerð (stærðfræði)                                                        0                 10                  0               0
aðgerð (forritun)                                                          0                 10                  0               0
aðils                                                                      0                 10                  0               0
aðferðafræðileg náttúruhyggja                                              0                 10                  0               0
aðflutningur                                                               1                 10                  0              17
aðfangadagur                                                               0                 10                  0               0
að ferninga hring                                                          0                 10                  0               0
aðskeyti                                                                   5                 10                  0             120
araneus                                                                    0                 10                  0               0
arabíska                                                                 107                 10                  0            2259
aralvatn                                                                   0                 10                  0               0
arabískar tölur                                                            0                 10                  0               0
argumentum ad baculum                                                      0                 10                  0               0
argumentum ad hominem                                                      0                 10                  0               0
argon                                                                      3                 10                  0             212
argentína                                                                  0                 10                  0               0
arkitekt                                                                  44                 10                  0             808
arkansas                                                                   0                 10                  0               0
ari magnússon                                                              0                 10                  0               0
ari                                                                     3766                 10                  0           56681
aris                                                                      89                 10                  0            1529
ari þorgilsson                                                             0                 10                  0               0
ariel sharon                                                               0                 10                  0               0
arizona                                                                    0                 10                  0               0
ari kristinsson                                                            0                 10                  0               0
arial                                                                      0                 10                  0               0
ari fróði þorgilsson                                                       0                 10                  0               0
ari matthíasson                                                            0                 10                  0               0
aron                                                                      20                 10                  0             310
arthur conan doyle                                                         0                 10                  0               0
arthur miller                                                              0                 10                  0               0
art spiegelman                                                             0                 10                  0               0
arthur c. clarke                                                           0                 10                  0               0
arthur                                                                     0                 10                  0               0
artur balder                                                               0                 10                  0               0
artúr                                                                      1                 10                  0              16
arthur rimbaud                                                             0                 10                  0               0
articolo 31                                                                0                 10                  0               0
arthur schopenhauer                                                        0                 10                  0               0
arnljótur                                                                  0                 10                  0               0
arnold                                                                     0                 10                  0               0
arna                                                                    1104                 10                  0           17233
arngeir (landnámsmaður)                                                    0                 10                  0               0
arndís auðga steinólfsdóttir                                               0                 10                  0               0
arnar grétarsson                                                           0                 10                  0               0
arnbjörg (mannsnafn)                                                       0                 10                  0               0
arnbjörg (landnámskona)                                                    0                 10                  0               0
arnaut daniel                                                              0                 10                  0               0
arnar                                                                    399                 10                  0            6200
arnaldur                                                                   0                 10                  0               0
arngrímur gíslason málari                                                  0                 10                  0               0
arnór                                                                      0                 10                  0               0
arnljótur ólafsson                                                         0                 10                  0               0
arnaldur indriðason                                                        0                 10                  0               0
arngrímur jónsson lærði                                                    0                 10                  0               0
arnór benónýsson                                                           0                 10                  0               0
arnór hannibalsson                                                         0                 10                  0               0
arnbjörg sveinsdóttir                                                      0                 10                  0               0
arnkell                                                                    0                 10                  0               0
arnar sævarsson                                                            0                 10                  0               0
arnar jónsson                                                              0                 10                  0               0
arnika                                                                     0                 10                  0               0
ares (mannsnafn)                                                           0                 10                  0               0
are                                                                      515                 10                  0            8124
ares                                                                      11                 10                  0             187
ares (aðgreining)                                                          0                 10                  0               0
aretha franklin                                                            0                 10                  0               0
arezzo (sýsla)                                                             0                 10                  0               0
arent                                                                      8                 10                  0             119
armenía (mannsnafn)                                                        0                 10                  0               0
armin meiwes                                                               0                 10                  0               0
armed forces radio and television service keflavik                         0                 10                  0               0
armenska                                                                   3                 10                  0             166
aríi                                                                       6                 10                  0             123
aríus (mannsnafn)                                                          0                 10                  0               0
arctic death ship                                                          0                 10                  0               0
arctic monkeys                                                             0                 10                  0               0
archetype                                                                  0                 10                  0               0
arsenal                                                                    0                 10                  0               0
arsen                                                                     11                 10                  0             302
arsène wenger                                                              0                 10                  0               0
ahmed yassin                                                               0                 10                  0               0
ahmad al-mansur                                                            0                 10                  0               0
ajax (sófókles)                                                            0                 10                  0               0
alvar                                                                     37                 10                  0             568
alvar aalto                                                                0                 10                  0               0
alvilda                                                                    0                 10                  0               0
alvin                                                                     11                 10                  0             191
alaska (1875)                                                              0                 10                  0               0
alabastur                                                                  1                 10                  0              55
alaskavíðir                                                                0                 10                  0               0
alan keyes                                                                 0                 10                  0               0
alaskalúpína                                                               0                 10                  0               0
alan shearer                                                               0                 10                  0               0
alabama                                                                    0                 10                  0               0
alaska                                                                     0                 10                  0               0
alan hollinghurst                                                          0                 10                  0               0
alan turing                                                                0                 10                  0               0
algebruleg tala                                                            0                 10                  0               0
algonkinsk tungumál                                                        0                 10                  0               0
algyðistrú                                                                 4                 10                  0             150
algarve                                                                    0                 10                  0               0
algildi                                                                    5                 10                  0              79
algebra                                                                    7                 10                  0             210
alæta                                                                      2                 10                  0              34
alkestis (evripídes)                                                       0                 10                  0               0
alkóhólismi                                                                0                 10                  0               0
alkóhól                                                                    9                 10                  0             282
alkibíades i (platon)                                                      0                 10                  0               0
alkibíades ii (platon)                                                     0                 10                  0               0
alkalímálmur                                                               8                 10                  0             264
alkul                                                                      3                 10                  0             138
alice                                                                      0                 10                  0               0
alibýfluga                                                                 0                 10                  0               0
ali                                                                     2110                 10                  0           37030
alive (tölvuleikur)                                                        0                 10                  0               0
alien syndrome                                                             0                 10                  0               0
alfons mucha                                                               0                 10                  0               0
alfred north whitehead                                                     0                 10                  0               0
alfred jules ayer                                                          0                 10                  0               0
alfred nobel                                                               0                 10                  0               0
alfreð                                                                     0                 10                  0               0
alfa (mannsnafn)                                                           0                 10                  0               0
alfons                                                                     0                 10                  0               0
alfred hitchcock                                                           0                 10                  0               0
alfred edward taylor                                                       0                 10                  0               0
alfasundrun                                                                0                 10                  0               0
alfa                                                                      29                 10                  0             471
alfræðirit                                                                 9                 10                  0             306
alfred binet                                                               0                 10                  0               0
alois alzheimer                                                            0                 10                  0               0
alta                                                                     209                 10                  0            3226
altari                                                                    14                 10                  0             317
alræði                                                                    11                 10                  0             259
allianz arena                                                              0                 10                  0               0
allt í drasli                                                              0                 10                  0               0
allsherjarþing sameinuðu þjóðanna                                          0                 10                  0               0
allrahanda                                                                 1                 10                  0              85
allir litir hafsins eru kaldir                                             0                 10                  0               0
allraheilagramessa                                                         0                 10                  0               0
allah                                                                     41                 10                  0             620
alnæmi                                                                     1                 10                  0              17
alex                                                                       5                 10                  0              76
alexander mikli                                                            0                 10                  0               0
alec guinness                                                              0                 10                  0               0
alexander (aðgreining)                                                     0                 10                  0               0
alexander nehamas                                                          0                 10                  0               0
alexander frá afrodísías                                                   0                 10                  0               0
alexander graham bell                                                      0                 10                  0               0
alexander litvinenko                                                       0                 10                  0               0
alexander anderson (hellsing)                                              0                 10                  0               0
alexandre dumas eldri                                                      0                 10                  0               0
alexander von humboldt                                                     0                 10                  0               0
alexander mccall smith                                                     0                 10                  0               0
alexandra bretadrottning                                                   0                 10                  0               0
alexander petersson                                                        0                 10                  0               0
alexander severus                                                          0                 10                  0               0
alexandr púshkín                                                           0                 10                  0               0
alexander fleming                                                          0                 10                  0               0
alexa vega                                                                 0                 10                  0               0
alexandría (mannsnafn)                                                     0                 10                  0               0
alexanders saga                                                            0                 10                  0               0
alexander (mannsnafn)                                                      0                 10                  0               0
alexandra                                                                  0                 10                  0               0
alexander i                                                                0                 10                  0               0
alberta (mannsnafn)                                                        0                 10                  0               0
albert camus                                                               0                 10                  0               0
albus dumbledore                                                           0                 10                  0               0
albert bandura                                                             0                 10                  0               0
alberta (fylki)                                                            0                 10                  0               0
albrecht dürer                                                             0                 10                  0               0
albert eymundsson                                                          0                 10                  0               0
alba                                                                      57                 10                  0            1055
albert guðmundsson                                                         0                 10                  0               0
albanska                                                                   4                 10                  0             217
albert einstein                                                            0                 10                  0               0
albert                                                                     3                 10                  0              45
albert 2. belgíukonungur                                                   0                 10                  0               0
alberta                                                                    0                 10                  0               0
almenningssamgöngur                                                        4                 10                  0              70
alma                                                                      72                 10                  0            1293
almenn brot                                                                0                 10                  0               0
almaty                                                                     0                 10                  0               0
almennt ár                                                                 2                 10                  0              39
almannatengsl                                                              2                 10                  0              75
almæli                                                                     0                 10                  0               0
almannagjá                                                                 0                 10                  0               0
almenna afstæðiskenningin                                                  0                 10                  0               0
almenna verslunarfélagið                                                   0                 10                  0               0
alí                                                                      623                 10                  0            9401
alísa                                                                      1                 10                  0              15
alís                                                                      37                 10                  0             617
alí ibn abu talib                                                          0                 10                  0               0
al gore                                                                    0                 10                  0               0
aldurstakmark (kvikmyndir)                                                 0                 10                  0               0
alda (mannsnafn)                                                           0                 10                  0               0
aldursgreining með geislunarmælingu                                        1                 10                  0              21
aldar                                                                    807                 10                  0           13262
aldís                                                                     10                 10                  0             184
aldo moro                                                                  0                 10                  0               0
aldursgreining                                                             7                 10                  0             151
alcatraz                                                                   0                 10                  0               0
alcide de gasperi                                                          0                 10                  0               0
alcoa                                                                      0                 10                  0               0
alþingiskosningar 1967                                                     0                 10                  0               0
alþjóða siglingasambandið                                                  0                 10                  0               0
alþjóða skáksambandið                                                      0                 10                  0               0
alþjóða veðurfræðistofnunin                                                0                 10                  0               0
alþingiskosningar 1991                                                     0                 10                  0               0
alþjóða heilbrigðisstofnunin                                               0                 10                  0               0
alþingiskosningar 1933                                                     0                 10                  0               0
alþingiskosningar 1995                                                     0                 10                  0               0
alþingiskosningar 1999                                                     0                 10                  0               0
alþjóðlega geimstöðin                                                      0                 10                  0               0
alþingiskosningar 1987                                                     0                 10                  0               0
alþýðusamband íslands                                                      0                 10                  0               0
alþjóðatengsl íslands                                                      0                 10                  0               0
alþingiskosningar 1844                                                     0                 10                  0               0
alþjóðasamtök um eldfjallafræði                                            0                 10                  0               0
alþjóðlega einingakerfið                                                   0                 10                  0               0
alþingiskosningar 1949                                                     0                 10                  0               0
alþingiskosningar 1971                                                     0                 10                  0               0
alþingiskosningar 1974                                                     0                 10                  0               0
alþjóðasamband um jarðmælingar og jarðeðlisfræði                           0                 10                  0               0
alþjóða sundsambandið                                                      0                 10                  0               0
alþýðubókin (1874)                                                         0                 10                  0               0
alþjóðastofnun                                                            12                 10                  0             327
alþingiskosningar 1978                                                     0                 10                  0               0
alþjóðlegur baráttudagur kvenna                                            0                 10                  0               0
alþýðulýðveldið kína                                                       0                 10                  0               0
alþjóðlega staðlastofnunin                                                 0                 10                  0               0
alþingiskosningar 1963                                                     0                 10                  0               0
alþingiskosningar 1983                                                     0                 10                  0               0
alþjóðlega núllbaugsráðstefnan                                             0                 10                  0               0
alþjóðlegu náttúruverndarsamtökin                                          0                 10                  0               0
alþjóða portúgölskustofnunin                                               0                 10                  0               0
alþingiskosningar 2007                                                     0                 10                  0               0
alþingiskosningar 1946                                                     0                 10                  0               0
alþingisbækur íslands                                                      0                 10                  0               0
alþingiskosningar 1979                                                     0                 10                  0               0
alþingiskosningar 1953                                                     0                 10                  0               0
alþjóðlega hljóðstafrófið                                                  3                 10                  0              79
alþingiskosningar 2003                                                     0                 10                  0               0
alþingi                                                                   70                 10                  0            2123
alþjóða kjarnorkumálastofnunin                                             0                 10                  0               0
alsheimer                                                                  0                 10                  0               0
alsjálfvirkt skotvopn                                                      1                 10                  0              17
ayn rand                                                                   0                 10                  0               0
ananas                                                                     7                 10                  0             206
anastasía                                                                  0                 10                  0               0
anatole france                                                             0                 10                  0               0
analysis                                                                   1                 10                  0              15
anastasia                                                                  0                 10                  0               0
angela merkel                                                              0                 10                  0               0
angóla                                                                     0                 10                  0               0
angela                                                                     1                 10                  0              15
angi                                                                     249                 10                  0            4142
angantýr                                                                   0                 10                  0               0
ankara                                                                     0                 10                  0               0
anima                                                                      1                 10                  0              17
anime                                                                     30                 10                  0            1090
animals                                                                    0                 10                  0               0
anita                                                                      7                 10                  0             125
anime á íslandi                                                            0                 10                  0               0
anthony kenny                                                              0                 10                  0               0
anton tsjekhov                                                             0                 10                  0               0
antoine de saint-exupéry                                                   0                 10                  0               0
antimon                                                                    2                 10                  0             205
antónio de oliveira salazar                                                0                 10                  0               0
antonio vivaldi                                                            0                 10                  0               0
antónio lobo antunes                                                       0                 10                  0               0
anton                                                                      4                 10                  0              61
anthony hopkins                                                            0                 10                  0               0
anthrax                                                                    1                 10                  0              16
anja                                                                      46                 10                  0             729
anna frank                                                                 0                 10                  0               0
anno domini                                                                1                 10                  0              98
annars stigs jafna                                                         0                 10                  0               0
ann                                                                    11770                 10                  0          192666
anna og skapsveiflurnar                                                    0                 10                  0               0
anne rice                                                                  0                 10                  0               0
anna komnene                                                               0                 10                  0               0
anne                                                                     269                 10                  0            4534
annes                                                                    202                 10                  0            2983
annie oliv                                                                 0                 10                  0               0
anna politkovskaja                                                         0                 10                  0               0
anna akmatova                                                              0                 10                  0               0
anna nicole smith                                                          0                 10                  0               0
anna                                                                    3719                 10                  0           58580
annus horribilis                                                           1                 10                  0              15
anwar sadat                                                                0                 10                  0               0
aníta                                                                      2                 10                  0              32
an essay concerning human understanding                                    0                 10                  0               0
andleg viðleitni                                                           0                 10                  0               0
andrá                                                                      4                 10                  0              63
andleg heilsa                                                              0                 10                  0               0
andrómakka (evripídes)                                                     0                 10                  0               0
andatrú                                                                    0                 10                  0               0
andrés þór gunnlaugsson                                                    0                 10                  0               0
andorra                                                                    0                 10                  0               0
andhverfa                                                                  9                 10                  0             219
andri                                                                    146                 10                  0            2648
andy warhol                                                                0                 10                  0               0
andrúmsloft                                                               31                 10                  0             608
andrés önd                                                                 0                 10                  0               0
andorra la vella                                                           0                 10                  0               0
andlitsmynd                                                                1                 10                  0              17
andra                                                                     17                 10                  0             290
andrew johnson                                                             0                 10                  0               0
andrómeda                                                                  0                 10                  0               0
andrés                                                                     0                 10                  0               0
andlag                                                                    10                 10                  0             313
andakílsá                                                                  0                 10                  0               0
anders fogh rasmussen                                                      0                 10                  0               0
andakílsskóli                                                              0                 10                  0               0
andheiti                                                                   3                 10                  0             109
andrew jackson                                                             0                 10                  0               0
andrómeda (grísk goðafræði)                                                0                 10                  0               0
andrés magnússon                                                           0                 10                  0               0
andlát (aðgreining)                                                        0                 10                  0               0
and                                                                    11967                 10                  0          179804
andri snær magnason                                                        0                 10                  0               0
andrea                                                                     0                 10                  0               0
andlitsbein                                                                2                 10                  0              62
andaætt                                                                    8                 10                  0             332
andrew w. mellon                                                           0                 10                  0               0
andrúmsloft jarðar                                                         2                 10                  0              39
anders                                                                    30                 10                  0             536
andlát (hljómsveit)                                                        0                 10                  0               0
andrew carnegie                                                            0                 10                  0               0
andspyrna (hreyfing)                                                       0                 10                  0               0
abraham (mannsnafn)                                                        0                 10                  0               0
abraham (aðgreining)                                                       0                 10                  0               0
abraham                                                                    7                 10                  0             110
abrahamísk trúarbrögð                                                      0                 10                  0               0
abraham lincoln                                                            0                 10                  0               0
abraham van helsing                                                        0                 10                  0               0
abel (mannsnafn)                                                           0                 10                  0               0
abel                                                                      77                 10                  0            1323
aberdeen                                                                   0                 10                  0               0
abel tasman                                                                0                 10                  0               0
abbas 2.                                                                   0                 10                  0               0
abbas mikli                                                                0                 10                  0               0
abba                                                                      65                 10                  0            1241
abbey road                                                                 0                 10                  0               0
abu nuwas                                                                  0                 10                  0               0
abu daoud                                                                  0                 10                  0               0
abú dabí                                                                   0                 10                  0               0
abdullah bin abdul aziz al-saud                                            0                 10                  0               0
abstraktlist                                                               1                 10                  0              19
absolution                                                                 0                 10                  0               0
absolution tour                                                            0                 10                  0               0
august immanuel bekker                                                     0                 10                  0               0
augustin louis cauchy                                                      0                 10                  0               0
augustus de morgan                                                         0                 10                  0               0
auguste comte                                                              0                 10                  0               0
auga                                                                     281                 10                  0            5606
auglýsingar                                                                6                 10                  0             179
augntönn                                                                   0                 10                  0               0
auglýsingastofa reykjavíkur                                                0                 10                  0               0
aukatenging                                                                4                 10                  0             113
aukasetning                                                                7                 10                  0             171
aukasól                                                                    0                 10                  0               0
aukafall                                                                   6                 10                  0             185
autobahn                                                                   0                 10                  0               0
autobahn (nemendafélag)                                                    0                 10                  0               0
auðnutittlingur                                                            0                 10                  0               0
auðkennislykill                                                            0                 10                  0               0
auður jónsdóttir                                                           0                 10                  0               0
auður djúpúðga                                                             0                 10                  0               0
auður                                                                     32                 10                  0             479
auðgað úran                                                                0                 10                  0               0
auðólfur (landnámsmaður)                                                   0                 10                  0               0
auður eir vilhjálmsdóttir                                                  0                 10                  0               0
auðna                                                                      3                 10                  0              46
auðunn blöndal                                                             0                 10                  0               0
auðgunarbrot                                                               1                 10                  0              21
auðunn rauði                                                               0                 10                  0               0
auðunn                                                                     1                 10                  0              15
auðhumla                                                                   0                 10                  0               0
auður auðuns                                                               0                 10                  0               0
auðkennislykill (auðkenni)                                                 0                 10                  0               0
aurora                                                                     0                 10                  0               0
aulus persius flaccus                                                      0                 10                  0               0
auld lang syne                                                             0                 10                  0               0
audioslave                                                                 0                 10                  0               0
auckland grammar school                                                    0                 10                  0               0
auckland                                                                   0                 10                  0               0
austurför kýrosar                                                          0                 10                  0               0
austurbyggð                                                                0                 10                  0               0
austurrísku hagfræðingarnir                                                0                 10                  0               0
austin (texas)                                                             0                 10                  0               0
austurvöllur                                                               0                 10                  0               0
austurríki                                                                 0                 10                  0               0
austri (mannsnafn)                                                         0                 10                  0               0
austurnorræn mál                                                           2                 10                  0              44
austurstræti                                                               0                 10                  0               0
austur-hérað                                                               0                 10                  0               0
austar                                                                    16                 10                  0             247
austræn heimspeki                                                          0                 10                  0               0
austfirðir                                                                 1                 10                  0              18
austurland                                                                11                 10                  0             210
amanda                                                                     0                 10                  0               0
amadou toumani touré                                                       0                 10                  0               0
amal                                                                     176                 10                  0            3312
amiga 500                                                                  0                 10                  0               0
amper                                                                     12                 10                  0             347
amperstund                                                                 1                 10                  0              58
amon tobin                                                                 0                 10                  0               0
amos                                                                      17                 10                  0             261
amtsbókasafnið á akureyri                                                  0                 10                  0               0
amtmaður                                                                  12                 10                  0             241
amt                                                                     1197                 10                  0           19612
amhrán na bhfiann                                                          0                 10                  0               0
amharíska                                                                  7                 10                  0             256
american dad!                                                              0                 10                  0               0
american journal of philology                                              0                 10                  0               0
amerískur fótbolti                                                         1                 10                  0              87
american kennel club                                                       0                 10                  0               0
ameríkudeildin (nfl)                                                       0                 10                  0               0
amen                                                                     273                 10                  0            4410
american idol                                                              0                 10                  0               0
ameríka                                                                    0                 10                  0               0
ambulance                                                                  0                 10                  0               0
amd                                                                      165                 10                  0            2823
amsterdam                                                                  0                 10                  0               0
amsterdam (bók)                                                            0                 10                  0               0
a (aðgreining)                                                             0                 10                  0               0
a portuguesa                                                               0                 10                  0               0
a priori                                                                   0                 10                  0               0
a treatise of human nature                                                 0                 10                  0               0
a rush of blood to the head                                                0                 10                  0               0
a new day at midnight                                                      0                 10                  0               0
a beautiful mind                                                           0                 10                  0               0
a momentary lapse of reason                                                0                 10                  0               0
a                                                                      20419                 10                  0          372654
a clockwork orange (bók)                                                   0                 10                  0               0
a clockwork orange                                                         0                 10                  0               0
a saucerful of secrets                                                     0                 10                  0               0
aó                                                                        53                 10                  0             926
advance australia fair                                                     0                 10                  0               0
ada lovelace                                                               0                 10                  0               0
adam smith                                                                 0                 10                  0               0
ada                                                                      532                 10                  0            8929
adam sandler                                                               0                 10                  0               0
adam curtis                                                                0                 10                  0               0
adam                                                                       8                 10                  0             147
adobe systems                                                              0                 10                  0               0
adobe photoshop                                                            0                 10                  0               0
adobe dreamweaver                                                          0                 10                  0               0
adel                                                                      28                 10                  0             559
adelaide                                                                   0                 10                  0               0
admiral graf spee                                                          0                 10                  0               0
addi                                                                      19                 10                  0             324
adda                                                                      29                 10                  0             534
addis ababa                                                                0                 10                  0               0
a. paul weber                                                              0                 10                  0               0
actavis                                                                    0                 10                  0               0
acre (fylki)                                                               0                 10                  0               0
acetýlsalicýlsýra                                                          0                 10                  0               0
ac milan                                                                   0                 10                  0               0
axel revold                                                                0                 10                  0               0
axel                                                                      10                 10                  0             167
axel oxenstierna                                                           0                 10                  0               0
aþena (gyðja)                                                              0                 10                  0               0
aþena (mannsnafn)                                                          0                 10                  0               0
askur yggdrasils                                                           0                 10                  0               0
askja (fjall)                                                              0                 10                  0               0
ask                                                                     1049                 10                  0           16341
askasleikir                                                                0                 10                  0               0
askur (ílát)                                                               0                 10                  0               0
askur og embla                                                             0                 10                  0               0
askja (mannsnafn)                                                          0                 10                  0               0
askja (aðgreining)                                                         0                 10                  0               0
askur (mannsnafn)                                                          0                 10                  0               0
askar capital                                                              0                 10                  0               0
askur                                                                     26                 10                  0             422
asperger heilkenni                                                         0                 10                  0               0
asp                                                                       99                 10                  0            1735
aspar                                                                      5                 10                  0              89
asperger                                                                   0                 10                  0               0
astrid lindgren                                                            0                 10                  0               0
astrid belgíudrottning                                                     0                 10                  0               0
aston villa                                                                0                 10                  0               0
astrid                                                                     1                 10                  0              18
astana                                                                     0                 10                  0               0
astrópía                                                                   0                 10                  0               0
astmi                                                                      0                 10                  0               0
ashley tisdale                                                             0                 10                  0               0
asymmetric digital subscriber line                                         0                 10                  0               0
asía                                                                      28                 10                  0             449
assa                                                                     253                 10                  0            3898
assa (mannsnafn)                                                           0                 10                  0               0
gavrilo princip                                                            0                 10                  0               0
gagnfræðaskóli                                                             2                 10                  0              35
gagntæk vörpun                                                             2                 10                  0              62
gagnkynhneigð                                                              2                 10                  0              45
gagnagrunnur                                                               4                 10                  0              97
gaggenau (fyrirtæki)                                                       0                 10                  0               0
gagnauga (vefsíða)                                                         0                 10                  0               0
gagnrýni hreinnar skynsemi                                                 0                 10                  0               0
gagnstrokka hreyfill                                                       0                 10                  0               0
gagnkvæmni                                                                 1                 10                  0              44
gaia                                                                       0                 10                  0               0
gapastokkur                                                                1                 10                  0              34
gao xingjian                                                               0                 10                  0               0
gata                                                                     103                 10                  0            1802
gareth evans                                                               0                 10                  0               0
garðar (grænlandi)                                                         0                 10                  0               0
garden state                                                               0                 10                  0               0
gargandi snilld                                                            0                 10                  0               0
garðar svavarson                                                           0                 10                  0               0
garðabær                                                                   0                 10                  0               0
gary valentine                                                             0                 10                  0               0
garðahlynur                                                                0                 10                  0               0
garðar (mannsnafn)                                                         0                 10                  0               0
garðar olgeirsson - meira fjör                                             0                 10                  0               0
garðar                                                                    18                 10                  0             299
garnaveiki                                                                 2                 10                  0              86
garðar cortes                                                              0                 10                  0               0
garðar thór cortes                                                         0                 10                  0               0
garði                                                                     84                 10                  0            1266
garri                                                                      7                 10                  0             115
garðskagi                                                                  0                 10                  0               0
garður                                                                   102                 10                  0            1701
garpur                                                                     4                 10                  0              71
garðakál                                                                   6                 10                  0             202
gallerý fold                                                               0                 10                  0               0
galdramaður                                                                5                 10                  0             100
galdur (aðgreining)                                                        0                 10                  0               0
galdramál á íslandi                                                        0                 10                  0               0
galdur (mannsnafn)                                                         0                 10                  0               0
galdrastafur                                                               1                 10                  0              17
gallastríðið (caesar)                                                      0                 10                  0               0
gallblaðra                                                                 1                 10                  0              25
galdramál                                                                  1                 10                  0              21
gallrás                                                                    1                 10                  0              18
galatasaray                                                                0                 10                  0               0
galdur                                                                     5                 10                  0             118
gall                                                                      51                 10                  0            1045
galeiða                                                                    2                 10                  0              38
gangandi íkorni                                                            0                 10                  0               0
gana                                                                      32                 10                  0             527
ganýmedes (tungl)                                                          0                 10                  0               0
ganges                                                                     0                 10                  0               0
gabbró                                                                     2                 10                  0              43
gabriel metsu                                                              0                 10                  0               0
gabriel fauré                                                              0                 10                  0               0
gabríel (mannsnafn)                                                        0                 10                  0               0
gabriel axel                                                               0                 10                  0               0
gabon                                                                      2                 10                  0              39
gabríela                                                                   0                 10                  0               0
gabriel garcía márquez                                                     0                 10                  0               0
gabriel                                                                    0                 10                  0               0
gaumljós                                                                   2                 10                  0              50
gautur                                                                     2                 10                  0              28
gautama búdda                                                              0                 10                  0               0
gaukur                                                                     3                 10                  0              45
gauß-jordan eyðing                                                         0                 10                  0               0
gautaborg                                                                  0                 10                  0               0
gaui                                                                       0                 10                  0               0
gaupa                                                                      1                 10                  0             124
gauti                                                                      0                 10                  0               0
gaumstol                                                                   1                 10                  0              43
game boy línan                                                             0                 10                  0               0
game & watch                                                               0                 10                  0               0
gamlárskvöld                                                               4                 10                  0              58
gamelan                                                                    0                 10                  0               0
gamla ríkið                                                                0                 10                  0               0
gamma                                                                     11                 10                  0             236
gamecube                                                                   0                 10                  0               0
gammageisli                                                                1                 10                  0              23
gamanmynd                                                                 14                 10                  0             248
gamla mjólkursamlagið í borgarnesi                                         0                 10                  0               0
game boy                                                                   0                 10                  0               0
gamli vesturbærinn                                                         0                 10                  0               0
gamal abdel nasser                                                         0                 10                  0               0
gamla bíó                                                                  1                 10                  0              39
gamli sáttmáli                                                             0                 10                  0               0
gaddjökull                                                                 0                 10                  0               0
gaddavír                                                                   2                 10                  0              76
gasstöð reykjavíkur                                                        0                 10                  0               0
gas                                                                      993                 10                  0           16083
gasrisi                                                                    0                 10                  0               0
gægjuhneigð                                                                1                 10                  0              64
gæflaug                                                                    0                 10                  0               0
gæðingur                                                                   1                 10                  0              16
gæðamiðlun                                                                 0                 10                  0               0
gæsapartí                                                                  0                 10                  0               0
gæs                                                                       58                 10                  0            1239
gæsalappir                                                                 1                 10                  0             144
göfugu sannindin fjögur                                                    0                 10                  0               0
göran kropp                                                                0                 10                  0               0
giacomo puccini                                                            0                 10                  0               0
gizur                                                                      0                 10                  0               0
gipsy kings                                                                0                 10                  0               0
gif                                                                     3197                 10                  0           48550
gifting                                                                   12                 10                  0             214
giovanni pierluigi da palestrina                                           0                 10                  0               0
giorgio de chirico                                                         0                 10                  0               0
giovanni leone                                                             0                 10                  0               0
giordano bruno                                                             0                 10                  0               0
giovanni boccaccio                                                         0                 10                  0               0
gilbert ryle                                                               0                 10                  0               0
gil (hvalvatnsfirði)                                                       0                 10                  0               0
gils                                                                      94                 10                  0            1636
gillette stadium                                                           0                 10                  0               0
giljaflækja                                                                0                 10                  0               0
gild röksemdafærsla                                                        0                 10                  0               0
gildran (kvikmynd)                                                         0                 10                  0               0
gil eanes                                                                  0                 10                  0               0
gilitrutt (kvikmynd)                                                       0                 10                  0               0
gilbert harman                                                             0                 10                  0               0
gilbert                                                                    3                 10                  0              49
gilbert murray                                                             0                 10                  0               0
giljagaur                                                                  0                 10                  0               0
ginseng                                                                    1                 10                  0              36
giuseppe pella                                                             0                 10                  0               0
giuliano amato                                                             0                 10                  0               0
giuseppe scarampella                                                       0                 10                  0               0
giuseppe rossi                                                             0                 10                  0               0
giuseppe ungaretti                                                         0                 10                  0               0
giuseppe verdi                                                             0                 10                  0               0
gissur ísleifsson                                                          0                 10                  0               0
gissur einarsson (biskup)                                                  0                 10                  0               0
gistilíf                                                                   0                 10                  0               0
gisela striker                                                             0                 10                  0               0
gisele bündchen                                                            0                 10                  0               0
googol                                                                     2                 10                  0             103
google                                                                     1                 10                  0              17
googolplex                                                                 1                 10                  0              76
gottskálk grimmi nikulásson                                                0                 10                  0               0
gotland                                                                    0                 10                  0               0
gotti sigurðarson                                                          0                 10                  0               0
gottfried wilhelm von leibniz                                              0                 10                  0               0
gotneskur                                                                  1                 10                  0              65
goði                                                                      14                 10                  0             334
goðafræði                                                                147                 10                  0            2764
goð                                                                      221                 10                  0            3999
gormánuður                                                                 0                 10                  0               0
gordon brown                                                               0                 10                  0               0
gorkúla                                                                    1                 10                  0              43
gormur gamli                                                               0                 10                  0               0
golfklúbburinn keilir                                                      0                 10                  0               0
golfklúbburinn kjölur                                                      0                 10                  0               0
golfklúbburinn vestarr                                                     0                 10                  0               0
golfklúbbur álftaness                                                      0                 10                  0               0
golfklúbbur                                                                7                 10                  0             142
golfvöllur                                                                 3                 10                  0              74
golfklúbbur reykjavíkur                                                    0                 10                  0               0
golf                                                                      16                 10                  0             424
golda meir                                                                 0                 10                  0               0
godspeed you black emperor!                                                0                 10                  0               0
god save the queen (sex pistols)                                           0                 10                  0               0
god save the queen                                                         0                 10                  0               0
godfrey harold hardy                                                       0                 10                  0               0
gosdrykkur                                                                 4                 10                  0              81
gt pro series                                                              0                 10                  0               0
gramm (útgáfa)                                                             0                 10                  0               0
graham greene                                                              0                 10                  0               0
gramm                                                                     27                 10                  0             548
grameðla                                                                   1                 10                  0              90
grasaætt                                                                  19                 10                  0             720
grafík                                                                    11                 10                  0             169
graz                                                                       0                 10                  0               0
grafarvogur                                                                0                 10                  0               0
"""
tsdae_data = """
query                                                           ground truth    semantic search    common articles    common links
------------------------------------------------------------  --------------  -----------------  -----------------  --------------
„weird al“ yankovic                                                        0                 10                  0               0
π (aðgreining)                                                             0                 10                  0               0
π dagur                                                                    1                 10                  0              15
vaasa                                                                      0                 10                  0               0
vaarst                                                                     0                 10                  0               0
vagna                                                                     15                 10                  0             231
vagnbjörg                                                                  0                 10                  0               0
vagn                                                                      29                 10                  0             446
vaktir                                                                     4                 10                  0              66
vaka                                                                      21                 10                  0             335
vaka (nafn)                                                                0                 10                  0               0
vaka-helgafell                                                             0                 10                  0               0
vafri                                                                      5                 10                  0              97
vatnshellir                                                                0                 10                  0               0
vatn                                                                     636                 10                  0            9978
vatnakarpar                                                                0                 10                  0               0
vatíkanið                                                                  0                 10                  0               0
vatnalíffræði                                                              2                 10                  0              30
vatnsmýri                                                                  0                 10                  0               0
vattarsaumur                                                               0                 10                  0               0
vatnsdalur                                                                 0                 10                  0               0
vatnajökulsþjóðgarður                                                      0                 10                  0               0
vatnafræði                                                                 2                 10                  0              31
vatnspelastikk                                                             0                 10                  0               0
vatnshlot                                                                  1                 10                  0              14
vatnaskógur                                                                0                 10                  0               0
vatnsorka                                                                  1                 10                  0              16
vatnafjöll                                                                 0                 10                  0               0
vatnsvik                                                                   0                 10                  0               0
vattnes                                                                    0                 10                  0               0
vatnsreykjarpípa                                                           0                 10                  0               0
vatnsdæla saga                                                             0                 10                  0               0
vatnajökull                                                                0                 10                  0               0
vattarfjörður                                                              0                 10                  0               0
vatnar                                                                     0                 10                  0               0
vatnsveita reykjavíkur                                                     0                 10                  0               0
vatt                                                                      13                 10                  0             210
vaðmál                                                                     4                 10                  0              62
varppípa                                                                   0                 10                  0               0
varmar                                                                     0                 10                  0               0
varnarhættir                                                               1                 10                  0              18
varberg                                                                    0                 10                  0               0
varablómabálkur                                                            0                 10                  0               0
varða                                                                    181                 10                  0            2967
varró                                                                      0                 10                  0               0
varmdal                                                                    0                 10                  0               0
varna                                                                    101                 10                  0            1657
varta                                                                     72                 10                  0            1253
varalið lögreglunnar                                                       0                 10                  0               0
varúlfur                                                                   0                 10                  0               0
varmahlíð                                                                  0                 10                  0               0
varnarræða sókratesar (xenofon)                                            0                 10                  0               0
varsjárbandalagið                                                          0                 10                  0               0
varnarstríð                                                                2                 10                  0              31
varðhundur                                                                 4                 10                  0              71
varmafræði                                                                 9                 10                  0             176
varmajafnvægi                                                              0                 10                  0               0
varmi                                                                      3                 10                  0              50
varmárskóli                                                                0                 10                  0               0
varpasveifgras                                                             1                 10                  0              17
varsímaeyja                                                                0                 10                  0               0
varðskip                                                                   7                 10                  0             136
varsjá                                                                     0                 10                  0               0
varaforseti bandaríkjanna                                                  0                 10                  0               0
varahljóð                                                                  1                 10                  0              16
varg vikernes                                                              0                 10                  0               0
varið land                                                                 1                 10                  0              16
varði goes europe                                                          0                 10                  0               0
varmaland                                                                  0                 10                  0               0
vajana tríó tungumál                                                       0                 10                  0               0
vallakirkja                                                                0                 10                  0               0
valdimar atterdag                                                          0                 10                  0               0
vallaskóli                                                                 2                 10                  0              32
vallarsveifgras                                                            2                 10                  0              35
valentínusar bræðurnir                                                     0                 10                  0               0
valgerður gunnarsdóttir                                                    0                 10                  0               0
vala                                                                      80                 10                  0            1164
valrós                                                                     0                 10                  0               0
valtýr                                                                     0                 10                  0               0
valentínus                                                                 0                 10                  0               0
valgerður dan                                                              0                 10                  0               0
vallhnúfa                                                                  0                 10                  0               0
valíant                                                                    0                 10                  0               0
valencia                                                                   0                 10                  0               0
valhildur                                                                  0                 10                  0               0
valshamar                                                                  0                 10                  0               0
valbjörg                                                                   0                 10                  0               0
valdís óskarsdóttir                                                        0                 10                  0               0
valgeir                                                                    0                 10                  0               0
valves                                                                     0                 10                  0               0
valentín                                                                   0                 10                  0               0
valréttarsamningur                                                         2                 10                  0              30
valý                                                                       0                 10                  0               0
valbjört                                                                   0                 10                  0               0
valgerður bjarnadóttir                                                     0                 10                  0               0
valmar                                                                     0                 10                  0               0
valgerður sverrisdóttir                                                    0                 10                  0               0
vallarrýgresi                                                              0                 10                  0               0
valladolid                                                                 0                 10                  0               0
valbrandur                                                                 0                 10                  0               0
valþrúður                                                                  0                 10                  0               0
vallardagslátta                                                            0                 10                  0               0
vallý                                                                      0                 10                  0               0
vallarfoxgras                                                              2                 10                  0              31
valbjörn                                                                   0                 10                  0               0
valþór                                                                     0                 10                  0               0
vallakía                                                                   0                 10                  0               0
valbergur                                                                  0                 10                  0               0
valletta                                                                   0                 10                  0               0
valgerður                                                                  0                 10                  0               0
valdimar sigursæli                                                         0                 10                  0               0
valberg                                                                    0                 10                  0               0
valtýr guðmundsson                                                         0                 10                  0               0
valdís arnardóttir                                                         0                 10                  0               0
valgarður                                                                  0                 10                  0               0
valrún                                                                     1                 10                  0              15
valdís                                                                     0                 10                  0               0
valkyrja                                                                   0                 10                  0               0
valgarð                                                                    0                 10                  0               0
valmundur                                                                  0                 10                  0               0
val                                                                     1347                 10                  0           22044
valsteinn                                                                  0                 10                  0               0
vallarheiði                                                                0                 10                  0               0
valný                                                                      0                 10                  0               0
valter                                                                     0                 10                  0               0
valborg                                                                    0                 10                  0               0
valur gunnarsson                                                           0                 10                  0               0
valdarno                                                                   0                 10                  0               0
vald                                                                     610                 10                  0            9343
valur (mannsnafn)                                                          0                 10                  0               0
valgarður egilsson                                                         0                 10                  0               0
vala þórsdóttir                                                            0                 10                  0               0
valdheiður                                                                 0                 10                  0               0
valey                                                                      3                 10                  0              51
val di chiana                                                              0                 10                  0               0
valfríður                                                                  0                 10                  0               0
valería                                                                    0                 10                  0               0
vallelfting                                                                1                 10                  0              15
valbjörk                                                                   0                 10                  0               0
vallaður                                                                   0                 10                  0               0
valdór                                                                     0                 10                  0               0
valur ingimundarson                                                        0                 10                  0               0
valdemar                                                                   0                 10                  0               0
valur                                                                     13                 10                  0             225
valdimar indriðason                                                        0                 10                  0               0
valdi                                                                    155                 10                  0            2504
valva                                                                     14                 10                  0             216
valka                                                                      0                 10                  0               0
valentína                                                                  0                 10                  0               0
valdimar                                                                   0                 10                  0               0
vanadín                                                                    0                 10                  0               0
vangakirtill                                                               0                 10                  0               0
van morrison                                                               0                 10                  0               0
vandalar                                                                   1                 10                  0              15
vantrú                                                                     0                 10                  0               0
vanda                                                                     78                 10                  0            1383
vantaa                                                                     0                 10                  0               0
vanessa hudgens                                                            0                 10                  0               0
vankynssveppir                                                             1                 10                  0              42
vanúatú                                                                    0                 10                  0               0
vankjálkar                                                                 0                 10                  0               0
vanir                                                                     14                 10                  0             240
vandsveinn                                                                 0                 10                  0               0
vaud                                                                       1                 10                  0              15
vampíra                                                                    3                 10                  0              52
vamm                                                                      40                 10                  0             637
vaduz                                                                      0                 10                  0               0
vax                                                                      242                 10                  0            3867
vaxtavextir                                                                0                 10                  0               0
vasilíj sjúiskíj                                                           0                 10                  0               0
vasco da gama                                                              0                 10                  0               0
vasco da gama brúin                                                        0                 10                  0               0
vasaættin                                                                  0                 10                  0               0
vashti bunyan                                                              0                 10                  0               0
vænir                                                                      0                 10                  0               0
væntigildi                                                                 0                 10                  0               0
vængskjöldur                                                               2                 10                  0              30
vænisýki                                                                   0                 10                  0               0
vængberar                                                                  0                 10                  0               0
vænghaf                                                                    9                 10                  0             139
vögguprent                                                                 1                 10                  0              16
vöggur                                                                     0                 10                  0               0
vöggudauði                                                                 0                 10                  0               0
vökulögin                                                                  0                 10                  0               0
vökvi                                                                     22                 10                  0             372
vötnin miklu                                                               0                 10                  0               0
vöðuselur                                                                  0                 10                  0               0
vöðlavík                                                                   0                 10                  0               0
vöðvi                                                                      5                 10                  0              87
vörður                                                                    38                 10                  0             608
vörtubirki                                                                 0                 10                  0               0
vörtusvín                                                                  2                 10                  0              32
vörðuskóli                                                                 0                 10                  0               0
vörtubaugur                                                                1                 10                  0              15
vörumerki                                                                 20                 10                  0             311
vörubíll                                                                   1                 10                  0              16
vörpun                                                                    28                 10                  0             494
völudepla                                                                  0                 10                  0               0
völundur                                                                   0                 10                  0               0
völuspá                                                                    0                 10                  0               0
vönun                                                                      0                 10                  0               0
viva la bam                                                                0                 10                  0               0
viasat history                                                             0                 10                  0               0
vigtýr                                                                     0                 10                  0               0
vignir                                                                     0                 10                  0               0
vigur                                                                     38                 10                  0             591
vigdís grímsdóttir                                                         0                 10                  0               0
vigri                                                                      4                 10                  0              63
viggó                                                                      0                 10                  0               0
vigdís finnbogadóttir                                                      0                 10                  0               0
viggó viðutan                                                              0                 10                  0               0
vigfús                                                                     1                 10                  0              15
vigdís gunnarsdóttir                                                       0                 10                  0               0
vignir svavarsson                                                          0                 10                  0               0
vigur (mannsnafn)                                                          0                 10                  0               0
vigur (eyja)                                                               0                 10                  0               0
vigdís                                                                     0                 10                  0               0
vigur (stærðfræði)                                                         0                 10                  0               0
vigurrúm                                                                   8                 10                  0             136
vigdís hrefna pálsdóttir                                                   0                 10                  0               0
viktor dyk                                                                 0                 10                  0               0
vikivaki (aðgreining)                                                      0                 10                  0               0
viktoría bretadrottning                                                    0                 10                  0               0
viktor                                                                     1                 10                  0              18
viktor emmanúel 2.                                                         0                 10                  0               0
vika bókarinnar                                                            0                 10                  0               0
vikur                                                                     20                 10                  0             322
vikivaki                                                                   2                 10                  0              35
viktoríuvatn                                                               0                 10                  0               0
vikar                                                                      5                 10                  0              76
vikulokin                                                                  0                 10                  0               0
viktoría                                                                   0                 10                  0               0
viktoríufossar                                                             0                 10                  0               0
viktor arnar ingólfsson                                                    0                 10                  0               0
viktoría spans - íslenzk lög gömul og ný                                   0                 10                  0               0
vika                                                                      42                 10                  0             739
vitré                                                                      0                 10                  0               0
vitus bering                                                               0                 10                  0               0
vitrúvíski maðurinn                                                        0                 10                  0               0
vitinn í faros við alexandríu                                              0                 10                  0               0
vitsmunavísindi                                                            0                 10                  0               0
vitis vinifera                                                             1                 10                  0              15
viti                                                                      36                 10                  0             588
vitrúvíus                                                                  0                 10                  0               0
viðskeyti                                                                 10                 10                  0             149
viðurlag                                                                   1                 10                  0              16
viðskiptaráð íslands                                                       0                 10                  0               0
viðbót maxwells                                                            0                 10                  0               0
viðtalsbil                                                                 0                 10                  0               0
viðskipti                                                                 22                 10                  0             337
viðtengingarháttur                                                         3                 10                  0              49
viðar eggertsson                                                           0                 10                  0               0
viðskiptafræði                                                            12                 10                  0             213
viðreisnarstjórnin                                                         0                 10                  0               0
viðbót                                                                    24                 10                  0             597
viðeyjarstofa                                                              0                 10                  0               0
viðeyjarbiblía                                                             0                 10                  0               0
viðfjörður                                                                 0                 10                  0               0
viðeyjarsund                                                               0                 10                  0               0
viðeyjarprent                                                              0                 10                  0               0
viður                                                                    195                 10                  0            2962
viðoy                                                                      0                 10                  0               0
viðskiptabann bandaríkjanna gegn kúbu                                      0                 10                  0               0
viðeyjarkirkja                                                             0                 10                  0               0
viðar                                                                     47                 10                  0             753
viðja                                                                      0                 10                  0               0
viðarkol                                                                   3                 10                  0              49
viðskiptavild                                                              0                 10                  0               0
viðfjörð                                                                   0                 10                  0               0
viðmótshönnun                                                              1                 10                  0              17
viðeyjarstjórnin                                                           0                 10                  0               0
viðskiptaáætlun                                                            1                 10                  0              16
viðlíking                                                                  2                 10                  0              36
viðurnefni                                                                27                 10                  0             493
viðey                                                                      0                 10                  0               0
viðvíkurhreppur                                                            0                 10                  0               0
virgill (mannsnafn)                                                        0                 10                  0               0
virginía (fylki)                                                           0                 10                  0               0
virki (stærðfræði)                                                         0                 10                  0               0
virðisaukaskattur                                                          0                 10                  0               0
virginíuháskóli                                                            0                 10                  0               0
virkisbrekka                                                               0                 10                  0               0
virk skilyrðing                                                            0                 10                  0               0
virtual console (wii)                                                      0                 10                  0               0
virginía (mannsnafn)                                                       0                 10                  0               0
virginia woolf                                                             0                 10                  0               0
virginíu-hagfræðingarnir                                                   0                 10                  0               0
virgill                                                                    0                 10                  0               0
virginía                                                                   0                 10                  0               0
vilhjálmur stefánsson                                                      0                 10                  0               0
vilhjálmur bretaprins                                                      0                 10                  0               0
viltaugakerfið                                                             3                 10                  0              46
vilfríður                                                                  0                 10                  0               0
villa (mannsnafn)                                                          0                 10                  0               0
vilníus                                                                    0                 10                  0               0
vilhjálmur 4. bretakonungur                                                0                 10                  0               0
vilbogi                                                                    0                 10                  0               0
villa park                                                                 0                 10                  0               0
vilhjálmur vilhjálmsson - glugginn hennar kötu                             0                 10                  0               0
villi                                                                     21                 10                  0             339
vilma                                                                      0                 10                  0               0
vilhjálmur og elly vilhjálms syngja jólalög                                0                 10                  0               0
vilbrandur                                                                 0                 10                  0               0
vilhjálmur og ellý vilhjálms - lög sigfúsar halldórssonar                  0                 10                  0               0
villiljós                                                                  0                 10                  0               0
vilhjálmur                                                                 0                 10                  0               0
vilmundur gylfason                                                         0                 10                  0               0
vilhjálmur 2. þýskalandskeisari                                            0                 10                  0               0
vilmundur                                                                  0                 10                  0               0
vilhjálmur vilhjálmsson - hún hring minn ber                               0                 10                  0               0
villanueva de azoague                                                      0                 10                  0               0
vilgeir                                                                    0                 10                  0               0
villingaholtshreppur                                                       0                 10                  0               0
vilmar                                                                     0                 10                  0               0
vilhjálmur þ. vilhjálmsson                                                 0                 10                  0               0
vilborg                                                                    0                 10                  0               0
vilberg                                                                    0                 10                  0               0
vilný                                                                      0                 10                  0               0
viljar                                                                     0                 10                  0               0
vilhjálmur tell                                                            0                 10                  0               0
vilhelm                                                                    0                 10                  0               0
villiköttur                                                                1                 10                  0              15
vildís                                                                     0                 10                  0               0
vilbergur                                                                  0                 10                  0               0
vilji (norræn goðafræði)                                                   0                 10                  0               0
vilhjálmur einarsson                                                       0                 10                  0               0
vilborg halldórsdóttir                                                     0                 10                  0               0
villach                                                                    0                 10                  0               0
villutrú                                                                   6                 10                  0             106
vilhjálmur árnason                                                         0                 10                  0               0
vila nova de gaia                                                          0                 10                  0               0
villeneuve-d'ascq                                                          0                 10                  0               0
vilhjálmur vilhjálmsson - allt er breytt                                   0                 10                  0               0
vilbert                                                                    0                 10                  0               0
vilhjálmur vilhjálmsson - myndin af þér - einni þér ég ann                 0                 10                  0               0
vilpa                                                                      0                 10                  0               0
vilji                                                                     15                 10                  0             315
vilhjálmur vilhjálmsson - fjórtán fyrstu lögin                             0                 10                  0               0
vilhjálmur þögli                                                           0                 10                  0               0
vilbjörn                                                                   0                 10                  0               0
vilhjálmur og elly vilhjálms - lög tólfta september                        0                 10                  0               0
vilhelm marstrand                                                          0                 10                  0               0
vilhjálmur alexander hollandsprins                                         0                 10                  0               0
vilhelmína                                                                 0                 10                  0               0
vilgerður                                                                  0                 10                  0               0
vindrós                                                                    2                 10                  0              31
vindhani                                                                   0                 10                  0               0
vinir einkabílsins                                                         0                 10                  0               0
vingjarnlegar tölur                                                        1                 10                  0              15
vinaleið                                                                   0                 10                  0               0
vinný                                                                      0                 10                  0               0
vinsælasti sjónvarpsmaður ársins                                           0                 10                  0               0
vinarþel ókunnugra                                                         0                 10                  0               0
vinna                                                                    188                 10                  0            2967
vinir                                                                     12                 10                  0             189
vinglar                                                                    0                 10                  0               0
vinnsluminni                                                               4                 10                  0              63
vinstrihreyfingin – grænt framboð                                          0                 10                  0               0
vincent van gogh                                                           0                 10                  0               0
vindáshlíð                                                                 0                 10                  0               0
vindur                                                                    15                 10                  0             225
vindauga                                                                   1                 10                  0              15
vindhraði                                                                  4                 10                  0              67
vinstristefna                                                              0                 10                  0               0
vinstri                                                                   50                 10                  0             768
vindar og breytingar                                                       0                 10                  0               0
vinbjörg                                                                   0                 10                  0               0
vindmylla                                                                  2                 10                  0              31
vinnusálfræði                                                              1                 10                  0              18
vinabæir                                                                   3                 10                  0              57
vindhælishreppur                                                           0                 10                  0               0
vinnuveitendaábyrgð                                                        1                 10                  0              15
vindátt                                                                    8                 10                  0             122
vindorka                                                                   0                 10                  0               0
vientiane                                                                  0                 10                  0               0
viborg                                                                     0                 10                  0               0
victoria                                                                   0                 10                  0               0
victor cilia                                                               0                 10                  0               0
victor                                                                     0                 10                  0               0
victor hugo                                                                0                 10                  0               0
victoría                                                                   0                 10                  0               0
victor moses                                                               0                 10                  0               0
victor williams                                                            0                 10                  0               0
vistfræði                                                                  7                 10                  0             138
visa-bikar karla 2008                                                      0                 10                  0               0
visa-bikar karla                                                           0                 10                  0               0
vistfang                                                                   3                 10                  0              53
vistmenning                                                                0                 10                  0               0
visa-bikar karla 2007                                                      0                 10                  0               0
vistuð stefja                                                              0                 10                  0               0
vistkerfi                                                                 10                 10                  0             152
visual basic .net                                                          0                 10                  0               0
visla                                                                      0                 10                  0               0
viseu                                                                      0                 10                  0               0
visa-bikarinn                                                              0                 10                  0               0
visnjú                                                                     0                 10                  0               0
vogar                                                                     10                 10                  0             177
vogarstöng                                                                 2                 10                  0              37
vogvængjur                                                                 1                 10                  0              16
voice                                                                      1                 10                  0              15
vopnadómur                                                                 0                 10                  0               0
vopnuð átök                                                                9                 10                  0             138
vopnafjörður                                                               0                 10                  0               0
vopnafjarðarhreppur                                                        0                 10                  0               0
vopn                                                                     121                 10                  0            1845
vopni                                                                     10                 10                  0             167
vottar jehóva                                                              0                 10                  0               0
votheysveiki                                                               0                 10                  0               0
vordís                                                                     0                 10                  0               0
vorm                                                                       5                 10                  0              79
vorið í prag                                                               0                 10                  0               0
vorperla                                                                   1                 10                  0              15
vorpunktur                                                                 3                 10                  0              45
vorarlberg                                                                 0                 10                  0               0
vorlaukur                                                                  0                 10                  0               0
vor                                                                     2207                 10                  0           35213
volvo                                                                      0                 10                  0               0
voltaire                                                                   0                 10                  0               0
voldemort                                                                  0                 10                  0               0
voltakross                                                                 0                 10                  0               0
volt                                                                      11                 10                  0             167
volga                                                                      2                 10                  0              34
volta                                                                      2                 10                  0              35
volfram                                                                    4                 10                  0              84
voynich-handritið                                                          0                 10                  0               0
von (mannsnafn)                                                            0                 10                  0               0
von                                                                      236                 10                  0            4292
vonlenska                                                                  0                 10                  0               0
von neumann arkitektúr                                                     0                 10                  0               0
vodafonevöllur                                                             0                 10                  0               0
vodka                                                                      0                 10                  0               0
vodskov                                                                    0                 10                  0               0
vodafone                                                                   0                 10                  0               0
vømmøl spellmannslag                                                       0                 10                  0               0
végerður                                                                   0                 10                  0               0
végeir                                                                     0                 10                  0               0
végeirsstaðir                                                              0                 10                  0               0
vékell                                                                     0                 10                  0               0
vér mótmælum allir                                                         0                 10                  0               0
vélbátur                                                                   2                 10                  0              31
vélhyggja                                                                  0                 10                  0               0
vélhjólaíþróttaklúbburinn                                                  0                 10                  0               0
vélbúnaður                                                                 2                 10                  0              31
vélaug                                                                     0                 10                  0               0
vélamál                                                                    7                 10                  0             108
vélaugur                                                                   0                 10                  0               0
vélinda                                                                    3                 10                  0              47
vélbyssa                                                                   3                 10                  0              54
vél                                                                      246                 10                  0            3689
véltækni hf.                                                               0                 10                  0               0
véný                                                                       0                 10                  0               0
vébjörn                                                                    0                 10                  0               0
vébjörg                                                                    0                 10                  0               0
vémundur                                                                   0                 10                  0               0
vé                                                                       353                 10                  0            5326
védís                                                                      0                 10                  0               0
vésteinn                                                                   0                 10                  0               0
vladivostok                                                                0                 10                  0               0
vladímír lenín                                                             0                 10                  0               0
vlad drakúla                                                               0                 10                  0               0
vladímír pútín                                                             0                 10                  0               0
vladimir nabokov                                                           0                 10                  0               0
vyre                                                                       0                 10                  0               0
vegamannahellir                                                            0                 10                  0               0
vegir liggja til allra átta                                                0                 10                  0               0
vegemite                                                                   0                 10                  0               0
vegur                                                                    168                 10                  0            2596
veggfóður (kvikmynd)                                                       0                 10                  0               0
veggfóður                                                                  1                 10                  0              41
vegamót (hús)                                                              0                 10                  0               0
vegamót                                                                    3                 10                  0              48
vegabréfsáritun                                                            2                 10                  0              31
vegalengd                                                                 22                 10                  0             344
veiðileysufjörður (ströndum)                                               0                 10                  0               0
veik beyging                                                               0                 10                  0               0
veigrunarorð                                                               1                 10                  0              15
veira                                                                      6                 10                  0              90
veiðivötn                                                                  0                 10                  0               0
veirufræði                                                                 1                 10                  0              17
veiðileysufjörður                                                          0                 10                  0               0
veigar                                                                    11                 10                  0             176
veiðar                                                                    32                 10                  0             487
veiðiferðin                                                                0                 10                  0               0
veiki kjarnakraftur                                                        1                 10                  0              18
veigur                                                                     1                 10                  0              16
veiðimenn og safnarar                                                      0                 10                  0               0
veiga                                                                     18                 10                  0             275
veisla                                                                     7                 10                  0             100
veitingahús                                                                8                 10                  0             135
veitur                                                                     1                 10                  0              16
vefur                                                                     49                 10                  0             731
vefsíða                                                                   13                 10                  0             198
vefverslun                                                                 1                 10                  0              17
vefrallý                                                                   1                 10                  0              20
vefrit                                                                     8                 10                  0             132
vefritið                                                                   1                 10                  0              15
veffang                                                                    0                 10                  0               0
vefleiðangur                                                               1                 10                  0              15
vetrarundur í múmíndal                                                     0                 10                  0               0
vetrarbrautarhnit                                                          0                 10                  0               0
vetrarólympíuleikarnir 1980                                                0                 10                  0               0
vetrarólympíuleikarnir 1968                                                0                 10                  0               0
vetur                                                                     92                 10                  0            1496
vetrarólympíuleikarnir 1936                                                0                 10                  0               0
vetrarbrautin                                                              1                 10                  0              14
veturliði                                                                  0                 10                  0               0
vetrarólympíuleikarnir 2002                                                0                 10                  0               0
vetni                                                                     52                 10                  0             809
vetrarborgin                                                               0                 10                  0               0
vetrarólympíuleikarnir 2006                                                0                 10                  0               0
vetrarólympíuleikarnir 1952                                                0                 10                  0               0
vetnissýaníð                                                               1                 10                  0              15
vetrarólympíuleikarnir 1984                                                0                 10                  0               0
vetrarstríðið                                                              0                 10                  0               0
veðurathugunarstöð                                                        32                 10                  0             541
veðurstofa íslands                                                         0                 10                  0               0
veðurathugunarmaður                                                        1                 10                  0              23
veðkall                                                                    0                 10                  0               0
veðramót                                                                   0                 10                  0               0
veðurathugun                                                              34                 10                  0             630
veður                                                                    127                 10                  0            2269
veðurathugunartími                                                         0                 10                  0               0
veðurfarsfræði                                                             3                 10                  0              54
veðurkóngur                                                                0                 10                  0               0
veðurfarssagan með kjarnaborunum í grænlandsjökli                          0                 10                  0               0
veðurspá                                                                   3                 10                  0              44
veðrun                                                                     7                 10                  0             119
veðurfræði                                                                25                 10                  0             443
verðlaun                                                                 336                 10                  0            5440
vernon g. little                                                           0                 10                  0               0
verslunarmannahelgi                                                        0                 10                  0               0
verkfæri                                                                  18                 10                  0             275
verðbréf                                                                  11                 10                  0             173
ver                                                                     6923                 10                  0          118727
verðbólga                                                                  3                 10                  0              51
verkfall                                                                   7                 10                  0             112
veraldarvefurinn                                                           2                 10                  0              30
verkmenntaskólinn á akureyri                                               0                 10                  0               0
verslunarleið                                                              6                 10                  0              91
vera                                                                    1056                 10                  0           16390
vertíð                                                                     4                 10                  0              63
verdun-samningurinn                                                        0                 10                  0               0
versalasamningurinn                                                        0                 10                  0               0
vera (tímarit)                                                             0                 10                  0               0
verkstæði jólasveinanna                                                    0                 10                  0               0
vermundur                                                                  0                 10                  0               0
verksmiðja                                                                20                 10                  0             298
verzlunarskóli íslands                                                     0                 10                  0               0
veróníka                                                                   0                 10                  0               0
vercingetorix                                                              0                 10                  0               0
verslanasambandið                                                          0                 10                  0               0
verkamannaflokkurinn                                                       1                 10                  0              15
versalir                                                                   0                 10                  0               0
vera (mannsnafn)                                                           0                 10                  0               0
veronika                                                                   0                 10                  0               0
ver (mannsnafn)                                                            0                 10                  0               0
verkstæði jólasveinanna - barnaleikrit eftir thorbjörn egner               0                 10                  0               0
verkfall grunnskólakennara 2004                                            0                 10                  0               0
vertigo                                                                    0                 10                  0               0
verund                                                                     3                 10                  0              46
verufræði                                                                 10                 10                  0             165
verslunarbankinn                                                           0                 10                  0               0
verk og dagar                                                              0                 10                  0               0
veröld andrésar andar                                                      0                 10                  0               0
verkfræði                                                                 70                 10                  0            1227
vernharð                                                                   0                 10                  0               0
vernharður                                                                 0                 10                  0               0
verðtrygging                                                               0                 10                  0               0
vermont                                                                    0                 10                  0               0
verónika                                                                   0                 10                  0               0
verkakvennafélagið framsókn                                                0                 10                  0               0
verkamannabústaðir                                                         2                 10                  0              55
vermut                                                                     0                 10                  0               0
vertollur                                                                  1                 10                  0              24
vejle                                                                      0                 10                  0               0
velskur corgi                                                              0                 10                  0               0
veldi (stærðfræði)                                                         0                 10                  0               0
velletri                                                                   0                 10                  0               0
vellir                                                                    16                 10                  0             254
vellankatla                                                                0                 10                  0               0
veldismengi                                                                2                 10                  0              32
veldisfall                                                                 7                 10                  0             110
veldaröð                                                                   5                 10                  0              74
velvet revolver                                                            0                 10                  0               0
velska                                                                     5                 10                  0              78
venus (mannsnafn)                                                          0                 10                  0               0
venus (reikistjarna)                                                       0                 10                  0               0
vendée                                                                     0                 10                  0               0
venesúela                                                                  0                 10                  0               0
venetian snares                                                            0                 10                  0               0
venetó                                                                     0                 10                  0               0
veni, vidi, vici                                                           0                 10                  0               0
venus                                                                      0                 10                  0               0
venus (gyðja)                                                              0                 10                  0               0
venslagagnagrunnur                                                         0                 10                  0               0
vendilskagi                                                                0                 10                  0               0
vennmynd                                                                   0                 10                  0               0
veber (si-mælieining)                                                      0                 10                  0               0
vedaritin                                                                  0                 10                  0               0
vedanta                                                                    0                 10                  0               0
vesturlandskjördæmi                                                        1                 10                  0              16
vesturnorræn mál                                                           1                 10                  0              18
vestfold                                                                   0                 10                  0               0
vestri                                                                   245                 10                  0            3799
vestmannsvatn                                                              0                 10                  0               0
vestur-kasakstanfylki                                                      0                 10                  0               0
vestur-landeyjahreppur                                                     0                 10                  0               0
vestur-ástralía                                                            0                 10                  0               0
vestnorræna ráðið                                                          0                 10                  0               0
vestfirskur einhljóðaframburður                                            0                 10                  0               0
vestrahorn                                                                 0                 10                  0               0
vestfjarðaprófastsdæmi                                                     0                 10                  0               0
vestur-ísafjarðarsýsla                                                     0                 10                  0               0
vestur-sussex                                                              0                 10                  0               0
vestbjerg                                                                  0                 10                  0               0
vestmar                                                                    0                 10                  0               0
vesturbær                                                                  0                 10                  0               0
vestur-afríka                                                              0                 10                  0               0
vestar                                                                    25                 10                  0             487
vestmanna                                                                  0                 10                  0               0
vesturhópshólakirkja                                                       0                 10                  0               0
vestur-sahara                                                              0                 10                  0               0
vesturkirkjan                                                              0                 10                  0               0
vestur-eyjafjallahreppur                                                   0                 10                  0               0
vestmannaeyjar                                                             0                 10                  0               0
vestrómverska keisaradæmið                                                 0                 10                  0               0
vestur-húnavatnssýsla                                                      0                 10                  0               0
vesturland                                                                19                 10                  0             313
vestfirðir                                                                 1                 10                  0              16
vestur-miðhéruð                                                            0                 10                  0               0
vestari-krókar                                                             0                 10                  0               0
vestur-skaftafellssýsla                                                    0                 10                  0               0
vestur                                                                   591                 10                  0           11764
vesturbyggð                                                                0                 10                  0               0
vespasíanus                                                                0                 10                  0               0
vestur-evrópa                                                              0                 10                  0               0
vestur-þýskaland                                                           0                 10                  0               0
vestur-virginía                                                            0                 10                  0               0
vestur-nýja-gínea                                                          0                 10                  0               0
vesturfarar                                                                0                 10                  0               0
vestur-yorkshire                                                           0                 10                  0               0
vesturgata                                                                 0                 10                  0               0
vesturbakkinn                                                              0                 10                  0               0
vestribyggð                                                                0                 10                  0               0
vesturbæjarskóli                                                           0                 10                  0               0
vestur-agðir                                                               0                 10                  0               0
vestfjarðakjördæmi                                                         0                 10                  0               0
vestur-kongó                                                               0                 10                  0               0
vestræn heimspeki                                                          0                 10                  0               0
vesturamt                                                                  2                 10                  0              32
vbscript                                                                   0                 10                  0               0
vágar                                                                      0                 10                  0               0
vágur                                                                      3                 10                  0              53
vápni                                                                      0                 10                  0               0
vátrygging                                                                 3                 10                  0              45
váli                                                                       0                 10                  0               0
vulcanus                                                                   0                 10                  0               0
vma                                                                        0                 10                  0               0
v-2 flugskeyti                                                             0                 10                  0               0
víghóll                                                                    0                 10                  0               0
víggunnur                                                                  0                 10                  0               0
víglundur                                                                  0                 10                  0               0
vígdögg                                                                    0                 10                  0               0
vígsteinn                                                                  0                 10                  0               0
vígmundur                                                                  0                 10                  0               0
vígslubiskup                                                               7                 10                  0             107
vígþór                                                                     0                 10                  0               0
vígslustig klerka                                                          0                 10                  0               0
vígvöllur                                                                  1                 10                  0              15
vígmar                                                                     0                 10                  0               0
víkurkirkja (reykjavík)                                                    0                 10                  0               0
vík í mýrdal                                                               0                 10                  0               0
víkingaskip                                                                3                 10                  0              45
vík                                                                     1317                 10                  0           22183
víkingur                                                                   4                 10                  0              61
víkingar                                                                   8                 10                  0             114
víkingur (mannsnafn)                                                       0                 10                  0               0
víkin                                                                     74                 10                  0            1185
víkin (noregi)                                                             0                 10                  0               0
víkin (reykjavík)                                                          0                 10                  0               0
víkurkirkja                                                                5                 10                  0              79
víkursveit                                                                 1                 10                  0              15
víkur                                                                    452                 10                  0            7739
vífill (þræll)                                                             0                 10                  0               0
vífill                                                                     0                 10                  0               0
vífilsstaðir                                                               0                 10                  0               0
vífilsgata                                                                 0                 10                  0               0
vífill (mannsnafn)                                                         0                 10                  0               0
víf                                                                       14                 10                  0             220
vítamín                                                                   15                 10                  0             287
vítisenglar                                                                0                 10                  0               0
vítaspyrnukeppni (knattspyrna)                                             0                 10                  0               0
víðidalstungukirkja                                                        0                 10                  0               0
víðir (mannsnafn)                                                          0                 10                  0               0
víðar (mannsnafn)                                                          0                 10                  0               0
víðavangshlaup ír                                                          0                 10                  0               0
víðar                                                                     43                 10                  0             686
víðistaðaskóli                                                             0                 10                  0               0
víðnet                                                                     1                 10                  0              21
víðgelmir                                                                  0                 10                  0               0
víðar (norræn goðafræði)                                                   0                 10                  0               0
víðisætt                                                                   4                 10                  0              63
víðidalsá                                                                  0                 10                  0               0
víðir                                                                      5                 10                  0              80
vín (austurríki)                                                           0                 10                  0               0
vínarhringurinn                                                            0                 10                  0               0
vínber                                                                     3                 10                  0              51
vínarterta                                                                 1                 10                  0              16
vínlandskortið                                                             0                 10                  0               0
vínland                                                                    0                 10                  0               0
vín                                                                      149                 10                  0            2324
víetnam                                                                    9                 10                  0             158
víetnamstríðið                                                             0                 10                  0               0
víetnamska                                                                 6                 10                  0             118
víbekka                                                                    0                 10                  0               0
vímara peres                                                               0                 10                  0               0
vímuefni                                                                   1                 10                  0              15
víóletta                                                                   0                 10                  0               0
víóla                                                                      0                 10                  0               0
vídalín                                                                    0                 10                  0               0
vídalínspostilla                                                           0                 10                  0               0
vídalínsætt                                                                0                 10                  0               0
víxlverkun                                                                14                 10                  0             220
víxlregla                                                                  1                 10                  0              16
vísindagrein                                                              27                 10                  0             482
vísir (stærðfræði)                                                         0                 10                  0               0
vísitala um þróun lífsgæða                                                 0                 10                  0               0
vísindaheimspeki                                                          16                 10                  0             261
vísir (dagblað)                                                            0                 10                  0               0
vísir (aðgreiningarsíða)                                                   0                 10                  0               0
vísindaleg aðferð                                                          1                 10                  0              15
vísindi                                                                   51                 10                  0             798
vísitala                                                                  12                 10                  0             195
vísindavefurinn                                                            0                 10                  0               0
vísa                                                                     176                 10                  0            2984
vísindabyltingin                                                           0                 10                  0               0
vísitala neysluverðs                                                       2                 10                  0              32
vísitala atvinnufrelsis                                                    0                 10                  0               0
vísindaleg flokkun                                                         1                 10                  0              15
vúdú                                                                       0                 10                  0               0
v for vendetta                                                             0                 10                  0               0
v for vendetta (kvikmynd)                                                  0                 10                  0               0
v                                                                      17953                 10                  0          276243
avarska                                                                    1                 10                  0              15
avicenna                                                                   0                 10                  0               0
avogadrosartala                                                            0                 10                  0               0
avril lavigne                                                              0                 10                  0               0
aveiro (borg)                                                              0                 10                  0               0
averróes                                                                   0                 10                  0               0
aveiro                                                                     0                 10                  0               0
aagot                                                                      0                 10                  0               0
aage                                                                       4                 10                  0              64
aappilattoq                                                                0                 10                  0               0
aarbøger for nordisk oldkyndighed og historie                              0                 10                  0               0
aargau                                                                     0                 10                  0               0
aabenraa                                                                   0                 10                  0               0
aa-samtökin                                                                0                 10                  0               0
aa                                                                       280                 10                  0            4615
aachen                                                                     0                 10                  0               0
aasiaat                                                                    0                 10                  0               0
agat                                                                      44                 10                  0             728
agamemnon (æskýlos)                                                        0                 10                  0               0
against me!                                                                0                 10                  0               0
agata                                                                     29                 10                  0             469
agamemnon                                                                  0                 10                  0               0
agatha                                                                     0                 10                  0               0
aggersborg                                                                 0                 10                  0               0
agile                                                                      0                 10                  0               0
agða                                                                      72                 10                  0            1183
agrippa (heimspekingur)                                                    0                 10                  0               0
agla                                                                      12                 10                  0             199
agyness deyn                                                               0                 10                  0               0
agnes (nafn)                                                               0                 10                  0               0
agneta                                                                     0                 10                  0               0
agnar kofoed-hansen                                                        0                 10                  0               0
agnieszka włodarczyk                                                       0                 10                  0               0
agnea                                                                      4                 10                  0              60
agni                                                                     163                 10                  0            2801
agnar már magnússon                                                        0                 10                  0               0
agnes (kvikmynd)                                                           0                 10                  0               0
agnar jón egilsson                                                         0                 10                  0               0
agnageislun                                                                3                 10                  0              45
agnar                                                                    193                 10                  0            2979
agnes                                                                     10                 10                  0             173
agent fresco                                                               0                 10                  0               0
a4                                                                         0                 10                  0               0
aš                                                                         4                 10                  0              74
akademían                                                                  4                 10                  0              73
akanmál                                                                    1                 10                  0              18
akabaflói                                                                  0                 10                  0               0
akavajo                                                                    1                 10                  0              18
akademískt frelsi                                                          0                 10                  0               0
akkra                                                                      0                 10                  0               0
akkeron                                                                    0                 10                  0               0
akkadíska                                                                  3                 10                  0              54
akkilles                                                                   0                 10                  0               0
akkilles tatíos                                                            0                 10                  0               0
akihito                                                                    0                 10                  0               0
akonkagúa                                                                  0                 10                  0               0
aktöbefylki                                                                0                 10                  0               0
aktiníð                                                                    4                 10                  0              61
akrahreppur                                                                0                 10                  0               0
akraneshreppur                                                             0                 10                  0               0
akranes                                                                    0                 10                  0               0
akrafjall                                                                  0                 10                  0               0
aklanska                                                                   1                 10                  0              16
akershus                                                                   0                 10                  0               0
akbar mikli                                                                0                 10                  0               0
akureyrarflugvöllur                                                        0                 10                  0               0
akurblessun                                                                0                 10                  0               0
akureyri                                                                   0                 10                  0               0
akurhæna                                                                   1                 10                  0              15
akurey (landeyjum)                                                         0                 10                  0               0
akureyrarveikin                                                            0                 10                  0               0
akurey (kollafirði)                                                        0                 10                  0               0
akureyrarkirkja                                                            0                 10                  0               0
akurey                                                                     0                 10                  0               0
akmeð 1.                                                                   0                 10                  0               0
ak-47                                                                      0                 10                  0               0
akíra kúrósava                                                             0                 10                  0               0
akstursíþróttir                                                            0                 10                  0               0
azumanga daioh                                                             0                 10                  0               0
aikido                                                                     1                 10                  0              84
airbus a380                                                                0                 10                  0               0
airport                                                                    0                 10                  0               0
aino freyja järvelä                                                        0                 10                  0               0
apavatn                                                                    0                 10                  0               0
apalhraun                                                                  3                 10                  0              58
apar                                                                      94                 10                  0            1483
apalaí                                                                     1                 10                  0              15
apaplánetan (1968 kvikmynd)                                                0                 10                  0               0
apa                                                                      552                 10                  0            8620
appleworks                                                                 0                 10                  0               0
apple ii                                                                   0                 10                  0               0
appennínaskagi                                                             0                 10                  0               0
appelsínusafi                                                              0                 10                  0               0
apple cinema display                                                       0                 10                  0               0
appennínafjöll                                                             0                 10                  0               0
apple mighty mouse                                                         0                 10                  0               0
apple inc.                                                                 0                 10                  0               0
apple i                                                                    0                 10                  0               0
apple store                                                                0                 10                  0               0
apple tv                                                                   0                 10                  0               0
appalachiafjöll                                                            0                 10                  0               0
apple (aðgreining)                                                         0                 10                  0               0
appelsína                                                                  3                 10                  0              67
apocalypse now                                                             0                 10                  0               0
apollóníos frá aþenu                                                       0                 10                  0               0
apollonia schwartzkopf                                                     0                 10                  0               0
apolloníos frá perga                                                       0                 10                  0               0
apolloníos dyskolos                                                        0                 10                  0               0
apollonia (illyríu)                                                        0                 10                  0               0
aprílgabb                                                                  1                 10                  0              20
apríl                                                                    507                 10                  0            8539
aphex twin                                                                 0                 10                  0               0
aperture                                                                   0                 10                  0               0
apuleius                                                                   0                 10                  0               0
apúlía                                                                     0                 10                  0               0
apókrýf rit                                                                0                 10                  0               0
afganistan                                                                 0                 10                  0               0
aftaka                                                                     6                 10                  0              99
afturbrennari                                                              0                 10                  0               0
afturbolur                                                                 0                 10                  0               0
afturvirk hömlun                                                           1                 10                  0              15
afturbeygt fornafn                                                         1                 10                  0              33
afródíta                                                                   0                 10                  0               0
afró-evrasía                                                               0                 10                  0               0
afréttur                                                                   2                 10                  0              30
afríska þjóðarráðið                                                        0                 10                  0               0
afríka sunnan sahara                                                       0                 10                  0               0
africa united                                                              0                 10                  0               0
afríkusambandið                                                            0                 10                  0               0
afríkanska                                                                 3                 10                  0              55
afrískur svartviður                                                        0                 10                  0               0
afríka                                                                     3                 10                  0              61
afríka (skattland)                                                         0                 10                  0               0
afhöfðun                                                                   1                 10                  0              18
afhending                                                                 18                 10                  0             289
aflagssögn                                                                 0                 10                  0               0
afleiðing                                                                 41                 10                  0             685
afleiðsla                                                                  1                 10                  0              16
afleiða (fjármál)                                                          0                 10                  0               0
afl                                                                     1067                 10                  0           18657
afleiðingarlögmálið                                                        1                 10                  0              15
afleiða (stærðfræði)                                                       0                 10                  0               0
afleiða                                                                   19                 10                  0             321
afbygging                                                                  0                 10                  0               0
afbrigði latneska stafrófsins                                              0                 10                  0               0
afc suður                                                                  0                 10                  0               0
afc vestur                                                                 0                 10                  0               0
afc norður                                                                 0                 10                  0               0
afc austur                                                                 0                 10                  0               0
afþreying                                                                 15                 10                  0             242
afskautun                                                                  0                 10                  0               0
afstæðiskenningin                                                          4                 10                  0              72
afs                                                                      790                 10                  0           12269
afsjálfgun                                                                 0                 10                  0               0
afstapahraun                                                               0                 10                  0               0
afstæðishyggja                                                             1                 10                  0              17
afstæðiskenning                                                           11                 10                  0             196
atvinnuvegir á íslandi                                                     0                 10                  0               0
atvinnubótavinna                                                           0                 10                  0               0
atviksorð                                                                  9                 10                  0             141
atviksliður                                                                0                 10                  0               0
atvinna                                                                    3                 10                  0              50
atvinnumálaráðherrar á íslandi                                             0                 10                  0               0
atabaskamál                                                                1                 10                  0              15
atacama                                                                    0                 10                  0               0
atar                                                                     307                 10                  0            5183
atkvæðatáknróf                                                             2                 10                  0              36
atýráfylki                                                                 0                 10                  0               0
atferlisgreining                                                           2                 10                  0              30
atferlishyggja                                                             1                 10                  0              18
atferlismeðferð                                                            1                 10                  0              15
atom heart mother                                                          0                 10                  0               0
atorka group                                                               0                 10                  0               0
attention (gusgus plata)                                                   0                 10                  0               0
attísku ræðumennirnir                                                      0                 10                  0               0
atti katti nóa                                                             0                 10                  0               0
atreifur                                                                   0                 10                  0               0
athafnafræði                                                               6                 10                  0              96
athafnaheimspeki                                                           1                 10                  0              19
athena                                                                     0                 10                  0               0
athyglisbrestur                                                            1                 10                  0              80
athygli                                                                   81                 10                  0            1379
atlanta                                                                    0                 10                  0               0
atlasfjöll                                                                 0                 10                  0               0
atli (mannsnafn)                                                           0                 10                  0               0
atlantshafsbandalagið                                                      0                 10                  0               0
atlas (mannsnafn)                                                          0                 10                  0               0
atlantshafshryggurinn                                                      0                 10                  0               0
atlas                                                                      1                 10                  0              17
atlavík                                                                    0                 10                  0               0
atli húnakonungur                                                          0                 10                  0               0
atli valason                                                               0                 10                  0               0
atli (ritverk)                                                             0                 10                  0               0
atlantis                                                                   0                 10                  0               0
atla                                                                      40                 10                  0             614
atli gíslason                                                              0                 10                  0               0
atlantsskip                                                                0                 10                  0               0
atli harðarson                                                             0                 10                  0               0
atli                                                                       4                 10                  0              64
atlantshaf                                                                 2                 10                  0              41
atli rafn sigurðarson                                                      0                 10                  0               0
atlantshafsþorskur                                                         0                 10                  0               0
ate                                                                      439                 10                  0            7413
atena                                                                      2                 10                  0              35
atburðaminni                                                               2                 10                  0              30
atburður (líkindafræði)                                                    0                 10                  0               0
atómmassi                                                                  3                 10                  0              47
atómstöðin (kvikmynd)                                                      0                 10                  0               0
atómstöðin                                                                 0                 10                  0               0
atómstöðin/núlleinn                                                        0                 10                  0               0
atómstöðin (skáldsaga)                                                     0                 10                  0               0
aðventa                                                                    0                 10                  0               0
aðventukrans                                                               1                 10                  0              16
aðalbjörg                                                                  0                 10                  0               0
aðalbjört                                                                  0                 10                  0               0
aðalgeir                                                                   0                 10                  0               0
aðalstræti                                                                 0                 10                  0               0
aðalsteinn                                                                 0                 10                  0               0
aðalvík                                                                    0                 10                  0               0
aðalveig                                                                   0                 10                  0               0
aðalsögn                                                                   3                 10                  0              42
aðalborg                                                                   1                 10                  0              17
aðalsveldi                                                                 0                 10                  0               0
aðalsetning                                                                5                 10                  0              79
aðalheiður                                                                 0                 10                  0               0
aðalsteina                                                                 0                 10                  0               0
aðaltenging                                                                5                 10                  0              72
aðalbergur                                                                 0                 10                  0               0
aðaltengingar                                                              4                 10                  0              58
aðalsteinunn                                                               0                 10                  0               0
aðalbjörn                                                                  0                 10                  0               0
aðalfríður                                                                 0                 10                  0               0
aðaldælahreppur                                                            0                 10                  0               0
aðalmundur                                                                 0                 10                  0               0
aðalráður                                                                  0                 10                  0               0
aðalskipulag                                                               9                 10                  0             146
aðalborgar                                                                 1                 10                  0              17
aðalsteinn bergdal                                                         0                 10                  0               0
aðalberg                                                                   0                 10                  0               0
aðalorð                                                                    2                 10                  0              32
aðalsöngvari                                                               8                 10                  0             125
aðalbert                                                                   0                 10                  0               0
aðgerð pólstjarnan                                                         0                 10                  0               0
aðgerð (stærðfræði)                                                        0                 10                  0               0
aðgerð (forritun)                                                          0                 10                  0               0
aðils                                                                      0                 10                  0               0
aðfeldi                                                                    3                 10                  0              45
aðferðaminni                                                               1                 10                  0              15
aðferðafræðileg náttúruhyggja                                              0                 10                  0               0
aðflutningur                                                               1                 10                  0              16
aðfangadagur                                                               0                 10                  0               0
að ferninga hring                                                          0                 10                  0               0
að                                                                     15569                 10                  0          261645
aðskeyti                                                                   5                 10                  0              95
aðskilnaðardómurinn                                                        0                 10                  0               0
aðskilnaðarstefnan í suður-afríku                                          0                 10                  0               0
arvaníska                                                                  1                 10                  0              18
araneus                                                                    0                 10                  0               0
arabíska                                                                 107                 10                  0            1891
aralvatn                                                                   0                 10                  0               0
aradan                                                                     0                 10                  0               0
aragónska                                                                  1                 10                  0              17
aravakíska                                                                 1                 10                  0              15
arabíuhaf                                                                  0                 10                  0               0
araniko                                                                    0                 10                  0               0
arababandalagið                                                            0                 10                  0               0
arabískar tölur                                                            0                 10                  0               0
arabíuskaginn                                                              0                 10                  0               0
argobba                                                                    1                 10                  0              15
argumentum ad baculum                                                      0                 10                  0               0
argumentum ad hominem                                                      0                 10                  0               0
argon                                                                      3                 10                  0              59
argentína                                                                  0                 10                  0               0
arkitekt                                                                  44                 10                  0             806
arkesilás                                                                  0                 10                  0               0
arkansas                                                                   0                 10                  0               0
arkarvísir                                                                 0                 10                  0               0
arkímedes                                                                  0                 10                  0               0
arkílokkos                                                                 0                 10                  0               0
ari magnússon                                                              0                 10                  0               0
ari                                                                     3766                 10                  0           59905
aris                                                                      89                 10                  0            1523
aristarkos frá samóþrake                                                   0                 10                  0               0
arinbjörg                                                                  0                 10                  0               0
ari þorgilsson                                                             0                 10                  0               0
ariston                                                                    0                 10                  0               0
arilíus                                                                    0                 10                  0               0
ariel sharon                                                               0                 10                  0               0
aristarkos frá tegeu                                                       0                 10                  0               0
arizona                                                                    0                 10                  0               0
ari kristinsson                                                            0                 10                  0               0
aristokles frá messenu                                                     0                 10                  0               0
aristarkos                                                                 0                 10                  0               0
aristippos frá kýrenu                                                      0                 10                  0               0
arial                                                                      0                 10                  0               0
arisa                                                                      1                 10                  0              17
aristófanes frá býzantíon                                                  0                 10                  0               0
aristóteles                                                                0                 10                  0               0
arinbjörn                                                                  0                 10                  0               0
ari fróði þorgilsson                                                       0                 10                  0               0
ari matthíasson                                                            0                 10                  0               0
aristófanes                                                                0                 10                  0               0
arpitanska                                                                 2                 10                  0              37
arfsmálið                                                                  0                 10                  0               0
aron                                                                      20                 10                  0             311
arthur conan doyle                                                         0                 10                  0               0
artemidóros                                                                0                 10                  0               0
arthur miller                                                              0                 10                  0               0
art spiegelman                                                             0                 10                  0               0
arthur c. clarke                                                           0                 10                  0               0
arthur                                                                     0                 10                  0               0
artur balder                                                               0                 10                  0               0
artúr                                                                      1                 10                  0              15
arthur rimbaud                                                             0                 10                  0               0
arthúr                                                                     0                 10                  0               0
articolo 31                                                                0                 10                  0               0
arthur schopenhauer                                                        0                 10                  0               0
aryabhata                                                                  0                 10                  0               0
arnljótur                                                                  0                 10                  0               0
arnþrúður                                                                  1                 10                  0              15
arndór                                                                     0                 10                  0               0
arngrímur                                                                  0                 10                  0               0
arnbjörg                                                                   0                 10                  0               0
arnóra                                                                     0                 10                  0               0
arnold                                                                     0                 10                  0               0
arnrós                                                                     0                 10                  0               0
arna                                                                    1104                 10                  0           18290
arnarneshreppur                                                            1                 10                  0              27
arngeir (landnámsmaður)                                                    0                 10                  0               0
arndís auðga steinólfsdóttir                                               0                 10                  0               0
arnareyri                                                                  2                 10                  0              35
arnlín                                                                     0                 10                  0               0
arnfinnur                                                                  1                 10                  0              15
arnberg                                                                    1                 10                  0              20
arnar grétarsson                                                           0                 10                  0               0
arnbjörg (mannsnafn)                                                       0                 10                  0               0
arnbjörg (landnámskona)                                                    0                 10                  0               0
arnviður                                                                   0                 10                  0               0
arnleif                                                                    1                 10                  0              16
arnaut daniel                                                              0                 10                  0               0
arney                                                                      2                 10                  0              33
arngeir                                                                    0                 10                  0               0
arnsteinn                                                                  1                 10                  0              15
arnmóður                                                                   0                 10                  0               0
arnheiður                                                                  1                 10                  0              15
arnar                                                                    399                 10                  0            6178
arngunnur                                                                  0                 10                  0               0
arndís                                                                     1                 10                  0              15
arnaldur                                                                   0                 10                  0               0
arngrímur gíslason málari                                                  0                 10                  0               0
arnald                                                                     0                 10                  0               0
arnarhóll                                                                  0                 10                  0               0
arnrún                                                                     1                 10                  0              15
arnbjörn                                                                   0                 10                  0               0
arnfreyr                                                                   0                 10                  0               0
arnaldo forlani                                                            0                 10                  0               0
arnoddur                                                                   0                 10                  0               0
arnór                                                                      0                 10                  0               0
arnljótur ólafsson                                                         0                 10                  0               0
arnljót                                                                    0                 10                  0               0
arnaldur indriðason                                                        0                 10                  0               0
arnfjörð                                                                   1                 10                  0              15
arngrímur jónsson lærði                                                    0                 10                  0               0
arnleifur                                                                  1                 10                  0              16
arnes                                                                    103                 10                  0            1577
arnþóra                                                                    1                 10                  0              15
arnór benónýsson                                                           0                 10                  0               0
arngils                                                                    0                 10                  0               0
arnhildur                                                                  1                 10                  0              16
arnkatla                                                                   0                 10                  0               0
arnþór                                                                     2                 10                  0              30
arnúlfur                                                                   0                 10                  0               0
arnbergur                                                                  0                 10                  0               0
arnór hannibalsson                                                         0                 10                  0               0
arnfinna                                                                   0                 10                  0               0
arnlaugur                                                                  1                 10                  0              15
arnbjörg sveinsdóttir                                                      0                 10                  0               0
arnkell                                                                    0                 10                  0               0
arnó                                                                       4                 10                  0              62
arnborg                                                                    0                 10                  0               0
arnar sævarsson                                                            0                 10                  0               0
arngerður                                                                  1                 10                  0              15
arnarfjörður                                                               5                 10                  0              97
arnar jónsson                                                              0                 10                  0               0
arnfríður                                                                  1                 10                  0              15
arnlaug                                                                    2                 10                  0              30
arnika                                                                     0                 10                  0               0
arnmundur                                                                  0                 10                  0               0
arey                                                                      36                 10                  0             582
ares (mannsnafn)                                                           0                 10                  0               0
arete frá kýrenu                                                           0                 10                  0               0
are                                                                      515                 10                  0            9206
ares                                                                      11                 10                  0             182
arezzo                                                                     0                 10                  0               0
ares (aðgreining)                                                          0                 10                  0               0
aretha franklin                                                            0                 10                  0               0
arezzo (sýsla)                                                             0                 10                  0               0
arent                                                                      8                 10                  0             132
armenía (mannsnafn)                                                        0                 10                  0               0
armenía                                                                    0                 10                  0               0
armin meiwes                                                               0                 10                  0               0
armed forces radio and television service keflavik                         0                 10                  0               0
armenska                                                                   3                 10                  0              52
aríi                                                                       6                 10                  0             110
aríella                                                                    0                 10                  0               0
aríel                                                                      0                 10                  0               0
aríanna hollandsprinsessa                                                  0                 10                  0               0
aríus (mannsnafn)                                                          0                 10                  0               0
arína                                                                      8                 10                  0             122
aríanna                                                                    1                 10                  0              15
arín                                                                      30                 10                  0             465
arís                                                                     682                 10                  0           11720
aríus                                                                      8                 10                  0             124
arúba                                                                      0                 10                  0               0
ardís                                                                      1                 10                  0              15
arctic death ship                                                          0                 10                  0               0
arctic monkeys                                                             0                 10                  0               0
archetype                                                                  0                 10                  0               0
arseface                                                                   0                 10                  0               0
arsenal                                                                    0                 10                  0               0
arsiafjall                                                                 0                 10                  0               0
arsen                                                                     11                 10                  0             159
arsène wenger                                                              0                 10                  0               0
ahmed yassin                                                               0                 10                  0               0
ahmad al-mansur                                                            0                 10                  0               0
ajax (sófókles)                                                            0                 10                  0               0
ajas                                                                       2                 10                  0              32
ajas telamonsson                                                           0                 10                  0               0
alvar                                                                     37                 10                  0             589
alvar aalto                                                                0                 10                  0               0
alvilda                                                                    0                 10                  0               0
alva                                                                      80                 10                  0            1214
alvin                                                                     11                 10                  0             191
alaska (1875)                                                              0                 10                  0               0
alabastur                                                                  1                 10                  0              55
alaskavíðir                                                                0                 10                  0               0
alan keyes                                                                 0                 10                  0               0
alaskalúpína                                                               0                 10                  0               0
alan shearer                                                               0                 10                  0               0
alasdair macintyre                                                         0                 10                  0               0
alabama                                                                    0                 10                  0               0
alaska                                                                     0                 10                  0               0
alan hollinghurst                                                          0                 10                  0               0
alan turing                                                                0                 10                  0               0
alain robbe-grillet                                                        0                 10                  0               0
algebruleg tala                                                            0                 10                  0               0
algonkinsk tungumál                                                        0                 10                  0               0
algyðistrú                                                                 4                 10                  0              64
algarve                                                                    0                 10                  0               0
algildi                                                                    5                 10                  0              82
algebra                                                                    7                 10                  0             113
algeirsborg                                                                0                 10                  0               0
alæta                                                                      2                 10                  0              32
alkestis (evripídes)                                                       0                 10                  0               0
alkanar                                                                    2                 10                  0              48
alkajos                                                                    0                 10                  0               0
alkóhólismi                                                                0                 10                  0               0
alkman                                                                     1                 10                  0              17
alkóhól                                                                    9                 10                  0             166
alkibíades i (platon)                                                      0                 10                  0               0
alkibíades ii (platon)                                                     0                 10                  0               0
alkalímálmur                                                               8                 10                  0             120
alkenar                                                                    1                 10                  0              16
alkul                                                                      3                 10                  0              46
alice                                                                      0                 10                  0               0
alibýfluga                                                                 0                 10                  0               0
ali                                                                     2110                 10                  0           31248
alive (tölvuleikur)                                                        0                 10                  0               0
alicante                                                                   0                 10                  0               0
alien syndrome                                                             0                 10                  0               0
alpafjöll                                                                  0                 10                  0               0
alfons mucha                                                               0                 10                  0               0
alfred north whitehead                                                     0                 10                  0               0
alfred jules ayer                                                          0                 10                  0               0
alfred nobel                                                               0                 10                  0               0
alfreð                                                                     0                 10                  0               0
alfífa                                                                     0                 10                  0               0
alfa (mannsnafn)                                                           0                 10                  0               0
alfred                                                                     0                 10                  0               0
alfred tarski                                                              0                 10                  0               0
alfons                                                                     0                 10                  0               0
alfred hitchcock                                                           0                 10                  0               0
alfred edward taylor                                                       0                 10                  0               0
alfasundrun                                                                0                 10                  0               0
alfa                                                                      29                 10                  0             531
alfred jolson                                                              0                 10                  0               0
alfræðirit                                                                 9                 10                  0             306
alfred binet                                                               0                 10                  0               0
alois hitler                                                               0                 10                  0               0
alois alzheimer                                                            0                 10                  0               0
altstätten                                                                 0                 10                  0               0
alta                                                                     209                 10                  0            3420
altari                                                                    14                 10                  0             227
altbier                                                                    0                 10                  0               0
alrekur                                                                    0                 10                  0               0
alræði                                                                    11                 10                  0             175
alrún                                                                      2                 10                  0              30
alheimurinn                                                                7                 10                  0             114
allianz arena                                                              0                 10                  0               0
allt í drasli                                                              0                 10                  0               0
allsherjarþing sameinuðu þjóðanna                                          0                 10                  0               0
alla                                                                    2482                 10                  0           40114
allrahanda                                                                 1                 10                  0              18
allý                                                                       3                 10                  0              46
allan                                                                    217                 10                  0            3239
allir litir hafsins eru kaldir                                             0                 10                  0               0
allraheilagramessa                                                         0                 10                  0               0
allah                                                                     41                 10                  0             663
alnæmi                                                                     1                 10                  0              15
alexíus                                                                    0                 10                  0               0
alex                                                                       5                 10                  0              78
alexía hollandsprinsessa                                                   0                 10                  0               0
alexander mikli                                                            0                 10                  0               0
alec guinness                                                              0                 10                  0               0
alexander (aðgreining)                                                     0                 10                  0               0
alexander nehamas                                                          0                 10                  0               0
alek wek                                                                   0                 10                  0               0
alexander frá afrodísías                                                   0                 10                  0               0
alexander graham bell                                                      0                 10                  0               0
alexander litvinenko                                                       0                 10                  0               0
alexander anderson (hellsing)                                              0                 10                  0               0
alexandre dumas eldri                                                      0                 10                  0               0
alexandría                                                                 0                 10                  0               0
aleuteyjar                                                                 0                 10                  0               0
alexander von humboldt                                                     0                 10                  0               0
alexander mccall smith                                                     0                 10                  0               0
alexandra bretadrottning                                                   0                 10                  0               0
alexander petersson                                                        0                 10                  0               0
alentejo                                                                   0                 10                  0               0
alemanníska                                                                2                 10                  0              30
alexía                                                                     0                 10                  0               0
alexander severus                                                          0                 10                  0               0
alexandr púshkín                                                           0                 10                  0               0
alexander fleming                                                          0                 10                  0               0
alexa vega                                                                 0                 10                  0               0
alexandría (mannsnafn)                                                     0                 10                  0               0
alessandro costacurta                                                      0                 10                  0               0
alexanders saga                                                            0                 10                  0               0
alexa                                                                      5                 10                  0              84
alexander (mannsnafn)                                                      0                 10                  0               0
alexandra                                                                  0                 10                  0               0
aleutíska                                                                  3                 10                  0              47
alexander i                                                                0                 10                  0               0
alberto jori                                                               0                 10                  0               0
albertsvatn                                                                0                 10                  0               0
alberta (mannsnafn)                                                        0                 10                  0               0
albert camus                                                               0                 10                  0               0
albus dumbledore                                                           0                 10                  0               0
albanía                                                                    0                 10                  0               0
albert bandura                                                             0                 10                  0               0
alberta (fylki)                                                            0                 10                  0               0
albrecht dürer                                                             0                 10                  0               0
albína                                                                     0                 10                  0               0
albert eymundsson                                                          0                 10                  0               0
alba                                                                      57                 10                  0             940
albert guðmundsson                                                         0                 10                  0               0
albanska                                                                   4                 10                  0              68
albert einstein                                                            0                 10                  0               0
albert                                                                     3                 10                  0              51
albert 2. belgíukonungur                                                   0                 10                  0               0
alberta                                                                    0                 10                  0               0
albufeira                                                                  0                 10                  0               0
alutor                                                                     1                 10                  0              15
alucard (hellsing)                                                         0                 10                  0               0
alucard                                                                    0                 10                  0               0
almenningssamgöngur                                                        4                 10                  0              66
alma                                                                      72                 10                  0            1226
almatyfylki                                                                0                 10                  0               0
almenn brot                                                                0                 10                  0               0
almaty                                                                     0                 10                  0               0
almennt ár                                                                 2                 10                  0              31
almere                                                                     0                 10                  0               0
almannatengsl                                                              2                 10                  0              33
almengi                                                                    1                 10                  0              15
almar                                                                     28                 10                  0             434
almæli                                                                     0                 10                  0               0
almannagjá                                                                 0                 10                  0               0
almenna afstæðiskenningin                                                  0                 10                  0               0
almenna verslunarfélagið                                                   0                 10                  0               0
almazán                                                                    0                 10                  0               0
al-khwarizmi                                                               0                 10                  0               0
al-kaída                                                                   0                 10                  0               0
alída                                                                      1                 10                  0              17
alí                                                                      623                 10                  0            9209
alísa                                                                      1                 10                  0              15
alís                                                                      37                 10                  0             565
alí ibn abu talib                                                          0                 10                  0               0
al gore                                                                    0                 10                  0               0
aldurstakmark (kvikmyndir)                                                 0                 10                  0               0
aldinborgarar                                                              0                 10                  0               0
aldan                                                                     69                 10                  0            1210
aldinborg                                                                  0                 10                  0               0
alda (mannsnafn)                                                           0                 10                  0               0
aldný                                                                      0                 10                  0               0
aldursgreining með geislunarmælingu                                        1                 10                  0              17
aldinbori                                                                  0                 10                  0               0
aldar                                                                    807                 10                  0           15248
aldebaran                                                                  0                 10                  0               0
aldís                                                                     10                 10                  0             152
aldo moro                                                                  0                 10                  0               0
aldursgreining                                                             7                 10                  0             115
alcatraz                                                                   0                 10                  0               0
alcide de gasperi                                                          0                 10                  0               0
alcoa                                                                      0                 10                  0               0
alþingiskosningar 1967                                                     0                 10                  0               0
alþjóða siglingasambandið                                                  0                 10                  0               0
alþjóða skáksambandið                                                      0                 10                  0               0
alþjóða veðurfræðistofnunin                                                0                 10                  0               0
alþingiskosningar 1991                                                     0                 10                  0               0
alþjóða heilbrigðisstofnunin                                               0                 10                  0               0
alþingiskosningar 1933                                                     0                 10                  0               0
alþýðubankinn                                                              0                 10                  0               0
alþingiskosningar 1995                                                     0                 10                  0               0
alþjóðasiglingamálastofnunin                                               0                 10                  0               0
alþingiskosningar 1999                                                     0                 10                  0               0
alþjóðlega geimstöðin                                                      0                 10                  0               0
alþingiskosningar 1987                                                     0                 10                  0               0
alþýðusamband íslands                                                      0                 10                  0               0
alþjóðatengsl íslands                                                      0                 10                  0               0
alþingiskosningar 1844                                                     0                 10                  0               0
alþjóðasamtök um eldfjallafræði                                            0                 10                  0               0
alþjóðlega einingakerfið                                                   0                 10                  0               0
alþjóðlegi sakamáladómstóllinn                                             0                 10                  0               0
alþingiskosningar 1949                                                     0                 10                  0               0
alþingiskosningar 1971                                                     0                 10                  0               0
alþingiskosningar 1974                                                     0                 10                  0               0
alþjóðasamband um jarðmælingar og jarðeðlisfræði                           0                 10                  0               0
alþjóða sundsambandið                                                      0                 10                  0               0
alþýðubókin (1874)                                                         0                 10                  0               0
alþjóðaflugvöllurinn í kansai                                              0                 10                  0               0
alþjóðastofnun                                                            12                 10                  0             243
alþjóðaflugmálastofnunin                                                   0                 10                  0               0
alþingiskosningar 1978                                                     0                 10                  0               0
alþjóðlegur baráttudagur kvenna                                            0                 10                  0               0
alþýðulýðveldið kína                                                       0                 10                  0               0
alþýðuflokkurinn                                                           0                 10                  0               0
alþjóðlega staðlastofnunin                                                 0                 10                  0               0
alþingiskosningar 1963                                                     0                 10                  0               0
alþingiskosningar 1983                                                     0                 10                  0               0
alþjóðadómstóllinn                                                         0                 10                  0               0
alþjóðabankinn                                                             0                 10                  0               0
alþingishúsið                                                              0                 10                  0               0
alþjóðlega núllbaugsráðstefnan                                             0                 10                  0               0
alþingishátíðin                                                            0                 10                  0               0
alþingiskosningar                                                          3                 10                  0              46
alþjóðlegu náttúruverndarsamtökin                                          0                 10                  0               0
alþjóðaviðskiptastofnunin                                                  0                 10                  0               0
alþýðubandalagið                                                           0                 10                  0               0
alþjóða portúgölskustofnunin                                               0                 10                  0               0
alþingiskosningar 2007                                                     0                 10                  0               0
alþingiskosningar 1946                                                     0                 10                  0               0
alþingisbækur íslands                                                      0                 10                  0               0
alþjóðagjaldeyrissjóðurinn                                                 0                 10                  0               0
alþingiskosningar 1979                                                     0                 10                  0               0
alþingiskosningar 1953                                                     0                 10                  0               0
alþjóðlega hljóðstafrófið                                                  3                 10                  0              47
alþingiskosningar 2003                                                     0                 10                  0               0
alþingi                                                                   70                 10                  0            1084
alþjóðaklósettstofnunin                                                    0                 10                  0               0
alþjóðasteindarfræðisamtökin                                               0                 10                  0               0
alþjóða kjarnorkumálastofnunin                                             0                 10                  0               0
alsheimer                                                                  0                 10                  0               0
alsatíska                                                                  2                 10                  0              32
alsdorf                                                                    0                 10                  0               0
alsjálfvirkt skotvopn                                                      1                 10                  0              21
alsír                                                                      0                 10                  0               0
alsíkusmári                                                                0                 10                  0               0
ayreon                                                                     0                 10                  0               0
ayn rand                                                                   0                 10                  0               0
anaxímenes frá lampsakos                                                   0                 10                  0               0
ananas                                                                     7                 10                  0             126
anaxagóras                                                                 0                 10                  0               0
anatólía                                                                   0                 10                  0               0
anaxímandros                                                               0                 10                  0               0
anastasía                                                                  0                 10                  0               0
anaxímenes                                                                 0                 10                  0               0
analía                                                                     0                 10                  0               0
anatole france                                                             0                 10                  0               0
analysis                                                                   1                 10                  0              16
anaxarkos                                                                  0                 10                  0               0
anastasia                                                                  0                 10                  0               0
angela merkel                                                              0                 10                  0               0
angáríska                                                                  1                 10                  0              16
angelíka                                                                   0                 10                  0               0
angóla                                                                     0                 10                  0               0
angela                                                                     1                 10                  0              18
angvilla                                                                   0                 10                  0               0
angi                                                                     249                 10                  0            4528
angurboða                                                                  0                 10                  0               0
angantýr                                                                   0                 10                  0               0
ankara                                                                     0                 10                  0               0
anima                                                                      1                 10                  0              17
animeklúbbur                                                               0                 10                  0               0
anime                                                                     30                 10                  0             524
animals                                                                    0                 10                  0               0
anita                                                                      7                 10                  0             116
anika                                                                      0                 10                  0               0
anime á íslandi                                                            0                 10                  0               0
antonio segni                                                              0                 10                  0               0
anthony kenny                                                              0                 10                  0               0
anthony                                                                    0                 10                  0               0
anton tsjekhov                                                             0                 10                  0               0
antoine de saint-exupéry                                                   0                 10                  0               0
antananarívó                                                               0                 10                  0               0
antoníus                                                                   0                 10                  0               0
antimon                                                                    2                 10                  0              42
antífon                                                                    0                 10                  0               0
antónio de oliveira salazar                                                0                 10                  0               0
antonio vivaldi                                                            0                 10                  0               0
antonínus píus                                                             0                 10                  0               0
antoni grabowski                                                           0                 10                  0               0
antonía                                                                    0                 10                  0               0
antígóna (sófókles)                                                        0                 10                  0               0
antonín dvořák                                                             0                 10                  0               0
antillaeyjar                                                               0                 10                  0               0
antwerpen                                                                  0                 10                  0               0
antígva og barbúda                                                         0                 10                  0               0
antonio stradivari                                                         0                 10                  0               0
antónio lobo antunes                                                       0                 10                  0               0
anton                                                                      4                 10                  0              63
anthony hopkins                                                            0                 10                  0               0
antonio starabba                                                           0                 10                  0               0
anthrax                                                                    1                 10                  0              15
antwerpen-hérað                                                            0                 10                  0               0
antoine arnauld                                                            0                 10                  0               0
anjou                                                                      0                 10                  0               0
anja                                                                      46                 10                  0             707
anló                                                                       1                 10                  0              16
anna frank                                                                 0                 10                  0               0
anno domini                                                                1                 10                  0              17
annars stigs jafna                                                         0                 10                  0               0
ann                                                                    11770                 10                  0          182310
anna og skapsveiflurnar                                                    0                 10                  0               0
anne rice                                                                  0                 10                  0               0
annalísa                                                                   0                 10                  0               0
annabella                                                                  0                 10                  0               0
anna komnene                                                               0                 10                  0               0
annar                                                                   1044                 10                  0           17725
annamít fjallgarðurinn                                                     0                 10                  0               0
annel                                                                     21                 10                  0             362
annetta                                                                    0                 10                  0               0
anne                                                                     269                 10                  0            4335
annað púnverska stríðið                                                    0                 10                  0               0
annes                                                                    202                 10                  0            3339
annie oliv                                                                 0                 10                  0               0
annía                                                                      0                 10                  0               0
anna politkovskaja                                                         0                 10                  0               0
annika                                                                     0                 10                  0               0
anna akmatova                                                              0                 10                  0               0
anna nicole smith                                                          0                 10                  0               0
anný                                                                       3                 10                  0              44
anna                                                                    3719                 10                  0           54434
anney                                                                     15                 10                  0             262
annus horribilis                                                           1                 10                  0              20
anes                                                                     302                 10                  0            4610
anetta                                                                     1                 10                  0              15
anett griffel                                                              0                 10                  0               0
anwar sadat                                                                0                 10                  0               0
aníta                                                                      2                 10                  0              35
aníka                                                                      0                 10                  0               0
anína                                                                      7                 10                  0             108
an essay concerning human understanding                                    0                 10                  0               0
andleg viðleitni                                                           0                 10                  0               0
andrá                                                                      4                 10                  0              78
andakílshreppur                                                            0                 10                  0               0
andrei nikolaevitsch kolmogorov                                            0                 10                  0               0
andleg heilsa                                                              0                 10                  0               0
andrew rogers                                                              0                 10                  0               0
andrij sjevtsjenko                                                         0                 10                  0               0
andrómakka (evripídes)                                                     0                 10                  0               0
andrej kolmogorov                                                          0                 10                  0               0
andamanhaf                                                                 0                 10                  0               0
andatrú                                                                    0                 10                  0               0
andrés þór gunnlaugsson                                                    0                 10                  0               0
andorra                                                                    0                 10                  0               0
andhverfa                                                                  9                 10                  0             139
andri                                                                    146                 10                  0            2616
andy warhol                                                                0                 10                  0               0
andalúsíska                                                                1                 10                  0              16
andrúmsloft                                                               31                 10                  0             573
andrés önd                                                                 0                 10                  0               0
andorra la vella                                                           0                 10                  0               0
andlitsmynd                                                                1                 10                  0              16
andra                                                                     17                 10                  0             312
andrew wiles                                                               0                 10                  0               0
andrew johnson                                                             0                 10                  0               0
andesfjöll                                                                 0                 10                  0               0
andop                                                                      0                 10                  0               0
andré-marie ampère                                                         0                 10                  0               0
andrómeda                                                                  0                 10                  0               0
andrés                                                                     0                 10                  0               0
andrew ridgeley                                                            0                 10                  0               0
andlag                                                                    10                 10                  0             191
andakílsá                                                                  0                 10                  0               0
anders fogh rasmussen                                                      0                 10                  0               0
andókídes                                                                  0                 10                  0               0
andlitsókenni                                                              0                 10                  0               0
andakílsskóli                                                              0                 10                  0               0
andrómakka                                                                 0                 10                  0               0
andheiti                                                                   3                 10                  0              44
andrew jackson                                                             0                 10                  0               0
andrómeda (grísk goðafræði)                                                0                 10                  0               0
andreas                                                                    0                 10                  0               0
andrés magnússon                                                           0                 10                  0               0
andlát (aðgreining)                                                        0                 10                  0               0
and                                                                    11967                 10                  0          185476
andri snær magnason                                                        0                 10                  0               0
andrea                                                                     0                 10                  0               0
andlitsbein                                                                2                 10                  0              32
andaætt                                                                    8                 10                  0             127
andrew w. mellon                                                           0                 10                  0               0
andrúmsloft jarðar                                                         2                 10                  0              31
anders                                                                    30                 10                  0             492
andlát (hljómsveit)                                                        0                 10                  0               0
andrew carnegie                                                            0                 10                  0               0
andspyrna (hreyfing)                                                       0                 10                  0               0
anþeia                                                                     0                 10                  0               0
ansgar                                                                     0                 10                  0               0
aelius donatus                                                             0                 10                  0               0
aemilius                                                                   0                 10                  0               0
aqmolafylki                                                                0                 10                  0               0
abasínska                                                                  1                 10                  0              18
abanjommál                                                                 1                 10                  0              16
abkasíska                                                                  2                 10                  0              36
abýdos (egyptalandi)                                                       0                 10                  0               0
abýdos                                                                     0                 10                  0               0
abidjan                                                                    0                 10                  0               0
abo-blóðflokkar                                                            0                 10                  0               0
abraham (mannsnafn)                                                        0                 10                  0               0
abraham (aðgreining)                                                       0                 10                  0               0
abraham                                                                    7                 10                  0             106
abrútsi                                                                    0                 10                  0               0
abrahamísk trúarbrögð                                                      0                 10                  0               0
abraham lincoln                                                            0                 10                  0               0
abraham van helsing                                                        0                 10                  0               0
abel (mannsnafn)                                                           0                 10                  0               0
abela                                                                      1                 10                  0              16
abel                                                                      77                 10                  0            1273
aberdeen                                                                   0                 10                  0               0
aberffrwd                                                                  0                 10                  0               0
abelsverðlaunin                                                            0                 10                  0               0
abel tasman                                                                0                 10                  0               0
abbas 2.                                                                   0                 10                  0               0
abbas mikli                                                                0                 10                  0               0
abba                                                                      65                 10                  0            1151
abbey road                                                                 0                 10                  0               0
abu nuwas                                                                  0                 10                  0               0
abu daoud                                                                  0                 10                  0               0
abujmaria                                                                  1                 10                  0              15
abú dabí                                                                   0                 10                  0               0
abútja                                                                     0                 10                  0               0
abdullah bin abdul aziz al-saud                                            0                 10                  0               0
abc-ríkin                                                                  0                 10                  0               0
abstraktlist                                                               1                 10                  0              18
absolution                                                                 0                 10                  0               0
absolution tour                                                            0                 10                  0               0
august immanuel bekker                                                     0                 10                  0               0
augustin louis cauchy                                                      0                 10                  0               0
augustus de morgan                                                         0                 10                  0               0
auguste comte                                                              0                 10                  0               0
augnfyrirbrigði                                                            1                 10                  0              21
auga                                                                     281                 10                  0            4504
auglýsingar                                                                6                 10                  0             100
augustus meineke                                                           0                 10                  0               0
augntönn                                                                   0                 10                  0               0
augusto pinochet                                                           0                 10                  0               0
auguste rodin                                                              0                 10                  0               0
auglýsingastofa reykjavíkur                                                0                 10                  0               0
aukagetuhyggja                                                             0                 10                  0               0
aukatenging                                                                4                 10                  0             106
aukaandlag                                                                 1                 10                  0              16
aukasetning                                                                7                 10                  0             111
aukatengingar                                                              2                 10                  0              50
aukasól                                                                    0                 10                  0               0
aukafall                                                                   6                 10                  0             122
automatix                                                                  0                 10                  0               0
autobahn                                                                   0                 10                  0               0
autobahn (nemendafélag)                                                    0                 10                  0               0
auðný                                                                      0                 10                  0               0
auðnutittlingur                                                            0                 10                  0               0
auðkennislykill                                                            0                 10                  0               0
auður jónsdóttir                                                           0                 10                  0               0
auður djúpúðga                                                             0                 10                  0               0
auðdís                                                                     0                 10                  0               0
auðun                                                                      7                 10                  0             107
auður                                                                     32                 10                  0             541
auðkúluhreppur                                                             0                 10                  0               0
auðgað úran                                                                0                 10                  0               0
auðunarstofa                                                               0                 10                  0               0
auðkell                                                                    0                 10                  0               0
auðólfur (landnámsmaður)                                                   0                 10                  0               0
auðlín                                                                     0                 10                  0               0
auðbjört                                                                   0                 10                  0               0
auður eir vilhjálmsdóttir                                                  0                 10                  0               0
auðbjörn                                                                   0                 10                  0               0
auðna                                                                      3                 10                  0              49
auðrún                                                                     0                 10                  0               0
auðunn blöndal                                                             0                 10                  0               0
auðgunarbrot                                                               1                 10                  0              21
auðunn rauði                                                               0                 10                  0               0
auðunn                                                                     1                 10                  0              16
auðarstræti                                                                0                 10                  0               0
auðhumla                                                                   0                 10                  0               0
auður auðuns                                                               0                 10                  0               0
auðbert                                                                    0                 10                  0               0
auðbergur                                                                  0                 10                  0               0
auðmundur                                                                  0                 10                  0               0
auðbjörg                                                                   0                 10                  0               0
auðkennislykill (auðkenni)                                                 0                 10                  0               0
auðólfur                                                                   0                 10                  0               0
auðgeir                                                                    0                 10                  0               0
aurora                                                                     0                 10                  0               0
aulus persius flaccus                                                      0                 10                  0               0
auld lang syne                                                             0                 10                  0               0
aulus gellius                                                              0                 10                  0               0
audioslave                                                                 0                 10                  0               0
auckland grammar school                                                    0                 10                  0               0
auckland                                                                   0                 10                  0               0
austurför kýrosar                                                          0                 10                  0               0
austur-skaftafellssýsla                                                    0                 10                  0               0
austurlandskjördæmi                                                        0                 10                  0               0
austur-evrópa                                                              0                 10                  0               0
austmann                                                                   0                 10                  0               0
austurbyggð                                                                0                 10                  0               0
austurrísku hagfræðingarnir                                                0                 10                  0               0
austari-krókar                                                             0                 10                  0               0
austurríki-ungverjaland                                                    0                 10                  0               0
austur-afríka                                                              0                 10                  0               0
austurlönd                                                                 5                 10                  0             108
austur-asía                                                                0                 10                  0               0
austur-afríkutími                                                          0                 10                  0               0
austin (texas)                                                             0                 10                  0               0
austurvöllur                                                               0                 10                  0               0
austdal                                                                    0                 10                  0               0
austurbæjarbíó                                                             0                 10                  0               0
austurríki                                                                 0                 10                  0               0
austur-anglía                                                              0                 10                  0               0
austri (mannsnafn)                                                         0                 10                  0               0
austur-eyjafjallahreppur                                                   0                 10                  0               0
austur-tímor                                                               0                 10                  0               0
austur-húnavatnssýsla                                                      0                 10                  0               0
austrænar rétttrúnaðarkirkjur                                              0                 10                  0               0
austur                                                                   534                 10                  0            9415
austurnorræn mál                                                           2                 10                  0              35
austfold                                                                   0                 10                  0               0
austurstræti                                                               0                 10                  0               0
austmar                                                                    0                 10                  0               0
austur-hérað                                                               0                 10                  0               0
austurdalur                                                                0                 10                  0               0
austfjörð                                                                  0                 10                  0               0
austurbæjarskóli                                                           0                 10                  0               0
austur-indíur                                                              0                 10                  0               0
austur-kasakstanfylki                                                      0                 10                  0               0
austur-kongó                                                               0                 10                  0               0
austur-pakistan                                                            0                 10                  0               0
austur-agðir                                                               0                 10                  0               0
austurlönd nær                                                             0                 10                  0               0
austur-barðastrandarsýsla                                                  0                 10                  0               0
austur-yorkshire                                                           0                 10                  0               0
austar                                                                    16                 10                  0             289
austur-landeyjahreppur                                                     0                 10                  0               0
austurey                                                                   0                 10                  0               0
austræn heimspeki                                                          0                 10                  0               0
auschwitz                                                                  0                 10                  0               0
austur-sussex                                                              0                 10                  0               0
austur-þýskaland                                                           0                 10                  0               0
austurlönd fjær                                                            0                 10                  0               0
austfirðir                                                                 1                 10                  0              17
austrómverska keisaradæmið                                                 1                 10                  0              15
austfjarðaprófastsdæmi                                                     0                 10                  0               0
austurland                                                                11                 10                  0             184
amanda                                                                     0                 10                  0               0
amadou toumani touré                                                       0                 10                  0               0
amazonas                                                                   0                 10                  0               0
amalíuborg                                                                 0                 10                  0               0
amal                                                                     176                 10                  0            2968
amalþeia                                                                   0                 10                  0               0
amalía                                                                     0                 10                  0               0
amasónfljót                                                                0                 10                  0               0
amadea                                                                     0                 10                  0               0
amazon.com                                                                 0                 10                  0               0
amý                                                                       12                 10                  0             192
amintore fanfani                                                           0                 10                  0               0
amiga 500                                                                  0                 10                  0               0
amper                                                                     12                 10                  0             195
amperstund                                                                 1                 10                  0              15
amon tobin                                                                 0                 10                  0               0
amos                                                                      17                 10                  0             288
amtsbókasafnið á akureyri                                                  0                 10                  0               0
amtmaður                                                                  12                 10                  0             190
amtmannsstígur                                                             0                 10                  0               0
amt                                                                     1197                 10                  0           19914
amritsar                                                                   0                 10                  0               0
amhrán na bhfiann                                                          0                 10                  0               0
amharíska                                                                  7                 10                  0             112
american dad!                                                              0                 10                  0               0
american journal of philology                                              0                 10                  0               0
ameríkubikarinn                                                            0                 10                  0               0
amerískur fótbolti                                                         1                 10                  0              15
american kennel club                                                       0                 10                  0               0
ameríkudeildin (nfl)                                                       0                 10                  0               0
amen                                                                     273                 10                  0            4707
american idol                                                              0                 10                  0               0
amelía                                                                     0                 10                  0               0
ameríka                                                                    0                 10                  0               0
ambulance                                                                  0                 10                  0               0
ambrose bierce                                                             0                 10                  0               0
ammoníos                                                                   0                 10                  0               0
ammoníos sakkas                                                            0                 10                  0               0
ammoníos hermíasarson                                                      0                 10                  0               0
amman                                                                      6                 10                  0             106
ammassalik                                                                 0                 10                  0               0
ammoníos frá aþenu                                                         0                 10                  0               0
amíra                                                                      0                 10                  0               0
amúrhlébarði                                                               0                 10                  0               0
amdang                                                                     1                 10                  0              15
amd                                                                      165                 10                  0            2690
amstetten                                                                  0                 10                  0               0
amstel                                                                     0                 10                  0               0
amsterdam                                                                  0                 10                  0               0
amsterdam (bók)                                                            0                 10                  0               0
a-vítamín                                                                  0                 10                  0               0
aíníska                                                                    1                 10                  0              16
aínúmál                                                                    1                 10                  0              18
aímagíska                                                                  1                 10                  0              17
aímaríska                                                                  1                 10                  0              18
a (aðgreining)                                                             0                 10                  0               0
a portuguesa                                                               0                 10                  0               0
a priori                                                                   0                 10                  0               0
a treatise of human nature                                                 0                 10                  0               0
a rush of blood to the head                                                0                 10                  0               0
a new day at midnight                                                      0                 10                  0               0
a beautiful mind                                                           0                 10                  0               0
a momentary lapse of reason                                                0                 10                  0               0
a                                                                      20419                 10                  0          344189
a clockwork orange (bók)                                                   0                 10                  0               0
a clockwork orange                                                         0                 10                  0               0
a saucerful of secrets                                                     0                 10                  0               0
aó                                                                        53                 10                  0             918
advance australia fair                                                     0                 10                  0               0
ada lovelace                                                               0                 10                  0               0
adam smith                                                                 0                 10                  0               0
ada                                                                      532                 10                  0           10187
adam sandler                                                               0                 10                  0               0
adam curtis                                                                0                 10                  0               0
adam                                                                       8                 10                  0             123
adomoróbe-táknmál                                                          0                 10                  0               0
adobe systems                                                              0                 10                  0               0
adolf kirchhoff                                                            0                 10                  0               0
adolf                                                                      0                 10                  0               0
adolf hitler                                                               0                 10                  0               0
adobe photoshop                                                            0                 10                  0               0
adobe dreamweaver                                                          0                 10                  0               0
adolf eichmann                                                             0                 10                  0               0
adrían                                                                     8                 10                  0             171
adrarhásléttan                                                             0                 10                  0               0
adríahaf                                                                   0                 10                  0               0
adrien-marie legendre                                                      0                 10                  0               0
adrastos frá filippí                                                       0                 10                  0               0
adríel                                                                     0                 10                  0               0
adygeyska                                                                  1                 10                  0              24
adel                                                                      28                 10                  0             432
adeimantos                                                                 0                 10                  0               0
adelska                                                                    1                 10                  0              20
adenósínþrífosfat                                                          0                 10                  0               0
adela                                                                      0                 10                  0               0
adenflói                                                                   0                 10                  0               0
adelaide                                                                   0                 10                  0               0
admiral graf spee                                                          0                 10                  0               0
adíel                                                                      0                 10                  0               0
adólf                                                                      0                 10                  0               0
addi                                                                      19                 10                  0             343
addý                                                                       2                 10                  0              30
adda                                                                      29                 10                  0             480
addis ababa                                                                0                 10                  0               0
adsman                                                                     0                 10                  0               0
a. paul weber                                                              0                 10                  0               0
actavis                                                                    0                 10                  0               0
acre (fylki)                                                               0                 10                  0               0
acetýlsalicýlsýra                                                          0                 10                  0               0
ac milan                                                                   0                 10                  0               0
axgrös                                                                     3                 10                  0              53
axpuntgrös                                                                 4                 10                  0              67
axhnoðapuntur                                                              0                 10                  0               0
axlar-björn                                                                0                 10                  0               0
axel revold                                                                0                 10                  0               0
axelía                                                                     0                 10                  0               0
axelma                                                                     0                 10                  0               0
axel                                                                      10                 10                  0             153
axel oxenstierna                                                           0                 10                  0               0
axíokkos                                                                   0                 10                  0               0
aþena (gyðja)                                                              0                 10                  0               0
aþenodóros kordylíon                                                       0                 10                  0               0
aþenodóros frá kanönu                                                      0                 10                  0               0
aþena (mannsnafn)                                                          0                 10                  0               0
aþena                                                                      0                 10                  0               0
aþenajos                                                                   0                 10                  0               0
asvanstíflan                                                               0                 10                  0               0
asgabat                                                                    0                 10                  0               0
asksveppir                                                                 2                 10                  0              33
askúnska                                                                   1                 10                  0              15
askur yggdrasils                                                           0                 10                  0               0
askja (fjall)                                                              0                 10                  0               0
ask                                                                     1049                 10                  0           17037
askasleikir                                                                0                 10                  0               0
askur (ílát)                                                               0                 10                  0               0
askur og embla                                                             0                 10                  0               0
askja (mannsnafn)                                                          0                 10                  0               0
askja (aðgreining)                                                         0                 10                  0               0
askur (mannsnafn)                                                          0                 10                  0               0
askar capital                                                              0                 10                  0               0
askur                                                                     26                 10                  0             478
asperger heilkenni                                                         0                 10                  0               0
asp                                                                       99                 10                  0            1737
aspar                                                                      5                 10                  0              94
aspromonte                                                                 0                 10                  0               0
aspasía                                                                    0                 10                  0               0
aspasíus                                                                   0                 10                  0               0
asp.net                                                                    0                 10                  0               0
asperger                                                                   0                 10                  0               0
astara (aserbaídsjan)                                                      0                 10                  0               0
astrid lindgren                                                            0                 10                  0               0
astýanax                                                                   0                 10                  0               0
astrid belgíudrottning                                                     0                 10                  0               0
astekar                                                                    0                 10                  0               0
astat                                                                      1                 10                  0              17
aston villa                                                                0                 10                  0               0
astrid                                                                     1                 10                  0              16
astúríska                                                                  1                 10                  0              16
astana                                                                     0                 10                  0               0
astrópía                                                                   0                 10                  0               0
astmi                                                                      0                 10                  0               0
ashley tisdale                                                             0                 10                  0               0
asymmetric digital subscriber line                                         0                 10                  0               0
aserbaídsjanska stafrófið                                                  0                 10                  0               0
aserbaídsjanska                                                            2                 10                  0              32
aseton-peroxíð                                                             0                 10                  0               0
aserbaídsjan                                                               4                 10                  0              62
asmara                                                                     0                 10                  0               0
asíugullhnappur                                                            0                 10                  0               0
asía                                                                      28                 10                  0             487
asímál                                                                     1                 10                  0              18
asúnsjón                                                                   0                 10                  0               0
asóreyjar                                                                  0                 10                  0               0
ascraeusfjall                                                              0                 10                  0               0
assa                                                                     253                 10                  0            4767
assyríska                                                                  1                 10                  0              16
assameíska                                                                 1                 10                  0              17
assa (mannsnafn)                                                           0                 10                  0               0
gvam                                                                       2                 10                  0              34
gvatemalaborg                                                              0                 10                  0               0
gvatemala                                                                  0                 10                  0               0
gvadelúpeyjar                                                              0                 10                  0               0
gvæjana                                                                    0                 10                  0               0
gvæjanahálendið                                                            0                 10                  0               0
gvendarlaug í bjarnarfirði                                                 0                 10                  0               0
gavrilo princip                                                            0                 10                  0               0
gavin degraw                                                               0                 10                  0               0
gagnfræðaskóli                                                             2                 10                  0              29
gagntæk vörpun                                                             2                 10                  0              34
gagnastærð                                                                 1                 10                  0              16
gagnkynhneigð                                                              2                 10                  0              43
gagnatag                                                                   2                 10                  0              30
gagnagrunnur                                                               4                 10                  0              61
gaggenau (fyrirtæki)                                                       0                 10                  0               0
gagnauga (vefsíða)                                                         0                 10                  0               0
gagnrýni hreinnar skynsemi                                                 0                 10                  0               0
gagnhyggja                                                                 0                 10                  0               0
gagnagrind                                                                 9                 10                  0             166
gagnstrokka hreyfill                                                       0                 10                  0               0
gagnkvæmni                                                                 1                 10                  0              16
gagnsiðbótin                                                               0                 10                  0               0
gagnihessou                                                                0                 10                  0               0
gazprom                                                                    0                 10                  0               0
gaia                                                                       0                 10                  0               0
gaius maecenas                                                             0                 10                  0               0
gaius sempronius gracchus                                                  0                 10                  0               0
gapastokkur                                                                1                 10                  0              16
gaffalsegl                                                                13                 10                  0             196
gaflkæna                                                                   0                 10                  0               0
gao xingjian                                                               0                 10                  0               0
gaoming                                                                    0                 10                  0               0
gata                                                                     103                 10                  0            1624
gareth evans                                                               0                 10                  0               0
garðar (grænlandi)                                                         0                 10                  0               0
garrí kasparov                                                             0                 10                  0               0
garden state                                                               0                 10                  0               0
gargandi snilld                                                            0                 10                  0               0
garðar svavarson                                                           0                 10                  0               0
gary becker                                                                0                 10                  0               0
garðabær                                                                   0                 10                  0               0
garmisch-partenkirchen                                                     0                 10                  0               0
gary valentine                                                             0                 10                  0               0
garðahlynur                                                                0                 10                  0               0
garðar (mannsnafn)                                                         0                 10                  0               0
garðar olgeirsson - meira fjör                                             0                 10                  0               0
garðar                                                                    18                 10                  0             291
garnaveiki                                                                 2                 10                  0              35
garðar cortes                                                              0                 10                  0               0
garðar thór cortes                                                         0                 10                  0               0
garði                                                                     84                 10                  0            1389
garri                                                                      7                 10                  0             121
garibaldi                                                                  0                 10                  0               0
garageband                                                                 0                 10                  0               0
garðavegur                                                                 0                 10                  0               0
garðakornblóm                                                              0                 10                  0               0
garðskagi                                                                  0                 10                  0               0
garður                                                                   102                 10                  0            1687
garnaslagurinn                                                             0                 10                  0               0
garpur                                                                     4                 10                  0              60
garðastræti                                                                0                 10                  0               0
garðakál                                                                   6                 10                  0              95
gallerý fold                                                               0                 10                  0               0
galdramaður                                                                5                 10                  0              80
gallía                                                                     0                 10                  0               0
galdur (aðgreining)                                                        0                 10                  0               0
galdramál á íslandi                                                        0                 10                  0               0
galdur (mannsnafn)                                                         0                 10                  0               0
galdrastafur                                                               1                 10                  0              16
gallastríðið (caesar)                                                      0                 10                  0               0
gallín                                                                     4                 10                  0              66
gallblaðra                                                                 1                 10                  0              22
galaţi                                                                     0                 10                  0               0
gallastríðin                                                               0                 10                  0               0
galdramál                                                                  1                 10                  0              15
galíon                                                                     3                 10                  0              51
galdra-geiri                                                               0                 10                  0               0
galisía                                                                    0                 10                  0               0
galenos                                                                    0                 10                  0               0
galatía                                                                    0                 10                  0               0
galdra–loftur                                                              0                 10                  0               0
gallrás                                                                    1                 10                  0              15
galatasaray                                                                0                 10                  0               0
galdur                                                                     5                 10                  0              77
galdraskyttan                                                              0                 10                  0               0
galápagoseyjar                                                             0                 10                  0               0
galías                                                                     0                 10                  0               0
gall                                                                      51                 10                  0             819
galeiða                                                                    2                 10                  0              33
galíleó galílei                                                            0                 10                  0               0
gangandi íkorni                                                            0                 10                  0               0
ganaveldið                                                                 0                 10                  0               0
gana                                                                      32                 10                  0             614
ganýmedes (tungl)                                                          0                 10                  0               0
ganges                                                                     0                 10                  0               0
gabbró                                                                     2                 10                  0              34
gabriel metsu                                                              0                 10                  0               0
gabriel fauré                                                              0                 10                  0               0
gabríel                                                                    0                 10                  0               0
gabríel (mannsnafn)                                                        0                 10                  0               0
gaboróne                                                                   0                 10                  0               0
gabriel axel                                                               0                 10                  0               0
gabon                                                                      2                 10                  0              33
gabríela                                                                   0                 10                  0               0
gabríella                                                                  0                 10                  0               0
gabriel garcía márquez                                                     0                 10                  0               0
gabriel                                                                    0                 10                  0               0
gautviður                                                                  0                 10                  0               0
gaukshöfði                                                                 0                 10                  0               0
gaumljós                                                                   2                 10                  0              33
gautur                                                                     2                 10                  0              30
gauß-eyðing                                                                0                 10                  0               0
gauja                                                                      0                 10                  0               0
gautama búdda                                                              0                 10                  0               0
gaulverjabæjarfundur                                                       0                 10                  0               0
gautland                                                                   0                 10                  0               0
gaukfuglar                                                                 0                 10                  0               0
gaukur                                                                     3                 10                  0              47
gautelfur                                                                  0                 10                  0               0
gauß-jordan eyðing                                                         0                 10                  0               0
gautrekur                                                                  0                 10                  0               0
gauthildur                                                                 0                 10                  0               0
gautaborg                                                                  0                 10                  0               0
gaui                                                                       0                 10                  0               0
gaulverjabæjarhreppur                                                      0                 10                  0               0
gaupa                                                                      1                 10                  0              17
gauti                                                                      0                 10                  0               0
gautavík                                                                   0                 10                  0               0
gaumstol                                                                   1                 10                  0              43
gaullismi                                                                  0                 10                  0               0
game boy línan                                                             0                 10                  0               0
game & watch                                                               0                 10                  0               0
gammafallið                                                                2                 10                  0              35
gamlárskvöld                                                               4                 10                  0              62
gamalíel                                                                   0                 10                  0               0
gamelan                                                                    0                 10                  0               0
gamla ríkið                                                                0                 10                  0               0
gamma                                                                     11                 10                  0             178
gamecube                                                                   0                 10                  0               0
gambía                                                                     0                 10                  0               0
gammageisli                                                                1                 10                  0              16
gamanmynd                                                                 14                 10                  0             280
gamla mjólkursamlagið í borgarnesi                                         0                 10                  0               0
game boy                                                                   0                 10                  0               0
gamli vesturbærinn                                                         0                 10                  0               0
gamal abdel nasser                                                         0                 10                  0               0
gamla-hringbraut                                                           0                 10                  0               0
gamla bíó                                                                  1                 10                  0              16
gamli sáttmáli                                                             0                 10                  0               0
gaddjökull                                                                 0                 10                  0               0
gaddavír                                                                   2                 10                  0              38
gasaströndin                                                               0                 10                  0               0
gassendi                                                                   0                 10                  0               0
gasstöð reykjavíkur                                                        0                 10                  0               0
gas                                                                      993                 10                  0           18273
gasbíllinn                                                                 0                 10                  0               0
gasrisi                                                                    0                 10                  0               0
gægjuhneigð                                                                1                 10                  0              24
gæflaug                                                                    0                 10                  0               0
gæðingur                                                                   1                 10                  0              15
gæðamiðlun                                                                 0                 10                  0               0
gæsapartí                                                                  0                 10                  0               0
gæs                                                                       58                 10                  0             907
gæsalappir                                                                 1                 10                  0              18
gýgjar                                                                     0                 10                  0               0
gýmir                                                                      0                 10                  0               0
göksu                                                                      0                 10                  0               0
göfugu sannindin fjögur                                                    0                 10                  0               0
göran kropp                                                                0                 10                  0               0
giacomo puccini                                                            0                 10                  0               0
gianne albertoni                                                           0                 10                  0               0
gizur                                                                      0                 10                  0               0
gipsy kings                                                                0                 10                  0               0
gif                                                                     3197                 10                  0           45490
gifting                                                                   12                 10                  0             202
gifhorn                                                                    0                 10                  0               0
giovanni pierluigi da palestrina                                           0                 10                  0               0
giovanni spadolini                                                         0                 10                  0               0
giorgio de chirico                                                         0                 10                  0               0
giovanni giolitti                                                          0                 10                  0               0
giorgos seferis                                                            0                 10                  0               0
giovanni leone                                                             0                 10                  0               0
giovanni goria                                                             0                 10                  0               0
giordano bruno                                                             0                 10                  0               0
giovanni boccaccio                                                         0                 10                  0               0
girolamo cardano                                                           0                 10                  0               0
gillý                                                                      0                 10                  0               0
gilmar                                                                     0                 10                  0               0
gilbert ryle                                                               0                 10                  0               0
gilgamesharkviða                                                           0                 10                  0               0
gil (hvalvatnsfirði)                                                       0                 10                  0               0
gilslaug                                                                   0                 10                  0               0
gils                                                                      94                 10                  0            1519
gillette stadium                                                           0                 10                  0               0
giljaflækja                                                                0                 10                  0               0
gilgamesh                                                                  0                 10                  0               0
gillzenegger                                                               0                 10                  0               0
gild röksemdafærsla                                                        0                 10                  0               0
gildran (kvikmynd)                                                         0                 10                  0               0
gil eanes                                                                  0                 10                  0               0
gilitrutt (kvikmynd)                                                       0                 10                  0               0
gilbert harman                                                             0                 10                  0               0
gilbert                                                                    3                 10                  0              49
gilsfjörður                                                                0                 10                  0               0
giljan                                                                     0                 10                  0               0
gilbert murray                                                             0                 10                  0               0
giljagaur                                                                  0                 10                  0               0
ginseng                                                                    1                 10                  0              21
giuseppe pella                                                             0                 10                  0               0
giuliano amato                                                             0                 10                  0               0
giuseppe scarampella                                                       0                 10                  0               0
giuseppe rossi                                                             0                 10                  0               0
giuseppe ungaretti                                                         0                 10                  0               0
giuseppe verdi                                                             0                 10                  0               0
giulio andreotti                                                           0                 10                  0               0
gissur                                                                     0                 10                  0               0
gissur ísleifsson                                                          0                 10                  0               0
gissunn                                                                    0                 10                  0               0
gissur einarsson (biskup)                                                  0                 10                  0               0
gistilíf                                                                   0                 10                  0               0
gisela striker                                                             0                 10                  0               0
gisele bündchen                                                            0                 10                  0               0
gozewijn comhaer                                                           0                 10                  0               0
googol                                                                     2                 10                  0              36
google                                                                     1                 10                  0              15
googolplex                                                                 1                 10                  0              16
gottskálk keniksson                                                        0                 10                  0               0
gottskálk grimmi nikulásson                                                0                 10                  0               0
gotland                                                                    0                 10                  0               0
gottsveinn                                                                 0                 10                  0               0
gottskálk                                                                  0                 10                  0               0
gotti sigurðarson                                                          0                 10                  0               0
gottlob frege                                                              0                 10                  0               0
gottfried wilhelm von leibniz                                              0                 10                  0               0
gotneskur                                                                  1                 10                  0              18
gotlenska                                                                  3                 10                  0              45
gottfried helnwein                                                         0                 10                  0               0
gotar                                                                      3                 10                  0              54
goðmundur                                                                  0                 10                  0               0
goði                                                                      14                 10                  0             212
goðar                                                                      3                 10                  0              50
goðafoss                                                                   0                 10                  0               0
goðakyn                                                                    0                 10                  0               0
goðafræði                                                                147                 10                  0            2236
goð                                                                      221                 10                  0            3742
gormánuður                                                                 0                 10                  0               0
gorgías (platon)                                                           0                 10                  0               0
gordon brown                                                               0                 10                  0               0
gorgías                                                                    0                 10                  0               0
gorkúla                                                                    1                 10                  0              17
gormur gamli                                                               0                 10                  0               0
golfklúbburinn keilir                                                      0                 10                  0               0
golfklúbburinn kjölur                                                      0                 10                  0               0
golfklúbburinn vestarr                                                     0                 10                  0               0
golfklúbbur álftaness                                                      0                 10                  0               0
golfstraumurinn                                                            0                 10                  0               0
golfklúbbur                                                                7                 10                  0             111
golfvöllur                                                                 3                 10                  0              49
golgiflétta                                                                0                 10                  0               0
golfklúbbur reykjavíkur                                                    0                 10                  0               0
golf                                                                      16                 10                  0             256
golda meir                                                                 0                 10                  0               0
golíatbjalla                                                               0                 10                  0               0
gomlich áhrifin                                                            0                 10                  0               0
godspeed you black emperor!                                                0                 10                  0               0
god save the queen (sex pistols)                                           0                 10                  0               0
god save the queen                                                         0                 10                  0               0
godfrey harold hardy                                                       0                 10                  0               0
gosdrykkur                                                                 4                 10                  0              60
gt pro series                                                              0                 10                  0               0
grankell                                                                   0                 10                  0               0
grasbálkur                                                                 0                 10                  0               0
gramm (útgáfa)                                                             0                 10                  0               0
graham greene                                                              0                 10                  0               0
graubünden                                                                 0                 10                  0               0
gramm                                                                     27                 10                  0             502
grameðla                                                                   1                 10                  0              16
grasaætt                                                                  19                 10                  0             294
grallarinn                                                                 0                 10                  0               0
grafík                                                                    11                 10                  0             174
graz                                                                       0                 10                  0               0
grautaræxli                                                                0                 10                  0               0
grafarvogur                                                                0                 10                  0               0
granar                                                                     2                 10                  0              31
"""

word2vec = tabulated_data_to_list(word2vec_data)
tsdae = tabulated_data_to_list(tsdae_data)

# loop over each row and see if the first element is in the other list
merged = []
for row in word2vec:
    query = row[0]

    for tsdae_row in tsdae:
        if query == tsdae_row[0]:
            merged.append(row + tsdae_row[1:])


merged.pop(1)  # remove "---" row

df = pd.DataFrame(
    merged,
    index=None,
    columns=[
        "query",
        "ground truth",
        "semantic search (word2vec)",
        "common articles (word2vec)",
        "common links (word2vec)",
        "ground truth (tsdae)",
        "semantic search (tsdae)",
        "common articles (tsdae)",
        "common links (tsdae)",
    ],
)

df = df.drop(0)  # remove old header
df = df.drop("ground truth (tsdae)", axis=1)

# make sure all columns are numeric except the query column
df = df.apply(pd.to_numeric, errors="ignore")

# if the element in ground truth is equal to 0, then delete the row
df = df[df["ground truth"] != 0]


# Use DataFrame operations to calculate the counts
common_articles_tsdae = len(
    df[df["common articles (tsdae)"] < df["common articles (word2vec)"]]
)
common_links_tsdae = len(df[df["common links (tsdae)"] < df["common links (word2vec)"]])
common_articles_word2vec = len(
    df[df["common articles (tsdae)"] > df["common articles (word2vec)"]]
)
common_links_word2vec = len(
    df[df["common links (tsdae)"] > df["common links (word2vec)"]]
)

amount_of_zero_common_articles_tsdae = len(df[df["common articles (tsdae)"] == 0])
amount_of_zero_common_links_tsdae = len(df[df["common links (tsdae)"] == 0])
amount_of_zero_common_articles_word2vec = len(df[df["common articles (word2vec)"] == 0])
amount_of_zero_common_links_word2vec = len(df[df["common links (word2vec)"] == 0])

# Calculate the percentages
total_rows = len(df)
common_articles_tsdae_percentage = (
    len(df[df["common articles (tsdae)"] < df["common articles (word2vec)"]])
    / total_rows
    * 100
)
common_links_tsdae_percentage = (
    len(df[df["common links (tsdae)"] < df["common links (word2vec)"]])
    / total_rows
    * 100
)
common_articles_word2vec_percentage = (
    len(df[df["common articles (tsdae)"] > df["common articles (word2vec)"]])
    / total_rows
    * 100
)
common_links_word2vec_percentage = (
    len(df[df["common links (tsdae)"] > df["common links (word2vec)"]])
    / total_rows
    * 100
)


# Create a summary table
summary_table = [
    [
        "Common Articles",
        f"{common_articles_tsdae_percentage:.2f}%",
        f"{common_articles_word2vec_percentage:.2f}%",
    ],
    [
        "Common Links",
        f"{common_links_tsdae_percentage:.2f}%",
        f"{common_links_word2vec_percentage:.2f}%",
    ],
]

df.to_csv("merged.csv", index=False)

# Print the summary table using tabulate
print("processed data")
print(tabulate(summary_table, headers=["Metric", "TSDAE", "word2vec"]))


"""
Metric           TSDAE    word2vec
---------------  -------  ----------
Common Articles  0.00%    0.00%
Common Links     25.43%   6.91%
"""
