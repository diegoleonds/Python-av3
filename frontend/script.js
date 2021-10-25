$( document ).ready(function() {  
    $.ajax({
        url: 'http://localhost:5000/listar_contatos',
        method: 'GET',
        dataType: 'json', 
        success: listar_contatos, 
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });
    function listar_contatos(contatos) {
        linhas = ""
        for (var i in contatos) {
            linhas += criarLinha(contatos[i]);
        }
        $("#corpoTabela").html(linhas);
    }  

    function criarLinha(contato) {
        return "<tr>" + 
            "<td>" + contato.nome + "</td>" + 
            "<td>" + contato.sobrenome + "</td>" + 
            "<td>" + contato.email + "</td>" +
            "</tr>";
    }
  });