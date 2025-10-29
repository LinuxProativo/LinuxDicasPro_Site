import React, { useState } from "react";
import ItemList from "../components/ItemList";
import database from "../assets/database.json";

let produtosCache = null;

const Produtos = () => {
    const [amazonProdutos] = useState(
        produtosCache?.["produtos"]?.["amazon"] || database.produtos.amazon || []
    );
    const [mercadoLivreProdutos] = useState(
        produtosCache?.["produtos"]?.["mercado_livre"] || database.produtos.mercado_livre || []
    );

    if (!produtosCache) produtosCache = database;

    return (
        <div className="page">
            <div className="top-section top-column">
                <ItemList title="Recomendações da Amazon" type="produto" items={amazonProdutos} />
                <ItemList title="Recomendações do Mercado Livre" type="produto" items={mercadoLivreProdutos} />
            </div>
        </div>
    );
};

export default Produtos;
