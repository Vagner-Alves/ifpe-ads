document.addEventListener("DOMContentLoaded", function(){
    fetch('http://200.133.17.234:5000/consulta_decisiva')
    .then((response)=> response.json())
    .then((data)=>{
        document.getElementById('clientes-atendidos').innerText = data.clientes_atendidos;
        document.getElementById("distribuicao").innerText = data.distribuicao;
        document.getElementById("lucro").innerText = data.lucro;
        document.getElementById("total-vendas").innerText = data.total_de_vendas;
    })
})

