s="""ERHYAMCLAVLVEHEIEPFRFYRLRQDHWSGLANRKYMWQSMILFACRAQSRDVDPAKNY
FHFCRDHHEWPYKFQIICEASYDWQITVLIFQAWVMWMGDYIITPESNWNQDHYGNFGDN
KIMIDQRHHRHFIIVGLGPSMNIFRREVSIQMQWIDPMCFISWNICNLRNILPEFLCKIR
PHFCDRKDHFDRVNQQTQLAFTKFSGNYTECGPLAITQNSKEADQQGSNYEMTIMMMKDC
YILINFTGVPLCCRVNNMVDHHCMFATTAWRGIFSKPCAAFLGIETMEKTNLNTNTVQNT
EGPKRMHCMCDNWCGSQDTEESKTTRRGATYYTEGIKRAPCTFSTKMATLRIVIHQLMAG
NMAKRGMDTDRHWAVQCGKPIEFGCCHVYQRRAKYSNLSLWSFQNPNWNNNMVFKISMFC
HINTWHMATNKLYCIGQRHRVCGRCPCLIHEECVQDKLSPPLLGVVKYWMSHWESTYCCP
TKYFFVWRMNGLNMTAMTDVFNEPCIAAPQWIIREVSQHNNHLGAWIHYFFQDEWQGIIS
FFCIRFKFDQGRGKQEFVWEPTFYMTQCQYSIDMKWDGYGCFVLLESTYIAYMSMANNKR
NLQIMTDLNGTRLTMHSCWMNSFVLVTWLGDGKIVCDQNKTGDYTKHDYANRVLAMKKIG
MLSPRALYLGKGFWGEQDVACQHDHNPRHIMQKWFNTGCGCYIAPYCHRKCLMRPLWGPW
CKIELRQIQICGWALIDFWHKVGARVKWDENWNWYRYCHHRHPIPRKDWKRFYMVSVFAD
IEVCNVFVELQHWILREPAKYDAQIYDDQHDLNTDECYAADLTQSPNSTNSYMTALKMVE
ESIMAYTEKRCNKCNV"""
t="""ERHYAMCMNCLQMRKVAVLVEHEMKSDFCWRQDHWSGLANMSRDVDNYFHFCRDKHEWPF
KFQIDWQITVLCSHYMQSGMHYIITPFSNWGQDHYKNCGDNKIMIDHFIIVGLGPIMNIF
RREVSIQRQWIDPGKYSSVNMVFISWNICNLRNILPEKDFDEKDHFDRVMTCNLRQLASW
MNLNHNSKWNYEMTIMEPADLWSTGVPLCCRVNNMMGPGDHHWRLQVIFSKPCAAFYNKE
TMGDQTVQNTCMCEESKTTRRGATYYTEGIKRAPCTFSTKMATKWGTFDAGNMAKRGMDT
FDECHWNWKGGYQCKVQCGKPIEFGCCHVYQLWSFQNPNWNNNMVFIIRISMFCHIMTWH
MATNKAACIGCRHVKLSPPLLGVVKYWMNHTKQFNVYVMYYFIVWRMNGLNHTAMTDIAA
PQWIIREVSQHNNHLTAWIHIFKVNQRSTSQHIGRRKQEFVWEPTFYMTQLESTYIALPT
MSMANNKRNLQIMGTRLAMHSCWMNSIVLVTWLVPFWDGGDYTKHDYYATWGPHCLAMKK
IGMLSPRVLYLGKGFWGEQDVRCHMDHNPRPINFNRCWPFQKWFNTGQGCYCAPYCHRKC
LMRPLWGPWCKIECGWALIDFWHYFVGKHTFEGARVKWRYCSSKVFKGVHLKAKRFYMVS
VFARSRSEVCNVFSHDCMHMREPAKYDFYAHYCMIRSAKYIWMTLNTDECYAADHDRYEQ
SPNSTNSRCITCRKDEPWWSTHFQFYFVQYASDFESQSLCCPLRRCNNCNHHFP"""

s=s.replace('\n','')
t=t.replace('\n','')

M = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

for i in range(1,len(s) + 1):
    M[i][0] = i
for i in range(1, len(t) + 1):
    M[0][i] = i
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1] == t[j-1]:
            cost = 0
        else:
            cost = 1
        M[i][j] = min(M[i-1][j] + 1, M[i][j-1] + 1, M[i-1][j-1] + cost)

print(M[len(s)][len(t)])

s_prim = ''
t_prim = ''
i = len(s)
j = len(t)

#https://github.com/ssjunnebo/Rosalind/blob/master/edta/edta.py
def match(a,b):
    if a == b:
        return(0)
    return(1)

while i>0 and j> 0:
    if M[i][j] == M[i-1][j-1] + match(s[i-1], t[j-1]):
        s_prim += s[i-1]
        t_prim += t[j-1]
        i -= 1
        j -= 1
    elif i > 0 and M[i][j] == M[i-1][j] + 1:
        s_prim += s[i-1]
        t_prim += '-'
        i -= 1
    else:
        t_prim += t[j-1]
        s_prim += '-'
        j -= 1
print(s_prim[::-1])
print(t_prim[::-1])
