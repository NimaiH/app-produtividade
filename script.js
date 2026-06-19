// Script 

const botaoAdicionar = document.getElementById('botao-adicionar');
const campoTarefa = document.getElementById('campo-tarefa');
const listaTarefas = document.getElementById('lista-tarefas');

botaoAdicionar.addEventListener('click', adicionarTarefa);

function adicionarTarefa() {
    // 1- Pegar o texto que o usuário digitou no "CampoTarefa"
    const textoTarefa = campoTarefa.value;

    // Se o campo estiver VAZIO, exibe um aviso e para a execução do código.
    if (textoTarefa === '') {
        alert('Por favor, digite uma tarefa!');
        return; // O return faz a função parar aqui e não executar o resto.

    }

    // 2- Criamos um novo elemento de lista para a tarefa(?)
    const novaLi = document.createElement('li');

    // 3- Colocar o texto da tarefa dentro da lista.
    novaLi.textContent = textoTarefa;

    // 4- Colocamos a nova Li dentro da nossa lista (ul)
    listaTarefas.appendChild(novaLi);

    // 5- Limpar o campo de digitação para a próxima tarefa
    campoTarefa.value = '';
}   