import { useState } from "react";
import Comunicados from "../components/Comunicados";
import '../css/Welcome.css'
import '../css/ComunicadosModal.css';
import icon from "../assets/close.svg";

const Inicio = () => {
    const [modalOpen, setModalOpen] = useState(false);

    return (
        <div className="page">
            <div className="top-section">
                <div className="welcome">
                    <h2>Bem-Vindo 🚀</h2>
                    <p>
                        Um espaço para explorar o mundo Linux, com artigos detalhados, guias práticos e conteúdos
                        selecionados para ajudar iniciantes e usuários avançados a aproveitar ao máximo o sistema.
                    </p>
                    <p>
                        Indicações de produtos recomendados por meio de <b>Links de Afiliados</b>, cuidadosamente
                        selecionados para garantir qualidade e confiança. Ao adquirir algum produto por esses links,
                        você apoia o canal e ajuda a continuar produzindo conteúdo gratuito e de qualidade.
                    </p>
                    <p>
                        Acompanhe os projetos do canal, desenvolvidos para ajudar e agregar ao ecossistema <b>Linux</b>.
                    </p>
                    <div className="comunicados-button-wrapper">
                        <button className="comunicados-button" onClick={() => setModalOpen(true)}>
                            Comunicados e Dicas
                        </button>
                    </div>
                </div>

                <div className="welcome-comunicados">
                    <Comunicados />
                </div>

                {modalOpen && (
                    <div className="comunicados-modal" onClick={() => setModalOpen(false)} >
                        <div className="comunicados-modal-content" onClick={(e) => e.stopPropagation()} >
                            <div className="comunicados-modal-close-wrapper">
                                <button className="comunicados-modal-close" onClick={() => setModalOpen(false)} >
                                    <img src={String(icon)} alt="Voltar" className="icone-voltar" />
                                </button>
                            </div>
                            <Comunicados />
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Inicio;

