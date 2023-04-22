

def sureler(string):
    string = string.split('<option value=')
    listofsureler = []
    for sure in string:
        first_ind = sure.rfind(' ')
        last_ind = sure.rfind('(')
        sure = sure[first_ind+1:last_ind].lower()
        listofsureler.append(sure)
    return listofsureler

def characterfixer(L):
    wrongL = ['â','û','ü',"'",'î','i̇',"’"]
    correct = ['a','u','u','','i','i','']
    L1 = []
    for sure in L:
        for char in sure:
            if char in wrongL:
                ind = wrongL.index(char)
                sure = sure.replace(char,correct[ind])
        if 'i̇' in sure:
            sure = sure.replace('i̇','i')
        L1.append(sure)
    return L1

Ssureler = '<option value="1"> Fâtiha(1/7)</option><option selected="" value="2"> Bakara(2/286)</option><option value="3"> Âl-i İmrân(3/200)</option><option value="4"> Nisâ(4/176)</option><option value="5"> Mâide(5/120)</option><option value="6"> En’âm(6/165)</option><option value="7"> A’râf(7/206)</option><option value="8"> Enfâl(8/75)</option><option value="9"> Tevbe(9/129)</option><option value="10"> Yûnus(10/109)</option><option value="11"> Hûd(11/123)</option><option value="12"> Yûsuf(12/111)</option><option value="13"> Ra’d(13/43)</option><option value="14"> İbrahim(14/52)</option><option value="15"> Hicr(15/99)</option><option value="16"> Nahl(16/128)</option><option value="17"> İsrâ(17/111)</option><option value="18"> Kehf(18/110)</option><option value="19"> Meryem(19/98)</option><option value="20"> Tâ-Hâ(20/135)</option><option value="21"> Enbiyâ(21/112)</option><option value="22"> Hac(22/78)</option><option value="23"> Mü’minûn(23/118)</option><option value="24"> Nûr(24/64)</option><option value="25"> Furkân(25/77)</option><option value="26"> Şu’arâ(26/227)</option><option value="27"> Neml(27/93)</option><option value="28"> Kasas(28/88)</option><option value="29"> Ankebût(29/69)</option><option value="30"> Rûm(30/60)</option><option value="31"> Lokman(31/34)</option><option value="32"> Secde(32/30)</option><option value="33"> Ahzâb(33/73)</option><option value="34"> Sebe’(34/54)</option><option value="35"> Fâtır(35/45)</option><option value="36"> Yâsîn(36/83)</option><option value="37"> Sâffât(37/182)</option><option value="38"> Sâd(38/88)</option><option value="39"> Zümer(39/75)</option><option value="40"> Mü’min(40/85)</option><option value="41"> Fussilet(41/54)</option><option value="42"> Şûrâ(42/53)</option><option value="43"> Zuhruf(43/89)</option><option value="44"> Duhân(44/59)</option><option value="45"> Câsiye(45/37)</option><option value="46"> Ahkâf(46/35)</option><option value="47"> Muhammed(47/38)</option><option value="48"> Fetih(48/29)</option><option value="49"> Hucurât(49/18)</option><option value="50"> Kâf(50/45)</option><option value="51"> Zâriyât(51/60)</option><option value="52"> Tûr(52/49)</option><option value="53"> Necm(53/62)</option><option value="54"> Kamer(54/55)</option><option value="55"> Rahmân(55/78)</option><option value="56"> Vâkı’a(56/96)</option><option value="57"> Hadîd(57/29)</option><option value="58"> Mücâdele(58/22)</option><option value="59"> Haşr(59/24)</option><option value="60"> Mümtehine(60/13)</option><option value="61"> Saff(61/14)</option><option value="62"> Cum’a(62/11)</option><option value="63"> Münâfikûn(63/11)</option><option value="64"> Teğâbun(64/18)</option><option value="65"> Talâk(65/12)</option><option value="66"> Tahrîm(66/12)</option><option value="67"> Mülk(67/30)</option><option value="68"> Kalem(68/52)</option><option value="69"> Hâkka(69/52)</option><option value="70"> Me’âric(70/44)</option><option value="71"> Nûh(71/28)</option><option value="72"> Cin(72/28)</option><option value="73"> Müzzemmil(73/20)</option><option value="74"> Müddessir(74/56)</option><option value="75"> Kıyâme(75/40)</option><option value="76"> İnsan(76/31)</option><option value="77"> Mürselât(77/50)</option><option value="78"> Nebe’(78/40)</option><option value="79"> Nâzi’ât(79/46)</option><option value="80"> Abese(80/42)</option><option value="81"> Tekvîr(81/29)</option><option value="82"> İnfitâr(82/19)</option><option value="83"> Mutaffifîn(83/36)</option><option value="84"> İnşikâk(84/25)</option><option value="85"> Bürûc(85/22)</option><option value="86"> Târık(86/17)</option><option value="87"> A’lâ(87/19)</option><option value="88"> Gâşiye(88/26)</option><option value="89"> Fecr(89/30)</option><option value="90"> Beled(90/20)</option><option value="91"> Şems(91/15)</option><option value="92"> Leyl(92/21)</option><option value="93"> Duhâ(93/11)</option><option value="94"> İnşirâh(94/8)</option><option value="95"> Tîn(95/8)</option><option value="96"> Alak(96/19)</option><option value="97"> Kadr(97/5)</option><option value="98"> Beyyine(98/8)</option><option value="99"> Zilzâl(99/8)</option><option value="100"> Âdiyât(100/11)</option><option value="101"> Kâri’a(101/11)</option><option value="102"> Tekâsür(102/8)</option><option value="103"> Asr(103/3)</option><option value="104"> Hümeze(104/9)</option><option value="105"> Fil(105/5)</option><option value="106"> Kureyş(106/4)</option><option value="107"> Mâ’ûn(107/7)</option><option value="108"> Kevser(108/3)</option><option value="109"> Kâfirûn(109/6)</option><option value="110"> Nasr(110/3)</option><option value="111"> Tebbet(111/5)</option><option value="112"> İhlâs(112/4)</option><option value="113"> Felâk(113/5)</option><option value="114"> Nâs(114/6)</option>'
L1 = sureler(Ssureler)
L1 = characterfixer(L1)
print(L1)
"""
class CEVIRI:
    list = L1
    def __init__(self, name, translation):
        self.name = name
        self.translation = translation

sureler = {'fatiha':'1',
               'bakara':'2',
               'al-i imran':'3',
               'nisa':'4',
               'maide':'5',
               "en'am":'6',
               "a'raf":'7',
               'enfal':'8',
               "tevbe":'9',
               'yunus':'10',
               'hud':'11',
               'yusuf':'12',
               "ra'd":'13',
               'ibrahim':'14',
               'hicr':'15',
               'nahl':'16',
               'isra':'17',
               'kehf':'18',
               'meryem':'19',
               'ta-ha':'20',
               'enbiya':'21',
               'hac':'22',
               }
"""
