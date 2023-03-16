// window.onload = iniciar();

window.onload = iniciar();
function iniciar() {
    // TODO! obtener del env
    const serverUrl= `${window.location.href}asinex`
    console.log(serverUrl);
    localStorage.serverUrl = serverUrl;
    localStorage.rootAlias = "index0"
    localStorage.lan = 'es'
    localStorage.card3 = ''
    
    manageLayout("layouts",
        `&locked=1&internal=1&root_alias=${localStorage.rootAlias}`,
        'last_alias');
    manageLayout("layouti18ns",
        `&locked=1&internal=1&layout_root_alias=${localStorage.rootAlias}&sort=${localStorage.lan}`,
        'layout_last_alias');
}
//===================================

async function getModelData(model, filtro) {
    const url = `${localStorage.serverUrl}/apirest/${model}/?format=json${filtro}`;
    console.log(url); 
    let respuesta = await fetch(url);
    let resultado = await respuesta.json();
    let data = resultado.results;
    console.log(resultado)
    return data
}

function listToDict(data_list){
    let data_dict = {};
    data_list.forEach(function(row){
        data_dict[row['pos']] = row
    });
    return data_dict
}
    


async function manageLayout(model, filtro, idElementField) {
    console.log(`Ejecutar manageLayout
        model=${model} filtro=${filtro} idElementField=${idElementField}`);

    let data = await getModelData(model,filtro)
    let data_dict = await listToDict(data);

    if (data==null) {
        alert('No hay datos');
        return;
    };
    
    await data.forEach(function(obj) {
   
        if (obj == null) {
            alert(`El objeto es nulo `);
            return;
        };
        
        
        idElement = obj[idElementField] 
        element = document.getElementById(idElement);

        if (element==null) {
            alert(`El elemento ${idElement} no está en el DOM`);
            return;
        };
    
        const mark = obj.mark.split('__')// funcion__parametro
        const action = mark[0];

        // console.log(`--- ${idElementField}=${idElement} mark=${mark}` )
        // console.log(element)

        switch (action) {

            case 'loadLanguages':
                loadLanguages(element,obj)
                break;
            case 'loadNavbar':
                loadNavbar(element,obj)
                break;
            case 'loadSidebar':
                loadSidebar(element,obj)
                break;
            //-------------------------------
            case 'loadCard1':
                loadCard1(element,obj)
                break;
            //-------------------------------
            case 'loadCard2':
                loadCard2(element,obj)
                break;
            //-------------------------------
            case 'loadCard2Team':
                loadCard2Team(element,obj)
                break;

            //-------------------------------
            case 'loadCard3':
                loadCard3(element,obj)
                break;
            //-------------------------------
            case 'loadImageName':
                // value = `/media/${obj.name}`
                element.setAttribute('src', obj.name);
                break;
            //-------------------------------
            case 'loadFileName':
                // value = `/media/${obj.name}`
                element.setAttribute('href', obj.name);
                break;
 
            //-------------------------------  
            case 'setAttr':
                if (obj.active) {
                    const field = mark[1];
                    const params = obj[field].split(',');
                    for  (let i=0; i < params.length; i++) {
                        attr = params[i].split(':')[0];
                        value = params[i].split(':')[1];
                        element.setAttribute(attr, value);
                    }
                }
                break;
            case 'innerHTML':
                if (obj.active) {                
                    field = mark[1];
                    element.innerHTML = obj[field];
                }
                break;

            default: // traducir principalmente
                break;
        };
    });
};


//----------------------------------
// seleccion de idiomas
//--------------------------------
function selectLan(e) {
    let lan = e.target.id.split('-')[1]
    console.log("Tengo que traducir a " + lan);
    localStorage.language = lan;
    // alert("Tengo que traducir a " + lan);
    manageLayout("layouti18ns",
        `&active=1&layout_root_alias=${localStorage.rootAlias}&sort=${localStorage.language}`,
        'layout_last_alias');

    //    `&locked=1&internal=1&layout_root_alias=${localStorage.rootAlias}&sort=${localStorage.lan}`,
    // si hay una pagina activa --> traducirla??? no es imprescindible
    // selectCard3(e);
}
//----------------------------------
// seleccion de Page
//--------------------------------

async function selectCard3(e){
    console.log("Paso por selectCard3")
    if (localStorage.card3 != ''){
        document.getElementById(localStorage.card3).innerHTML = '';
    };
    localStorage.card3 = e.target.id;
    //-------------------------
    const origenId = e.target.id.slice(-2);
    const filtro =
        `&active=1&layout_root_alias=${localStorage.rootAlias}
         &sort=${localStorage.language}&layout_last_alias=${origenId}`,
         data = await getModelData("layouti18ns",filtro)
         if (data==null) {
             alert('No hay datos');
             return;
         };
        const origenObj = data[0]
        const destinoId = `${e.target.id.slice(0,-2)}x` // main25x
        const destino = document.getElementById(destinoId);
        loadCard3(destino, origenObj);
        location.href = `#${destinoId}`;

}


//----------------------------------
// lan-xx carga de idiomas
//--------------------------------
async function x_loadLan(element, obj) {
    
    if (obj.active == 0) {
        // data = ''
        // element.innerHTML = data
        // ------------------------
        element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
    } else {
        let lan
        let name
        lan = await element.id.split('-')[1]
        name = await obj.name
        element.setAttribute('src', `../static/img/flag-${lan}.jpg`)
        element.setAttribute('class', `w3-padding-small w3-display-container w3-hover-opacity`)
        element.setAttribute('alt', `${name}`)
        element.setAttribute('style', 'width:40px')
        // element.setAttribute('onclick', `selectLan()`)
        // data = `<img src="../static/img/flag-${lan}.jpg"
        //     class="w3-padding-small w3-display-container w3-hover-opacity" 
        //     style="display:inline;width:180"
        //     alt="${name}" onclick="selectLan()">`
        // element.innerHTML = data
        //-----------------------
        // solo en caso de que no funcione el onclik anterior, añadir??
        //------------------------ 
        element.addEventListener('click', selectLan);
    }
}

async function loadLanguages(element, obj) {
    
    if (obj.active == 0) {
        // data = ''
        // element.innerHTML = data
        // ------------------------
        element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
    } else {
        let lans = obj.name.split(',');
        let data = ''
        await lans.forEach(function(lan) {
            data += `<img id="lan-${lan}" 
                src="../static/img/flag-${lan}.jpg"
                class="w3-padding-small w3-display-container w3-hover-opacity" 
                style="display:inline;width:40px"
                alt="${lan}" ">`
            element.innerHTML = data
            // onclick="selectLan(e)            
         })
            //------------------------ 
        element.innerHTML = data
        //-----------------------
        // solo en caso de que no funcione el onclik anterior, añadir??
        await lans.forEach(function(lan) {
            lang = `lan-${lan}`
            elemLan = document.getElementById(lang);
            elemLan.addEventListener('click', selectLan);
        })
    }
}
///----------------------------------
// navbar: carga y traduccion de navbar y sidebar
//--------------------------------
async function loadNavbar(element, obj) {
    if (obj.active == 0) {
        element.innerHTML = ''
        // element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
    } else {
        const href = await obj.last_alias.slice(-1);
        element.setAttribute('href',`#main${href}`); 
        element.setAttribute('class', 'w3-bar-item w3-button'); 
        let icono = await obj.note
        if (icono == '') {
            icono = "";
        } else {
            //let icono = `<i class="fa fa-${obj.note}"></i>`;
            icono = `<i class="fa ${icono}"></i>`;
        }
        // icono = ""
        data = `${icono} ${obj.name}`;


        // data = ` `
        element.innerHTML = data;
    }
}


///----------------------------------
// sidebar: carga y traduccion de navbar y sidebar
//--------------------------------
async function loadSidebar(element, obj) {
    await loadNavbar(element, obj);
    element.addEventListener('click', w3_close);
}

//----------------------------------
// carga y traduccion de main2
//--------------------------------/
function x_getAttrs(element, obj, paramsField){
    params = obj.paramsField.split(',')

    params.map()
    // codigo html y parametros
}

function loadCard1(element, obj){
    console.log('Estoy en loadCard1')
    console.log(obj);
    // params = obj.params.split(',');
    if (obj.active == 0) {
        // element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
        element.innerHTML = ''
        return;
    };
    const content = obj.content ? obj.content: ""
    // const foto = element.getElementById("main10")
    // const id1 = `${obj.last_alias}1`;
    // const id2 = `${obj.last_alias}2`;
    // let campo1 = element.getElementById(id1);
    // let campo2 = element.getElementById(id2);
    data = `<h2 class="w3-center">${obj.name}</h2>
            <p class="w3-center w3-large">
                ${content}
            </p>`

    element.innerHTML = data;
    // campo2.innerHTML = obj.content;
    return;
}


function loadCard2(element, obj) {

    if (obj.active == 0) {
        // element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
        element.innerHTML = ''
        return;
    };

    if (obj.note == null) {
        imagen = ""
    } else {
        if (obj.note.slice(0,3) == 'fa-') {
            imagen = `<i class="fa ${obj.note} w3-margin-bottom w3-jumbo"></i>`
        } else {
            imagen = `<img src="${obj.note}" alt="${obj.name}" style="width:40%">`
        }
    }

    nombre = (obj.name == null | obj.name == '' ) ? '' : obj.name;
    text1 = (obj.text1 == null) ? '' : obj.text1;
    text2 = (obj.text2 == null) ? '' : obj.text2;

    if (obj.text3 == null | obj.text3 == '' ){
        text3 = "";
    } else {
        if (obj.text3.includes("@")) {
            text3 = `<a class="w3-button w3-theme-l3 w3-block" 
                href="mailto:${obj.text3}">
                <i class="fa fa-envelope"></i>
                ${obj.text3}
                </a>`   
        } else {
        text3 = `<a class="w3-button w3-theme-l3 w3-block" 
                   href="http://${obj.text3}">
                   ${obj.text3}
                 </a>`
        }
    }

    if (obj.text4 == null| obj.text4 == '' ){
        leermasId = '';
        text4 = '';
    } else {
        leermasId =  `${element.id}x`;
        // console.log('leermasId = ' + leermasId)
        text4 = `<button id="${leermasId}" 
                            class="w3-button w3-theme-l3 w3-block">
                            ${obj.text4}
                        </button>`
    };

    data = `${imagen}
            <div class="w3-container">
                <h6 >${nombre}</h6>
                <p >${text1}</p>
                <p class="w3-opacity">${text2}</p>
                <p>${text3}</p>
                <p>${text4}</p>
            </div>`
               
    // console.log(data)
    element.innerHTML = data; 
    if (text4 != ''){
        buttonCard3 =  document.getElementById(leermasId); 
        buttonCard3.addEventListener('click', selectCard3);
    };
}


function loadCard2Team(element, obj) {

    if (obj.active == 0) {
        // element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
        element.innerHTML = ''
        return;
    };

    if (obj.note == null) {
        imagen = ""
    } else {
        if (obj.note.slice(0,3) == 'fa-') {
            imagen = `<i class="fa ${obj.note} w3-margin-bottom w3-jumbo"></i>`
        } else {
            imagen = `<img src="${obj.note}" alt="${obj.name}" style="width:100%">`
        }
    }

    nombre = (obj.name == null | obj.name == '' ) ? '' : obj.name;
    text1 = (obj.text1 == null) ? '' : obj.text1;
    text2 = (obj.text2 == null) ? '' : obj.text2;

    if (obj.text3 == null | obj.text3 == '' ){
        text3 = "";
    } else {
        text3 = `<a class="w3-button w3-theme-l3 w3-block" 
                   href="mailto:${obj.text3}">
                   <i class="fa fa-envelope"></i>
                   ${obj.text3}
                 </a>`
    }

    if (obj.text4 == null| obj.text4 == '' ){
        leermasId = '';
        text4 = '';
    } else {
        leermasId =  `${element.id}x`;
        // console.log('leermasId = ' + leermasId)
        text4 = `<button id="${leermasId}" 
                            class="w3-button w3-theme-l3 w3-block">
                            ${obj.text4}
                        </button>`
    };


    data = `
            <div class="w3-card">
                ${imagen}
                <div class="w3-container">
                    <h6 >${nombre}</h6>
                    <p >${text1}</p>
                    <p class="w3-opacity">${text2}</p>
                    <p>${text3}</p>
                    <p>${text4}</p>
                </div>
            </div>`

 
    // console.log(data)
    element.innerHTML = data; 
    if (text4 != ''){
        buttonCard3 =  document.getElementById(leermasId); 
        buttonCard3.addEventListener('click', selectCard3);
    };
}
function loadCard3(element, obj){
    loadCard1(element, obj);
}

function x_loadCard3(element, obj) {
    if (obj.active == 0) {
        element.innerHTML = ''
        // element.setAttribute('style', 'display:none'); 
        // element.setattrAttribute('style', 'visibility:hidden')
    } else {

        const foto = obj.note; //'equipo6-esperanza.jpeg'
        const nombre = obj.name; // 'Esperanza Rodríguez Mendoza'
        const cargo = obj.text1; // 'Coach'
        const aboutMe = obj.text2; // 'Write Two lines about me and my hobbies.'
        const email = obj.text3; //  'esperanza@asinex.es
        let data = `
            <div class="w3-col  l4 m6 w3-margin-bottom">
                <div class="w3-card">
                    <img src="../static/img/${foto}" alt="${nombre}" style="width:100%">
                    <div class="w3-container">
                        <h4 >${nombre}</h4>
                        <p class="w3-opacity">${cargo}</p>
                        <p >${aboutMe}</p>
                        <p><button class="w3-button w3-theme-l3 w3-block">
                            <i class="fa fa-envelope"></i>
                            ${email}</button></p>
                    </div>
                </div>
            </div>
        `
        element.innerHTML = data;
    }        
}
