function buscaCurso() {
    let curso = document.querySelector('select[name=curso]').value;
    let aula = document.querySelector('select[name=aula]').value;

    switch(curso) {
    case "apps":
        url = 'https://dl.dropboxusercontent.com/s/uoj0l5vw2xyyam6/apps.json';
        break;
    case "robotica":
        url = 'https://dl.dropboxusercontent.com/s/q129f4nh1xlanm7/robotica.json';
        break;
    default:
        url = "undefined";
}
    
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
        if (xhr.status = 200)
            preencheCampos(JSON.parse(xhr.responseText), aula);
        }
    }
    xhr.send();
}

function preencheCampos(json, n) {
    n = n - 1;
    document.querySelector('textarea[name=resumo]').value = json.aula[n].resumo;
    document.querySelector('textarea[name=resultados]').value = json.aula[n].resultados;

}