db.synchro.find({doctype:"revisao", identificador:/dou_2015/, }, 
    {"conteudo.data_publicacao":1, _id:0}).forEach(
        function bla(revisao) {
            print(revisao.conteudo.data_publicacao);
        }
    
    )
