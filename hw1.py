from matplotlib import pyplot as plt
crpyto = 'APS ZU BMS THAAMT KB SOP CHAAPJ MQ LPUWHKX. K UHJ SM JMZ SMLHJ VJ QXKPBLU -- UM PCPB SOMZDO TP QHEP SOP LKQQKEZASKPU MQ SMLHJ HBL SMVMXXMT, K USKAA OHCP H LXPHV. KS KU H LXPHV LPPWAJ XMMSPL KB SOP HVPXKEHB LXPHV. K OHCP H LXPHV SOHS MBP LHJ SOKU BHSKMB TKAA XKUP ZW HBL AKCP MZS SOP SXZP VPHBKBD MQ KSU EXPPL: "TP OMAL SOPUP SXZSOU SM IP UPAQ-PCKLPBS, SOHS HAA VPB HXP EXPHSPL PGZHA." K OHCP H LXPHV SOHS MBP LHJ MB SOP XPL OKAAU MQ DPMXDKH SOP UMBU MQ QMXVPX UAHCPU HBL SOP UMBU MQ QMXVPX UAHCP MTBPXU TKAA IP HIAP SM UKS LMTB SMDPSOPX HS SOP SHIAP MQ IXMSOPXOMML. K OHCP H LXPHV SOHS MBP LHJ PCPB SOP USHSP MQ VKUUKUUKWWK, H USHSP UTPASPXKBD TKSO SOP OPHS MQ KBFZUSKEP, UTPASPXKBD TKSO SOP OPHS MQ MWWXPUUKMB, TKAA IP SXHBUQMXVPL KBSM HB MHUKU MQ QXPPLMV HBL FZUSKEP. K OHCP H LXPHV SOHS VJ QMZX AKSSAP EOKALXPB TKAA MBP LHJ AKCP KB H BHSKMB TOPXP SOPJ TKAA BMS IP FZLDPL IJ SOP EMAMX MQ SOPKX URKB IZS IJ SOP EMBSPBS MQ SOPKX EOHXHESPX. K OHCP H LXPHV SMLHJ. K OHCP H LXPHV SOHS MBP LHJ LMTB KB HAHIHVH, TKSO KSU CKEKMZU XHEKUSU, TKSO KSU DMCPXBMX OHCKBD OKU AKWU LXKWWKBD TKSO SOP TMXLU MQ KBSPXWMUKSKMB HBL BZAAKQKEHSKMB -- MBP LHJ XKDOS SOPXP KB HAHIHVH AKSSAP IAHER IMJU HBL IAHER DKXAU TKAA IP HIAP SM FMKB OHBLU TKSO AKSSAP TOKSP IMJU HBL TOKSP DKXAU HU UKUSPXU HBL IXMSOPXU. K OHCP H LXPHV SMLHJ. K OHCP H LXPHV SOHS MBP LHJ PCPXJ CHAAPJ UOHAA IP PNHASPL, HBL PCPXJ OKAA HBL VMZBSHKB UOHAA IP VHLP AMT, SOP XMZDO WAHEPU TKAA IP VHLP WAHKB, HBL SOP EXMMRPL WAHEPU TKAA IP VHLP USXHKDOS, HBL SOP DAMXJ MQ SOP AMXL UOHAA IP XPCPHAPL HBL HAA QAPUO UOHAA UPP KS SMDPSOPX.'

def frequency(inputString): # 문자열의 구성 알파벳들의 빈도를 체크할 함수
    elements = sorted(set(list(inputString))) # 입력 문자열의 구성 문자 리스트 선언
    alphabets = {} # 빈도수를 체크할 딕셔너리
    for ch in elements:
        if ch ==' ': # 띄어쓰기 무시
            continue
        alphabets[ch] = 0 # 딕셔너리에 해당 항목 추가
    for ch in inputString: # 입력 문자열을 한글자씩 읽어들임
        if ch==' ':
            continue
        alphabets[ch] = alphabets.get(ch)+1 # 딕셔너리의 해당 문자 값을 1씩 증가
    plt.bar(alphabets.keys(),alphabets.values()) # 딕셔너리의 키값을 x 축, 빈도수를 y축으로 그래프 생성
    plt.show() # 그래프 표시
frequency(crpyto)

def replaceString(inputString): # 입력 문자열의 특정 문자를 다른 문자로 바꿔쓰는 함수
    stringList = list(inputString) # 입력 문자열을 리스트로 관리
    # Key Table을 딕셔너리로 정의
    translation = {'A':'L','S':'T','O':'H','P':'E','H':'A','K':'I','Q':'F','B':'N','L':'D','C':'V','M':'O','Z':'U','D':'G','T':'W','U':'S','J':'Y','X':'R','E':'C','V':'M','W':'P','I':'B',
    'F':'J','R':'K','G':'Q','Y':'X','N':'Z'}
    for i in range(len(stringList)): #stringList의 값들을 하나씩 읽어들임 = 입력 문자열을 하나씩 읽어들임
        if stringList[i] in translation.keys(): # 특수문자를 제외한 알파벳들을 대상으로 문자를 변환
            stringList[i] = translation.get(stringList[i])
    return ''.join(stringList) #stringList를 문자열의 형태로 반환
print(replaceString(crpyto))

def pattern(inputString): # 특정 길이의 반복되는 문자열의 빈도수를 알아낼때 사용하는 함수
    elements = sorted(inputString.split(' ')) # 입력 문자열을 공백을 기준으로 나눠서 리스트로 반환 = 단어들로 이루어진 리스트
    alphabets = {} # 특정 문자열의 빈도수를 체크할 딕셔너리 변수 선언
    for word in elements: # 리스트의 원소(단어)를 하나씩 읽어들임
        if len(word) != 3: # 특정 길이가 아니면 넘어감 -> if문의 조건을 바꿈으로써 확인하고 싶은 문자열의 길이를 조정 가능
            continue
        alphabets[word] = 0 # 딕셔너리 변수에 해당 key 값 추가와 동시에 0으로 초기화
    for word in elements: # 
        if len(word) != 3:
            continue
        alphabets[word] = alphabets.get(word)+1 # 해당 단어의 빈도수를 1씩 증가
    plt.bar(alphabets.keys(),alphabets.values()) # x축은 단어, y축은 그 빈도수로 그래프 생성
    plt.show() # 그래프 표시
pattern(crpyto)