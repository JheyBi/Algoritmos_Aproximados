
function firstFitDecreasing(items, binCapacity) {
    console.log("Iniciando o algoritmo aproximativo FFD, com a capacidade de cada caixa em: " + binCapacity);
    console.log("Peso de cara item: " + items);
    
    // Primeiro ordena os itens em ordem decrescente
    items.sort((a, b) => b - a);
    
    let bins = []; // Lista das caixas e seus itens
    let binRemain = []; // Espaço restante em cada caixa
    
    // Para cada item verifique as caixas disponíveis
    for (let i = 0; i < items.length; i++) {
        
        let j; // Caixa atual em que o item está verificando
        
        for (j = 0; j < bins.length; j++) { 
            if (binRemain[j] >= items[i]) { // Se o item for <= ao espaço que está sobrando na caixa
                bins[j].push(items[i]);     // o item é colocado
                binRemain[j] -= items[i];   // e o espaço restante da caixa é reduzido
                break;
            }
        }
        
        // Se nenhuma caixa pôde acomodar items[i]
        if (j == bins.length) {
            bins.push([items[i]]); // Adiciona o item a uma caixa nova
            // O espaço restante da caixa nova é igual a capacidade total - o valor do item
            binRemain.push(binCapacity - items[i]);
        }
    }
    
    // Retorna a quantidade minima de caixas
    return bins.length;
}

let binCapacity = Math.floor(Math.random() * 10) + 1; // Definindo a capacidade das caixas de forma aleatória de 1 até 10
let items = []; // Definindo 50 itens com pesos aleatórios entre 1 e a capacidade das caixas
for (let i = 0; i < 50; i++) {
    let number = Math.floor(Math.random() * binCapacity) + 1;
    items.push(number);
}

let opt = items.reduce((sum, item) => sum + item, 0); // Solução ótima do problema >= somatório dos pesos dos itens

// Resultado da quantidade mínima de caixas usando o algoritmo FFD
let result = firstFitDecreasing(items, binCapacity);
console.log("Resultado aproximado: " + result);
console.log("Solução ótima: " + (opt/binCapacity));



