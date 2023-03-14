#-----------------------
def get_params(id):
    data = {
        'main15n': 'note,name,text1,text2,text3,text4',
        'main25n': 'note,name,text1,text2,text3,text4',
        'main45n': 'note,name,text1,text2,text3,text4',
        'main75n': 'note,name,text1,text2,text3,text4',
    }
    return data[id]

def get_params_i18n(id):
    data = {
        'main15n': 'note,name,text1,text2,text3,text4',
        'main25n': 'note,name,text1,text2,text3,text4',
        'main45n': 'note,name,text1,text2,text3,text4',
        'main75n': 'note,name,text1,text2,text3,text4',
    }
    return data[id]


def get_LAYOUT_index1():
    return [
    # pos=parent+sort, last_alias, active, locked, mark, mark_i18n, name, tags, note, content, params, params_i18n
    # ['', 'index0', 1, 1,'', '', ''],
    #---------------------------------------------
    ['_00', 'head', 1, 0,'', '', ''],
    ['_00_00', 'head0', 1, 0,'setAttr__tags', '', 'Favicon', 
                                    'href:../static/img/favicon.jpg/', '', '', 'tags', ''],
 
    ['_00_20', 'head2', 1, 0,'setAttr__tags', '', 'Theme',
                                    'href:https://www.w3schools.com/lib/w3-theme-cyan.css'], # theme
    ['_00_30', 'head3', 1, 0,'setAttr__tags', '', 'Font-awesome', ], # index.css
    ['_00_30', 'head3', 1, 0,'setAttr__tags', '', 'Font-awesome', ], # index.css
    ['_00_40', 'head4', 1, 0,'setAttr__tags', '', 'Index.css', 'href:../static/css/index0.css'], # index.js
    ['_00_50', 'head5', 1, 0,'setAttr__tags', '', 'Index.js', 'src:../static/js/index0.js'],

    #-------------------------------------------
    ['_10', 'header', 1, 0,'', '', ''], 
    ['_10_10', 'appbar', 1, 0,'setAttr__tags', '', 'Cabecera', 'class:w3-bar w3-white w3-card'],
    ['_10_10_10', 'logo', 1, 0,'setAttr__tags', '', 'Logo', 'href:/static/img/logo1.jpg/'], # tags='s
    ['_10_10_20', 'titulo', 1, 0,'', '', ''], # tags='s
    ['_10_10_20_10', 'titulo1', 1, 1,'innerHTML__name', 'innerHTML__name', 'ASESORIA LEGAL & FISCAL'], # tags='s
    ['_10_10_20_20', 'titulo2', 1, 1,'innerHTML__name', 'innerHTML__name', 'SEGUROS'], # tags='s
    ['_10_10_30', 'languages', 1, 1,'loadLanguages', '', 'es,en,fr,de,dk', ], # languages
    ['_10_10_30_10', 'lan-es', 1, 0,'loadLan', '', 'Español'],
    ['_10_10_30_20', 'lan-en', 1, 0,'loadLan', '', 'Inglés'],
    ['_10_10_30_30', 'lan-de', 1, 0,'loadLan', '', 'Alemán'],
    ['_10_10_30_40', 'lan-fr', 1, 0,'loadLan', '', 'Francés'],
    ['_10_10_30_50', 'lan-dk', 1, 0,'loadLan', '', 'Danés'],
    ['_10_10_30_60', 'lan-xx', 0, 0,'loadLan', '', 'xx'],
    ['_10_10_40', 'navbar', 1, 1,'', '', 'Barra de Menú'],
    ['_10_10_40_00', 'navbar0', 1, 1,'loadNavbar', 'innerHTML__name', 'Home',      'href:#main0','home',],
    ['_10_10_40_10', 'navbar1', 0, 1,'loadNavbar', 'innerHTML__name', 'Nosotros',  'href:#main1','cubes'],
    ['_10_10_40_20', 'navbar2', 1, 1,'loadNavbar', 'innerHTML__name', 'Servicios', 'href:#main2','th'],
    ['_10_10_40_30', 'navbar3', 1, 1,'loadNavbar', 'innerHTML__name', 'Costa Tropical', 'href:#main3','map-signs'],
    ['_10_10_40_40', 'navbar4', 1, 0,'loadNavbar', 'innerHTML__name', 'navbar4',   'href:#main4','th'],
    ['_10_10_40_50', 'navbar5', 1, 0,'loadNavbar', 'innerHTML__name', 'navbar5',   'href:#main5','th-large'],
    ['_10_10_40_60', 'navbar6', 1, 0,'loadNavbar', 'innerHTML__name', 'navbar6',   'href:#main6','th'],
    ['_10_10_40_70', 'navbar7', 1, 1,'loadNavbar', 'innerHTML__name', 'Equipo',    'href:#main7','users'],
    ['_10_10_40_80', 'navbar8', 1, 1,'loadNavbar', 'innerHTML__name', 'Contacto',  'href:#main8','envelope'],
    ['_10_10_40_90', 'navbar9', 1, 0,'loadNavbar', 'innerHTML__name', 'navbar9',   'href:#main9','th'],
    #-------------------------------------------------
    ['_10_20', 'sidebar', 1, 1,'', '', 'Menú lateral'],

    ['_10_20_00', 'sidebar0', 1, 1,'loadSidebar', 'innerHTML__name', 'Home',      'href:#main0','home'],
    ['_10_20_10', 'sidebar1', 1, 1,'loadSidebar', 'innerHTML__name', 'Nosotros',  'href:#main1','cubes'],
    ['_10_20_20', 'sidebar2', 1, 1,'loadSidebar', 'innerHTML__name', 'Servicios', 'href:#main2','th'],
    ['_10_20_30', 'sidebar3', 1, 1,'loadSidebar', 'innerHTML__name', 'Costa Tropical', 'href:#main3','map-signs'],
    ['_10_20_40', 'sidebar4', 1, 0,'loadSidebar', 'innerHTML__name', 'sidebar4',  'href:#main4','th'],
    ['_10_20_50', 'sidebar5', 1, 0,'loadSidebar', 'innerHTML__name', 'sidebar5',  'href:#main5','th'],
    ['_10_20_60', 'sidebar6', 1, 0,'loadSidebar', 'innerHTML__name', 'sidebar6',  'href:#main6','th'],
    ['_10_20_70', 'sidebar7', 1, 1,'loadSidebar', 'innerHTML__name', 'Equipo',    'href:#main7','users'],
    ['_10_20_80', 'sidebar8', 1, 1,'loadSidebar', 'innerHTML__name', 'Contacto',  'href:#main8','envelope'],
    ['_10_20_90', 'sidebar9', 0, 0,'loadSidebar', 'innerHTML__name', 'sidebar9',  'href:#main9','th'],
    ['_10_20_X0', 'sidebarx', 1, 1,'', 'innerHTML__name', 'Cerrar', ''],
    #===================================
    ['_20', 'main', 1, 1,'', '', ''],
    #--------------------------------
    ['_20_00', 'main0', 1, 1,'', '', 'Home'],
    ['_20_00_10', 'main01', 1, 1,'loadImageName', '', '../static/img/fachada1.jpeg'],
    ['_20_00_20', 'main02', 1, 1,'loadImageName', '', '../static/img/fachada2.jpeg'],
    ['_20_00_30', 'main03', 1, 1,'loadImageName', '', '../static/img/fachada3.jpeg'],
    ['_20_00_40', 'main04', 0, 1,'loadImageName', '', '../static/img/fachada1.jpeg'],
    ['_20_00_50', 'main05', 0, 1,'loadImageName', '', '../static/img/fachada2.jpeg'],
    ['_20_00_60', 'main06', 0, 1,'loadImageName', '', '../static/img/fachada3.jpeg'],
    ['_20_00_70', 'main07', 0, 1,'loadImageName', '', '../static/img/colores.jpeg'],
    ['_20_00_80', 'main08', 0, 1,'loadImageName', '', '../static/img/fachada2.jpeg'],
    ['_20_00_90', 'main09', 0, 1,'loadImageName', '', '../static/img/fachada3.jpeg'],
    #=============================================
    ['_20_10', 'main1', 1, 1,'', '', ''], #name, content
    ['_20_10_00', 'main10', 1, 1, 'loadCard1', 'loadCard1', 'Nosotros', '', '', 'Nosotros: content',
                                'name,content', 'name,content'],

    ['_20_10_50', 'main15', 0, 0,'', '', 'Valores'],
    ['_20_10_50_10', 'main151', 1, 1,'loadCard2', 'loadCard2', 'Confianza', 'fa-desktop', '', '', 
                        get_params('main15n')],
    ['_20_10_50_20', 'main152', 1, 1,'loadCard2', 'loadCard2', 'Pasion', 'fa-heart', '', '', 
                        get_params('main15n')],
    ['_20_10_50_30', 'main153', 1, 1,'loadCard2', 'loadCard2', 'Calidad', 'fa-diamond','', '', 
                        get_params('main15n')],
    ['_20_10_50_40', 'main154', 1, 1,'loadCard2', 'loadCard2', 'Ética', 'fa-cog', '', '', 
                        get_params('main15n')],
    #================================================================
    ['_20_20', 'main2', 1, 1,'', '', ''],
    ['_20_20_00', 'main20', 1, 1,'loadCard1', 'loadCard1', 'Servicios', '', '', 'Servicios: content',
                                'name,content', 'name,content'],
    ['_20_20_50', 'main25', 1, 1,'', '', 'lista hijos-desplegar'],
    ['_20_20_50_10', 'main251', 1, 1,'loadCard2', 'loadCard2', 'Asesoría Legal', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_20', 'main252', 1, 1,'loadCard2', 'loadCard2', 'Fiscal y Contabilidad', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_30', 'main253', 1, 1,'loadCard2', 'loadCard2', 'Seguros', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_40', 'main254', 1, 1,'loadCard2', 'loadCard2', 'ECCO', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_50', 'main255', 1, 1,'loadCard2', 'loadCard2', 'Costa Tropical', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_60', 'main256', 1, 1,'loadCard2', 'loadCard2', 'Medio Ambiente', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_70', 'main257', 0, 1,'loadCard2', 'loadCard2', 'Inmobiliaria', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_80', 'main258', 1, 1,'loadCard2', 'loadCard2', 'Otros Servicios', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_90', 'main259', 0, 1,'loadCard2', 'loadCard2', 'Servicios 9', '', '', '',
                        get_params('main25n')],
    ['_20_20_50_XX', 'main25x', 0, 0,'', 'loadCard3', 'Servicio Desplegado', '', '', '',
                        get_params('main25n')],
    #====================================================
    ['_20_30', 'main3', 1, 1,'', '', 'main3'],
    #======================================================
    ['_20_40', 'main4', 1, 1,'', '', ''],
    ['_20_40_00', 'main40', 1, 1,'loadCard1', 'loadCard1', 'Costa Tropical', '', '', 'Costa Tropical: content',
                                'name,content', 'name,content'],
    # ['_20_40_10', 'main41', 1, 1,'', 'innerHTML__name', 'Titulo'],
    # ['_20_40_20', 'main42', 1, 1,'', 'innerHTML__name', 'Descripción'],
    # ['_20_40_30', 'main43', 0, 1,'', 'innerHTML__name', 'texto3-simple'],
    # ['_20_40_40', 'main44', 0, 1,'', 'innerHTML__name', 'texto4-richt'],
    ['_20_40_50', 'main45', 1, 1,'', '', 'lista hijos-desplegar'],
    ['_20_40_50_10', 'main451', 1, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_20', 'main452', 1, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_30', 'main453', 1, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_40', 'main454', 1, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_50', 'main455', 1, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_60', 'main456', 1, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_70', 'main457', 0, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_80', 'main458', 0, 1,'loadCard2', 'loadCard2', '', '', '', '',
                        get_params('main45n')],
    ['_20_40_50_XX', 'main45x', 0, 1,'', 'loadCard3', 'Costa Tropical desplegado'],
    #=================================================
    ['_20_50', 'main5', 0, 1,'', '', 'Referencias'],

    #-=================================================
    ['_20_60', 'main6', 0, 1,'', '', 'main6'],
 
    #=========================================================
    ['_20_70', 'main7', 0, 1,'', '', ''],
    ['_20_70_00', 'main70', 1, 1,'loadCard1', 'loadCard1', 'Equipo', '', '', 'Equipo: content',
                                'name,content', 'name,content'],  
    # ['_20_70_10', 'main71', 1, 1,'', 'innerHTML__name', 'EL EQUIPO'],
    # ['_20_70_20', 'main72', 1, 1,'', 'innerHTML__name', 'Quienes formamos esta empresa'],
    # ['_20_70_30', 'main73', 0, 1,'', 'innerHTML__name', 'texto3-simple'],
    # ['_20_70_40', 'main74', 0, 1,'', 'innerHTML__name', 'texto4-richt'],
    ['_20_70_50', 'main75', 1, 1,'', '', '', '', '', '',
        get_params('main75n')],
    ['_20_70_50_10', 'main751', 1, 1,'loadCard2Team', 'loadCard2Team', 'Andrea', '', '/static/img/equipo1-andrea.jpeg','',
                     get_params('main75n')], # cargo, descripción
    ['_20_70_50_20', 'main752', 1, 1,'loadCard2Team', 'loadCard2Team', 'Fran','','/static/img/equipo2-fran.jpeg','',
                     get_params('main75n')],
    ['_20_70_50_30', 'main753', 1, 1,'loadCard2Team', 'loadCard2Team', 'Pilar', '','/static/img/equipo3-pilar.jpeg','',
                     get_params('main75n')],
    ['_20_70_50_40', 'main754', 1, 1,'loadCard2Team', 'loadCard2Team', 'Samuel', '','/static/img/equipo4-samuel.jpeg','',
                     get_params('main75n')],
    ['_20_70_50_50', 'main755', 1, 1,'loadCard2Team', 'loadCard2Team', 'Monique', '','/static/img/equipo5-monique.jpeg','',
                     get_params('main75n')],
    ['_20_70_50_60', 'main756', 1, 1,'loadCard2Team', 'loadCard2Team', 'Issa', '','/static/img/equipo6-issa.jpeg','',
                     get_params('main75n')],
    ['_20_70_50_70', 'main757', 1, 0,'loadCard2Team', 'loadCard2Team', 'Esperanza', '','/static/img/equipo7-esperanza.jpeg','',
                     get_params('main75n')],
    ['_20_70_50_80', 'main758', 0, 0,'loadCard2Team', 'loadCard2Team', 'main758', '','','',
                     get_params('main75n')],
    ['_20_70_50_90', 'main759', 0, 0,'loadCard2Team', 'loadCard2Team', 'main759', '','','',
                     get_params('main75n')],
    ['_20_70_50_XX', 'main75x', 0, 0,'', 'loadCard3', 'Equipo deplegado', '','','',],
    #-----------------------------------------
    ['_20_80', 'main8', 1, 1, '', '', ''],
    ['_20_80_00', 'main80', 1, 1,'loadCard1', 'loadCard1', 'Contacto' '', '', 'Contacto: content',
                                'name,content', 'name,content'],
    # ['_20_80_10', 'main81', 1, 1,'', 'innerHTML__name', 'Contactanos'],
    # ['_20_80_20', 'main82', 1, 1,'', 'innerHTML__name', 'Cómo puedes ponerte en contacto con nosotros'],
    ['_20_80_30', 'main83', 1, 0,'', '', 'Logo'],
    ['_20_80_40', 'main84', 1, 0,'', '', 'Dirección'],
    ['_20_80_50', 'main85', 1, 0,'', '', 'Telefono'],
    ['_20_80_60', 'main86', 1, 0,'', '', 'Email'],
    ['_20_80_70', 'main87', 1, 0,'', '', 'Ubicación en google map'],
    ['_20_80_80', 'main88', 0, 0,'', '', 'Contacto 8'],
    ['_20_80_90', 'main89', 0, 0,'', '', 'Contacto 9'],
    #--------------------------------------------------------
    ['_20_90', 'main9', 0, 0,'', 'innerHTML__name', 'main9'],
    #=========================================
    ['_30', 'footer', 1, 0,'', '', 'Pie'],
    ['_30_10', 'footer1', 1, 0,'', 'innerHTML__name', 'Volver a Home'],
    ['_30_20', 'footer2', 1, 0,'', '', 'Políticas'],
    ['_30_20_10', 'footer21', 1, 0,'', 'innerHTML__name', 'Aviso legal'],
    ['_30_20_20', 'footer22', 1, 0,'', 'innerHTML__name', 'Política de Privacidad'],
    ['_30_20_30', 'footer23', 1, 0,'', 'innerHTML__name', 'Política de Cookies'],
    ['_30_30', 'footer3', 1, 0,'', '', 'Redes sociales'],
    ['_30_30_10', 'footer31', 1, 0,'', '', 'facebook'],
    ['_30_30_20', 'footer32', 1, 0,'', '', 'twiter'],
    ['_30_30_30', 'footer33', 1, 0,'', '', 'linkedin'],
    ['_30_04', 'footer4', 1, 0,'', '', 'Copyright'],
    ['_30_05', 'footer5', 1, 0,'', '', 'footer5'],

    ]

