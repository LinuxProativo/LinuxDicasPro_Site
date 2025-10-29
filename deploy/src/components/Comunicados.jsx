import {useState} from "react";
import '../css/Comunicados.css'
import database from "../assets/database.json";

const Comunicados = () => {
    const [comunicados] = useState(database.comunicados.slice().reverse());

    return (
        <div>
            <h2>📢 Comunicados e Dicas</h2>
            <div className="comunicados">
                {comunicados.map(({ titulo, descricao }, index) => (
                    <div className="comunicado-card" key={index}>
                        <h3>{titulo}</h3>
                        <p>{descricao}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Comunicados;
