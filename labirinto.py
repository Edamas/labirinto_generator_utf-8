 direita = {
'∙': ' ',
'‗˾__':'____˾‗_‗',
'˭‾':'‾˭',
'—―':'―—―═╕╗╛╝╡╣╤╦╧╩╪╬',
' ▐▌▀▄■╿╽╻╹╸╷╵╴╯╮╢╣╡╝╜╛╗╖╕┒┦┨┋┩┆┪║┛┙┫┐┑┧╎╏┓┃┊┚┘┇┤│┥ ': '    ┣╺╚╹├╙┋┆║╵╘┖╔╒╻┠▐╰╠╶╞┢╓╎╏┃╷╭╽┡╟ ╿┊┟┇┞│└',
'╾╶—―╰╭╫╨╥╟╙╓─┄┈┎┌└┖├┞┟┠┬┭┰┱┴┵┸┹┼┽╀╁╂╃╓╙╟╢╤╥╨╫╅╉╌┌┎': '┄─┈┐┒┘┚┤┦┧┨┬┮┰┲┴┶┸■┺┼┾╀╁╂╄╆╊╌╢╥╨╫╮╯╮╯╮╯╴╴╴╴╴╴╴╴╴╴╴╺╼╽╾╿╖╜╢╥╨╫', 
'╼╺━┅┉┍┏┕┗┝┡┢┣┮┯┲┳┶┷┺┻┾┿╄╆╇╈╊╋╍┍┏┕┗┝':                '━┅┉┑┓┙┛┥┩┪┫┭┯┱┳┵┷▌▀┹┻┽┿╃╅╇╈╉╋╍╸╾╸╸╸╸╸╸',
'╬╪╩╧╦╤╠╞╚╘╔═╒':                                      '═—―═╕╗╛╝╡╣╤╦╧╩╪╬█▄'
}
acima = {
'∙': ' ',
' ▀■╾╼╺╹╸╶╵╴╰╯╨╧╩╝╛╧╜╚╙╘═╍ ╌┉┈┴┻┺┹┸┷┵┶┕┛┚┙┘┖┗┄┅─└‾━˾‗―—_˭':'            _˭˾—―—―—―‗‾─━┄┅┈┉┌┍┎┏┐┑┒┓┬┭┮┯┰┱┲┳╌╍═╒╓╔╕╖╗╤╥╦╭╮╭╮╭╮╭╮╭╮╴╶╴╶╴╶╷╸╺╻╼╽╾▄',
'▌▐╿╷╮╭╪╤╡╞╕╒╎╇╄╃╀┿┾┼┽┬┭┮┯┩┦┥┤┡├┝┞│┆┊┌┍┐┑'				:'││┊┊└┕┘┘┘┙├┝┟┢┤┥┧┪┴┵┶┷┼┽┾┿╁╅╆╈╎╛╞╡╧╪╯╰╯╰╯╰╯╰╯╰╯╰╵╵╵╵╵╵╵╵╵╵╵╵╵╵╵╽▌▐',
'▄╽╻╏╋╊╉╈╆╅╁╂┳┲┱┰┫┪┨┧┣┢┟┠┃┇┋┎┏┓┒'						:'┃┋┖┗┚┛┞┠┡┣┦┨┩┫┸┹┺┻╀╂╃╄╇╉╊╋╏╹╹╹╹╹╹╹╹╹╹╹╹╹╹╹╹╹╹╹╿',
'█╬╫╦╥╣╢╠╟╗╖║╔╓'										:'║╙╙╙╙╚╜╜╜╜╝╟╟╟╠╢╢╢╣╨╨╨╨╨╨╩╫╬█'}

novo = random.choice(list(direita.keys()))
linhas = []
linha = ''
novo = ' '
for i in range(180):
    alternativas = ' '
    if novo not in list(direita.keys()):
        alternativas += random.choice(list(acima.keys()))
    else:
        alternativas += random.choice(direita[novo])
    novo = random.choice(alternativas)
    linha += novo
linhas.append(linha)
for j in range(100):
    linha = ''
    for i in linhas[-1]:
        for x in list(direita.keys()):
            if novo in x:
                listanovo = x
                altdir = direita[x]
        alternativas = ''
        for x in list(acima.keys()):
            if i in x:
                for j in list(acima[x]):
                    if j in altdir:
                        listaj = x
                        alternativas += j
        if alternativas:
            novo = random.choice(alternativas)
        else:
            novo = random.choice(listanovo + listaj)
        linha += novo
    linhas.append(linha)
for i in linhas:
    print(i)